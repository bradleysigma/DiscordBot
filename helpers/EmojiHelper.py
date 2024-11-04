
class Emoji:

    @staticmethod
    def getEmojiByName(name:str):
        emojiList = [
        "<:morph_shield:1301315782407356527>",
        "<:tachyon_drive:1301315477812940905>",
        "<:tachyon_source:1301314865058680972>",
        "<:fusion_source:1301315774060822578>",
        "<:hypergrid_source:1301314811312996453>",
        "<:muon_source:1301314830354874452>",
        "<:nuclear_source:1301314836948455506>",
        "<:zero_point_source:1301314870511140894>",
        "<:zeropoint_source:1301314873040572536>",
        "<:conformal_drive:1301314791218090064>",
        "<:fusion_drive:1301314799132606514>",
        "<:jump_drive:1301314826026618902>",
        "<:nonlinear_drive:1301314832880107550>",
        "<:nuclear_drive:1301315634113675265>",
        "<:transition_drive:1301315479364964404>",
        "<:antimatter_cannon:1301314785287344178>",
        "<:ion_cannon:1301315778787803257>",
        "<:plasma_cannon:1301314840752553984>",
        "<:rift_cannon:1301314847937396737>",
        "<:soliton_cannon:1301315640983949413>",
        "<:antimatter_missile:1301314787090628699>",
        "<:flux_missile:1301314795542151178>",
        "<:ion_missile:1301315780582965359>",
        "<:plasma_missile:1301315636550697020>",
        "<:soliton_missile:1301314860864241734>",
        "<:hull:1301314806535422113>",
        "<:hull_conifoldfield:1301315777328058408>",
        "<:improved_hull:1301314814534221986>",
        "<:sentient_hull:1301315639142776843>",
        "<:shard_hull:1301314854900072459>",
        "<:axion_computer:1301314789007429642>",
        "<:electron_computer:1301314793982001214>",
        "<:gluon_computer:1301315775784550531>",
        "<:positron_computer:1301315638089744474>",
        "<:rift_conductor:1301314851209089034>",
        "<:ion_turret:1301314824483115028>",
        "<:plasma_turret:1301314845077147708>",
        "<:ion_disruptor:1301314820452253727>",
        "<:absorption_shield:1301314783873728532>",
        "<:flux_shield:1301314798008537190>",
        "<:gauss_shield:1301314802471272498>",
        "<:inversion_shield:1301314816127799369>",
        "<:phase_shield:1301315635363581962>",
        "<:tech_absorption_shield:1301316497813016667>",
        "<:tech_advanced_economy:1301316279965319239>",
        "<:tech_advanced_labs:1301316438736371792>",
        "<:tech_advanced_mining:1301316376522264606>",
        "<:tech_advanced_robotics:1301316441219399680>",
        "<:tech_ancient_labs:1301316500056969329>",
        "<:tech_antimatter_cannon:1301316281768607744>",
        "<:tech_antimatter_splitter:1301316502427009024>",
        "<:tech_artifact_key:1301316443912142988>",
        "<:tech_cloaking_device:1301316504012460144>",
        "<:tech_conifold_field:1301316506852003901>",
        "<:tech_flux_missile:1301316508860940360>",
        "<:tech_fusion_drive:1301316446105632778>",
        "<:tech_fusion_source:1301316284117553282>",
        "<:tech_gauss_shield:1301316285904191510>",
        "<:tech_gluon_computer:1301316378510233653>",
        "<:tech_improved_hull:1301316287640895539>",
        "<:tech_improved_logistics:1301316510626877480>",
        "<:tech_metasynthesis:1301316512480755772>",
        "<:tech_monolith:1301316448375017473>",
        "<:tech_nano_robots:1301316450438479892>",
        "<:tech_neutron_absorber:1301316514510667788>",
        "<:tech_neutron_bombs:1301316380057931786>",
        "<:tech_orbital:1301316452778905652>",
        "<:tech_phase_shield:1301316382213804142>",
        "<:tech_pico_modulator:1301316516364419164>",
        "<:tech_plasma_cannon:1301316384172544030>",
        "<:tech_plasma_missile:1301316386160902255>",
        "<:tech_positron_computer:1301316289276416052>",
        "<:tech_quantum_grid:1301316290601816204>",
        "<:tech_rift_cannon:1301316518356717608>",
        "<:tech_sentient_hull:1301316520881688698>",
        "<:tech_soliton_cannon:1301316522832039997>",
        "<:tech_star_base:1301316388023177216>",
        "<:tech_tachyon_drive:1301316292237856849>",
        "<:tech_tachyon_source:1301316390078124063>",
        "<:tech_transition_drive:1301316572421292104>",
        "<:tech_warp_portal:1301316527533985842>",
        "<:tech_wormhole_generator:1301316454406426715>",
        "<:tech_zero_point_source:1301316530633576589>",
        "<:bluedrd:1301320104331448482>",
        "<:greendrd:1301320115597607005>",
        "<:purpledrd:1301319978749919243>",
        "<:reddrd:1301319916359520297>",
        "<:whitedrd:1301319924043612161>",
        "<:science:1301746859643240479>",
        "<:material:1301746857051029577>",
        "<:money:1301746858376298496>",
        "<:yellowdrd:1301319879441256559>",
        "<:dracotoken:1302090247735349330>",
        "<:eridanitoken:1302090245805703220>",
        "<:colony_ship:1302428460198924388>",
        "<:magellantoken:1302433939406852137>",
        "<:lyratoken:1302700320765251655>",
        "<:hydrantoken:1302090243440115754>",
        "<:mechanematoken:1302090241007685692>",
        "<:oriontoken:1302090239401263144>",
        "<:plantatoken:1302090237555511376>",
        "<:terran_alliance_token:1302090255771373620>",
        "<:terran_conglomerate_token:1302090251086462996>",
        "<:terran_directorate_token:1302090265976246352>",
        "<:terran_federation_token:1302090263468179528>",
        "<:terran_republic_token:1302090249509404753>",
        "<:terran_union_token:1302090253368037478>",
        "<:bluecru:1301320102888607754>",
        "<:greencru:1301320113584214096>",
        "<:purplecru:1301319976879390720>",
        "<:redcru:1301319914128281772>",
        "<:whitecru:1301319922592383017>",
        "<:yellowcru:1301319877809799180>",
        "<:bluesb:1301320107452137562>",
        "<:yellowsb:1301319883241558157>",
        "<:whitesb:1301319876215967774>",
        "<:redsb:1301319920667201557>",
        "<:purplesb:1301320055191244891>",
        "<:greensb:1301320120898945105>",
        "<:blueint:1301320105556185221>",
        "<:purpleint:1301320052519211142>",
        "<:redint:1301319918041567273>",
        "<:yellowint:1301319881047674934>",
        "<:greenint:1301320116813697064>",
        "<:whiteint:1301319925679390871>"]
        for emoj in emojiList:
            if ":"+name+":" in emoj:
                return emoj
        return "❓"
