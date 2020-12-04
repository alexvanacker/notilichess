import li
import json

# testing util

if __name__ == "__main__":
    # execute only if run as a script

    users=["Le_Scratch","justmaker","kazeriahm","Khrok","fauzi061089", "Vladismen", "kapuso", "Vadum-tv", "El-Nino9", "mathemagician18", "jongy", "shtrubi", "Teju12345", "papasi", "dalmatinac101"]
    for line in li.stream(users):
        print(li.game_to_message(line))
