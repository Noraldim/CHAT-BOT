from typing import Counter

import requests 
import pandas as pd
resp = ["ما فهمتك","معليش بحاول أتعلم في السوداني ","Sorry i didn understand you ","have a nice day"]
dburl = "https://raw.githubusercontent.com/Noraldim/RESOURCES/master/FULL%20BOT%20RESORSEs.tsv"
url = "xxxxxx"
counter = 0
# download the tsv file from the link and save it locally
df = pd.read_csv(dburl, sep = "\t")

def read(offset):

    para = {
            "offset" : offset          
        }

    req = requests.get(url + "getUpdates", data = para)
    data = req.json()
    print(data)

    for result in data["result"]:
        send(result)

    if data["result"]:
        return data["result"][-1]["update_id"] + 1

def out(message):
  global counter
  answer = df.loc[df['qus'].str.lower()== message.lower()]


  if not answer.empty:
    answer = answer.iloc[0]['ans']
    return answer
  else:
    counter = (counter + 1) % len(resp)
    return resp[counter]
    
              
 

def send(result):

  text = result["message"]["text"]
  answer = out(text)


  parameter = {
      
      "chat_id" : result["message"]["chat"]["id"],        
      "text" : answer  ,
      "reply_to_message_id" : None     
  }


  req = requests.get(url + "sendMessage", data = parameter)
  print(req.text)

offset = 0

while True :
  offset = read(offset)


///check part of the message 

def read(offset):
    para = {"offset": offset}
    req = requests.get(url + "getUpdates", data=para)
    data = req.json()
    print(data)
    
    for result in data["result"]:
        send(result)
    
    if data["result"]:
        return data["result"][-1]["update_id"] + 1

def out(message):
    global counter
    best_partial_match = None
    
    for _, row in df.iterrows():
        if row['qus'].lower() in message.lower() or message.lower() in row['qus'].lower():
            best_partial_match = row['ans']
    
    if best_partial_match:
        return best_partial_match
    else:
        counter = (counter + 1) % len(resp)
        return resp[counter]
              
def send(result):
    text = result["message"]["text"]
    answer = out(text)
    parameter = {
        "chat_id": result["message"]["chat"]["id"],
        "text": answer,
        "reply_to_message_id": None
    }
    req = requests.get(url + "sendMessage", data=parameter)
    print(req.text)

offset = 0
