

**data cleaning **
You can clean with basic cleaning commands in python using 'open' to open specific files and associate it with a variable and use 'replace ' to replace the element. In our case we just need to clean. Finally, we can use append to do the work.

```
import re


rmnum = re.compile(r'/d+')
one = []

with open("C:\\THINGS\\githup project\\meshochat.txt", 'r', encoding= "utf-8") as mesho:
    for line in mesho:
        rm = line.replace('/','').replace(':','').replace('AM','').replace('PM','').replace('-','').replace(',','').replace(' ','').replace('ميشووو','ques ').replace('Nõr','ans ')
        one.append(rm)

```
to delete the changing number in the date u can use re.compile(r'\d+') to delete any number from chat
after cleaning the chat you will start to sort data in the table and here you need to learn RELATIONAL DATABASE MANAGEMENT SYSTEM in order to handle the data and store them.
in my case, I use PostgreSQL to handle chat log data and there are some important things you must get hands-on :
1- IF you handle your data with PostgreSQL you have to realize that by default it only accepts ASCII characters:
2- you need to use the "UTF-8" encoding method to avoid any error especially if you use a character out site ASCII list like Arabic characters

.
.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9okivnm3p2fgxp16w5tf.jpeg)



`NOTE USE : _CREATE DATABASE bot WITH ENCODING'UTF8_' `

3- need to know how to handle data using psycopg2 or any other library to store and customize data in an effective way  

```
import psycopg2

conect = psycopg2.connect(

    host = "localhost",
    database = "time",
    user = "postgres",
    password = "timezone"
)
cur = conect.cursor()
cur.execute("INSERT INTO static(name, last_name, gender, email) VALUES('ONE','SALIH','FEMEAL','Eada@gmail.com');")
cur.execute("SELECT * FROM static;")
rows = cur.fetchall()
# use for loop to print ever line you spasify 
for line in rows:
    print(f"{line[0]} {line[1]} {line[2]} {line[3]} {line[4]}")
conect.commit()
cur.close()
conect.close()

```



After storing the data in CSV or TSV format you can use Git to upload your data to GitHub and there are some commands that will help you do that: "git init " and "git add ." 
These two commands are important the first is to  create the git hidden file to initialize the project and the second one is to add an initialized folders to git file and finally you can use git commit to commit your initialization and git push to upload to GitHub in this way avoid any uploading error happening when you use drag and drop method.
After uploading the tsv file opens it in row form and copies the link this link will be the database for the chatbox bot.

From now on you can use any language to code the bot. In my case I use python because again I have many ways to handle data and here using pandas this tool gives you a mighty hand on accessing your data and distributing them in a way that serves your needs .  
The actual bot is divided into four parts. The first part just defines the database and bot api .

```
from typing import Counter

import requests 
import pandas as pd
resp = [ "Sorry ","have a nice day"]
dburl = "DATABASElink.tsv"
url = "botapi/"
counter = 0

```

the second part is reading the user message offset is the message id or "update_id" each message has an unique id and here you need to extract some information from json format like message and user id that change automatically .



```
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
```

The third part is to process input given by the user if there is any capital letter it will make it small and so on and if  there is any message that not exist in the database it will give auto response from a list created privily in this case "resp".


```
def out(message):
  global counter
  answer = df.loc[df['qus'].str.lower()== message.lower()]


  if not answer.empty:
    answer = answer.iloc[0]['ans']
    return answer
  else:
    counter = (counter + 1) % len(resp)
    return resp[counter]
    
              
```

the final part is sending message part here there is just a simple parameter take sends a message to the id that stores priestly from a list in the database.

```

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

```

### try tun the bot from here :)
[Life 2.0](https://t.me/dootobot)

THANK YOU :)
