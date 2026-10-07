import pandas as pd
from urllib.request import urlretrieve

seasons = ["1617", "1718", "1819", "1920", "2021", "2122", "2223", "2324", "2425", "2526", "2627"]

def download_seasons():
    for season in seasons:
        path = f"data/raw/E0_{season}.csv"
        address = f"https://football-data.co.uk/mmz4281/{season}/E0.csv"

        urlretrieve(address, path)

def load_matches():    
    tables = []
    
    for season in seasons:
        path = f"data/raw/E0_{season}.csv"           

        matches = pd.read_csv(path)

        matches["Season"] = season

        tables.append(matches)
        
        print(season, len(matches))
        
    all_matches = pd.concat(tables, ignore_index=True)

    return all_matches


if __name__ == "__main__":
    download_seasons()
    all_matches = load_matches()
    print(len(all_matches))