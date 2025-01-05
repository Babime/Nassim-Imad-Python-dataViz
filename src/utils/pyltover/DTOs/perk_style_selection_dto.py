class PerkStyleSelectionDto:
    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def perk(self) -> int:
        try:
            return self.raw_data['perk']
        except KeyError as e:
            e.add_note('Could not retrieve perk, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def var1(self) -> int:
        try:
            return self.raw_data['var1']
        except KeyError as e:
            e.add_note('Could not retrieve perkStyle, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def var2(self) -> int:
        try:
            return self.raw_data['var2']
        except KeyError as e:
            e.add_note('Could not retrieve var2, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def var3(self) -> int:
        try:
            return self.raw_data['var3']
        except KeyError as e:
            e.add_note('Could not retrieve var3, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
