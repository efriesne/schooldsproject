#!/usr/bin/env python3
import re
import csv
from operator import itemgetter

#stores a dict of each schools test results for a year
ela_dict = {}
maths_dict = {}

def transform():
    with open('final_clean_test_data.csv','r') as inputfile:
        reader = csv.reader(inputfile)
        #skip over header
        next(reader, None)
        count = 0;
        #for each row
        for row in reader:
            year = int(float(row[4]))
            #convert id to global id
            school_id = str(int(float(row[2])))
            ela_grade = row[8]
            if ela_grade == "PRG":
                ela_grade = "P"
            if ela_grade == "F":
                ela_grade = "W"
            maths_grade = row[11]
            if maths_grade == "PRG":
                maths_grade = "P"
            if maths_grade == "F":
                maths_grade = "W"

            add_to_dict(school_id, year, ela_dict, ela_grade)
            add_to_dict(school_id, year, maths_dict, maths_grade)

            count += 1
            if count % 100000 == 0:
                print("reading line " + str(count))

    #we now have ela_dict, with all the ela scores per school per year, and the same with maths
    #now we iterate through to tally up the scores

    with open('success_metric.csv','w') as outputfile:
        writer = csv.writer(outputfile)
        writer.writerow(["school_id", "year", "success", "ela_success", "math_success"])
        for school_id in ela_dict.keys():
            for year in ela_dict[school_id].keys():
                raw, ela_final, maths_final = calc_raw(school_id, year)
                record = [school_id, year, str(raw), str(ela_final), str(maths_final)]
                writer.writerow(record)

def add_to_dict(school_id, year, curr_dict, curr_grade):
    if school_id not in curr_dict.keys():
        curr_dict[school_id] = {}
    if year not in curr_dict[school_id].keys() :
        curr_dict[school_id][year] = {}
    if curr_grade not in curr_dict[school_id][year].keys():
        curr_dict[school_id][year][curr_grade] = 0
    if 'total' not in curr_dict[school_id][year].keys():
        curr_dict[school_id][year]['total'] = 0
    curr_dict[school_id][year][curr_grade] += 1
    curr_dict[school_id][year]['total'] += 1 

def calc_raw(school_id, year):
    #first, calculate the ela score
    ela_raw = calc_indiv(school_id, year, ela_dict)
    if ela_raw != "":
        ela_final = ela_raw*3.3333333
        ela_final = round(ela_final, 3)
    #then the math score
    maths_raw = calc_indiv(school_id, year, maths_dict)
    if maths_raw != "":
        maths_final = maths_raw*3.3333333
        maths_final = round(maths_final, 3)


    #count the same score twice if one is missing
    if ela_raw == "":
       ela_raw = maths_raw
       ela_final = ""
       total_raw = maths_final
    if maths_raw == "":
       maths_raw = ela_raw
       maths_final = ""
       total_raw = ela_final
    if maths_final != "" and ela_final != "":
        total_raw = ela_raw + maths_raw
        total_raw = total_raw*1.6666667
        total_raw = round(total_raw, 3)
    return total_raw, ela_final, maths_final

def calc_indiv(school_id, year, curr_dict):
    #add up weighted scores
    w = 0
    ni = 0
    p = 0
    a = 0
    if 'W' in curr_dict[school_id][year]:
        w = curr_dict[school_id][year]['W']*0
    if 'NI' in curr_dict[school_id][year]:
        ni = (curr_dict[school_id][year]['NI'])*1
    if 'P' in curr_dict[school_id][year]:
        p = (curr_dict[school_id][year]['P'])*2
    if 'A' in curr_dict[school_id][year]:
        a = (curr_dict[school_id][year]['A'])*3

    indiv_total = w + ni + p + a
    #divide by total number of students
    indiv_total = float(indiv_total)/float(curr_dict[school_id][year]['total'])
    if '' in curr_dict[school_id][year].keys():
        if curr_dict[school_id][year]['total'] == curr_dict[school_id][year]['']:
            indiv_total = ""
    return indiv_total

if __name__ == '__main__':
    transform()
