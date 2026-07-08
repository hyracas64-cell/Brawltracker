import requests

def get_player(tag):
    try:
        tag = tag.replace("#", "%23")

        url = f"https://api.brawlify.com/v1/players/{tag}"
        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        return {
            "name": data.get("name"),
            "trophies": data.get("trophies"),
            "highest": data.get("highestTrophies"),
            "level": data.get("expLevel"),
            "club": data.get("club", {}).get("name", "Aucun"),
        }

    except Exception as e:
        print("Erreur API:", e)
        return None