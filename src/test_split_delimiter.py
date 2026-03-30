import unittest

from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):
    def test_diff_delimiters_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
    
    def test_diff_delimiters_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[1].text, "bold block")
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
    
    def test_diff_delimiters_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[1].text, "italic block")
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)

    def test_non_TEXT_node(self):
        node = TextNode("This is already BOLD", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(node, new_nodes[0])

    def test_invalid_markdown(self):
        node = TextNode("This is missing a **closing delimiter", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)
    
    def test_empty_text_segments(self):
        node = TextNode("**Bold block** is at the start and **the end**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text, "Bold block")
        self.assertEqual(new_nodes[1].text, " is at the start and ")
        self.assertEqual(new_nodes[2].text, "the end")
        self.assertEqual(new_nodes[0].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text_type, TextType.BOLD)

    
if __name__ == "__main__":
    unittest.main()