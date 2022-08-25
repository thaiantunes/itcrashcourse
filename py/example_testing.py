#from testing import rearrange_name #what I would usually do is have the script to be tested in a different file and import it
import unittest
import re

def rearrange_name(name):
    result = re.search(r"(.*?), (.*)$", name)
    if result is None:
        return name #first bug fix was return ''
    return "{} {}".format(result[2], result[1])

class Test_Rearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ''
        expected = ''
        self.assertEqual(rearrange_name(testcase), expected) #this will fail since the "return" of the regex is None. will add a if to the main code to fix the bug

    def test_single(self):
        testcase = "Dan"
        expected = 'Dan' 
        self.assertEqual(rearrange_name(testcase), expected) #this will fail since after the first bug fix the test case will return '' (the regex result will be None) and the expected is Dan. will re-fix the code.

unittest.main() 