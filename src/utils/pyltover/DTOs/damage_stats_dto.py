class DamageStatsDto():
    def __init__(self, raw_data : dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    

    @property
    def magicDamageDone(self) -> int:
        try:
            return self.raw_data['magicDamageDone']
        except KeyError as e:
            e.add_note('Could not retrieve magicDamageDone, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def magicDamageDoneToChampions(self) -> int:
        try:
            return self.raw_data['magicDamageDoneToChampions']
        except KeyError as e:
            e.add_note('Could not retrieve magicDamageDoneToChampions, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def magicDamageTaken(self) -> int:
        try:
            return self.raw_data['magicDamageTaken']
        except KeyError as e:
            e.add_note('Could not retrieve magicDamageTaken, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def physicalDamageDone(self) -> int:
        try:
            return self.raw_data['physicalDamageDone']
        except KeyError as e:
            e.add_note('Could not retrieve physicalDamageDone, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def physicalDamageDoneToChampions(self) -> int:
        try:
            return self.raw_data['physicalDamageDoneToChampions']
        except KeyError as e:
            e.add_note('Could not retrieve physicalDamageDoneToChampions, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def physicalDamageTaken(self) -> int:
        try:
            return self.raw_data['physicalDamageTaken']
        except KeyError as e:
            e.add_note('Could not retrieve physicalDamageTaken, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def totalDamageDone(self) -> int:
        try:
            return self.raw_data['totalDamageDone']
        except KeyError as e:
            e.add_note('Could not retrieve totalDamageDone, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def totalDamageDoneToChampions(self) -> int:
        try:
            return self.raw_data['totalDamageDoneToChampions']
        except KeyError as e:
            e.add_note('Could not retrieve totalDamageDoneToChampions, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def totalDamageTaken(self) -> int:
        try:
            return self.raw_data['totalDamageTaken']
        except KeyError as e:
            e.add_note('Could not retrieve totalDamageTaken, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def trueDamageDone(self) -> int:
        try:
            return self.raw_data['trueDamageDone']
        except KeyError as e:
            e.add_note('Could not retrieve trueDamageDone, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def trueDamageDoneToChampions(self) -> int:
        try:
            return self.raw_data['trueDamageDoneToChampions']
        except KeyError as e:
            e.add_note('Could not retrieve trueDamageDoneToChampions, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def trueDamageTaken(self) -> int:
        try:
            return self.raw_data['trueDamageTaken']
        except KeyError as e:
            e.add_note('Could not retrieve trueDamageTaken, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        