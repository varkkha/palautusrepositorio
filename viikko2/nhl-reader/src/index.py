import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    finnish = filter(lambda player: player.nationality == "FIN", players)

    sort_list = sorted(finnish, key=lambda player: player.points, reverse=True)

    print("Players from FIN")
    print("")
    for player in sort_list:
        print(player)

if __name__ == "__main__":
    main()
