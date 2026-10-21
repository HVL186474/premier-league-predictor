WARM_UP_SEASONS = ["1617"]
TRAIN_SEASONS = ["1718", "1819", "1920", "2021", "2122", "2223", "2324"]
VALIDATION_SEASONS = ["2425"]
TEST_SEASONS = ["2526"]

FINAL_TRAIN_SEASONS = TRAIN_SEASONS + VALIDATION_SEASONS + TEST_SEASONS
  

def select_seasons(matches, seasons):
      selected = matches[matches["Season"].isin(seasons)].copy()
      missing = set(seasons) - set(selected["Season"])
      if missing:
          raise ValueError(f"No matches for seasons: {sorted(missing)}")
      return selected
 

def split_by_season(matches):
      """Split into train, validation and test by season. Warm-up and current season are left out."""
      train = select_seasons(matches, TRAIN_SEASONS)
      validation = select_seasons(matches, VALIDATION_SEASONS)
      test = select_seasons(matches, TEST_SEASONS)
      return train, validation, test