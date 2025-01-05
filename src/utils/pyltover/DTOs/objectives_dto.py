from pyltover.DTOs.objective_dto import ObjectiveDto


class ObjectivesDto:
    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def baron(self) -> ObjectiveDto:
        try:
            return ObjectiveDto(self.raw_data['baron'])
        except KeyError as e:
            e.add_note('Could not retrieve baron, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def champion(self) -> ObjectiveDto:
        try:
            return ObjectiveDto(self.raw_data['champion'])
        except KeyError as e:
            e.add_note('Could not retrieve champion, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def dragon(self) -> ObjectiveDto:
        try:
            return ObjectiveDto(self.raw_data['dragon'])
        except KeyError as e:
            e.add_note('Could not retrieve dragon, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def horde(self) -> ObjectiveDto:
        try:
            return ObjectiveDto(self.raw_data['horde'])
        except KeyError as e:
            e.add_note('Could not retrieve inhhordeibitor, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def inhibitor(self) -> ObjectiveDto:
        try:
            return ObjectiveDto(self.raw_data['inhibitor'])
        except KeyError as e:
            e.add_note('Could not retrieve inhibitor, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def riftHerald(self) -> ObjectiveDto:
        try:
            return ObjectiveDto(self.raw_data['riftHerald'])
        except KeyError as e:
            e.add_note('Could not retrieve riftHerald, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def tower(self) -> ObjectiveDto:
        try:
            return ObjectiveDto(self.raw_data['tower'])
        except KeyError as e:
            e.add_note('Could not retrieve tower, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise