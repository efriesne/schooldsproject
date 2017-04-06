#!/usr/bin/env python3
import re
import csv

import random

from operator import itemgetter

def get_td():
    #teacher data stores a list of lists with all the relevant fields
    td = []
    with open('incidents_cleaned.csv','r') as inputfile:
        reader = csv.reader(inputfile)
        #skip over header
        next(reader, None)
        count = 0;
        #for each row
        for row in reader:
            keep = True
            year = row[0]
            #don't include unhelpful data
            if int(year) < 2006:
                keep = False
            if len(row) < 7:
                keep = False
            #choose fields to keep
            if keep == True:
                school_id = row[1]
                off_des = row[4]
                disc_desc = row[5]
                days_missed = row[6]

                curr = [year, school_id, off_des, disc_desc, days_missed]
                td.append(curr)
    print("length is ", len(td))
    return td

def combine_data(td):
    td_training = []
    td_test = []
    with open('success_metric.csv','r') as inputfile:
        reader = csv.reader(inputfile)
        #skip over header
        next(reader, None)
        count = 0;
        #for each row
        for row in reader:
            #match year and school
            school_id = row[0]
            year = row[1]
            for record in td:
                if (record[0] == year) and (record[1] == school_id):
                    curr = [row[3], row[2]] + record
                    rand = random.random()*5
                    if rand < 4:
                        td_training.append(curr)
                    else:
                        td_test.append(curr)

                if count % 50000000 == 0:
                    print("comp line ", count)
                count += 1
    return td_training, td_test
            
def write_comb_data(td_training, td_test):
    with open('pred_incidents/training.csv','w') as outputfile:
        writer = csv.writer(outputfile)
        for record in td_training:
            writer.writerow(record)

    with open('pred_incidents/test.csv','w') as outputfile:
        writer = csv.writer(outputfile)
        for record in td_test:
            writer.writerow(record)

if __name__ == '__main__':
    td = get_td()
    td_training, td_test = combine_data(td)
    print("training length ", len(td_training))
    print("test length ", len(td_test))
    write_comb_data(td_training, td_test)