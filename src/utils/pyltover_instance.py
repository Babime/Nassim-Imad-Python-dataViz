
from src.utils.pyltover import Pyltover
from src.utils.pyltover.enums import By, Region, Loading

# défini l'instance de Pyltover avec le loading style EAGER afin de charger automatiquement les données
pyl = Pyltover(api_key='RGAPI-1bd654a2-dffb-4216-b237-f9b8dc6ebe00', region=Region.EUW1, loading_style=Loading.EAGER)