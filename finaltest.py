#the folloing code is how to distrbute the table in database using psycopg2 

import psycopg2

#this dicsinary we pass our database information and NOTE that usernaem is just USER 

conect = psycopg2.connect(

    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "timezone"
)

#the cursor it all the commend of postgrs SQL like the basic commend that u enter while u intraction with database shell

cur = conect.cursor()

#here after typing cur witch meen that execute the following commend 

cur.execute("SELECT * FROM static;")

#here the fetchall is the the acutuall rows and colloms so i thinks that you need to spacifay it insade the code using this{}

rows = cur.fetchall()
# use for loop to print ever line you spasify 
for line in rows:
    print(f"qus {line[0]} ans {line[1]}")


cur.close()
conect.close()