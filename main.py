import argparse
import os.path

import constants

parser = argparse.ArgumentParser(description="Reads a tagged input training set and creates a set of rules to tag any"
                                             "new sentences")
parser.add_argument('--input', type=str, help='Relative path of training set', default='')
parser.add_argument('--output', type=str, help='Name of file to write to. If not given, prints to console',
                    default='')

args = parser.parse_args()

input_file = "HW2_S18_NLP6320_POSTaggedTrainingSet-Unix.txt"  # default file to read

if args.input != '':
    input_file = args.input

if not os.path.isfile(input_file):
    print("Invalid input file:", input_file)
