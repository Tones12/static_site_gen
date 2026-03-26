import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_empty_node(self):
        node = str(HTMLNode())
        node2 = str(HTMLNode(None, None, None, None))
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

    def test_ineq(self):
        node = str(HTMLNode("tag tag tag", "value value value", None, None))
        node2 = str(HTMLNode("tag tag tag", "value value value"))
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()