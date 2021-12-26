from datetime import *
from datetime import datetime
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

players = pd.read_csv('fifa20-21.csv')
teams = {
 'Alavés': 1,
 'Cádiz': 2,
 'Getafe': 3,
 'Real Betis': 4,
 'Sevilla': 5,
 'Granada': 6,
 'Valencia': 7,
 'Elche': 8,
 'Real Sociedad': 9,
 'Eibar': 10,
 'Athletic Club': 11,
 'Atlético Madrid': 12,
 'Osasuna': 13,
 'Celta Vigo': 14,
 'Huesca': 15,
 'Real Madrid': 16,
 'Levante': 17,
 'Valladolid': 18,
 'Barcelona': 19,
 'Villarreal': 20
}
modified_teams =  {
 'Deportivo Alavés': 'Alavés',
 'Cádiz CF': 'Cádiz',
 'Getafe CF': 'Getafe',
 'Real Betis': 'Real Betis',
 'Sevilla FC': 'Sevilla',
 'Granada CF': 'Granada',
 'Valencia CF': 'Valencia',
 'Elche CF': 'Elche',
 'Real Sociedad': 'Real Sociedad',
 'SD Eibar': 'Eibar',
 'Athletic Club de Bilbao': 'Athletic Club',
 'Atlético Madrid': 'Atlético Madrid',
 'CA Osasuna': 'Osasuna',
 'RC Celta': 'Celta Vigo',
 'SD Huesca': 'Huesca',
 'Real Madrid': 'Real Madrid',
 'Levante UD': 'Levante',
 'Real Valladolid CF': 'Valladolid',
 'FC Barcelona': 'Barcelona',
 'Villarreal CF': 'Villarreal'}
ligaPlayers = players[players["Club"].isin(modified_teams.keys())]
clubs = []
for club in ligaPlayers["Club"]:
    clubs.append(modified_teams[club])
ligaPlayers["Club"]= clubs
print(ligaPlayers["Club"])