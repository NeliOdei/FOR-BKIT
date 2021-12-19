import unittest
import sys, os

from main import *


class TestMain(unittest.TestCase):
    def test_1(self):
        one_to_many = [(c.title, c.sal,l.name)
                       for l in libs
                       for c in cds
                       if c.lib_id == l.id]
        self.assertEqual(B1(one_to_many),[('Amy Winehouse Pop hits', 'CDAGE'), ('All music', 'Discs')])

    def test_2(self):
        one_to_many = [(c.title, c.sal,l.name)
                       for l in libs
                       for c in cds
                       if c.lib_id == l.id]
        self.assertEqual(B2(one_to_many),[['CDAGE', 220], ['Discs', 250], ['Archive', 450]])

    def test_3(self):
        many_to_many_temp = [(l.name, cl.lib_id, cl.cd_id)
                             for l in libs
                             for cl in cds_libs
                             if l.id == cl.lib_id]

        many_to_many = [(c.title, c.sal, lib_name)
                        for lib_name, lib_id, cd_id in many_to_many_temp
                        for c in cds if c.id == cd_id]
        self.assertEqual(B3(many_to_many),[('All music', 'Discs'), ('All music', 'Archive'), ('Amy Winehouse Pop hits', 'CDAGE'), ('Amy Winehouse Pop hits', 'CDshop'), ('Jazz for all', 'Discs'), ('Orchestra music', 'NewCD'), ('Orchestra music', 'CDAGE'), ('Orchestra music', 'CDshop'), ('Rock music', 'NewCD'), ('Rock music', 'Archive')])
