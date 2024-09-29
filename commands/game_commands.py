import os
import discord
from Buttons.Turn import TurnButtons
import config
from discord.ext import commands
from discord import app_commands
from discord.ui import View, Button
from typing import Optional, List
from helpers.CombatHelper import Combat
from setup.GameInit import GameInit
from helpers.GamestateHelper import GamestateHelper
from helpers.DrawHelper import DrawHelper
import random
import time


class GameCommands(commands.GroupCog, name="game"):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="end")
    async def end(self,interaction: discord.Interaction):
        game = GamestateHelper(interaction.channel)
        await game.endGame(interaction)

    @app_commands.command(name="start_combats")
    async def start_combats(self,interaction: discord.Interaction):
        game = GamestateHelper(interaction.channel)
        interaction.response.defer()
        await Combat.startCombatThreads(game, interaction)

    @app_commands.command(name="upkeep")
    async def upkeep(self,interaction: discord.Interaction):
        interaction.response.defer()
        game = GamestateHelper(interaction.channel)
        await TurnButtons.runUpkeep(game, interaction,self.bot)
    
    @app_commands.command(name="set_round")
    async def set_round(self,interaction: discord.Interaction, round:int):
        game = GamestateHelper(interaction.channel)
        game.setRound(round)
        await interaction.response.send_message("Set the round number to "+str(round))

    @app_commands.command(name="show_game")
    async def show_game(self, interaction: discord.Interaction):
        game = GamestateHelper(interaction.channel)
        await interaction.response.defer(thinking=True)
        start_time = time.perf_counter()
        drawing = DrawHelper(game.gamestate)
        await interaction.followup.send(file=drawing.show_map())
        await interaction.followup.send(file=drawing.show_stats())
        view = View()
        button = Button(label="Show Game",style=discord.ButtonStyle.blurple, custom_id="showGame")
        view.add_item(button)
        view.add_item(Button(label="Show Reputation",style=discord.ButtonStyle.gray, custom_id="showReputation"))
        await interaction.channel.send(view=view)
        end_time = time.perf_counter()  
        elapsed_time = end_time - start_time  
        print(f"Total elapsed time for show game command: {elapsed_time:.2f} seconds")  
    
    @app_commands.command(name="undo")
    async def undo(self, interaction: discord.Interaction):
        game = GamestateHelper(interaction.channel)
        if game.backUpToLastSaveFile():
            await interaction.response.send_message("Successfully backed up to the last save file. "+str(game.getNumberOfSaveFiles())+" save files remain")
        else:
            await interaction.response.send_message("Ran out of save files, could not back up")
    