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
            n1, int,
            n2, int,
            n3, int, 
            n4, int, 
            n5, int,
            n6, int, 
            n7, int,
            n8, int,
            n9, int,
            n10, int)
                    ''')

conn.commit()


# Insert records into table
with open('../ml/neighbors.csv','r') as csvfile:
    
    reader = csv.reader(csvfile)
    for row in reader:
        c.execute('''
		INSERT INTO neighbors
	        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (int(row[0]), int(row[1]), int(row[2], 
                    int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]),
                    int(row[9]), int(row[10]), int(row[11]))))


conn.commit()
conn.close()
