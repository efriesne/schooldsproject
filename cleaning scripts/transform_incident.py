import os
import csv

cleaned = [['year', 'school_id', 'school', 'grade', 'off_desc', 'disc_desc', 'days_missed']]

for filename in os.listdir(os.getcwd()):

	extension = os.path.splitext(filename)[1]
	if extension != '.csv':
		continue

	year = filename.split('_')
	
	year = year[2].split('.')[0]

	print(year)
	year = int(year)

	
	with open(filename, 'r') as file:
		reader = csv.reader(file)
		
		headers = next(reader, None)
		print(headers)
		print(len(headers))
		print('\n')
		for row in reader:
			clean_row = []
			clean_row.append(year)
			if len(headers) == 10:
				for i in range(2, 10):
					if i != 5 and i != 6:
						clean_row.append(row[i])

			elif len(headers) == 9:
				for i in range(1, 9):
					if i != 4 and i != 5:
						clean_row.append(row[i])
			else:
				for i in range(3, 7):
					clean_row.append(row[i])

				days = row[7].split()[0]
				clean_row.append(days)

			cleaned.append(clean_row)


with open('incidents_cleaned.csv', 'w') as clean:
	writer = csv.writer(clean)
	for row in cleaned:
		writer.writerow(row)