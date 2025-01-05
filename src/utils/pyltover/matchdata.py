import json

import requests

from pyltover.DTOs.info_dto import InfoDto
from pyltover.DTOs.metadata_dto import MetadataDto

from .enums import By, Loading, QueueType, Matchtype

class MatchData():
    def __init__(self, pyltover_instance, raw_data : dict):
        """
        """
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
            if 'matchId' in _attr:
                self._fetch_data_from_matchId()
            else:
                raise ValueError('Invalid account data provided. Please provide either matchId.')

        return object.__getattribute__(self, name)
    
    def _fetch_data_from_matchId(self) -> None:
        try:
            self.raw_data = self.pyltover_instance.make_request(f'lol/match/v5/matches/{self.raw_data["matchId"]}')
        except requests.exceptions.RequestException as e:
            e.add_note(e.response.json()['status']['message'])
            raise
        self._is_loaded = True
    
    @staticmethod
    def from_matchId(pyltover_instance, matchId : str) -> 'MatchData':
        match = MatchData(pyltover_instance, {'matchId': matchId})
        if pyltover_instance.loading_style == Loading.EAGER:
            match._fetch_data_from_matchId()
        return match

    @property
    def metadata(self) -> MetadataDto:
        try:
            return MetadataDto(self.raw_data['metadata'])
        except KeyError as e:
            e.add_note('Could not retrieve metadata, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise

    @property
    def info(self) -> InfoDto:
        try:
            return InfoDto(self.raw_data['info'])
        except KeyError as e:
            e.add_note('Could not retrieve info, instance may not be loaded correctly. Check Loading style, region and API key of Pyltover instance.')
            raise
    