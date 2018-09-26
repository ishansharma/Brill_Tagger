from unittest import TestCase
from brill_tagger.rules import *


class TestRule(TestCase):
    def test_single_rule_creation(self):
        # making sure that objects are created properly and don't affect each other
        test_rule_1 = Rule('VBZ', 'VB', 'TO')
        test_rule_2 = Rule('VB', 'VBZ', 'TO')

        self.assertEqual(test_rule_1.old_tag, 'VBZ')
        self.assertEqual(test_rule_1.new_tag, 'VB')
        self.assertEqual(test_rule_1.condition, 'TO')

        self.assertEqual(test_rule_2.old_tag, 'VB')
        self.assertEqual(test_rule_2.new_tag, 'VBZ')
        self.assertEqual(test_rule_2.condition, 'TO')

    def test_rules_creation(self):
        # making sure that wrapper is fine
        test_rules_1 = Rules()
        test_rules_2 = Rules()

        test_rules_1.enqueue(Rule('VBZ', 'VB', 'TO'))

        self.assertEqual(len(test_rules_1), 1)
        self.assertEqual(len(test_rules_2), 0)

    def test_single_rule_printing(self):
        test_rule_1 = Rule('VBZ', 'VB', 'TO')
        self.assertEqual(str(test_rule_1), 'VBZ VB TO')

    def test_rules_printing(self):
        test_rules = Rules()

        test_rules.enqueue(Rule('VBZ', 'VB', 'TO'))
        test_rules.enqueue(Rule('VBZ', 'VB', 'TO'))
        test_rules.enqueue(Rule('VBZ', 'VB', 'TO'))

        self.assertEqual(str(test_rules), "VBZ VB TO\nVBZ VB TO\nVBZ VB TO\n")

    def test_rule_equality(self):
        tr1 = Rule()
        tr2 = Rule()
        tr3 = Rule('VBZ', 'VB', 'TO')

        self.assertTrue(tr1 == tr2)
        self.assertFalse(tr2 == tr3)
