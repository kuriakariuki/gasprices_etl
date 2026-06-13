import requests
import pandas as pd
import http.client
import os
import json
from dotenv import load_dotenv

load_dotenv()

def extract_gasprices():
    API_KEY=os.getenv("API_KEY")
    conn = http.client.HTTPSConnection("api.collectapi.com")
    headers = {
        'content-type': "application/json",
        'authorization': API_KEY
        }
    conn.request("GET", "/gasPrice/stateUsaPrice?state=WA", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data= data.decode("utf-8")
    data =json.loads(data)
    data =pd.DataFrame(data["result"]["cities"])

    return data
