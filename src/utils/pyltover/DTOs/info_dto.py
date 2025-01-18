from .participant_dto import ParticipantDto
from .team_dto import TeamDto


class InfoDto():
    def __init__(self, raw_data : dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)

    @property
    def endOfGameResult(self) -> str:
        try:
            return self.raw_data['endOfGameResult']
        except KeyError as e:
            e.add_note('Could not retrieve endOfGameResult, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def gameCreation(self) -> int:
        try:
            return self.raw_data['gameCreation']
        except KeyError as e:
            e.add_note('Could not retrieve gameCreation, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def gameDuration(self) -> int:
        try:
            return self.raw_data['gameDuration']
        except KeyError as e:
            e.add_note('Could not retrieve gameDuration, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def gameEndTimestamp(self) -> int:
        try:
            return self.raw_data['gameEndTimestamp']
        except KeyError as e:
            e.add_note('Could not retrieve gameEndTimestamp, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def gameId(self) -> int:
        try:
            return self.raw_data['gameId']
        except KeyError as e:
            e.add_note('Could not retrieve gameId, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def gameMode(self) -> str:
        try:
            return self.raw_data['gameMode']
        except KeyError as e:
            e.add_note('Could not retrieve gameMode, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def gameName(self) -> str:
        try:
            return self.raw_data['gameName']
        except KeyError as e:
            e.add_note('Could not retrieve gameName, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def gameStartTimestamp(self) -> int:
        try:
            return self.raw_data['gameStartTimestamp']
        except KeyError as e:
            e.add_note('Could not retrieve gameStartTimestamp, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def gameType(self) -> str:
        try:
            return self.raw_data['gameType']
        except KeyError as e:
            e.add_note('Could not retrieve gameType, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def gameVersion(self) -> str:
        try:
            return self.raw_data['gameVersion']
        except KeyError as e:
            e.add_note('Could not retrieve gameVersion, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def mapId(self) -> int:
        try:
            return self.raw_data['mapId']
        except KeyError as e:
            e.add_note('Could not retrieve mapId, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def participants(self) -> list[ParticipantDto]: 
        try:
            participants = []
            for id in self.raw_data['participants']:
                participants.append(ParticipantDto(id))
            return participants
        except KeyError as e:
            e.add_note('Could not retrieve participants, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def platformId(self) -> str:
        try:
            return self.raw_data['platformId']
        except KeyError as e:
            e.add_note('Could not retrieve platformId, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def queueId(self) -> int:
        try:
            return self.raw_data['queueId']
        except KeyError as e:
            e.add_note('Could not retrieve queueId, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def teams(self) -> list[TeamDto]: 
        try:
            teams = []
            for id in self.raw_data['teams']:
                teams.append(TeamDto(id))
            return teams
        except KeyError as e:
            e.add_note('Could not retrieve teams, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def tournamentCode(self) -> str:
        try:
            return self.raw_data['tournamentCode']
        except KeyError as e:
            e.add_note('Could not retrieve tournamentCode, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        