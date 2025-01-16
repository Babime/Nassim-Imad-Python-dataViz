from .metadata_dto import MetadataDto

class MatchDto():
    def __init__(self, raw_data : dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def metadata(self) -> MetadataDto:
        try:
            return MetadataDto(self.raw_data['metadata'])
        except KeyError as e:
            e.add_note('Could not retrieve metadata, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise 