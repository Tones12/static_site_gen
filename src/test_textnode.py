import unittest

from textnode import TextNode, TextType, text_node_to_html_node




class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ineq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(repr(node), "TextNode(This is a text node, TextType.TEXT)")
    
    def test_str(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(str(node), "TextNode(This is a text node, TextType.TEXT)")

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text2(self):
        node = TextNode("alt text here", TextType.IMAGE, "https://example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props['src'], "https://example.com/image.jpg")
        self.assertEqual(html_node.props['alt'], "alt text here")
    

    def test_text3(self):
        node = TextNode("This is a link text node", TextType.LINK, "https://example.com/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props['href'], "https://example.com/")
    
    def test_text4(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a bold text node")
    
    def test_text5(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is a italic text node")
    
    def test_text6(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "This is a code text node")

    def test_invalid_type(self):
        node = TextNode("some text", "not_a_real_type")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
    




if __name__ == "__main__":
    unittest.main()