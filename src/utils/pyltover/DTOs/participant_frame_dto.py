from pyltover.DTOs.champion_stats_dto import ChampionStatsDto
from pyltover.DTOs.damage_stats_dto import DamageStatsDto
from pyltover.DTOs.position_dto import PositionDto

class ParticipantFrameDto():
    def __init__(self, raw_data : dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def championStats(self) -> ChampionStatsDto: 
        try:
            return ChampionStatsDto(self.raw_data['championStats'])
        except KeyError as e:
            e.add_note('Could not retrieve championStats, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def currentGold(self) -> int:
        try:
            return self.raw_data['currentGold']
        except KeyError as e:
            e.add_note('Could not retrieve currentGold, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def damageStats(self) -> DamageStatsDto: 
        try:
            return DamageStatsDto(self.raw_data['damageStats'])
        except KeyError as e:
            e.add_note('Could not retrieve damageStats, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def goldPerSecond(self) -> int:
        try:
            return self.raw_data['goldPerSecond']
        except KeyError as e:
            e.add_note('Could not retrieve goldPerSecond, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def jungleMinionsKilled(self) -> int:
        try:
            return self.raw_data['jungleMinionsKilled']
        except KeyError as e:
            e.add_note('Could not retrieve jungleMinionsKilled, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def level(self) -> int:
        try:
            return self.raw_data['level']
        except KeyError as e:
            e.add_note('Could not retrieve level, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def minionsKilled(self) -> int:
        try:
            return self.raw_data['minionsKilled']
        except KeyError as e:
            e.add_note('Could not retrieve minionsKilled, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def participantId(self) -> int:
        try:
            return self.raw_data['participantId']
        except KeyError as e:
            e.add_note('Could not retrieve participantId, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def position(self) -> PositionDto: 
        try:
            return PositionDto(self.raw_data['position'])
        except KeyError as e:
            e.add_note('Could not retrieve position, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def timeEnemySpentControlled(self) -> int:
        try:
            return self.raw_data['timeEnemySpentControlled']
        except KeyError as e:
            e.add_note('Could not retrieve timeEnemySpentControlled, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def totalGold(self) -> int:
        try:
            return self.raw_data['totalGold']
        except KeyError as e:
            e.add_note('Could not retrieve totalGold, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def xp(self) -> int:
        try:
            return self.raw_data['xp']
        except KeyError as e:
            e.add_note('Could not retrieve xp, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
