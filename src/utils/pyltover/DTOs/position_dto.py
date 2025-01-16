class PositionDto():
    def __init__(self, raw_data : dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def x(self) -> int:
        try:
            return self.raw_data['x']
        except KeyError as e:
            e.add_note('Could not retrieve x, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def y(self) -> int:
        try:
            return self.raw_data['y']
        except KeyError as e:
            e.add_note('Could not retrieve y, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise