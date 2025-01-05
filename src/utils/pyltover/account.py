import json

import requests

from .summoner import Summoner
from .enums import By, Loading

class Account():
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
            elif 'gameName' in _attr and 'tagLine' in _attr:
                self._fetch_data_from_riot_id()
            else:
                raise ValueError('Invalid account data provided. Please provide either puuid or riot_id.')

        return object.__getattribute__(self, name)
    
    def _fetch_data_from_puuid(self) -> None:
        try:
            self.raw_data = self.pyltover_instance.make_request(f'riot/account/v1/accounts/by-puuid/{self.raw_data["puuid"]}')
        except requests.exceptions.RequestException as e:
            e.add_note(e.response.json()['status']['message'])
            raise
        self._is_loaded = True
        
    def _fetch_data_from_riot_id(self) -> None:
        try:
            self.raw_data = self.pyltover_instance.make_request(f'riot/account/v1/accounts/by-riot-id/{self.raw_data["gameName"]}/{self.raw_data["tagLine"]}')
        except requests.exceptions.RequestException as e:
            e.add_note(e.response.json()['status']['message'])
            raise
        self._is_loaded = True
    
    @staticmethod
    def from_puuid(pyltover_instance, puuid : str) -> 'Account':
        account = Account(pyltover_instance, {'puuid': puuid})
        if pyltover_instance.loading_style == Loading.EAGER:
            account._fetch_data_from_puuid()
        return account
    
    @staticmethod
    def from_riot_id(pyltover_instance, game_name : str, tag_line : str) -> 'Account':
        account = Account(pyltover_instance, {'gameName': game_name, 'tagLine': tag_line})
        if pyltover_instance.loading_style == Loading.EAGER:
            account._fetch_data_from_riot_id()
        return account
    
    @property
    def puuid(self) -> str:
        try:
            return self.raw_data['puuid']
        except KeyError as e:
            e.add_note('Could not retrieve puuid, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    
    @property
    def game_name(self) -> str:
        try:
            return self.raw_data['gameName']
        except KeyError as e:
            e.add_note('Could not retrieve gameName, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    
    @property
    def tag_line(self) -> str:
        try:
            return self.raw_data['tagLine']
        except KeyError as e:
            e.add_note('Could not retrieve tagLine, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
        
    def get_summoner(self) -> Summoner:
        return self.pyltover_instance.get_summoner(By.PUUID, self.puuid)