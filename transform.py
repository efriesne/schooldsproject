import csv

cleaned = [['district_id', 'district', 'school_id', 'school', 'year', 'grade', 'ela_raw', 'ela_scaled',	'ela_perf_level',
			'math_raw', 'math_scaled',	'math_perf_level']]

for i in range(7, 15):
	print(i)
	if i < 10:
		csv_file = 'g080' + str(i) + 'nd.csv'
	else:
		csv_file = 'g08' + str(i) + 'nd.csv'

	with open(csv_file, 'r') as file:
		reader = csv.DictReader(file)
		for row in reader:

			if row['eteststat'] == 'T' and row['mteststat'] == 'T':
				district_id = float(row['sprp_dis'])
				district = row['DistrictName'].title()
				school_id = float(row['sprp_sch'])
				school = row['SchoolName'].title()
				year = float(row['adminyear']) 
				grade = float(row['grade'])

				if row['eperflev'] != ' ': ela_perf_level = row['eperflev'] 
				if row['mperflev'] != ' ': math_perf_level = row['mperflev'] 


				if row['erawsc'] != ' ': ela_raw = float(row['erawsc']) 
				if row['escaleds'] != ' ': ela_scaled = float(row['escaleds']) 
				
				if row['mrawsc'] != ' ': math_raw = float(row['mrawsc']) 
				if row['mscaleds'] != ' ': math_scaled = float(row['mscaleds']) 
				

				new_row = [district_id, district, school_id, school, year, grade, ela_raw, ela_scaled, ela_perf_level,
							math_raw, math_scaled, math_perf_level]

				cleaned.append(new_row)

for i in range(7, 15):
	print(i)
	if i < 10:
		csv_file = 'ghs0' + str(i) + 'nd.csv'
	else:
		csv_file = 'ghs' + str(i) + 'nd.csv'

	with open(csv_file, 'r') as file:
		reader = csv.DictReader(file)
		for row in reader:

			if row['eteststat'] == 'T' and row['mteststat'] == 'T':
				district_id = float(row['sprp_dis'])
				district = row['DistrictName'].title()
				school_id = float(row['sprp_sch'])
				school = row['SchoolName'].title()
				year = float(row['adminyear']) 
				grade = float(row['grade'])

				if row['eperflev'] != ' ': ela_perf_level = row['eperflev'] 
				if row['mperflev'] != ' ': math_perf_level = row['mperflev'] 


				if row['erawsc'] != ' ': ela_raw = float(row['erawsc']) 
				if row['escaleds'] != ' ': ela_scaled = float(row['escaleds']) 
				
				if row['mrawsc'] != ' ': math_raw = float(row['mrawsc']) 
				if row['mscaleds'] != ' ': math_scaled = float(row['mscaleds']) 
				

				new_row = [district_id, district, school_id, school, year, grade, ela_raw, ela_scaled, ela_perf_level,
							math_raw, math_scaled, math_perf_level]

				cleaned.append(new_row)

with open('cleaned.csv', 'w') as cleaned_file:
	writer = csv.writer(cleaned_file)
	for row in cleaned:
		writer.writerow(row)

