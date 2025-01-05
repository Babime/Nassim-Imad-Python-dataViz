class ChallengesDto:
    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)

    @property
    def AssistStreakCount(self) -> int:
        try:
            return self.raw_data['12AssistStreakCount']
        except KeyError as e:
            e.add_note('Could not retrieve 12AssistStreakCount, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def baronBuffGoldAdvantageOverThreshold(self) -> int:
        try:
            return self.raw_data['baronBuffGoldAdvantageOverThreshold']
        except KeyError as e:
            e.add_note('Could not retrieve baronBuffGoldAdvantageOverThreshold, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def controlWardTimeCoverageInRiverOrEnemyHalf(self) -> float:
        try:
            return self.raw_data['controlWardTimeCoverageInRiverOrEnemyHalf']
        except KeyError as e:
            e.add_note('Could not retrieve controlWardTimeCoverageInRiverOrEnemyHalf, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def earliestBaron(self) -> int:
        try:
            return self.raw_data['earliestBaron']
        except KeyError as e:
            e.add_note('Could not retrieve earliestBaron, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def earliestDragonTakedown(self) -> int:
        try:
            return self.raw_data['earliestDragonTakedown']
        except KeyError as e:
            e.add_note('Could not retrieve earliestDragonTakedown, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def earliestElderDragon(self) -> int:
        try:
            return self.raw_data['earliestElderDragon']
        except KeyError as e:
            e.add_note('Could not retrieve earliestElderDragon, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def earlyLaningPhaseGoldExpAdvantage(self) -> int:
        try:
            return self.raw_data['earlyLaningPhaseGoldExpAdvantage']
        except KeyError as e:
            e.add_note('Could not retrieve earlyLaningPhaseGoldExpAdvantage, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def fasterSupportQuestCompletion(self) -> int:
        try:
            return self.raw_data['fasterSupportQuestCompletion']
        except KeyError as e:
            e.add_note('Could not retrieve fasterSupportQuestCompletion, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def fastestLegendary(self) -> int:
        try:
            return self.raw_data['fastestLegendary']
        except KeyError as e:
            e.add_note('Could not retrieve fastestLegendary, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def hadAfkTeammate(self) -> int:
        try:
            return self.raw_data['hadAfkTeammate']
        except KeyError as e:
            e.add_note('Could not retrieve hadAfkTeammate, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def highestChampionDamage(self) -> int:
        try:
            return self.raw_data['highestChampionDamage']
        except KeyError as e:
            e.add_note('Could not retrieve highestChampionDamage, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def highestCrowdControlScore(self) -> int:
        try:
            return self.raw_data['highestCrowdControlScore']
        except KeyError as e:
            e.add_note('Could not retrieve highestCrowdControlScore, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def highestWardKills(self) -> int:
        try:
            return self.raw_data['highestWardKills']
        except KeyError as e:
            e.add_note('Could not retrieve highestWardKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def junglerKillsEarlyJungle(self) -> int:
        try:
            return self.raw_data['junglerKillsEarlyJungle']
        except KeyError as e:
            e.add_note('Could not retrieve junglerKillsEarlyJungle, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def killsOnLanersEarlyJungleAsJungler(self) -> int:
        try:
            return self.raw_data['killsOnLanersEarlyJungleAsJungler']
        except KeyError as e:
            e.add_note('Could not retrieve killsOnLanersEarlyJungleAsJungler, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def laningPhaseGoldExpAdvantage(self) -> int:
        try:
            return self.raw_data['laningPhaseGoldExpAdvantage']
        except KeyError as e:
            e.add_note('Could not retrieve laningPhaseGoldExpAdvantage, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def legendaryCount(self) -> int:
        try:
            return self.raw_data['legendaryCount']
        except KeyError as e:
            e.add_note('Could not retrieve legendaryCount, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def maxCsAdvantageOnLaneOpponent(self) -> float:
        try:
            return self.raw_data['maxCsAdvantageOnLaneOpponent']
        except KeyError as e:
            e.add_note('Could not retrieve maxCsAdvantageOnLaneOpponent, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def maxLevelLeadLaneOpponent(self) -> int:
        try:
            return self.raw_data['maxLevelLeadLaneOpponent']
        except KeyError as e:
            e.add_note('Could not retrieve maxLevelLeadLaneOpponent, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def mostWardsDestroyedOneSweeper(self) -> int:
        try:
            return self.raw_data['mostWardsDestroyedOneSweeper']
        except KeyError as e:
            e.add_note('Could not retrieve mostWardsDestroyedOneSweeper, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def mythicItemUsed(self) -> int:
        try:
            return self.raw_data['mythicItemUsed']
        except KeyError as e:
            e.add_note('Could not retrieve mythicItemUsed, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def playedChampSelectPosition(self) -> int:
        try:
            return self.raw_data['playedChampSelectPosition']
        except KeyError as e:
            e.add_note('Could not retrieve playedChampSelectPosition, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def soloTurretsLategame(self) -> int:
        try:
            return self.raw_data['soloTurretsLategame']
        except KeyError as e:
            e.add_note('Could not retrieve soloTurretsLategame, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def takedownsFirst25Minutes(self) -> int:
        try:
            return self.raw_data['takedownsFirst25Minutes']
        except KeyError as e:
            e.add_note('Could not retrieve takedownsFirst25Minutes, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def teleportTakedowns(self) -> int:
        try:
            return self.raw_data['teleportTakedowns']
        except KeyError as e:
            e.add_note('Could not retrieve teleportTakedowns, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def thirdInhibitorDestroyedTime(self) -> int:
        try:
            return self.raw_data['thirdInhibitorDestroyedTime']
        except KeyError as e:
            e.add_note('Could not retrieve thirdInhibitorDestroyedTime, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def threeWardsOneSweeperCount(self) -> int:
        try:
            return self.raw_data['threeWardsOneSweeperCount']
        except KeyError as e:
            e.add_note('Could not retrieve threeWardsOneSweeperCount, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def visionScoreAdvantageLaneOpponent(self) -> float:
        try:
            return self.raw_data['visionScoreAdvantageLaneOpponent']
        except KeyError as e:
            e.add_note('Could not retrieve visionScoreAdvantageLaneOpponent, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def InfernalScalePickup(self) -> int:
        try:
            return self.raw_data['InfernalScalePickup']
        except KeyError as e:
            e.add_note('Could not retrieve InfernalScalePickup, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def fistBumpParticipation(self) -> int:
        try:
            return self.raw_data['fistBumpParticipation']
        except KeyError as e:
            e.add_note('Could not retrieve fistBumpParticipation, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def voidMonsterKill(self) -> int:
        try:
            return self.raw_data['voidMonsterKill']
        except KeyError as e:
            e.add_note('Could not retrieve voidMonsterKill, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def abilityUses(self) -> int:
        try:
            return self.raw_data['abilityUses']
        except KeyError as e:
            e.add_note('Could not retrieve abilityUses, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def acesBefore15Minutes(self) -> int:
        try:
            return self.raw_data['acesBefore15Minutes']
        except KeyError as e:
            e.add_note('Could not retrieve acesBefore15Minutes, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def alliedJungleMonsterKills(self) -> float:
        try:
            return self.raw_data['alliedJungleMonsterKills']
        except KeyError as e:
            e.add_note('Could not retrieve alliedJungleMonsterKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def baronTakedowns(self) -> int:
        try:
            return self.raw_data['baronTakedowns']
        except KeyError as e:
            e.add_note('Could not retrieve baronTakedowns, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def blastConeOppositeOpponentCount(self) -> int:
        try:
            return self.raw_data['blastConeOppositeOpponentCount']
        except KeyError as e:
            e.add_note('Could not retrieve blastConeOppositeOpponentCount, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def bountyGold(self) -> int:
        try:
            return self.raw_data['bountyGold']
        except KeyError as e:
            e.add_note('Could not retrieve bountyGold, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def buffsStolen(self) -> int:
        try:
            return self.raw_data['buffsStolen']
        except KeyError as e:
            e.add_note('Could not retrieve buffsStolen, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def completeSupportQuestInTime(self) -> int:
        try:
            return self.raw_data['completeSupportQuestInTime']
        except KeyError as e:
            e.add_note('Could not retrieve completeSupportQuestInTime, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def controlWardsPlaced(self) -> int:
        try:
            return self.raw_data['controlWardsPlaced']
        except KeyError as e:
            e.add_note('Could not retrieve controlWardsPlaced, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def damagePerMinute(self) -> float:
        try:
            return self.raw_data['damagePerMinute']
        except KeyError as e:
            e.add_note('Could not retrieve damagePerMinute, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def damageTakenOnTeamPercentage(self) -> float:
        try:
            return self.raw_data['damageTakenOnTeamPercentage']
        except KeyError as e:
            e.add_note('Could not retrieve damageTakenOnTeamPercentage, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def dancedWithRiftHerald(self) -> int:
        try:
            return self.raw_data['dancedWithRiftHerald']
        except KeyError as e:
            e.add_note('Could not retrieve dancedWithRiftHerald, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def deathsByEnemyChamps(self) -> int:
        try:
            return self.raw_data['deathsByEnemyChamps']
        except KeyError as e:
            e.add_note('Could not retrieve deathsByEnemyChamps, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def dodgeSkillShotsSmallWindow(self) -> int:
        try:
            return self.raw_data['dodgeSkillShotsSmallWindow']
        except KeyError as e:
            e.add_note('Could not retrieve dodgeSkillShotsSmallWindow, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def doubleAces(self) -> int:
        try:
            return self.raw_data['doubleAces']
        except KeyError as e:
            e.add_note('Could not retrieve doubleAces, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def dragonTakedowns(self) -> int:
        try:
            return self.raw_data['dragonTakedowns']
        except KeyError as e:
            e.add_note('Could not retrieve dragonTakedowns, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def legendaryItemUsed(self) -> list[int]:
        try:
            return self.raw_data['legendaryItemUsed']
        except KeyError as e:
            e.add_note('Could not retrieve legendaryItemUsed, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def effectiveHealAndShielding(self) -> float:
        try:
            return self.raw_data['effectiveHealAndShielding']
        except KeyError as e:
            e.add_note('Could not retrieve effectiveHealAndShielding, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def elderDragonKillsWithOpposingSoul(self) -> int:
        try:
            return self.raw_data['elderDragonKillsWithOpposingSoul']
        except KeyError as e:
            e.add_note('Could not retrieve elderDragonKillsWithOpposingSoul, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def elderDragonMultikills(self) -> int:
        try:
            return self.raw_data['elderDragonMultikills']
        except KeyError as e:
            e.add_note('Could not retrieve elderDragonMultikills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def enemyChampionImmobilizations(self) -> int:
        try:
            return self.raw_data['enemyChampionImmobilizations']
        except KeyError as e:
            e.add_note('Could not retrieve enemyChampionImmobilizations, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def enemyJungleMonsterKills(self) -> float:
        try:
            return self.raw_data['enemyJungleMonsterKills']
        except KeyError as e:
            e.add_note('Could not retrieve enemyJungleMonsterKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def epicMonsterKillsNearEnemyJungler(self) -> int:
        try:
            return self.raw_data['epicMonsterKillsNearEnemyJungler']
        except KeyError as e:
            e.add_note('Could not retrieve epicMonsterKillsNearEnemyJungler, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def epicMonsterKillsWithin30SecondsOfSpawn(self) -> int:
        try:
            return self.raw_data['epicMonsterKillsWithin30SecondsOfSpawn']
        except KeyError as e:
            e.add_note('Could not retrieve epicMonsterKillsWithin30SecondsOfSpawn, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def epicMonsterSteals(self) -> int:
        try:
            return self.raw_data['epicMonsterSteals']
        except KeyError as e:
            e.add_note('Could not retrieve epicMonsterSteals, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def epicMonsterStolenWithoutSmite(self) -> int:
        try:
            return self.raw_data['epicMonsterStolenWithoutSmite']
        except KeyError as e:
            e.add_note('Could not retrieve epicMonsterStolenWithoutSmite, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def firstTurretKilled(self) -> int:
        try:
            return self.raw_data['firstTurretKilled']
        except KeyError as e:
            e.add_note('Could not retrieve firstTurretKilled, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def firstTurretKilledTime(self) -> float:
        try:
            return self.raw_data['firstTurretKilledTime']
        except KeyError as e:
            e.add_note('Could not retrieve firstTurretKilledTime, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def flawlessAces(self) -> int:
        try:
            return self.raw_data['flawlessAces']
        except KeyError as e:
            e.add_note('Could not retrieve flawlessAces, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def fullTeamTakedown(self) -> int:
        try:
            return self.raw_data['fullTeamTakedown']
        except KeyError as e:
            e.add_note('Could not retrieve fullTeamTakedown, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def gameLength(self) -> float:
        try:
            return self.raw_data['gameLength']
        except KeyError as e:
            e.add_note('Could not retrieve gameLength, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def getTakedownsInAllLanesEarlyJungleAsLaner(self) -> int:
        try:
            return self.raw_data['getTakedownsInAllLanesEarlyJungleAsLaner']
        except KeyError as e:
            e.add_note('Could not retrieve getTakedownsInAllLanesEarlyJungleAsLaner, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def goldPerMinute(self) -> float:
        try:
            return self.raw_data['goldPerMinute']
        except KeyError as e:
            e.add_note('Could not retrieve goldPerMinute, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def hadOpenNexus(self) -> int:
        try:
            return self.raw_data['hadOpenNexus']
        except KeyError as e:
            e.add_note('Could not retrieve hadOpenNexus, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def immobilizeAndKillWithAlly(self) -> int:
        try:
            return self.raw_data['immobilizeAndKillWithAlly']
        except KeyError as e:
            e.add_note('Could not retrieve immobilizeAndKillWithAlly, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def initialBuffCount(self) -> int:
        try:
            return self.raw_data['initialBuffCount']
        except KeyError as e:
            e.add_note('Could not retrieve initialBuffCount, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def initialCrabCount(self) -> int:
        try:
            return self.raw_data['initialCrabCount']
        except KeyError as e:
            e.add_note('Could not retrieve initialCrabCount, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def jungleCsBefore10Minutes(self) -> float:
        try:
            return self.raw_data['jungleCsBefore10Minutes']
        except KeyError as e:
            e.add_note('Could not retrieve jungleCsBefore10Minutes, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def junglerTakedownsNearDamagedEpicMonster(self) -> int:
        try:
            return self.raw_data['junglerTakedownsNearDamagedEpicMonster']
        except KeyError as e:
            e.add_note('Could not retrieve junglerTakedownsNearDamagedEpicMonster, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def kda(self) -> float:
        try:
            return self.raw_data['kda']
        except KeyError as e:
            e.add_note('Could not retrieve kda, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def killAfterHiddenWithAlly(self) -> int:
        try:
            return self.raw_data['killAfterHiddenWithAlly']
        except KeyError as e:
            e.add_note('Could not retrieve killAfterHiddenWithAlly, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def killedChampTookFullTeamDamageSurvived(self) -> int:
        try:
            return self.raw_data['killedChampTookFullTeamDamageSurvived']
        except KeyError as e:
            e.add_note('Could not retrieve killedChampTookFullTeamDamageSurvived, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def killingSprees(self) -> int:
        try:
            return self.raw_data['killingSprees']
        except KeyError as e:
            e.add_note('Could not retrieve killingSprees, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def killParticipation(self) -> float:
        try:
            return self.raw_data['killParticipation']
        except KeyError as e:
            e.add_note('Could not retrieve killParticipation, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def killsNearEnemyTurret(self) -> int:
        try:
            return self.raw_data['killsNearEnemyTurret']
        except KeyError as e:
            e.add_note('Could not retrieve killsNearEnemyTurret, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def killsOnOtherLanesEarlyJungleAsLaner(self) -> int:
        try:
            return self.raw_data['killsOnOtherLanesEarlyJungleAsLaner']
        except KeyError as e:
            e.add_note('Could not retrieve killsOnOtherLanesEarlyJungleAsLaner, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def killsOnRecentlyHealedByAramPack(self) -> int:
        try:
            return self.raw_data['killsOnRecentlyHealedByAramPack']
        except KeyError as e:
            e.add_note('Could not retrieve killsOnRecentlyHealedByAramPack, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def killsUnderOwnTurret(self) -> int:
        try:
            return self.raw_data['killsUnderOwnTurret']
        except KeyError as e:
            e.add_note('Could not retrieve killsUnderOwnTurret, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def killsWithHelpFromEpicMonster(self) -> int:
        try:
            return self.raw_data['killsWithHelpFromEpicMonster']
        except KeyError as e:
            e.add_note('Could not retrieve killsWithHelpFromEpicMonster, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def knockEnemyIntoTeamAndKill(self) -> int:
        try:
            return self.raw_data['knockEnemyIntoTeamAndKill']
        except KeyError as e:
            e.add_note('Could not retrieve knockEnemyIntoTeamAndKill, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def kTurretsDestroyedBeforePlatesFall(self) -> int:
        try:
            return self.raw_data['kTurretsDestroyedBeforePlatesFall']
        except KeyError as e:
            e.add_note('Could not retrieve kTurretsDestroyedBeforePlatesFall, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def landSkillShotsEarlyGame(self) -> int:
        try:
            return self.raw_data['landSkillShotsEarlyGame']
        except KeyError as e:
            e.add_note('Could not retrieve landSkillShotsEarlyGame, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def laneMinionsFirst10Minutes(self) -> int:
        try:
            return self.raw_data['laneMinionsFirst10Minutes']
        except KeyError as e:
            e.add_note('Could not retrieve laneMinionsFirst10Minutes, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def lostAnInhibitor(self) -> int:
        try:
            return self.raw_data['lostAnInhibitor']
        except KeyError as e:
            e.add_note('Could not retrieve lostAnInhibitor, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def maxKillDeficit(self) -> int:
        try:
            return self.raw_data['maxKillDeficit']
        except KeyError as e:
            e.add_note('Could not retrieve maxKillDeficit, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def mejaisFullStackInTime(self) -> int:
        try:
            return self.raw_data['mejaisFullStackInTime']
        except KeyError as e:
            e.add_note('Could not retrieve mejaisFullStackInTime, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def moreEnemyJungleThanOpponent(self) -> float:
        try:
            return self.raw_data['moreEnemyJungleThanOpponent']
        except KeyError as e:
            e.add_note('Could not retrieve moreEnemyJungleThanOpponent, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def multiKillOneSpell(self) -> int:
        try:
            return self.raw_data['multiKillOneSpell']
        except KeyError as e:
            e.add_note('Could not retrieve multiKillOneSpell, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def multikills(self) -> int:
        try:
            return self.raw_data['multikills']
        except KeyError as e:
            e.add_note('Could not retrieve multikills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def multikillsAfterAggressiveFlash(self) -> int:
        try:
            return self.raw_data['multikillsAfterAggressiveFlash']
        except KeyError as e:
            e.add_note('Could not retrieve multikillsAfterAggressiveFlash, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def multiTurretRiftHeraldCount(self) -> int:
        try:
            return self.raw_data['multiTurretRiftHeraldCount']
        except KeyError as e:
            e.add_note('Could not retrieve multiTurretRiftHeraldCount, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def outerTurretExecutesBefore10Minutes(self) -> int:
        try:
            return self.raw_data['outerTurretExecutesBefore10Minutes']
        except KeyError as e:
            e.add_note('Could not retrieve outerTurretExecutesBefore10Minutes, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def outnumberedKills(self) -> int:
        try:
            return self.raw_data['outnumberedKills']
        except KeyError as e:
            e.add_note('Could not retrieve outnumberedKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def outnumberedNexusKill(self) -> int:
        try:
            return self.raw_data['outnumberedNexusKill']
        except KeyError as e:
            e.add_note('Could not retrieve outnumberedNexusKill, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def perfectDragonSoulsTaken(self) -> int:
        try:
            return self.raw_data['perfectDragonSoulsTaken']
        except KeyError as e:
            e.add_note('Could not retrieve perfectDragonSoulsTaken, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def perfectGame(self) -> int:
        try:
            return self.raw_data['perfectGame']
        except KeyError as e:
            e.add_note('Could not retrieve perfectGame, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def pickKillWithAlly(self) -> int:
        try:
            return self.raw_data['pickKillWithAlly']
        except KeyError as e:
            e.add_note('Could not retrieve pickKillWithAlly, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def poroExplosions(self) -> int:
        try:
            return self.raw_data['poroExplosions']
        except KeyError as e:
            e.add_note('Could not retrieve poroExplosions, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def quickCleanse(self) -> int:
        try:
            return self.raw_data['quickCleanse']
        except KeyError as e:
            e.add_note('Could not retrieve quickCleanse, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def quickFirstTurret(self) -> int:
        try:
            return self.raw_data['quickFirstTurret']
        except KeyError as e:
            e.add_note('Could not retrieve quickFirstTurret, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def quickSoloKills(self) -> int:
        try:
            return self.raw_data['quickSoloKills']
        except KeyError as e:
            e.add_note('Could not retrieve quickSoloKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def riftHeraldTakedowns(self) -> int:
        try:
            return self.raw_data['riftHeraldTakedowns']
        except KeyError as e:
            e.add_note('Could not retrieve riftHeraldTakedowns, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def saveAllyFromDeath(self) -> int:
        try:
            return self.raw_data['saveAllyFromDeath']
        except KeyError as e:
            e.add_note('Could not retrieve saveAllyFromDeath, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def scuttleCrabKills(self) -> int:
        try:
            return self.raw_data['scuttleCrabKills']
        except KeyError as e:
            e.add_note('Could not retrieve scuttleCrabKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def shortestTimeToAceFromFirstTakedown(self) -> float:
        try:
            return self.raw_data['shortestTimeToAceFromFirstTakedown']
        except KeyError as e:
            e.add_note('Could not retrieve shortestTimeToAceFromFirstTakedown, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def skillshotsDodged(self) -> int:
        try:
            return self.raw_data['skillshotsDodged']
        except KeyError as e:
            e.add_note('Could not retrieve skillshotsDodged, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def skillshotsHit(self) -> int:
        try:
            return self.raw_data['skillshotsHit']
        except KeyError as e:
            e.add_note('Could not retrieve skillshotsHit, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def snowballsHit(self) -> int:
        try:
            return self.raw_data['snowballsHit']
        except KeyError as e:
            e.add_note('Could not retrieve snowballsHit, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def soloBaronKills(self) -> int:
        try:
            return self.raw_data['soloBaronKills']
        except KeyError as e:
            e.add_note('Could not retrieve soloBaronKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def SWARM_DefeatAatrox(self) -> int:
        try:
            return self.raw_data['SWARM_DefeatAatrox']
        except KeyError as e:
            e.add_note('Could not retrieve SWARM_DefeatAatrox, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def SWARM_DefeatBriar(self) -> int:
        try:
            return self.raw_data['SWARM_DefeatBriar']
        except KeyError as e:
            e.add_note('Could not retrieve SWARM_DefeatBriar, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def SWARM_DefeatMiniBosses(self) -> int:
        try:
            return self.raw_data['SWARM_DefeatMiniBosses']
        except KeyError as e:
            e.add_note('Could not retrieve SWARM_DefeatMiniBosses, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def SWARM_EvolveWeapon(self) -> int:
        try:
            return self.raw_data['SWARM_EvolveWeapon']
        except KeyError as e:
            e.add_note('Could not retrieve SWARM_EvolveWeapon, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def SWARM_Have3Passives(self) -> int:
        try:
            return self.raw_data['SWARM_Have3Passives']
        except KeyError as e:
            e.add_note('Could not retrieve SWARM_Have3Passives, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def SWARM_KillEnemy(self) -> int:
        try:
            return self.raw_data['SWARM_KillEnemy']
        except KeyError as e:
            e.add_note('Could not retrieve SWARM_KillEnemy, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def SWARM_PickupGold(self) -> float:
        try:
            return self.raw_data['SWARM_PickupGold']
        except KeyError as e:
            e.add_note('Could not retrieve SWARM_PickupGold, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def SWARM_ReachLevel50(self) -> int:
        try:
            return self.raw_data['SWARM_ReachLevel50']
        except KeyError as e:
            e.add_note('Could not retrieve SWARM_ReachLevel50, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def SWARM_Survive15Min(self) -> int:
        try:
            return self.raw_data['SWARM_Survive15Min']
        except KeyError as e:
            e.add_note('Could not retrieve SWARM_Survive15Min, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def SWARM_WinWith5EvolvedWeapons(self) -> int:
        try:
            return self.raw_data['SWARM_WinWith5EvolvedWeapons']
        except KeyError as e:
            e.add_note('Could not retrieve SWARM_WinWith5EvolvedWeapons, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def soloKills(self) -> int:
        try:
            return self.raw_data['soloKills']
        except KeyError as e:
            e.add_note('Could not retrieve soloKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def stealthWardsPlaced(self) -> int:
        try:
            return self.raw_data['stealthWardsPlaced']
        except KeyError as e:
            e.add_note('Could not retrieve stealthWardsPlaced, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def survivedSingleDigitHpCount(self) -> int:
        try:
            return self.raw_data['survivedSingleDigitHpCount']
        except KeyError as e:
            e.add_note('Could not retrieve survivedSingleDigitHpCount, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def survivedThreeImmobilizesInFight(self) -> int:
        try:
            return self.raw_data['survivedThreeImmobilizesInFight']
        except KeyError as e:
            e.add_note('Could not retrieve survivedThreeImmobilizesInFight, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def takedownOnFirstTurret(self) -> int:
        try:
            return self.raw_data['takedownOnFirstTurret']
        except KeyError as e:
            e.add_note('Could not retrieve takedownOnFirstTurret, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def takedowns(self) -> int:
        try:
            return self.raw_data['takedowns']
        except KeyError as e:
            e.add_note('Could not retrieve takedowns, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def takedownsAfterGainingLevelAdvantage(self) -> int:
        try:
            return self.raw_data['takedownsAfterGainingLevelAdvantage']
        except KeyError as e:
            e.add_note('Could not retrieve takedownsAfterGainingLevelAdvantage, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def takedownsBeforeJungleMinionSpawn(self) -> int:
        try:
            return self.raw_data['takedownsBeforeJungleMinionSpawn']
        except KeyError as e:
            e.add_note('Could not retrieve takedownsBeforeJungleMinionSpawn, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def takedownsFirstXMinutes(self) -> int:
        try:
            return self.raw_data['takedownsFirstXMinutes']
        except KeyError as e:
            e.add_note('Could not retrieve takedownsFirstXMinutes, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def takedownsInAlcove(self) -> int:
        try:
            return self.raw_data['takedownsInAlcove']
        except KeyError as e:
            e.add_note('Could not retrieve takedownsInAlcove, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def takedownsInEnemyFountain(self) -> int:
        try:
            return self.raw_data['takedownsInEnemyFountain']
        except KeyError as e:
            e.add_note('Could not retrieve takedownsInEnemyFountain, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def teamBaronKills(self) -> int:
        try:
            return self.raw_data['teamBaronKills']
        except KeyError as e:
            e.add_note('Could not retrieve teamBaronKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def teamDamagePercentage(self) -> float:
        try:
            return self.raw_data['teamDamagePercentage']
        except KeyError as e:
            e.add_note('Could not retrieve teamDamagePercentage, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def teamElderDragonKills(self) -> int:
        try:
            return self.raw_data['teamElderDragonKills']
        except KeyError as e:
            e.add_note('Could not retrieve teamElderDragonKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def teamRiftHeraldKills(self) -> int:
        try:
            return self.raw_data['teamRiftHeraldKills']
        except KeyError as e:
            e.add_note('Could not retrieve teamRiftHeraldKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def tookLargeDamageSurvived(self) -> int:
        try:
            return self.raw_data['tookLargeDamageSurvived']
        except KeyError as e:
            e.add_note('Could not retrieve tookLargeDamageSurvived, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def turretPlatesTaken(self) -> int:
        try:
            return self.raw_data['turretPlatesTaken']
        except KeyError as e:
            e.add_note('Could not retrieve turretPlatesTaken, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def turretsTakenWithRiftHerald(self) -> int:
        try:
            return self.raw_data['turretsTakenWithRiftHerald']
        except KeyError as e:
            e.add_note('Could not retrieve turretsTakenWithRiftHerald, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def turretTakedowns(self) -> int:
        try:
            return self.raw_data['turretTakedowns']
        except KeyError as e:
            e.add_note('Could not retrieve turretTakedowns, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def twentyMinionsIn3SecondsCount(self) -> int:
        try:
            return self.raw_data['twentyMinionsIn3SecondsCount']
        except KeyError as e:
            e.add_note('Could not retrieve twentyMinionsIn3SecondsCount, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def twoWardsOneSweeperCount(self) -> int:
        try:
            return self.raw_data['twoWardsOneSweeperCount']
        except KeyError as e:
            e.add_note('Could not retrieve twoWardsOneSweeperCount, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def unseenRecalls(self) -> int:
        try:
            return self.raw_data['unseenRecalls']
        except KeyError as e:
            e.add_note('Could not retrieve unseenRecalls, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def visionScorePerMinute(self) -> float:
        try:
            return self.raw_data['visionScorePerMinute']
        except KeyError as e:
            e.add_note('Could not retrieve visionScorePerMinute, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def wardsGuarded(self) -> int:
        try:
            return self.raw_data['wardsGuarded']
        except KeyError as e:
            e.add_note('Could not retrieve wardsGuarded, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def wardTakedowns(self) -> int:
        try:
            return self.raw_data['wardTakedowns']
        except KeyError as e:
            e.add_note('Could not retrieve wardTakedowns, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def wardTakedownsBefore20M(self) -> int:
        try:
            return self.raw_data['wardTakedownsBefore20M']
        except KeyError as e:
            e.add_note('Could not retrieve wardTakedownsBefore20M, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

