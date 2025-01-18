from .ban_dto import BanDto
from .objectives_dto import ObjectivesDto


class TeamDto():
    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def bans(self) -> list[BanDto]: 
        try:
            list_of_bans = []
            for ban in self.raw_data['bans']:
                list_of_bans.append(BanDto(ban))
            return list_of_bans
        except KeyError as e:
            e.add_note('Could not retrieve bans, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def objectives(self) -> ObjectivesDto:
        try:
            return ObjectivesDto(self.raw_data['objectives'])
        except KeyError as e:
            e.add_note('Could not retrieve allInPings, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def teamId(self) -> int:
        try:
            return self.raw_data['teamId']
        except KeyError as e:
            e.add_note('Could not retrieve allInPings, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def win(self) -> bool:
        try:
            return self.raw_data['win']
        except KeyError as e:
            e.add_note('Could not retrieve allInPings, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise