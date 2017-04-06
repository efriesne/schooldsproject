from __future__ import division
import sys
import csv
import argparse
from collections import defaultdict

import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn import svm

def load_file(file_path):
	letters = []
	ratios = []
	with open(file_path, 'r', encoding='latin1') as file_reader:
		reader = csv.reader(file_reader, delimiter=',', quotechar='"')
		for row in reader:
			letter = int(float(row[1]))
			ratio = [float(row[4]), float(row[5]), float(row[6])]
			letters.append(letter)
			ratios.append(ratio)
	return (letters, ratios)

def main():

	##### DO NOT MODIFY THESE OPTIONS ##########################
	parser = argparse.ArgumentParser()
	parser.add_argument('-training', required=True, help='Path to training data')
	parser.add_argument('-test', required=True, help='Path to test data')
	opts = parser.parse_args()
	############################################################

	##### BUILD TRAINING SET ###################################

	# Load training text and training labels
	(training_labels, training_ratios) = load_file(opts.training)

	# Get training features using vectorizer
	scaler = preprocessing.StandardScaler()
	training_ratios = numpy.array(training_ratios)
	#training_ratios = training_ratios.reshape(-1, 1)
	training_features = scaler.fit_transform(training_ratios)

	# Transform training labels to numpy array (numpy.array)
	training_labels = numpy.array(training_labels)
	############################################################

	##### TRAIN THE MODEL ######################################
	# Initialize the corresponding type of the classifier
	# NOTE: Be sure to name the variable for your classifier "classifier" so that our stencil works for you!
	classifier = svm.SVC(C=1.0, kernel='rbf',gamma=1.65)

	# # Train your classifier using 'fit'
	classifier.fit(training_features, training_labels)

	############################################################


	###### VALIDATE THE MODEL ##################################
	# Print training mean accuracy using 'score'
	print('training mean accuracy:', classifier.score(training_features, training_labels))

	# Perform 10 fold cross validation (cross_val_score) with scoring='accuracy'

	scores = cross_val_score(classifier, training_features, training_labels, cv=10) 
	mean = numpy.mean(scores)
	std_dev = numpy.std(scores)

	#Print the mean and std deviation of the cross validation score
	print('mean and std dev for cross validation scores:', mean, std_dev)

	###########################################################

	# Test the classifier on the given test set
	# Load test labels and texts using load_file()
	(test_labels, test_ratios) = load_file(opts.test)

	test_ratios = numpy.array(test_ratios)
	#test_ratios = test_ratios.reshape(-1, 1)

	# Extract test features using vectorizer.transform()
	test_features = scaler.transform(test_ratios)

	# Predict the labels for the test set
	predicted_labels = classifier.predict(test_features)
	print(predicted_labels)

	# Print mean test accuracy
	print('predicted mean accuracy:', accuracy_score(test_labels, predicted_labels))

	print('sklearn confusion matrix:', confusion_matrix(test_labels, predicted_labels))



if __name__ == '__main__':
	main()
