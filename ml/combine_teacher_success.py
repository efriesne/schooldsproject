#!/usr/bin/env python3
import re
import csv

import random

from operator import itemgetter

def get_td():
    #teacher data stores a list of lists with all the relevant fields
    td = []
    with open('teacherdata_cleaned.csv','r') as inputfile:
        reader = csv.reader(inputfile)
        #skip over header
        next(reader, None)
        count = 0;
        #for each row
        for row in reader:
            #choose fields to keep
            year = row[0]
            school_id = row[2]
            percent_licensed = row[4]
            percent_highly_qualified = row[6]
            ratio = row[7]

            curr = [year, school_id, percent_licensed, percent_highly_qualified, ratio]
            td.append(curr)

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
    return td_training, td_test
            
def write_comb_data(td_training, td_test):
    with open('pred_teacherdata/training.csv','w') as outputfile:
        writer = csv.writer(outputfile)
        for record in td_training:
            writer.writerow(record)

    with open('pred_teacherdata/test.csv','w') as outputfile:
        writer = csv.writer(outputfile)
        for record in td_test:
            writer.writerow(record)

if __name__ == '__main__':
    td = get_td()
    td_training, td_test = combine_data(td)
    print("traning l ", len(td_training))
    print("training t ", len(td_test))
    write_comb_data(td_training, td_test)