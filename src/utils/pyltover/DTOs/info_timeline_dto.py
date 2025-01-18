from .participant_timeline_dto import ParticipantTimelineDto
from .frames_timeline_dto import FramesTimelineDto

class InfoTimelineDto():
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
    def frameInterval(self) -> int:
        try:
            return self.raw_data['frameInterval']
        except KeyError as e:
            e.add_note('Could not retrieve frameInterval, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def gameId(self) -> int:
        try:
            return self.raw_data['gameId']
        except KeyError as e:
            e.add_note('Could not retrieve gameId, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def participants(self) -> list[ParticipantTimelineDto]: 
        try:
            return [ParticipantTimelineDto(p) for p in self.raw_data['participants']]
        except KeyError as e:
            e.add_note('Could not retrieve participants, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def frames(self) -> list[FramesTimelineDto]: 
        try:
            return [FramesTimelineDto(f) for f in self.raw_data['frames']]
        except KeyError as e:
            e.add_note('Could not retrieve frames, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise