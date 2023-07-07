import json
import os
from datetime import datetime
import requests as requests


header = {
    "x-app-id   ": os.environ["APP_ID"],
    "x-app-key": os.environ['API_KEY'],
    "Authorization": os.environ['AUTHORIZATION'],
}

body = {
    "query": input("Tell me what exercised today?"),
}

reply = requests.post(url=os.environ['URL'], headers=header, json=body)
r = reply.text
data = json.loads(r)
print(data)
count = 0
for i in data['exercises']:
    cal = i["nf_calories"]
    exercise = i["name"]
    duration = i['duration_min']

    today1 = datetime.now()
    today = today1.strftime('%d/%m/%Y')
    time = today1.strftime("%X")
    print(time)

    info = {
        'workout': {
            "date": today,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": cal,
        }
    }

    s_reply = requests.post(url=os.environ['sheet_url'], json=info)

sr_reply = requests.get(url=os.environ['R_URL'])
s = sr_reply.text
print(s)
