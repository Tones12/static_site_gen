import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """
###### This is a level 6 heading

##### This is a level 5 heading

#### This is a level 4 heading

### This is a level 3 heading

## This is a level 2 heading

# This is a level 1 heading"""
        
        extracted_title = extract_title(md)
        self.assertEqual(extracted_title, "This is a level 1 heading")

    def test_extract_title_no_h1(self):
        md = """
###### This is a level 6 heading

##### This is a level 5 heading

#### This is a level 4 heading

### This is a level 3 heading

## This is a level 2 heading"""
        
        with self.assertRaises(Exception):
            extracted_title = extract_title(md)

    def test_extract_title_empty(self):
        md = ""
        
        with self.assertRaises(Exception):
            extracted_title = extract_title(md)

if __name__ == "__main__":
    unittest.main()