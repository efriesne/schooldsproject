import sqlite3
import random
import numpy as np
import csv
import operator
import argparse

def load_file():
	schools = []
	feats = []

	with open('all.csv', 'r', encoding='latin1') as file_reader:
		reader = csv.reader(file_reader, delimiter=',', quotechar='"')
		
		for row in reader:

			school = float(row[0])

			if len(schools) > 0 and school == schools[-1]:
				pass
			else:
				#starts at 10
				feat = []

				#add total enrollment
				add_feat(row[7], feat)
				#add selected population
				for i in range(10, 23):
					add_feat(row[i], feat)
				#add race
				for i in range(33, 38):
					add_feat(row[i], feat)
				#add gender
				for i in range(38, 40):
					add_feat(row[i], feat)
				#add higher ed
				for i in range(42, 47):
					add_feat(row[i], feat)
				#add incidents
				for i in range(47, 51):
					add_feat(row[i], feat)

				#teacher information makes no difference!
				#add teachers
				for i in range(27, 31):
					add_feat(row[i], feat)

				#incident descriptors make no difference!
				#if row[51] not in off_desc_dict.keys():
				#	off_desc_dict[row[51]] = off_desc_int
				#row[51] = off_desc_dict[row[51]]
				#if row[52] not in off_desc_dict.keys():
				#	off_desc_dict[row[52]] = off_desc_int
				#row[52] = off_desc_dict[row[52]]
				
				schools.append(school)
				feats.append(feat)
			
	return (schools, feats)

def add_feat(toAdd, feat):
	if toAdd != "": 
		feat.append(float(toAdd))
	else:
		feat.append(-1)

def do_kmeans(schools, characteristics):

	schools_dict = {}

	for i in range(len(schools)):

		differences = []

		school_id = schools[i]
		
		features = np.array(characteristics[i])

		for j in range(len(characteristics)):
			if j == i:
				pass
			else:
				other = np.array(characteristics[j])
				other_id = schools[j]

				difference_list = features - other
				difference = sum([abs(dif) for dif in difference_list])

				differences.append((other_id, difference))

		differences.sort(key=operator.itemgetter(1))

		schools_dict[school_id] = differences[:10]

	return schools_dict


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('-year', required=True, help='Year of data')

	opts = parser.parse_args()

	year = float(opts.year)

	schools, characteristics = load_file()

	#assert len(schools) == len(characteristics), "FAIL"

	sims_dict = do_kmeans(schools, characteristics)

	print(year)
	print(len(sims_dict))

	with open('neighbors.csv', 'a') as file:
		writer = csv.writer(file)
		#headers = ['school_id', 'year', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
		#writer.writerow(headers)
		for item in sims_dict:
			row = [item, year]
			row += [i[0] for i in sims_dict[item]]
			writer.writerow(row)

if __name__ == '__main__':
	main()








