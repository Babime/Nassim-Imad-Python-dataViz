from pyltover.DTOs.challenges_dto import ChallengesDto
from pyltover.DTOs.mission_dto import MissionDto
from pyltover.DTOs.perks_dto import PerksDto


class ParticipantDto():
    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    def __str__(self):
        import json
        return json.dumps(self.raw_data, indent=4)
    
    @property
    def allInPings(self) -> int:
        try:
            return self.raw_data['allInPings']
        except KeyError as e:
            e.add_note('Could not retrieve allInPings, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def assistMePings(self) -> int:
        try:
            return self.raw_data['assistMePings']
        except KeyError as e:
            e.add_note('Could not retrieve assistMePings, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def assists(self) -> int:
        try:
            return self.raw_data['assists']
        except KeyError as e:
            e.add_note('Could not retrieve assists, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def baronKills(self) -> int:
        try:
            return self.raw_data['baronKills']
        except KeyError as e:
            e.add_note('Could not retrieve baronKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def bountyLevel(self) -> int:
        try:
            return self.raw_data['bountyLevel']
        except KeyError as e:
            e.add_note('Could not retrieve bountyLevel, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def champExperience(self) -> int:
        try:
            return self.raw_data['champExperience']
        except KeyError as e:
            e.add_note('Could not retrieve champExperience, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def champLevel(self) -> int:
        try:
            return self.raw_data['champLevel']
        except KeyError as e:
            e.add_note('Could not retrieve champLevel, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def championId(self) -> int:
        try:
            return self.raw_data['championId']
        except KeyError as e:
            e.add_note('Could not retrieve championId, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def championName(self) -> str:
        try:
            return self.raw_data['championName']
        except KeyError as e:
            e.add_note('Could not retrieve championName, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def commandPings(self) -> int:
        try:
            return self.raw_data['commandPings']
        except KeyError as e:
            e.add_note('Could not retrieve commandPings, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def championTransform(self) -> int:
        try:
            return self.raw_data['championTransform']
        except KeyError as e:
            e.add_note('Could not retrieve championTransform, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def consumablesPurchased(self) -> int:
        try:
            return self.raw_data['consumablesPurchased']
        except KeyError as e:
            e.add_note('Could not retrieve consumablesPurchased, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def challenges(self) -> ChallengesDto:
        try:
            return ChallengesDto(self.raw_data['challenges'])
        except KeyError as e:
            e.add_note('Could not retrieve challenges, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def damageDealtToBuildings(self) -> int:
        try:
            return self.raw_data['damageDealtToBuildings']
        except KeyError as e:
            e.add_note('Could not retrieve damageDealtToBuildings, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def damageDealtToObjectives(self) -> int:
        try:
            return self.raw_data['damageDealtToObjectives']
        except KeyError as e:
            e.add_note('Could not retrieve damageDealtToObjectives, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def damageDealtToTurrets(self) -> int:
        try:
            return self.raw_data['damageDealtToTurrets']
        except KeyError as e:
            e.add_note('Could not retrieve damageDealtToTurrets, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def damageSelfMitigated(self) -> int:
        try:
            return self.raw_data['damageSelfMitigated']
        except KeyError as e:
            e.add_note('Could not retrieve damageSelfMitigated, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def deaths(self) -> int:
        try:
            return self.raw_data['deaths']
        except KeyError as e:
            e.add_note('Could not retrieve deaths, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def detectorWardsPlaced(self) -> int:
        try:
            return self.raw_data['detectorWardsPlaced']
        except KeyError as e:
            e.add_note('Could not retrieve detectorWardsPlaced, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def doubleKills(self) -> int:
        try:
            return self.raw_data['doubleKills']
        except KeyError as e:
            e.add_note('Could not retrieve doubleKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def dragonKills(self) -> int:
        try:
            return self.raw_data['dragonKills']
        except KeyError as e:
            e.add_note('Could not retrieve dragonKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def eligibleForProgression(self) -> bool:
        try:
            return self.raw_data['eligibleForProgression']
        except KeyError as e:
            e.add_note('Could not retrieve eligibleForProgression, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def enemyMissingPings(self) -> int:
        try:
            return self.raw_data['enemyMissingPings']
        except KeyError as e:
            e.add_note('Could not retrieve enemyMissingPings, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def enemyVisionPings(self) -> int:
        try:
            return self.raw_data['enemyVisionPings']
        except KeyError as e:
            e.add_note('Could not retrieve enemyVisionPings, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def firstBloodAssist(self) -> bool:
        try:
            return self.raw_data['firstBloodAssist']
        except KeyError as e:
            e.add_note('Could not retrieve firstBloodAssist, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def firstBloodKill(self) -> bool:
        try:
            return self.raw_data['firstBloodKill']
        except KeyError as e:
            e.add_note('Could not retrieve firstBloodKill, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def firstTowerAssist(self) -> bool:
        try:
            return self.raw_data['firstTowerAssist']
        except KeyError as e:
            e.add_note('Could not retrieve firstTowerAssist, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def firstTowerKill(self) -> bool:
        try:
            return self.raw_data['firstTowerKill']
        except KeyError as e:
            e.add_note('Could not retrieve firstTowerKill, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def gameEndedInEarlySurrender(self) -> bool:
        try:
            return self.raw_data['gameEndedInEarlySurrender']
        except KeyError as e:
            e.add_note('Could not retrieve gameEndedInEarlySurrender, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def gameEndedInSurrender(self) -> bool:
        try:
            return self.raw_data['gameEndedInSurrender']
        except KeyError as e:
            e.add_note('Could not retrieve gameEndedInSurrender, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def holdPings(self) -> int:
        try:
            return self.raw_data['holdPings']
        except KeyError as e:
            e.add_note('Could not retrieve holdPings, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def getBackPings(self) -> int:
        try:
            return self.raw_data['getBackPings']
        except KeyError as e:
            e.add_note('Could not retrieve getBackPings, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def goldEarned(self) -> int:
        try:
            return self.raw_data['goldEarned']
        except KeyError as e:
            e.add_note('Could not retrieve goldEarned, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def goldSpent(self) -> int:
        try:
            return self.raw_data['goldSpent']
        except KeyError as e:
            e.add_note('Could not retrieve goldSpent, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def individualPosition(self) -> str:
        try:
            return self.raw_data['individualPosition']
        except KeyError as e:
            e.add_note('Could not retrieve individualPosition, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def inhibitorKills(self) -> int:
        try:
            return self.raw_data['inhibitorKills']
        except KeyError as e:
            e.add_note('Could not retrieve inhibitorKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def inhibitorTakedowns(self) -> int:
        try:
            return self.raw_data['inhibitorTakedowns']
        except KeyError as e:
            e.add_note('Could not retrieve inhibitorTakedowns, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def inhibitorsLost(self) -> int:
        try:
            return self.raw_data['inhibitorsLost']
        except KeyError as e:
            e.add_note('Could not retrieve inhibitorsLost, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def item0(self) -> int:
        try:
            return self.raw_data['item0']
        except KeyError as e:
            e.add_note('Could not retrieve item0, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def item1(self) -> int:
        try:
            return self.raw_data['item1']
        except KeyError as e:
            e.add_note('Could not retrieve item1, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def item2(self) -> int:
        try:
            return self.raw_data['item2']
        except KeyError as e:
            e.add_note('Could not retrieve item2, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def item3(self) -> int:
        try:
            return self.raw_data['item3']
        except KeyError as e:
            e.add_note('Could not retrieve item3, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def item4(self) -> int:
        try:
            return self.raw_data['item4']
        except KeyError as e:
            e.add_note('Could not retrieve item4, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def item5(self) -> int:
        try:
            return self.raw_data['item5']
        except KeyError as e:
            e.add_note('Could not retrieve item5, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def item6(self) -> int:
        try:
            return self.raw_data['item6']
        except KeyError as e:
            e.add_note('Could not retrieve item6, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def itemsPurchased(self) -> int:
        try:
            return self.raw_data['itemsPurchased']
        except KeyError as e:
            e.add_note('Could not retrieve itemsPurchased, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def killingSprees(self) -> int:
        try:
            return self.raw_data['killingSprees']
        except KeyError as e:
            e.add_note('Could not retrieve killingSprees, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def kills(self) -> int:
        try:
            return self.raw_data['kills']
        except KeyError as e:
            e.add_note('Could not retrieve kills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def lane(self) -> str:
        try:
            return self.raw_data['lane']
        except KeyError as e:
            e.add_note('Could not retrieve lane, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def largestCriticalStrike(self) -> int:
        try:
            return self.raw_data['largestCriticalStrike']
        except KeyError as e:
            e.add_note('Could not retrieve largestCriticalStrike, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def largestKillingSpree(self) -> int:
        try:
            return self.raw_data['largestKillingSpree']
        except KeyError as e:
            e.add_note('Could not retrieve largestKillingSpree, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def largestMultiKill(self) -> int:
        try:
            return self.raw_data['largestMultiKill']
        except KeyError as e:
            e.add_note('Could not retrieve largestMultiKill, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def longestTimeSpentLiving(self) -> int:
        try:
            return self.raw_data['longestTimeSpentLiving']
        except KeyError as e:
            e.add_note('Could not retrieve longestTimeSpentLiving, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def magicDamageDealt(self) -> int:
        try:
            return self.raw_data['magicDamageDealt']
        except KeyError as e:
            e.add_note('Could not retrieve magicDamageDealt, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def magicDamageDealtToChampions(self) -> int:
        try:
            return self.raw_data['magicDamageDealtToChampions']
        except KeyError as e:
            e.add_note('Could not retrieve magicDamageDealtToChampions, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def magicDamageTaken(self) -> int:
        try:
            return self.raw_data['magicDamageTaken']
        except KeyError as e:
            e.add_note('Could not retrieve magicDamageTaken, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def missions(self) -> MissionDto: 
        try:
            return MissionDto(self.raw_data['missions'])
        except KeyError as e:
            e.add_note('Could not retrieve missions, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def neutralMinionsKilled(self) -> int:
        try:
            return self.raw_data['neutralMinionsKilled']
        except KeyError as e:
            e.add_note('Could not retrieve neutralMinionsKilled, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def needVisionPings(self) -> int:
        try:
            return self.raw_data['needVisionPings']
        except KeyError as e:
            e.add_note('Could not retrieve needVisionPings, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def nexusKills(self) -> int:
        try:
            return self.raw_data['nexusKills']
        except KeyError as e:
            e.add_note('Could not retrieve nexusKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def nexusTakedowns(self) -> int:
        try:
            return self.raw_data['nexusTakedowns']
        except KeyError as e:
            e.add_note('Could not retrieve nexusTakedowns, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def nexusLost(self) -> int:
        try:
            return self.raw_data['nexusLost']
        except KeyError as e:
            e.add_note('Could not retrieve nexusLost, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def objectivesStolen(self) -> int:
        try:
            return self.raw_data['objectivesStolen']
        except KeyError as e:
            e.add_note('Could not retrieve objectivesStolen, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def objectivesStolenAssists(self) -> int:
        try:
            return self.raw_data['objectivesStolenAssists']
        except KeyError as e:
            e.add_note('Could not retrieve objectivesStolenAssists, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def onMyWayPings(self) -> int:
        try:
            return self.raw_data['onMyWayPings']
        except KeyError as e:
            e.add_note('Could not retrieve onMyWayPings, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def participantId(self) -> int:
        try:
            return self.raw_data['participantId']
        except KeyError as e:
            e.add_note('Could not retrieve participantId, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerScore0(self) -> int:
        try:
            return self.raw_data['playerScore0']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore0, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerScore1(self) -> int:
        try:
            return self.raw_data['playerScore1']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore1, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerScore2(self) -> int:
        try:
            return self.raw_data['playerScore2']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore2, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerScore3(self) -> int:
        try:
            return self.raw_data['playerScore3']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore3, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerScore4(self) -> int:
        try:
            return self.raw_data['playerScore4']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore4, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerScore5(self) -> int:
        try:
            return self.raw_data['playerScore5']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore5, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerScore6(self) -> int:
        try:
            return self.raw_data['playerScore6']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore6, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerScore7(self) -> int:
        try:
            return self.raw_data['playerScore7']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore7, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerScore8(self) -> int:
        try:
            return self.raw_data['playerScore8']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore8, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerScore9(self) -> int:
        try:
            return self.raw_data['playerScore9']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore9, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerScore10(self) -> int:
        try:
            return self.raw_data['playerScore10']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore10, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerScore11(self) -> int:
        try:
            return self.raw_data['playerScore11']
        except KeyError as e:
            e.add_note('Could not retrieve playerScore11, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def pentaKills(self) -> int:
        try:
            return self.raw_data['pentaKills']
        except KeyError as e:
            e.add_note('Could not retrieve pentaKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def perks(self) -> PerksDto: 
        try:
            return PerksDto(self.raw_data['perks'])
        except KeyError as e:
            e.add_note('Could not retrieve perks, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def physicalDamageDealt(self) -> int:
        try:
            return self.raw_data['physicalDamageDealt']
        except KeyError as e:
            e.add_note('Could not retrieve physicalDamageDealt, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def physicalDamageDealtToChampions(self) -> int:
        try:
            return self.raw_data['physicalDamageDealtToChampions']
        except KeyError as e:
            e.add_note('Could not retrieve physicalDamageDealtToChampions, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def physicalDamageTaken(self) -> int:
        try:
            return self.raw_data['physicalDamageTaken']
        except KeyError as e:
            e.add_note('Could not retrieve physicalDamageTaken, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def placement(self) -> int:
        try:
            return self.raw_data['placement']
        except KeyError as e:
            e.add_note('Could not retrieve placement, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerAugment1(self) -> int:
        try:
            return self.raw_data['playerAugment1']
        except KeyError as e:
            e.add_note('Could not retrieve playerAugment1, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerAugment2(self) -> int:
        try:
            return self.raw_data['playerAugment2']
        except KeyError as e:
            e.add_note('Could not retrieve playerAugment2, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerAugment3(self) -> int:
        try:
            return self.raw_data['playerAugment3']
        except KeyError as e:
            e.add_note('Could not retrieve playerAugment3, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def playerAugment4(self) -> int:
        try:
            return self.raw_data['playerAugment4']
        except KeyError as e:
            e.add_note('Could not retrieve playerAugment4, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def playerSubteamId(self) -> int:
        try:
            return self.raw_data['playerSubteamId']
        except KeyError as e:
            e.add_note('Could not retrieve playerSubteamId, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def pushPings(self) -> int:
        try:
            return self.raw_data['pushPings']
        except KeyError as e:
            e.add_note('Could not retrieve pushPings, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def profileIcon(self) -> int:
        try:
            return self.raw_data['profileIcon']
        except KeyError as e:
            e.add_note('Could not retrieve profileIcon, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def puuid(self) -> str:
        try:
            return self.raw_data['puuid']
        except KeyError as e:
            e.add_note('Could not retrieve puuid, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def quadraKills(self) -> int:
        try:
            return self.raw_data['quadraKills']
        except KeyError as e:
            e.add_note('Could not retrieve quadraKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def riotIdGameName(self) -> str:
        try:
            return self.raw_data['riotIdGameName']
        except KeyError as e:
            e.add_note('Could not retrieve riotIdGameName, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def riotIdTagline(self) -> str:
        try:
            return self.raw_data['riotIdTagline']
        except KeyError as e:
            e.add_note('Could not retrieve riotIdTagline, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def role(self) -> str:
        try:
            return self.raw_data['role']
        except KeyError as e:
            e.add_note('Could not retrieve role, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def sightWardsBoughtInGame(self) -> int:
        try:
            return self.raw_data['sightWardsBoughtInGame']
        except KeyError as e:
            e.add_note('Could not retrieve sightWardsBoughtInGame, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def spell1Casts(self) -> int:
        try:
            return self.raw_data['spell1Casts']
        except KeyError as e:
            e.add_note('Could not retrieve spell1Casts, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def spell2Casts(self) -> int:
        try:
            return self.raw_data['spell2Casts']
        except KeyError as e:
            e.add_note('Could not retrieve spell2Casts, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def spell3Casts(self) -> int:
        try:
            return self.raw_data['spell3Casts']
        except KeyError as e:
            e.add_note('Could not retrieve spell3Casts, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def spell4Casts(self) -> int:
        try:
            return self.raw_data['spell4Casts']
        except KeyError as e:
            e.add_note('Could not retrieve spell4Casts, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def summoner1Casts(self) -> int:
        try:
            return self.raw_data['summoner1Casts']
        except KeyError as e:
            e.add_note('Could not retrieve summoner1Casts, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def summoner1Id(self) -> int:
        try:
            return self.raw_data['summoner1Id']
        except KeyError as e:
            e.add_note('Could not retrieve summoner1Id, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def summoner2Casts(self) -> int:
        try:
            return self.raw_data['summoner2Casts']
        except KeyError as e:
            e.add_note('Could not retrieve summoner2Casts, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def summoner2Id(self) -> int:
        try:
            return self.raw_data['summoner2Id']
        except KeyError as e:
            e.add_note('Could not retrieve summoner2Id, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def summonerId(self) -> str:
        try:
            return self.raw_data['summonerId']
        except KeyError as e:
            e.add_note('Could not retrieve summonerId, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def summonerLevel(self) -> int:
        try:
            return self.raw_data['summonerLevel']
        except KeyError as e:
            e.add_note('Could not retrieve summonerLevel, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def summonerName(self) -> str:
        try:
            return self.raw_data['summonerName']
        except KeyError as e:
            e.add_note('Could not retrieve summonerName, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def teamEarlySurrendered(self) -> bool:
        try:
            return self.raw_data['teamEarlySurrendered']
        except KeyError as e:
            e.add_note('Could not retrieve teamEarlySurrendered, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def teamId(self) -> int:
        try:
            return self.raw_data['teamId']
        except KeyError as e:
            e.add_note('Could not retrieve teamId, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def teamPosition(self) -> str:
        try:
            return self.raw_data['teamPosition']
        except KeyError as e:
            e.add_note('Could not retrieve teamPosition, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def timeCCingOthers(self) -> int:
        try:
            return self.raw_data['timeCCingOthers']
        except KeyError as e:
            e.add_note('Could not retrieve timeCCingOthers, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def timePlayed(self) -> int:
        try:
            return self.raw_data['timePlayed']
        except KeyError as e:
            e.add_note('Could not retrieve timePlayed, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def totalAllyJungleMinionsKilled(self) -> int:
        try:
            return self.raw_data['totalAllyJungleMinionsKilled']
        except KeyError as e:
            e.add_note('Could not retrieve totalAllyJungleMinionsKilled, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def totalDamageDealt(self) -> int:
        try:
            return self.raw_data['totalDamageDealt']
        except KeyError as e:
            e.add_note('Could not retrieve totalDamageDealt, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def totalDamageDealtToChampions(self) -> int:
        try:
            return self.raw_data['totalDamageDealtToChampions']
        except KeyError as e:
            e.add_note('Could not retrieve totalDamageDealtToChampions, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def totalDamageShieldedOnTeammates(self) -> int:
        try:
            return self.raw_data['totalDamageShieldedOnTeammates']
        except KeyError as e:
            e.add_note('Could not retrieve totalDamageShieldedOnTeammates, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def totalDamageTaken(self) -> int:
        try:
            return self.raw_data['totalDamageTaken']
        except KeyError as e:
            e.add_note('Could not retrieve totalDamageTaken, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def totalEnemyJungleMinionsKilled(self) -> int:
        try:
            return self.raw_data['totalEnemyJungleMinionsKilled']
        except KeyError as e:
            e.add_note('Could not retrieve totalEnemyJungleMinionsKilled, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def totalHeal(self) -> int:
        try:
            return self.raw_data['totalHeal']
        except KeyError as e:
            e.add_note('Could not retrieve totalHeal, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def totalHealsOnTeammates(self) -> int:
        try:
            return self.raw_data['totalHealsOnTeammates']
        except KeyError as e:
            e.add_note('Could not retrieve totalHealsOnTeammates, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def totalMinionsKilled(self) -> int:
        try:
            return self.raw_data['totalMinionsKilled']
        except KeyError as e:
            e.add_note('Could not retrieve totalMinionsKilled, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def totalTimeCCDealt(self) -> int:
        try:
            return self.raw_data['totalTimeCCDealt']
        except KeyError as e:
            e.add_note('Could not retrieve totalTimeCCDealt, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def totalTimeSpentDead(self) -> int:
        try:
            return self.raw_data['totalTimeSpentDead']
        except KeyError as e:
            e.add_note('Could not retrieve totalTimeSpentDead, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def totalUnitsHealed(self) -> int:
        try:
            return self.raw_data['totalUnitsHealed']
        except KeyError as e:
            e.add_note('Could not retrieve totalUnitsHealed, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def tripleKills(self) -> int:
        try:
            return self.raw_data['tripleKills']
        except KeyError as e:
            e.add_note('Could not retrieve tripleKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def trueDamageDealt(self) -> int:
        try:
            return self.raw_data['trueDamageDealt']
        except KeyError as e:
            e.add_note('Could not retrieve trueDamageDealt, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def trueDamageDealtToChampions(self) -> int:
        try:
            return self.raw_data['trueDamageDealtToChampions']
        except KeyError as e:
            e.add_note('Could not retrieve trueDamageDealtToChampions, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def trueDamageTaken(self) -> int:
        try:
            return self.raw_data['trueDamageTaken']
        except KeyError as e:
            e.add_note('Could not retrieve trueDamageTaken, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def turretKills(self) -> int:
        try:
            return self.raw_data['turretKills']
        except KeyError as e:
            e.add_note('Could not retrieve turretKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def turretTakedowns(self) -> int:
        try:
            return self.raw_data['turretTakedowns']
        except KeyError as e:
            e.add_note('Could not retrieve turretTakedowns, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def turretsLost(self) -> int:
        try:
            return self.raw_data['turretsLost']
        except KeyError as e:
            e.add_note('Could not retrieve turretsLost, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def unrealKills(self) -> int:
        try:
            return self.raw_data['unrealKills']
        except KeyError as e:
            e.add_note('Could not retrieve unrealKills, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def visionScore(self) -> int:
        try:
            return self.raw_data['visionScore']
        except KeyError as e:
            e.add_note('Could not retrieve visionScore, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def visionClearedPings(self) -> int:
        try:
            return self.raw_data['visionClearedPings']
        except KeyError as e:
            e.add_note('Could not retrieve visionClearedPings, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def visionWardsBoughtInGame(self) -> int:
        try:
            return self.raw_data['visionWardsBoughtInGame']
        except KeyError as e:
            e.add_note('Could not retrieve visionWardsBoughtInGame, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def wardsKilled(self) -> int:
        try:
            return self.raw_data['wardsKilled']
        except KeyError as e:
            e.add_note('Could not retrieve wardsKilled, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def wardsPlaced(self) -> int:
        try:
            return self.raw_data['wardsPlaced']
        except KeyError as e:
            e.add_note('Could not retrieve wardsPlaced, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    @property
    def win(self) -> bool:
        try:
            return self.raw_data['win']
        except KeyError as e:
            e.add_note('Could not retrieve win, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise