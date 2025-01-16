import logging
import json

import requests

from .match import Matchs
from .enums import By, Loading

class Summoner():
    def __init__(self, pyltover_instance, raw_data : dict):
        self.pyltover_instance = pyltover_instance
        self.raw_data = raw_data
        self._is_loaded = False
        
    def __str__(self):
        return json.dumps(self.raw_data, indent=4)
        
    def __getattribute__(self, name):
        if name[0] == '_' or name in {'pyltover_instance', 'raw_data'}:
            return object.__getattribute__(self, name)

        is_loaded = object.__getattribute__(self, '_is_loaded')

        if not is_loaded:
            _attr = object.__getattribute__(self, 'raw_data')
            if 'puuid' in _attr:
                self._fetch_data_from_puuid()
            elif 'id' in _attr:
                self._fetch_data_from_summoner_id()
            elif 'accountId' in _attr:
                self._fetch_data_from_account_id()
            else:
                raise ValueError('Invalid summoner data provided. Please provide either puuid, summoner_id or account_id.')

        return object.__getattribute__(self, name)
    
    def _fetch_data_from_puuid(self) -> None:
        try:
            self.raw_data = self.pyltover_instance.make_request(f'lol/summoner/v4/summoners/by-puuid/{self.raw_data["puuid"]}')
        except requests.exceptions.RequestException as e:
            e.add_note(e.response.json()['status']['message'])
            raise
        self._is_loaded = True
    
    def _fetch_data_from_summoner_id(self) -> None:
        try:
            self.raw_data = self.pyltover_instance.make_request(f'lol/summoner/v4/summoners/{self.raw_data["id"]}')
        except requests.exceptions.RequestException as e:
            e.add_note(e.response.json()['status']['message'])
            raise
        self._is_loaded = True

    def _fetch_data_from_account_id(self) -> None:
        try:
            self.raw_data = self.pyltover_instance.make_request(f'lol/summoner/v4/summoners/by-account/{self.raw_data["accountId"]}')
        except requests.exceptions.RequestException as e:
            e.add_note(e.response.json()['status']['message'])
            raise
        self._is_loaded = True

    @staticmethod
    def from_puuid(pyltover_instance, puuid : str) -> 'Summoner':
        summoner = Summoner(pyltover_instance, {'puuid': puuid})
        if pyltover_instance.loading_style == Loading.EAGER:
            summoner._fetch_data_from_puuid()
        return summoner
    
    @staticmethod
    def from_summoner_id(pyltover_instance, summoner_id : str) -> 'Summoner':
        summoner = Summoner(pyltover_instance, {'id': summoner_id})
        if pyltover_instance.loading_style == Loading.EAGER:
            summoner._fetch_data_from_summoner_id()
        return summoner
    
    @staticmethod
    def from_account_id(pyltover_instance, account_id : str) -> 'Summoner':
        summoner = Summoner(pyltover_instance, {'accountId': account_id})
        if pyltover_instance.loading_style == Loading.EAGER:
            summoner._fetch_data_from_account_id()
        return summoner
    
    def get_matchs(self) -> Matchs:
        return self.pyltover_instance.get_matchs(By.PUUID, self.puuid)

    @property
    def puuid(self) -> str:
        try:
            return self.raw_data['puuid']
        except KeyError as e:
            e.add_note('Could not retrieve puuid, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def summoner_id(self) -> str:
        try:
            return self.raw_data['id']
        except KeyError as e:
            e.add_note('Could not retrieve id, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def account_id(self) -> str:
        try:
            return self.raw_data['accountId']
        except KeyError as e:
            e.add_note('Could not retrieve id, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def profile_icon_id(self) -> int:
        try:
            return self.raw_data['profileIconId']
        except KeyError as e:
            e.add_note('Could not retrieve profile icon id, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def revision_date(self) -> int:
        try:
            return self.raw_data['revisionDate']
        except KeyError as e:
            e.add_note('Could not retrieve revision date, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def summoner_level(self) -> int:
        try:
            return self.raw_data['summonerLevel']
        except KeyError as e:
            e.add_note('Could not retrieve summoner level, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise