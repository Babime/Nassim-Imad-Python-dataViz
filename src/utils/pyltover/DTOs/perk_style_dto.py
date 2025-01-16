from .perk_style_selection_dto import PerkStyleSelectionDto


class PerkStyleDto:
    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def description(self) -> str:
        try:
            return self.raw_data['description']
        except KeyError as e:
            e.add_note('Could not retrieve description, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def selections(self) -> list[PerkStyleSelectionDto]:
        try:
            list_of_selections = []
            for selection in self.raw_data['selections']:
                list_of_selections.append(PerkStyleSelectionDto(selection))
            return list_of_selections
        except KeyError as e:
            e.add_note('Could not retrieve selections, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def style(self) -> int:
        try:
            return self.raw_data['style']
        except KeyError as e:
            e.add_note('Could not retrieve style, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise