import pandas as pd
import psycopg2


conn = psycopg2.connect(database="your_db_name", user="your_username", password="your_password", host="your_host", port="your_port")


df = pd.read_csv("your_csv_file.csv", delimiter=",")


for index, row in df.iterrows():
    cursor = conn.cursor()
    query = """INSERT INTO your_table_name (id, name, english_name, active, short_description, detailed_description, english_short_description, english_detailed_description, ...)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, ...);"""
    cursor.execute(query, (row["id:"], 
        row["Название:"], row["Название (in english):"], 
        row["Активный:"], row["Краткое описание:"], 
        row["Детальное описание:"], row["Краткое описание (in english):"], 
        row["Детальное описание (in english):"]))
    conn.commit()
