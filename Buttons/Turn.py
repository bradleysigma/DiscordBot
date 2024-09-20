import discord
from Buttons.Population import PopulationButtons
from helpers.GamestateHelper import GamestateHelper
from helpers.PlayerHelper import PlayerHelper
from helpers.DrawHelper import DrawHelper
from discord.ui import View, Button
import concurrent.futures
import time
import asyncio
class TurnButtons:




    @staticmethod
    def noOneElsePassed(player, game: GamestateHelper):
        for p2 in game.get_gamestate()["players"]:
            if "passed" in game.get_gamestate()["players"][p2] and game.get_gamestate()["players"][p2]["passed"] == True:
                return False
        return True


    @staticmethod
    def getFirstPlayer(game: GamestateHelper):
        listHS = [201,203,205,207,209,211]
        for number in listHS:
            nextPlayer = game.getPlayerFromHSLocation(str(number))
            if nextPlayer is not None and game.get_gamestate()["players"].get(nextPlayer, {}).get("firstPlayer", False):
                return game.get_gamestate()["players"][nextPlayer]
        return None

    @staticmethod
    async def restartTurn(player, game:GamestateHelper, interaction: discord.Interaction):
        view = TurnButtons.getStartTurnButtons(game, player)
        await interaction.response.send_message(player["player_name"]+ " use buttons to do your turn"+ game.displayPlayerStats(player),view=view)
        await interaction.message.delete()
        



    @staticmethod
    async def endTurn(player, game:GamestateHelper, interaction: discord.Interaction, bot):
        nextPlayer = game.get_next_player(player)
        if nextPlayer != None and not game.is_everyone_passed():
            view = TurnButtons.getStartTurnButtons(game,nextPlayer)
            await interaction.response.send_message(nextPlayer["player_name"]+ " use buttons to do your turn"+ game.displayPlayerStats(nextPlayer),view=view)
        else:
            await interaction.response.send_message("All players have passed")
        await interaction.message.delete()
        await game.showUpdate(f"End of {interaction.user.name}'s turn",interaction, bot)


    @staticmethod
    async def passForRound(player, game: GamestateHelper, interaction: discord.Interaction, player_helper : PlayerHelper, bot):
        if TurnButtons.noOneElsePassed(player,game):
            player_helper.adjust_money(2)
            await interaction.channel.send(f"{interaction.user.mention} you gained 2 money and the first player marker for next round for passing first")
            player_helper.setFirstPlayer(True)
            for p2 in game.get_gamestate()["players"]:
                if game.get_gamestate()["players"][p2]["color"] == player["color"]:
                    continue
                player_helper2 = PlayerHelper(p2, game.get_gamestate()["players"][p2])
                player_helper2.setFirstPlayer(False)
                game.update_player(player_helper2)
        player_helper.passTurn(True)
        game.update_player(player_helper)
        nextPlayer = game.get_next_player(player)
        if nextPlayer != None and not game.is_everyone_passed():
            view = TurnButtons.getStartTurnButtons(game,nextPlayer)
            await interaction.response.send_message(nextPlayer["player_name"]+ " use buttons to do your turn"+ game.displayPlayerStats(nextPlayer),view=view)

            view2 = View()
            view2.add_item(Button(label=f"Permanently Pass", style=discord.ButtonStyle.green, custom_id="permanentlyPass"))
            await interaction.followup.send(interaction.user.mention+ " you can use this button to permanently pass on reactions if you want.",view=view2,ephemeral=True)
        else:
            view = View()
            view.add_item(Button(label="Run Cleanup",style=discord.ButtonStyle.blurple, custom_id="runCleanup"))
            await interaction.response.send_message("All players have passed, you can use this button to start the next round after all battles are resolved", view=view)
        await interaction.message.delete()
        await game.showUpdate(f"{interaction.user.name} Passing",interaction, bot)


    @staticmethod
    async def permanentlyPass(player, game: GamestateHelper, interaction: discord.Interaction, player_helper : PlayerHelper):
        player_helper.permanentlyPassTurn(True)
        game.update_player(player_helper)
        await interaction.response.edit_message(content="You permanently passed", view=None)

    @staticmethod
    async def runCleanup(game: GamestateHelper, interaction: discord.Interaction):
        game.cleanUp()
        await interaction.response.defer(thinking=False)
        nextPlayer = TurnButtons.getFirstPlayer(game)
        if nextPlayer != None:
            view = TurnButtons.getStartTurnButtons(game,nextPlayer)
            await interaction.followup.send(nextPlayer["player_name"]+ " use buttons to do the first turn of the round"+game.displayPlayerStats(nextPlayer),view=view)
        else:
            await interaction.followup.send("Could not find first player, someone run /player start_turn")


    @staticmethod
    async def showReputation(game: GamestateHelper,interaction: discord.Interaction, player):
        msg = f"{interaction.user.mention} Your reputation tiles hold the following values: "
        for reputation in player["reputation_track"]:
            if reputation != "mixed" and reputation != "amb":
                msg = msg + str(reputation)+" "

        await interaction.response.send_message(msg,ephemeral=True)
    @staticmethod
    async def send_files(interaction, files):
        for file in files:
            await interaction.followup.send(file=file,ephemeral=True)

    @staticmethod
    async def send_file(interaction, file):
        await interaction.followup.send(file=file,ephemeral=True)

    @staticmethod
    async def showGame(game: GamestateHelper, interaction: discord.Interaction, bot):
        await interaction.response.defer(thinking=True,ephemeral=True)
        game.updateNamesAndOutRimTiles(interaction)
        drawing = DrawHelper(game.gamestate)
        view = View()
        view.add_item(Button(label="Show Game",style=discord.ButtonStyle.blurple, custom_id="showGame"))
        view.add_item(Button(label="Show Reputation",style=discord.ButtonStyle.gray, custom_id="showReputation"))
        map = drawing.show_map()
        stats = drawing.show_stats()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(asyncio.run_coroutine_threadsafe, TurnButtons.send_files(interaction, [map,stats]),bot.loop)
        #await interaction.followup.send(file=drawing.show_map(),ephemeral=True)
        # end_time = time.perf_counter()  
        # elapsed_time = end_time - start_time  
        # print(f"Total elapsed time for showing map: {elapsed_time:.2f} seconds")
        # start_time = time.perf_counter() 
        # await interaction.followup.send(file=drawing.show_stats(),ephemeral=True, view=view)
        # end_time = time.perf_counter()  
        # elapsed_time = end_time - start_time  
        # print(f"Total elapsed time for showing stats: {elapsed_time:.2f} seconds")

    @staticmethod
    def getStartTurnButtons(game: GamestateHelper,p1):
        view = View()
        player = p1
        if "passed" in p1 and p1["passed"]== True:
            view.add_item(Button(label=f"Build (1)", style=discord.ButtonStyle.green, custom_id=f"FCID{player['color']}_startBuild"))
            view.add_item(Button(label=f"Upgrade (1)", style=discord.ButtonStyle.blurple, custom_id=f"FCID{player['color']}_startUpgrade"))
            view.add_item(Button(label=f"Move (1)", style=discord.ButtonStyle.green, custom_id=f"FCID{player['color']}_startMove"))
            view.add_item(Button(label="End Turn", style=discord.ButtonStyle.red, custom_id=f"FCID{player['color']}_endTurn"))
        else:
            view.add_item(Button(label=f"Explore ({p1['explore_apt']})", style=discord.ButtonStyle.green, custom_id=f"FCID{player['color']}_startExplore"))
            view.add_item(Button(label=f"Research ({p1['research_apt']})", style=discord.ButtonStyle.blurple, custom_id=f"FCID{player['color']}_startResearch"))
            view.add_item(Button(label=f"Build ({p1['build_apt']})", style=discord.ButtonStyle.green, custom_id=f"FCID{player['color']}_startBuild"))
            view.add_item(Button(label=f"Upgrade ({p1['upgrade_apt']})", style=discord.ButtonStyle.blurple, custom_id=f"FCID{player['color']}_startUpgrade"))
            view.add_item(Button(label=f"Move ({p1['move_apt']})", style=discord.ButtonStyle.green, custom_id=f"FCID{player['color']}_startMove"))
            view.add_item(Button(label=f"Influence ({p1['influence_apt']})", style=discord.ButtonStyle.gray, custom_id=f"FCID{player['color']}_startInfluence"))
            view.add_item(Button(label="Pass", style=discord.ButtonStyle.red, custom_id=f"FCID{p1['color']}_passForRound"))
        view.add_item(Button(label="Show Game",style=discord.ButtonStyle.gray, custom_id="showGame"))
        view.add_item(Button(label="Show Reputation",style=discord.ButtonStyle.gray, custom_id="showReputation"))
        if len(PopulationButtons.findEmptyPopulation(game,p1)) > 0 and p1["colony_ships"] > 0:
            view.add_item(Button(label="Put Down Population", style=discord.ButtonStyle.gray, custom_id=f"FCID{p1['color']}_startPopDrop"))
        return view