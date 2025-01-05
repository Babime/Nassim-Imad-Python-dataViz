class MetadataDto():
    def __init__(self, raw_data : dict):
        self.raw_data = raw_data
    
    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def dataVersion(self) -> str:
        try:
            return self.raw_data['dataVersion']
        except KeyError as e:
            e.add_note('Could not retrieve dataVersion, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def matchId(self) -> str:
        try:
            return self.raw_data['matchId']
        except KeyError as e:
            e.add_note('Could not retrieve matchId, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def participants(self) -> list:
        try:
            return self.raw_data['participants']
        except KeyError as e:
            e.add_note('Could not retrieve participants, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise