import requests
import json

def info(target):
    response = requests.get("https://api.viewdns.info/reversedns/?ip="+target+"&apikey=131f8092fc74a404acb826a4aa19877e86c1c766&output=json")
    output=json.loads(response.text)
    return output