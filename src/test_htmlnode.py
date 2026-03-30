import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Hello, world!</a>')

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>",)

    def test_to_html_with_grandgrandchildren(self):
        grandgrandchild_node = LeafNode("b", "grandgrandchild")
        grandchild_node = ParentNode("span", [grandgrandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><span><b>grandgrandchild</b></span></span></div>",)

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i></p>")
    
    def test_headings(self):
        node = ParentNode("h2", [LeafNode(None, "Hello")])
        self.assertEqual(node.to_html(), "<h2>Hello</h2>")
    
    def test_no_tag_raises(self):
        node = ParentNode(None, [LeafNode("b", "text")])
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()