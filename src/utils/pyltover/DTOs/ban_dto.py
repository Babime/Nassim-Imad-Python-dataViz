class BanDto:
    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def championId(self) -> int:
        try:
            return self.raw_data['championId']
        except KeyError as e:
            e.add_note('Could not retrieve championId, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def pickTurn(self) -> int:
        try:
            return self.raw_data['pickTurn']
        except KeyError as e:
            e.add_note('Could not retrieve pickTurn, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    