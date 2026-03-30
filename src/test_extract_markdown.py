import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with an [anchor text](https://website.com)")
        self.assertListEqual([("anchor text", "https://website.com")], matches)

    def test_extract_markdown_images_no_link(self):
        matches = extract_markdown_images("This text is missing the link ![image]")
        self.assertListEqual([], matches)
    
    def test_extract_markdown_link_no_link(self):
        matches = extract_markdown_links("This text is missing the link ![anchor text]")
        self.assertListEqual([], matches)
    
    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "![cat](https://cat.png) and ![dog](https://dog.png)"
        )
        self.assertListEqual(
            [("cat", "https://cat.png"), ("dog", "https://dog.png")],
            matches
        )
    
    def test_extract_markdown_images_empty(self):
        matches = extract_markdown_images("This is just plain text")
        self.assertListEqual([], matches)
    
    def test_extract_markdown_links_excludes_images(self):
        matches = extract_markdown_links("![image](https://img.png) and [link](https://site.com)")
        self.assertListEqual([("link", "https://site.com")], matches)


if __name__ == "__main__":
    unittest.main()