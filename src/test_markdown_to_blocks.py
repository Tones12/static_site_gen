import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            []
        )
    
    def test_one_block(self):
        md = "This is a paragraph"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["This is a paragraph"]
        )

    def test_empty_with_linebreaks(self):
        md = "\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            []
        )   

if __name__ == "__main__":
    unittest.main()

