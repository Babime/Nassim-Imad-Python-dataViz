class MissionDto:
    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)

    @property
    def playerScore0(self) -> int:
        try:
            return self.raw_data['playerScore0']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore0	int	, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def playerScore1(self) -> int:
        try:
            return self.raw_data['playerScore1']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore1	int	, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def playerScore2(self) -> int:
        try:
            return self.raw_data['playerScore2']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore2	int	, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def playerScore3(self) -> int:
        try:
            return self.raw_data['playerScore3']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore3	int	, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def playerScore4(self) -> int:
        try:
            return self.raw_data['playerScore4']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore4	int	, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def playerScore5(self) -> int:
        try:
            return self.raw_data['playerScore5']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore5	int	, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def playerScore6(self) -> int:
        try:
            return self.raw_data['playerScore6']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore6	int	, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def playerScore7(self) -> int:
        try:
            return self.raw_data['playerScore7']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore7	int	, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def playerScore8(self) -> int:
        try:
            return self.raw_data['playerScore8']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore8	int	, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def playerScore9(self) -> int:
        try:
            return self.raw_data['playerScore9']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore9	int	, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def playerScore10(self) -> int:
        try:
            return self.raw_data['playerScore10']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore10	int	, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def playerScore11(self) -> int:
        try:
            return self.raw_data['playerScore11']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore11	int, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

