import argparse

import input_reader.reader as r
from brill_tagger.tagger import *
from brill_tagger.rules import Rule

parser = argparse.ArgumentParser(description="Reads a tagged input training set and creates a set of rules to tag any"
                                             "new sentences")
parser.add_argument('--input', type=str, help='Relative path of training set', default='')
parser.add_argument('--output', type=str, help='Name of file to write to. If not given, prints to console',
                    default='')

args = parser.parse_args()

input_file = "HW2_S18_NLP6320_POSTaggedTrainingSet-Unix.txt"  # default file to read

if args.input != '':
    input_file = args.input

tagger = BrillTagger(r.read_file(input_file))
tagger.apply_transform(Rule('VBZ', 'VB', 'TO'))
# print(r.read_file(input_file))
