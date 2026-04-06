import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTexttoTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )
    
    def test_simple_text(self):
        text = "This is just plain text"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
            TextNode("This is just plain text", TextType.TEXT),
            ],
            nodes
        )
    
    def test_no_text(self):
        text = ""
        with self.assertRaises(Exception):
            text_to_textnodes(text)
    
    def test_all_bold(self):
        text = "**This is all bold text**"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
            TextNode("This is all bold text", TextType.BOLD),
            ],
            nodes
        )
    
    def test_all_italic(self):
        text = "_This is all italic text_"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
            TextNode("This is all italic text", TextType.ITALIC),
            ],
            nodes
        )
    
    def test_all_code(self):
        text = "`This is all code text`"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
            TextNode("This is all code text", TextType.CODE),
            ],
            nodes
        )
    
    def test_initial_and_trailing_white_space(self):
        text = "  This is text with initial white space   "
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
            TextNode("This is text with initial white space", TextType.TEXT),
            ],
            nodes
        )

if __name__ == "__main__":
    unittest.main()