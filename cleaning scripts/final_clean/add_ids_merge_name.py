import re
import csv
import math



def run(): 
    cleaned = ["school_id", "school","year","charter","level","town", "lat","long"]
    id_file = 'testdata/cleaned_current_ids.csv'
    non_id_file = 'basic_chars_cleaned.csv'
    new_file = 'basic_chars_cleaned_ids.csv'

    schools = {}

    with open(id_file,'r') as id_file:
        csv_reader = csv.DictReader(id_file)
        next(csv_reader, None)
        for row in csv_reader:
            if row['name'] not in schools:
                schools[row['name']] = (row['id'], row['lat'], row['town'])

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

                if row['name'] in schools:
                    #print(schools[row['name']])
                    sid = schools[row['name']][0]
                    town = schools[row['name']][2]
                    writer.writerow([sid, row['name'], row['year'], row['charter'], row['level'], town, row['lat'], row['long']])

                else:
                    no_id_count += 1
                    for school in schools:
                        jac = jaccard(school, row['name'])
                        lat_dif = float(row['lat']) - float(schools[school][1])
                        if jac > 0.5 and abs(lat_dif) < 0.001:
                            writer.writerow([schools[school][0], row['name'], row['year'], row['charter'], row['level'], schools[school][2], row['lat'], row['long']])


            print(no_id_count)
            print(total)


def jaccard(str1, str2):
    str1 = set(str1.split())
    str2 = set(str2.split())
    return float(len(str1 & str2)) / len(str1 | str2)


if __name__ == '__main__':
    run()
