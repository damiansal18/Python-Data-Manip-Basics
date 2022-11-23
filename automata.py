import pandas as pd

simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
print(len(simpsons)) 
print(simpsons[1])

premLeague = pd.read_csv('https://www.football-data.co.uk/mmz4281/2223/E0.csv')
print(premLeague)