import json, os
import requests


def store_alert(team, severity, summary, description):
    "format name --> alerts --> team_severity.json"
    file_path = os.path.join(os.getcwd(), 'web_hook', 'json_file', f'{team}_{severity}.json')
    try:
        with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
    except FileNotFoundError:
        data = []


    data.append({"team":team,
                 "serverity":severity,
                 "summary":summary,
                 "description":description})

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

            
def Send_notification(team, severity, summary, description):
    token_bale = os.getenv("token_bale")
    chat_id = os.getenv("chat_id")
    url_bale = "https://tapi.bale.ai/bot"
    url = f"https://tapi.bale.ai/bot{token_bale}/sendmessage?chat_id={chat_id}&text=team:{team}\nseverity:{severity}\nsummary:{summary}\ndescription:{description}"
    response = requests.request("POST", url, headers={}, data={})
