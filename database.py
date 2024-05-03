import json
import PlayerData
def load():
    try:
        with open("database.json", "rt") as file:
            text = file.read()
            g_list = json.loads(text)
            result = []
            for d in g_list:
                player_data = PlayerData()
                player_data.from_dictionary(d)
                result.append(player_data)
            return result
    except:
        print("failed to read DataBase")
        return {}


def save(dictionary):
    with open ("database.json", "wt")as file:
        glist = []
        for s in dictionary.keys():
            player_dict = dictionary[s].to_dictionary()
            glist.append(player_dict)
        json_text = json.dumps(glist)
        file.write(json_text)
