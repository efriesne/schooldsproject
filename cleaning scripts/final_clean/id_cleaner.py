import csv
import geocoder

cleaned = [['address', 'town', 'name', 'type', 'id', 'lat', 'long']]

'''with open('current_ids.csv', 'r', encoding='iso-8859-1') as file:
	reader = csv.reader(file)
	headers = next(reader, None)
	for row in reader:
		name = row[0].split(':')[1].lstrip()
		sid = row[1]
		charter = row[2]
		address = row[5]
		town = row[7]

		g = geocoder.google(address + ', ' + town + ', ' + 'MA')
		
		if len(g.latlng) == 0:
			lat, lng = None, None
		else:
			lat, lng = g.latlng

		clean = [address, town, name, charter, sid, lat, lng]
		cleaned.append(clean)
		print(name)

with open('cleaned_current_ids.csv', 'w') as file:
	writer = csv.writer(file)
	for row in cleaned:
		writer.writerow(row)'''

second = []

with open('cleaned_current_ids.csv', 'r') as file:
	reader = csv.reader(file)
	headers = next(reader, None)
	second.append(headers)
	for row in reader:
		clean = row

		town = row[1]
		address = row[0]

		if row[5] == '':
			print(row[2])
			g = geocoder.google(address + ', ' + town + ', ' + 'MA')
			if len(g.latlng) == 0:
				lat, lng = None, None
			else:
				lat, lng = g.latlng
				clean[5] = lat
				clean[6] = lng
				second.append(clean)

		else:
			second.append(clean)


with open('cleaned_current_ids.csv', 'w') as file:
	writer = csv.writer(file)
	for row in second:
		writer.writerow(row)

