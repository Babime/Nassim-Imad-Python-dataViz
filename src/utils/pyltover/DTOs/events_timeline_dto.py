class EventsTimelineDto():
    def __init__(self, raw_data : dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def timestamp(self) -> int:
        try:
            return self.raw_data['timestamp']
        except KeyError as e:
            e.add_note('Could not retrieve timestamp, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def realTimestamp(self) -> int:
        try:
            return self.raw_data['realTimestamp']
        except KeyError as e:
            e.add_note('Could not retrieve realTimestamp, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def type(self) -> str:
        try:
            return self.raw_data['type']
        except KeyError as e:
            e.add_note('Could not retrieve type, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise