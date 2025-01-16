class ChampionStatsDto():
    def __init__(self, raw_data : dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def abilityHaste(self) -> int:
        try:
            return self.raw_data['abilityHaste']
        except KeyError as e:
            e.add_note('Could not retrieve abilityHaste, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def abilityPower(self) -> int:
        try:
            return self.raw_data['abilityPower']
        except KeyError as e:
            e.add_note('Could not retrieve abilityPower, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def armor(self) -> int:
        try:
            return self.raw_data['armor']
        except KeyError as e:
            e.add_note('Could not retrieve armor, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property 
    def armorPen(self) -> int:
        try:
            return self.raw_data['armorPen']
        except KeyError as e:
            e.add_note('Could not retrieve armorPen, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def armorPenPercent(self) -> int:
        try:
            return self.raw_data['armorPenPercent']
        except KeyError as e:
            e.add_note('Could not retrieve armorPenPercent, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def attachDamage(self) -> int:
        try:
            return self.raw_data['attachDamage']
        except KeyError as e:
            e.add_note('Could not retrieve attachDamage, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def attackSpeed(self) -> int:
        try:
            return self.raw_data['attackSpeed']
        except KeyError as e:
            e.add_note('Could not retrieve attackSpeed, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def bonusArmorPenPercent(self) -> int:
        try:
            return self.raw_data['bonusArmorPenPercent']
        except KeyError as e:
            e.add_note('Could not retrieve bonusArmorPenPercent, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def bonusMagicPenPercent(self) -> int:
        try:
            return self.raw_data['bonusMagicPenPercent']
        except KeyError as e:
            e.add_note('Could not retrieve bonusMagicPenPercent, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def ccReduction(self) -> int:
        try:
            return self.raw_data['ccReduction']
        except KeyError as e:
            e.add_note('Could not retrieve ccReduction, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def cooldownReduction(self) -> int:
        try:
            return self.raw_data['cooldownReduction']
        except KeyError as e:
            e.add_note('Could not retrieve cooldownReduction, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def health(self) -> int:
        try:
            return self.raw_data['health']
        except KeyError as e:
            e.add_note('Could not retrieve health, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def healthMax(self) -> int:
        try:
            return self.raw_data['healthMax']
        except KeyError as e:
            e.add_note('Could not retrieve healthMax, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def healthRegen(self) -> int:
        try:
            return self.raw_data['healthRegen']
        except KeyError as e:
            e.add_note('Could not retrieve healthRegen, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def lifesteal(self) -> int:
        try:
            return self.raw_data['lifesteal']
        except KeyError as e:
            e.add_note('Could not retrieve lifesteal, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def magicPen(self) -> int:
        try:
            return self.raw_data['magicPen']
        except KeyError as e:
            e.add_note('Could not retrieve magicPen, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def magicPenPercent(self) -> int:
        try:
            return self.raw_data['magicPenPercent']
        except KeyError as e:
            e.add_note('Could not retrieve magicPenPercent, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def magicResist(self) -> int:
        try:
            return self.raw_data['magicResist']
        except KeyError as e:
            e.add_note('Could not retrieve magicResist, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def movementSpeed(self) -> int:
        try:
            return self.raw_data['movementSpeed']
        except KeyError as e:
            e.add_note('Could not retrieve movementSpeed, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def omnivamp(self) -> int:
        try:
            return self.raw_data['omnivamp']
        except KeyError as e:
            e.add_note('Could not retrieve omnivamp, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def physicalVamp(self) -> int:
        try:
            return self.raw_data['physicalVamp']
        except KeyError as e:
            e.add_note('Could not retrieve physicalVamp, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def power(self) -> int:
        try:
            return self.raw_data['power']
        except KeyError as e:
            e.add_note('Could not retrieve power, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def powerMax(self) -> int:
        try:
            return self.raw_data['powerMax']
        except KeyError as e:
            e.add_note('Could not retrieve powerMax, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def powerRegen(self) -> int:
        try:
            return self.raw_data['powerRegen']
        except KeyError as e:
            e.add_note('Could not retrieve powerRegen, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def spellVamp(self) -> int:
        try:
            return self.raw_data['spellVamp']
        except KeyError as e:
            e.add_note('Could not retrieve spellVamp, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        