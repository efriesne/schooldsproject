import csv 

all_ids = {}

final = []

with open('basic_chars_cleaned_ids.csv', 'r') as chars:
	with open('testdata/test_data_names_ids_cleaned.csv', 'r') as test:
		chars_reader = csv.reader(chars)
		chars_headers = next(chars_reader, None)

		test_reader = csv.reader(test)
		test_headers = next(test_reader, None)

		final.append(test_headers)
		print(final)

		for row in chars_reader:
			if float(row[0]) not in all_ids:
				all_ids[float(row[0])] = row[1]


		total = 0
		no_match = 0
		match = 0
		for row in test_reader:
			total += 1

			sid = float(row[2])
			if sid in all_ids:
				match += 1
				clean_row = row
				clean_row[3] = all_ids[sid]
				final.append(clean_row)

			else:
				no_match += 1

		print(no_match/total)
		print(match/total)

with open('final_clean_test_data.csv', 'w') as clean_file:
	writer = csv.writer(clean_file)
	for row in final:
		writer.writerow(row)

