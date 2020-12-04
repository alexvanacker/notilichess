import li
import json

# testing util

if __name__ == "__main__":
    # execute only if run as a script

    users=["Le_Scratch","justmaker","kazeriahm","Khrok","fauzi061089", "Vladismen", "kapuso", "Vadum-tv", "El-Nino9", "mathemagician18"]
    for line in li.stream(users):
        game = json.loads(line)
        player_white = game['players']['white']['userId']
        player_black=game['players']['black']['userId']
        # TODO Have a real Game object here
        game_state = "started" if game["status"] == 20 else "ended"
        url = "https://lichess.org/" + game["id"]
        message = "Game {} between {} and {}, URL is: {}".format(game_state,
                                                             player_white,
                                                             player_black,
                                                             url)
        print(message)
