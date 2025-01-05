from enum import Enum

class Loading(Enum):
    LAZY = 0
    EAGER = 1
    
class By(Enum):
    RIOT_ID = 1
    PUUID = 2
    SUMMONER_ID = 3
    ACCOUNT_ID = 4

class Region(Enum):
    EUN1 = "europe1"
    EUW1 = "europe2"
    ME1 = "europe3"
    RU = "europe4"
    TR1 = "europe5"
    BR1 = "americas1"
    LA1 = "americas2"
    LA2 = "americas3"
    NA1 = "americas4"
    OC1 = "americas5"
    JP1 = "asia1"
    KR = "asia2"
    PH2 = "asia3"
    SG2 = "asia4"
    TH2 = "asia5"
    TW2 = "asia6"
    VN2 = "asia7"

class Tier(Enum):
    IRON = 1
    BRONZE = 2
    SILVER = 3
    GOLD = 4
    PLATINUM = 5
    DIAMOND = 6
    MASTER = 7
    GRANDMASTER = 8
    CHALLENGER = 9

    def __eq__(self, other):
        return self.value == other.value
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)
        

class Division(Enum):
    I = 1
    II = 2
    III = 3
    IV = 4

    def __eq__(self, other):
        return self.value == other.value
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)
    
class Matchtype(Enum):
    RANKED = 'ranked'
    NORMAL = 'normal'
    TOURNEY = 'tourney'
    TUTORIAL = 'tutorial'
    
class QueueType(Enum):
    CUSTOM_GAMES = 0
    HOWLING_ABYSS_1V1_SNOWDOWN_SHOWDOWN_GAMES = 72
    HOWLING_ABYSS_2V2_SNOWDOWN_SHOWDOWN_GAMES = 73
    SUMMONERS_RIFT_6V6_HEXAKILL_GAMES = 75
    SUMMONERS_RIFT_ULTRA_RAPID_FIRE_GAMES = 76
    HOWLING_ABYSS_ONE_FOR_ALL_MIRROR_MODE_GAMES = 78
    SUMMONERS_RIFT_CO_OP_VS_AI_ULTRA_RAPID_FIRE_GAMES = 83
    TWISTED_TREELINE_6V6_HEXAKILL_GAMES = 98
    BUTCHERS_BRIDGE_5V5_ARAM_GAMES = 100
    SUMMONERS_RIFT_NEMESIS_GAMES = 310
    SUMMONERS_RIFT_BLACK_MARKET_BRAWLERS_GAMES = 313
    CRYSTAL_SCAR_DEFINITELY_NOT_DOMINION_GAMES = 317
    SUMMONERS_RIFT_ALL_RANDOM_GAMES = 325
    SUMMONERS_RIFT_5V5_DRAFT_PICK_GAMES = 400
    SUMMONERS_RIFT_5V5_RANKED_SOLO_GAMES = 420
    SUMMONERS_RIFT_5V5_BLIND_PICK_GAMES = 430
    SUMMONERS_RIFT_5V5_RANKED_FLEX_GAMES = 440
    HOWLING_ABYSS_5V5_ARAM_GAMES = 450
    SUMMONERS_RIFT_NORMAL_QUICKPLAY = 490
    SUMMONERS_RIFT_BLOOD_HUNT_ASSASSIN_GAMES = 600
    COSMIC_RUINS_DARK_STAR_SINGULARITY_GAMES = 610
    SUMMONERS_RIFT_SUMMONERS_RIFT_CLASH_GAMES = 700
    HOWLING_ABYSS_ARAM_CLASH_GAMES = 720
    TWISTED_TREELINE_CO_OP_VS_AI_BEGINNER_BOT_GAMES = 820
    SUMMONERS_RIFT_CO_OP_VS_AI_INTRO_BOT_GAMES = 870
    SUMMONERS_RIFT_CO_OP_VS_AI_BEGINNER_BOT_GAMES = 880
    SUMMONERS_RIFT_CO_OP_VS_AI_INTERMEDIATE_BOT_GAMES = 890
    SUMMONERS_RIFT_ARURF_GAMES = 900
    CRYSTAL_SCAR_ASCENSION_GAMES = 910
    HOWLING_ABYSS_LEGEND_OF_THE_PORO_KING_GAMES = 920
    SUMMONERS_RIFT_NEXUS_SIEGE_GAMES = 940
    SUMMONERS_RIFT_DOOM_BOTS_VOTING_GAMES = 950
    SUMMONERS_RIFT_DOOM_BOTS_STANDARD_GAMES = 960
    VALORAN_CITY_PARK_STAR_GUARDIAN_INVASION_NORMAL_GAMES = 980
    VALORAN_CITY_PARK_STAR_GUARDIAN_INVASION_ONSLAUGHT_GAMES = 990
    OVERCHARGE_PROJECT_HUNTERS_GAMES = 1000
    SUMMONERS_RIFT_SNOW_ARURF_GAMES = 1010
    SUMMONERS_RIFT_ONE_FOR_ALL_GAMES = 1020
    CRASH_SITE_ODYSSEY_EXTRACTION_INTRO_GAMES = 1030
    CRASH_SITE_ODYSSEY_EXTRACTION_CADET_GAMES = 1040
    CRASH_SITE_ODYSSEY_EXTRACTION_CREWMEMBER_GAMES = 1050
    CRASH_SITE_ODYSSEY_EXTRACTION_CAPTAIN_GAMES = 1060
    CRASH_SITE_ODYSSEY_EXTRACTION_ONSLAUGHT_GAMES = 1070
    CONVERGENCE_TEAMFIGHT_TACTICS_GAMES = 1090
    CONVERGENCE_RANKED_TEAMFIGHT_TACTICS_GAMES = 1100
    CONVERGENCE_TEAMFIGHT_TACTICS_TUTORIAL_GAMES = 1110
    CONVERGENCE_TEAMFIGHT_TACTICS_TEST_GAMES = 1111
    CONVERGENCE_TEAMFIGHT_TACTICS_CHONCCS_TREASURE_MODE = 1210
    NEXUS_BLITZ_NEXUS_BLITZ_GAMES = 1300
    SUMMONERS_RIFT_ULTIMATE_SPELLBOOK_GAMES = 1400
    RINGS_OF_WRATH_ARENA = 1700
    RINGS_OF_WRATH_ARENA_16 = 1710
    SWARM_SWARM_MODE_GAMES_1 = 1810
    SWARM_MODE_GAMES_SWARM_2 = 1820
    SWARM_MODE_GAMES_SWARM_3 = 1830
    SWARM_MODE_GAMES_SWARM_4 = 1840
    SUMMONERS_RIFT_PICK_URF_GAMES = 1900
    SUMMONERS_RIFT_TUTORIAL_1 = 2000
    SUMMONERS_RIFT_TUTORIAL_2 = 2010
    SUMMONERS_RIFT_TUTORIAL_3 = 2020