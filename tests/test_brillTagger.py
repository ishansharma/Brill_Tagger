from unittest import TestCase
from copy import copy
from input_reader.reader import Token
from brill_tagger.tagger import *
from brill_tagger.rules import *


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
