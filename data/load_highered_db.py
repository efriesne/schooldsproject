import sqlite3
import csv

conn = sqlite3.connect('final_data/schools_data.db')

c = conn.cursor()

# Delete table if already exists
c.execute('DROP TABLE IF EXISTS "highered";')

c.execute('''
        CREATE TABLE highered(
            school_id int not null,
            year int,
            perecent_college float,
            percent_priv_two_year float,
            percent_priv_four_year float,
            percent_public_two_year float,
            percent_public_four_year float)


                    ''')

conn.commit()


# Insert records into table
with open('final_data/higher_ed_data_cleaned.csv','r') as csvfile:
    
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('''
		INSERT INTO highered
	        VALUES (?, ?, ?, ?, ?, ?, ?)''', (row['school id'], int(row['year']), 
                float(row['percent attending college/univ']), float(row['percent attending prive two year']), 
                float(row['percent attending private four year']), float(row['percent attending public two year']),
                float(row['percent attending public four year'])))


conn.commit()
conn.close()
