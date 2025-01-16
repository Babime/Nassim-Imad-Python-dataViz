from participant_frames_dto import ParticipantFramesDto
from events_timeline_dto import EventsTimelineDto

class FramesTimelineDto():
    def __init__(self, raw_data : dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def events(self) -> list[EventsTimelineDto]: 
        try:
            return [EventsTimelineDto(event) for event in self.raw_data['events']]
        except KeyError as e:
            e.add_note('Could not retrieve events, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def participantFrames(self) -> ParticipantFramesDto:
        try:
            return ParticipantFramesDto(self.raw_data['participantFrames'])
        except KeyError as e:
            e.add_note('Could not retrieve participantFrames, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def timestamp(self) -> int:
        try:
            return self.raw_data['timestamp']
        except KeyError as e:
            e.add_note('Could not retrieve timestamp, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    