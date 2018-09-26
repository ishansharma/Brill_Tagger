from copy import copy
from unittest import TestCase

from brill_tagger.rules import *
from brill_tagger.tagger import *
from input_reader.reader import Token


class TestBrillTagger(TestCase):
    dummy_corpus = [Token('Brainpower', 'NNP'), Token(',', ','), Token('not', 'RB'), Token('physical', 'JJ'),
                    Token('plant', 'NN')]

    def test_apply_transform(self):
        r1 = Rule('NNP', 'NP', 'RB')
        corpus_copy = copy(self.dummy_corpus)
        tagger = BrillTagger(corpus_copy)
        tagger.apply_transform(r1)
        self.assertEqual(tagger.corpus, corpus_copy)

        r2 = Rule('RB', 'NP', ',')
        tagger = BrillTagger(corpus_copy)
        tagger.apply_transform(r2)

        # make sure that intended rule has been applied
        self.assertEqual(tagger.corpus[2].pos, 'NP')

        # making sure that everything else didn't change
        self.assertEqual(tagger.corpus[0].pos, 'NNP')
        self.assertEqual(tagger.corpus[1].pos, ',')
        self.assertEqual(tagger.corpus[3].pos, 'JJ')
        self.assertEqual(tagger.corpus[4].pos, 'NN')

    def test_word_freq_calculations(self):
        corpus = deepcopy(self.dummy_corpus)
        tagger = BrillTagger(corpus)
        expected_frequencies = {
            'Brainpower': {
                'NNP': 1,
                'total': 1
            },
            ',': {
                ',': 1,
                'total': 1
            },
            'not': {
                'RB': 1,
                'total': 1
            },
            'physical': {
                'JJ': 1,
                'total': 1
            },
            'plant': {
                'NN': 1,
                'total': 1
            }
        }

        self.assertEqual(tagger.frequencies, expected_frequencies)

        corpus2 = [Token('Brainpower', 'NNP'), Token(',', ','), Token('not', 'RB'), Token('physical', 'JJ'),
                   Token('plant', 'NN'), Token('Brainpower', 'VB'), Token('Brainpower', ',')]
        tagger = BrillTagger(corpus2)
        expected_frequencies['Brainpower'] = {
            'NNP': 1,
            'VB': 1,
            ',': 1,
            'total': 3
        }
        self.assertEqual(tagger.frequencies, expected_frequencies)

    def test_word_prob_calculations(self):
        corpus = deepcopy(self.dummy_corpus)
        tagger = BrillTagger(corpus)
        expected_probabilities = {
            'Brainpower': {
                'NNP': 1,
            },
            ',': {
                ',': 1,
            },
            'not': {
                'RB': 1,
            },
            'physical': {
                'JJ': 1,
            },
            'plant': {
                'NN': 1,
            }
        }
        self.assertEqual(tagger.probabilities, expected_probabilities)

        corpus2 = [Token('Brainpower', 'NNP'), Token(',', ','), Token('not', 'RB'), Token('physical', 'JJ'),
                   Token('plant', 'NN'), Token('Brainpower', 'VB'), Token('Brainpower', ','), Token('Brainpower', 'NN')]
        tagger = BrillTagger(corpus2)
        expected_probabilities['Brainpower'] = {
            'NNP': 0.25,
            'VB': 0.25,
            ',': 0.25,
            'NN': 0.25
        }

        self.assertEqual(tagger.probabilities, expected_probabilities)

    def test_initialization(self):
        corpus = [Token('Brainpower', 'NNP'), Token(',', ','), Token('not', 'RB'), Token('physical', 'JJ'),
                  Token('plant', 'NN'), Token('Brainpower', 'VB'), Token('Brainpower', 'VB'),
                  Token('Brainpower', 'NN')]
        tagger = BrillTagger(corpus)
        tagger.train()
        self.assertEqual(str(tagger.corpus),
                         '[(Brainpower VB), (, ,), (not RB), (physical JJ), (plant NN), (Brainpower VB), (Brainpower '
                         'VB), (Brainpower VB)]')

    def test_error_calculation(self):
        corpus = [Token('Brainpower', 'NNP'), Token(',', ','), Token('not', 'RB'), Token('physical', 'JJ'),
                  Token('plant', 'NN'), Token('Brainpower', 'VB'), Token('Brainpower', 'VB'),
                  Token('Brainpower', 'NN')]
        tagger = BrillTagger(corpus)
        tagger.train()
        self.assertEqual(tagger.calculate_errors(), 2)

        corpus = [Token('Brainpower', 'NNP'), Token(',', ','), Token('not', 'RB'), Token('physical', 'JJ'),
                  Token('plant', 'NN')]
        tagger = BrillTagger(corpus)
        tagger.train()
        self.assertEqual(tagger.calculate_errors(), 0)
