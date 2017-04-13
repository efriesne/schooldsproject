import re
import csv
import math

cleaned = ["school_id", "school","year","charter","level","lat","long"]
id_file = 'data/cleaned_test_ids.csv'
non_id_file = 'data/basic_chars_cleaned.csv'
new_file = 'basic_chars_cleaned_ids.csv'

schools = {}
with open(id_file,'r') as id_file:
    csv_reader = csv.DictReader(id_file)
    next(csv_reader, None)
    for row in csv_reader:
        if (schools.has_key(row['school']) == False):
            schools[row['school']] = row['school_id']

with open(non_id_file, 'r') as non_id_file:
    with open(new_file, 'w') as cleanfile:
        csv_reader = csv.DictReader(non_id_file)
        next(csv_reader, None)
        writer = csv.writer(cleanfile)
        writer.writerow(cleaned)
        no_id_count = 0
        total = 0
        for row in csv_reader:
            total += 1
            if schools.has_key(row['name']) == True:
                id = schools[row['name']]
                writer.writerow([id, row['name'], row['year'], row['charter'], row['level'], row['lat'], row['long']])
            else: 
                no_id_count += 1
        print(no_id_count)
        print(total)
