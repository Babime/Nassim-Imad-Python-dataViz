class ObjectiveDto:
    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def first(self) -> bool:
        try:
            return self.raw_data['first']
        except KeyError as e:
            e.add_note('Could not retrieve first, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def kills(self) -> int:
        try:
            return self.raw_data['kills']
        except KeyError as e:
            e.add_note('Could not retrieve kills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    