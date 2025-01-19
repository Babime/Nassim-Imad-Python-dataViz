
from src.utils.pyltover import Pyltover
from src.utils.pyltover.enums import By, Region, Loading

# défini les instances de Pyltover avec le loading style EAGER afin de charger automatiquement les données
instances = [Pyltover(api_key='RGAPI-1bd654a2-dffb-4216-b237-f9b8dc6ebe00', region=Region.EUW1, loading_style=Loading.EAGER),
            Pyltover(api_key='RGAPI-fd36d62b-0c5a-4adc-9452-36af590d7b16', region=Region.EUW1, loading_style=Loading.EAGER)]
index = 0

def getPyltoverInstance() -> Pyltover:
    global index
    index = 1 if index == 0 else 0
    return instances[index]