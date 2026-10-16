ELO_K = 20
ELO_START = 1500

# Definerer ELO hjelpere: 

# Forventet score for hjemmelaget gitt deres rating og bortelagets rating
def expected_score(home_rating, away_rating):
    return 1 / (1 + 10 ** ((away_rating - home_rating) / 400))

# Endrer rating basert på resultatet av kampen og forventet score
def rating_change(home_rating, away_rating, result, k=ELO_K):
    return k * (result - expected_score(home_rating, away_rating))
