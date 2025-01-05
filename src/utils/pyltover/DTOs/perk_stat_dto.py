class PerkStatDto:
    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def defense(self) -> int:
        try:
            return self.raw_data['defense']
        except KeyError as e:
            e.add_note('Could not retrieve defense, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def flex(self) -> int:
        try:
            return self.raw_data['flex']
        except KeyError as e:
            e.add_note('Could not retrieve flex, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def offense(self) -> int:
        try:
            return self.raw_data['offense']
        except KeyError as e:
            e.add_note('Could not retrieve offense, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise