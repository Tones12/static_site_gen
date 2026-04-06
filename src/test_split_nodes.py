import unittest

from split_nodes import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.boot.dev) and another [second link](https://www.google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://www.google.com"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links_wrong_input_type(self):
        node = TextNode(
            "This is just text without any links or images",
            TextType.LINK,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is just text without any links or images", TextType.LINK),
            ],
            new_nodes,
        )
    
    def test_split_images_wrong_input_type(self):
        node = TextNode(
            "This is just text without any links or images",
            TextType.IMAGE,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is just text without any links or images", TextType.IMAGE),
            ],
            new_nodes,
        )
    
    def test_split_images_no_images(self):
        node = TextNode(
            "This is text with a [link](https://www.boot.dev) and another [second link](https://www.google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with a [link](https://www.boot.dev) and another [second link](https://www.google.com)", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_no_links(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_split_images_mixed(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link [link](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a link [link](https://www.boot.dev)", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_split_links_mixed(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link [link](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev"),
            ],
            new_nodes,
        )
    
    def test_split_links_link_first(self):
        node = TextNode(
            "[link](https://www.boot.dev) the link is first and last [link two](https://www.boot.dev/memes)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://www.boot.dev"),
                TextNode(" the link is first and last ", TextType.TEXT),
                TextNode("link two", TextType.LINK, "https://www.boot.dev/memes"),
            ],
            new_nodes,
        )

    def test_split_images_image_first(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) the image is first and last ![image two](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" the image is first and last ", TextType.TEXT),
                TextNode("image two", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_images_mixed_input(self):
        nodes = [TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link [link](https://www.boot.dev)",
            TextType.TEXT),
            TextNode("This is just text", TextType.TEXT),
            TextNode("[link](https://google.com)", TextType.LINK)
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a link [link](https://www.boot.dev)", TextType.TEXT),
                TextNode("This is just text", TextType.TEXT),
                TextNode("[link](https://google.com)", TextType.LINK),
            ],
            new_nodes,
        )
    

if __name__ == "__main__":
    unittest.main()