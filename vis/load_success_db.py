import sqlite3
import csv

conn = sqlite3.connect('success_data.db')

c = conn.cursor()

# Delete table if already exists
c.execute('DROP TABLE IF EXISTS "success";')
# Create tables
#school_id,year,success_raw,success_letter
c.execute('''
        CREATE TABLE success(
            school_id int not null,
	    	year int,
            success_raw float,
            success_letter text)
                    ''')


conn.commit()


# Insert records into table
with open('data/success_metric.csv','r') as csvfile:
    
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('''
		INSERT INTO success
	        VALUES (?, ?, ?, ?)''', (row['school_id'], row['year'], row['success_raw'], row['success_letter']))



conn.commit()
conn.close()
