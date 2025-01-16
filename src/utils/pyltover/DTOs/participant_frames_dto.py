from participant_frame_dto import ParticipantFrameDto

class ParticipantFramesDto():
    def __init__(self, raw_data : dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def participantFrame(self) -> dict: 
        try:
            return {int(key): ParticipantFrameDto(value) for key, value in self.raw_data['participantFrames'].items()}
        except KeyError as e:
            e.add_note('Could not retrieve participantFrames, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise