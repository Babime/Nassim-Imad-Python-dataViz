import json

import requests

from pyltover.matchdata import MatchData

from .enums import By, Loading, QueueType, Matchtype

class Matchs():
    def __init__(self, pyltover_instance, raw_data : dict, start_time : int = None, end_time : int = None, queue : QueueType = None, type : Matchtype = None, start : int = None, count : int = None):
        """
        startTime : Epoch timestamp in seconds. The matchlist started storing timestamps on June 16th, 2021. Any matches played before June 16th, 2021 won't be included in the results if the startTime filter is set.
        endTime : Epoch timestamp in seconds.
        queue : Filter the list of match ids by a specific queue id. This filter is mutually inclusive of the type filter meaning any match ids returned must match both the queue and type filters.
        type : Filter the list of match ids by the type of match. This filter is mutually inclusive of the queue filter meaning any match ids returned must match both the queue and type filters.
        start : Defaults to 0. Start index.
        count : Defaults to 20. Valid values: 0 to 100. Number of match ids to return.
        """
        self.pyltover_instance = pyltover_instance
        self.raw_data = raw_data
        self._is_loaded = False
        self._start_time = start_time if start_time else ''
        self._end_time = end_time if end_time else ''
        self._queue = queue if queue else ''
        self._type = type if type else ''
        self._start = start if start else ''
        self._count = count if count else ''
        
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
            else:
                raise ValueError('Invalid account data provided. Please provide either puuid or riot_id.')

        return object.__getattribute__(self, name)
    
    def _fetch_data_from_puuid(self) -> None:
        try:
            self.raw_data = self.pyltover_instance.make_request(f'lol/match/v5/matches/by-puuid/{self.raw_data["puuid"]}/ids?startTime={str(self._start_time)}&endTime={str(self._end_time)}&queue={str(self._queue)}&type={str(self._type)}&start={str(self._start)}&count={str(self._count)}')
        except requests.exceptions.RequestException as e:
            e.add_note(e.response.json()['status']['message'])
            raise
        self._is_loaded = True
    
    def get_matchs_data(self) -> list[MatchData]:
        matchs_data = []
        for id in self.raw_data:
            matchs_data.append(MatchData.from_matchId(self.pyltover_instance, id))
        return matchs_data

    @staticmethod
    def from_puuid(pyltover_instance, puuid : str) -> 'Matchs':
        match = Matchs(pyltover_instance, {'puuid': puuid})
        if pyltover_instance.loading_style == Loading.EAGER:
            match._fetch_data_from_puuid()
        return match
    