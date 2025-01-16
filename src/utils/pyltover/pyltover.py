import inspect
import requests

from .summoner import Summoner
from .enums import Loading, By, Region
from .account import Account
from .match import Matchs

class Pyltover:
    """A class to interact with the Riot Games API.
    Args:
        api_key (str): The API key used for authenticating requests.
        loading_style (Loading): The style of loading data. It can be Loading.LAZY or Loading.EAGER.
            - Loading.LAZY: Data is loaded only when accessed.
            - Loading.EAGER: Data is loaded immediately.
        region (Region): The region for the API requests. Default is Region.EUW1.
            - For certain objects like Account, the region is automatically converted (ex: EUW1 become Europe)."""
    def __init__(self, region : Region, api_key : str = None, loading_style : Loading = Loading.LAZY):
        self.api_key = api_key
        self.loading_style = loading_style
        self.region = region
        self.session = requests.Session()
        
    def make_request(self, endpoint : str, params : dict = None) -> dict:
        _class = inspect.stack()[1][0].f_locals.get('self', None)
        class_name = type(_class).__name__
        if class_name in ['Account', 'Matchs', 'MatchData', 'MatchTimeline']:
            base_url = f'https://{self.region.value[:-1]}.api.riotgames.com/'
        elif class_name in ['Summoner']:
            base_url = f'https://{str(self.region.name).lower()}.api.riotgames.com/'

        if self.api_key:
            req = self.session.get(base_url+endpoint, params=params, headers={'X-Riot-Token': self.api_key})
            if req.status_code >= 400 and req.status_code <= 504:
                raise requests.exceptions.RequestException(response=req)
            return req.json()
    
    def set_region(self, region : Region) -> None:
        """Set the region for the API requests.
        Args:
            region (Region): The region for the API requests. Default is Region.EUW1.
                - For certain objects like Account, the region is automatically converted (ex: EUW1 become Europe)."""
        if type(region) != Region:
            raise ValueError('Invalid region provided.')
        self.region = region

    def get_account(self, by: By, *args) -> Account:
        """
        Retrieve an account based on the specified method. 
        
        The account object will be loaded based on the loading style of the Pyltover instance.

        Parameters:
            by (By): The method to use for retrieving the account. It can be By.RIOT_ID or By.PUUID.
            *args: Additional arguments required for the specified method.
                - For By.RIOT_ID: args should be (game_name: str, tag_line: str)
                - For By.PUUID: args should be (puuid: str)

        Returns:
            Account: The account retrieved based on the specified method.

        Raises:
            ValueError: If an invalid method is provided or if the the object is loaded whitout the required data.
            requests.exceptions.RequestException: If the request to the Riot API fails.
        """
        if by == By.RIOT_ID:
            return Account.from_riot_id(self, *args)
        elif by == By.PUUID:
            return Account.from_puuid(self, *args)
        else:
            raise ValueError("Invalid method to get account")
        
    def get_summoner(self, by: By, *args) -> Summoner:
        """
        Retrieve a summoner object based on the specified method. 
        
        The summoner object will be loaded based on the loading style of the Pyltover instance.

        Parameters:
            by (By): The method to use for retrieving the account. It can be By.RIOT_ID or By.PUUID.
            *args: Additional arguments required for the specified method.
                - For By.PUUID: args should be (puuid: str)
                - For By.ACCOUNT_ID: args should be (account_id: str)
                - For By.SUMMONER_ID: args should be (summoner_id: str)

        Returns:
            Summoner: The summoner retrieved based on the specified method.

        Raises:
            ValueError: If an invalid method is provided or if the the object is loaded whitout the required data.
            requests.exceptions.RequestException: If the request to the Riot API fails.
        """
        if by == By.PUUID:
            return Summoner.from_puuid(self, *args)
        elif by == By.ACCOUNT_ID:
            return Summoner.from_account_id(self, *args)
        elif by == By.SUMMONER_ID:
            return Summoner.from_summoner_id(self, *args)
        else:
            raise ValueError("Invalid method to get summoner")
        
    def get_matchs(self, by : By, *args) -> Matchs:
        """
        Retrieve a matchs object based on the specified method. 
        
        The match object will be loaded based on the loading style of the Pyltover instance.

        Parameters:
            by (By): The method to use for retrieving the account. It can be By.PUUID.
            *args: Additional arguments required for the specified method.
                - For By.PUUID: args should be (puuid: str)

        Returns:
            Match: The match retrieved based on the specified method.

        Raises:
            ValueError: If an invalid method is provided or if the the object is loaded whitout the required data.
            requests.exceptions.RequestException: If the request to the Riot API fails.
        """
        if by == By.PUUID:
            return Matchs.from_puuid(self, *args)
        else:
            raise ValueError("Invalid method to get match")