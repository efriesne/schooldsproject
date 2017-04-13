import re
import csv
import math

cleaned = ['district_id', 'district', 'school_id', 'school', 'year', 'grade', 'ela_raw', 'ela_scaled', 'ela_perf_level',
            'math_raw', 'math_scaled',  'math_perf_level']

with open('cleaned.csv','r') as dirtyfile:
    with open('cleaned_ids.csv', 'w') as cleanfile:
        csv_reader = csv.DictReader(dirtyfile)
        next(csv_reader, None)
        writer = csv.writer(cleanfile)
        writer.writerow(cleaned)
        for row in csv_reader:
            if float(row['year']) < 2006:
                cleaned_id = float(row['district_id'])*10000 + float(row['school_id'])
            else:
                cleaned_id = row['school_id']
            writer.writerow([row['district_id'], row['district'], cleaned_id, row['school'], row['year'], row['grade'], row['ela_raw'], row['ela_scaled'], row['ela_perf_level'], row['math_raw'], row['math_scaled'], row['math_perf_level']])
