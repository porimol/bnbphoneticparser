# coding=utf-8
from unittest import TestCase
from bnbphoneticparser import BengaliToBanglish


class TestBengaliToBanglish(TestCase):

    def test_bengali_to_banglish_parse(self):
        b2b = BengaliToBanglish()
        self.assertEqual(b2b.parse("ফ"), "f")
        self.assertEqual(b2b.parse("মুড়ি"), "muRi")

