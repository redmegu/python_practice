print("Enter team names: ")
team1 = input()
team2 = input()
team3 = input()
team4 = input()

def greet_teams(teams):
    for team in teams:
        print("Welcome Team " + team)

greet_teams([team1, team2, team3, team4])