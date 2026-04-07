import unittest

from block_to_block_type import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# This is a heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("```\nThis is a code block\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- This is an unordered list"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. This is an ordered list"), BlockType.ORDERED_LIST)

    def test_block_to_block_type_empty(self):
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)

    def test_block_to_block_type_level6_heading(self):
        self.assertEqual(block_to_block_type("###### This is a level 6 heading"), BlockType.HEADING)

    def test_block_to_block_type_improper_heading(self):
        self.assertEqual(block_to_block_type("####### This is an incorrect heading"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("#No space heading"), BlockType.PARAGRAPH)

    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type("```python\nprint('hello')\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("```\nmissing closing delimiter"), BlockType.PARAGRAPH)

    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type("> line 1\n> line 2"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("> line 1\nmissing quote mark"), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list(self):
        self.assertEqual(block_to_block_type("- item 1\n- item 2"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("* item 1\n* item 2"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("-missing space"), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First\n2. Second\n3. Third"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("1. First\n3. Third"), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()