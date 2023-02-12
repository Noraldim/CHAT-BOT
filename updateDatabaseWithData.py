import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres', 
    database = 'postgres',
    password = 'timezone',
    client_encoding="UTF8"
)

# Create a cursor object
cursor = conn.cursor()

# Open the file containing names
with open("C:\\THINGS\\githup project\\finalQ.txt", 'r', encoding='utf-8') as qus:
    # Read the names
    quest = qus.readlines()
    # Remove the newline character from each name
    quest = [name.strip() for name in quest]
    
# Open the file containing genders
with open("C:\\THINGS\\githup project\\finalA.txt", 'r', encoding='utf-8') as ans:
    # Read the genders
    answer = ans.readlines()
    # Remove the newline character from each gender
    answer = [gender.strip() for gender in answer]
    
    # Zip the names and genders together to create pairs
    data = zip(quest, answer)
    
    # Iterate over the data
    for quest, answer in data:
        # Use the cursor to execute an INSERT statement
        cursor.execute("INSERT INTO bots (qus, ans) VALUES (%s, %s)", (answer, quest))

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()