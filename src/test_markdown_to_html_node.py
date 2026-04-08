import unittest

from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """
###### This is a level 6 heading

##### This is a level 5 heading

#### This is a level 4 heading

### This is a level 3 heading

## This is a level 2 heading

# This is a level 1 heading"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>This is a level 6 heading</h6><h5>This is a level 5 heading</h5><h4>This is a level 4 heading</h4><h3>This is a level 3 heading</h3><h2>This is a level 2 heading</h2><h1>This is a level 1 heading</h1></div>")
    
    def test_quotes(self):
        md = """
> This is a multiline quote with
> **bolded** text and
> _italic_ text
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a multiline quote with <b>bolded</b> text and <i>italic</i> text</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- This is an unordered list with
- **bolded** text and
- _italic_ text
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is an unordered list with</li><li><b>bolded</b> text and</li><li><i>italic</i> text</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. This is an ordered list with
2. **bolded** text and
3. _italic_ text and
4. `code` text and
5. some random text
6. to get to the next line
7. until I reach the end of the list
8. and have a list numbering
9. greater than
10. 10
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an ordered list with</li><li><b>bolded</b> text and</li><li><i>italic</i> text and</li><li><code>code</code> text and</li><li>some random text</li><li>to get to the next line</li><li>until I reach the end of the list</li><li>and have a list numbering</li><li>greater than</li><li>10</li></ol></div>",
        )

if __name__ == "__main__":
    unittest.main()