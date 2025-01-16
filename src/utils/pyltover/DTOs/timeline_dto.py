from pyltover.DTOs.metadata_timeline_dto import MetadataTimelineDto
from pyltover.DTOs.info_timeline_dto import InfoTimelineDto

class TimelineDto():
    def __init__(self, raw_data : dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def metadata(self) -> MetadataTimelineDto:
        try:
            return MetadataTimelineDto(self.raw_data['metadata'])
        except KeyError as e:
            e.add_note('Could not retrieve metadata, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def info(self) -> InfoTimelineDto: 
        try:
            return InfoTimelineDto(self.raw_data['info'])
        except KeyError as e:
            e.add_note('Could not retrieve info, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise