import sqlite3
import csv

conn = sqlite3.connect('schools_data.db')

c = conn.cursor()

# Delete table if already exists
c.execute('DROP TABLE IF EXISTS "success";')
c.execute('DROP TABLE IF EXISTS "tests";')
c.execute('DROP TABLE IF EXISTS "basic";')
c.execute('DROP TABLE IF EXISTS "idset";')
c.execute('DROP TABLE IF EXISTS "racegender";')
c.execute('DROP TABLE IF EXISTS "incidents";')
c.execute('DROP TABLE IF EXISTS "selectedpopulation";')
c.execute('DROP TABLE IF EXISTS "teachers";')
c.execute('DROP TABLE IF EXISTS "enrollments";')

# Create tables
c.execute('''
        CREATE TABLE success(
            school_id int not null,
	    	year int,
            success float,
            ela_success float,
            math_success float)
                    ''')

c.execute('''
        CREATE TABLE tests(
            school_id int not null,
            year int,
            district_id int,
            district text,
            grade text,
            ela_raw float,
            ela_scaled float,
            ela_perf_level text,
            math_raw float,
            math_scaled float,
            math_perf_level text)
                    ''')


c.execute('''
        CREATE TABLE basic(
            school_id int not null,
            year int,
            school text,
            charter int,
            level text,
            town text,
            lat float,
            long float)
                    ''')

c.execute('''
        CREATE TABLE idset(
            school_id int not null,
            address text,
            town text,
            name text,
            type text,
            lat float,
            long float)
                    ''')

c.execute('''
        CREATE TABLE incidents(
            school_id int not null,
            year int,
            off_desc text,
            disc_desc text,
            days_missed int)
                    ''')

c.execute('''
        CREATE TABLE racegender(
            school_id int not null,
            year int,
            african_american float,
            asian float,
            hispanic float,
            white float,
            native float,
            male float,
            female float)
                    ''')
c.execute('''
        CREATE TABLE teachers(
            school_id int not null,
            year int,
            total_teachers float,
            percent_licensed float,
            total_in_core int,
            percent_highly_qualified float,
            stud_teach_ratio float)
                    ''')
c.execute('''
        CREATE TABLE selectedpopulation(
            school_id int not null,
            year int,
            first_lang_not_eng_num float,
            first_lang_not_eng_per float,
            ELL_num float,
            ELL_per float,
            disabilities_num float,
            disabilities_per float,
            low_inc_num float,
            low_inc_per float,
            free_lunch_num float,
            free_lunch_per float,
            reduced_lunch_num float,
            reduced_lunch_per float,
            high_needs_num float,
            high_needs_per float)
                    ''')

c.execute('''
        CREATE TABLE enrollments(
            school_id int not null,
            year int,
            total int)
                    ''')

conn.commit()


# Insert records into table
with open('final_data/success_metric.csv','r') as csvfile:
    
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('''
		INSERT INTO success
	        VALUES (?, ?, ?, ?, ?)''', (row['school_id'], int(row['year']), row['success'], row['ela_success'], row['math_success']))
with open('final_data/basic_chars.csv','r') as csvfile:
    
    reader = csv.DictReader(csvfile)
    for row in reader:
        charter = 0 if row['charter'] is 'No' else 1
        c.execute('''
        INSERT INTO basic
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (row['school_id'], int(row['year']), row['school'], charter, row['level'], row['town'], float(row['lat']), float(row['long'])))

with open('final_data/current_id_set.csv','r') as csvfile:
    
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('''
        INSERT INTO idset
            VALUES (?, ?, ?, ?, ?, ?, ?)''', (row['id'], row['address'], row['town'], row['name'], row['type'], float(row['lat']), float(row['long'])))

def convert(input, type):
    if type is 'float':
        return None if input is '' else float(input)
    if type is 'int':
        if input == '#NULL!' or input == '' or input == '***': return None
        else: return int(input)
     

with open('final_data/enrollmentracegender.csv','r') as csvfile:
    
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('''
        INSERT INTO racegender
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
            (row['school_id'], int(row['year']), convert(row['african_american'], 'float'), 
                convert(row['asian'],'float'), convert(row['hispanic'],'float'), 
                convert(row['white'], 'float'), convert(row['native'],'float'),convert(row['male'],'float'),
                convert(row['female'],'float')))

with open('final_data/incidents.csv','r') as csvfile:
    
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('''
        INSERT INTO incidents
            VALUES (?, ?, ?, ?, ?)''', (row['school_id'], int(row['year']), row['off_desc'], row['disc_desc'],convert(row['days_missed'], 'int')))

with open('final_data/selectedpopulation.csv','r') as csvfile:
    
    reader = csv.DictReader(csvfile)
    for row in reader:

        c.execute('''
        INSERT INTO selectedpopulation
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                (row['school_id'], int(row['year']), convert(row['first_lang_not_eng_num'], 'float'), convert(row['first_lang_not_eng_per'], 'float'), 
                    convert(row['ELL_num'], 'float'), convert(row['ELL_per'], 'float'), convert(row['disabilities_num'], 'float'),convert(row['disabilities_per'], 'float'),
                    convert(row['low_inc_num'], 'float'),convert(row['low_inc_per'], 'float'), convert(row['free_lunch_num'], 'float'),convert(row['free_lunch_per'], 'float'),
                    convert(row['reduced_lunch_num'], 'float'),convert(row['reduced_lunch_per'], 'float'), 
                    convert(row['high_needs_num'], 'float'),convert(row['high_needs_per'], 'float')))

with open('final_data/teacherdata.csv','r') as csvfile:
    
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('''
        INSERT INTO teachers
            VALUES (?, ?, ?, ?, ?, ?, ?)''', (row['school_id'], convert(row['year'],'int'), 
                float(row['total_teachers']), float(row['percent_licensed']), int(row['total_in_core'].replace(',','')), 
                float(row['percent_highly_qualified']),float(row['stud_teach_ratio'])))

with open('final_data/total_enrollment.csv','r') as csvfile:
    
    reader = csv.DictReader(csvfile)
    for row in reader:

        c.execute('''
        INSERT INTO enrollments
            VALUES (?, ?, ?)''', (row['school_id'], int(row['year']),int(row['total'])))

with open('final_data/testdata.csv','r') as csvfile:
    
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('''
        INSERT INTO tests
            VALUES (?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?)''', (row['school_id'], convert(float(row['year']), 'int'), row['district_id'], row['district'], str(int(float(row['grade']))), 
                convert(row['ela_raw'], 'float'), convert(row['ela_scaled'], 'float'), row['ela_perf_level'], convert(row['math_raw'], 'float'), 
                convert(row['math_scaled'], 'float'), row['math_perf_level']))

conn.commit()
conn.close()
