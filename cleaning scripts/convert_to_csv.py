import csv

def main():
	#DON'T RUN THIS UNLESS YOU ABSOLUTELY HAVE TO!!
	#Not working right. Skips rows for some reason

	for i in range(7, 15):
		print(i)
		if i < 10:
			txt_file = 'g080' + str(i) + 'nd.txt'
			csv_file = 'g080' + str(i) + 'nd.csv'
		else:
			txt_file = 'g08' + str(i) + 'nd.txt'
			csv_file = 'g08' + str(i) + 'nd.csv'

		with open(txt_file, 'r+') as in_txt, open(csv_file, 'w+') as out_csv:
			reader = csv.reader(in_txt, delimiter='\t')
			rows = [row for row in reader]
			header = [col.lower() for col in rows[0]]
			writer = csv.writer(out_csv)
			for row in rows:
				writer.writerow(row)

	for i in range(6, 15):
		print(i)
		if i < 8:
			txt_file = 'g100' + str(i) + 'nd.txt'
			csv_file = 'ghs0' + str(i) + 'nd.csv'
		elif i > 7 and i < 10:
			txt_file = 'ghs0' + str(i) + 'nd.txt'
			csv_file = 'ghs0' + str(i) + 'nd.csv'
		else:
			txt_file = 'ghs' + str(i) + 'nd.txt'
			csv_file = 'ghs' + str(i) + 'nd.csv'

		with open(txt_file, 'r') as in_txt, open(csv_file, 'w') as out_csv:
			reader = csv.reader(in_txt, delimiter='\t')
			rows = [row for row in reader]
			header = [col.lower() for col in rows[0]]
			writer = csv.writer(out_csv)
			for row in rows:
				writer.writerow(row)


if __name__ == '__main__':
	main()