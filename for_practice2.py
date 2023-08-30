teams = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
day = 1
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print("Day " + str(day) + ": " + home_team + " vs " + away_team)
            day +=   1