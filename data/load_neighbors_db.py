import sqlite3
import csv

conn = sqlite3.connect('final_data/schools_data.db')

c = conn.cursor()

# Delete table if already exists
c.execute('DROP TABLE IF EXISTS "neighbors";')

c.execute('''
        CREATE TABLE neighbors(
            school_id int not null,
            year int,
            n1 int,
            n2 int,
            n3 int, 
            n4 int, 
            n5 int,
            n6 int, 
            n7 int,
            n8 int,
            n9 int,
            n10 int)''')

conn.commit()


# Insert records into table
with open('../ml/neighbors.csv','r') as csvfile:
    
    reader = csv.reader(csvfile)
    for row in reader:
        c.execute('''
		INSERT INTO neighbors
	        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (row[0], int(float(row[1])), row[2], 
                    row[3], row[4], row[5], row[6], row[7], row[8],
                    row[9], row[10], row[11]))


conn.commit()
conn.close()
