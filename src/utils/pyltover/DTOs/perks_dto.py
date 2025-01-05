from pyltover.DTOs.perk_stat_dto import PerkStatDto
from pyltover.DTOs.perk_style_dto import PerkStyleDto


class PerksDto:
    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def statPerks(self) -> PerkStatDto:
        try:
            return PerkStatDto(self.raw_data['statPerks'])
        except KeyError as e:
            e.add_note('Could not retrieve statPerks, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def styles(self) -> list[PerkStyleDto]:
        from pyltover.DTOs.perk_style_dto import PerkStyleDto
        try:
            list_of_styles = []
            for style in self.raw_data['styles']:
                list_of_styles.append(PerkStyleDto(style))
            return list_of_styles
        except KeyError as e:
            e.add_note('Could not retrieve styles, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise