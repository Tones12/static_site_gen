from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

# HTMLNode inputs: tag=None, value=None, children=None, props=None
# ParentNode inputs: (self, tag, children, props=None)
# tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
# value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
# children - A list of HTMLNode objects representing the children of this node
# props - A dictionary of key-value pairs representing the attributes of the HTML tag.
#       For example, a link (<a> tag) might have {"href": "https://www.google.com"}

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        cleaned_text = cleaner(block, block_type)

        if block_type == BlockType.HEADING:
            level = determine_heading_level(block)
            children = text_to_children(cleaned_text)
            node =ParentNode(f"h{level}", children)
            block_nodes.append(node)
        if block_type == BlockType.PARAGRAPH:
            children = text_to_children(cleaned_text)
            node = ParentNode("p", children)
            block_nodes.append(node)
        if block_type == BlockType.CODE:
            text_node = TextNode(cleaned_text, TextType.CODE)
            children = [text_node_to_html_node(text_node)]
            node = ParentNode("pre", children)
            block_nodes.append(node)
        if block_type == BlockType.QUOTE:
            children = text_to_children(cleaned_text)
            node = ParentNode("blockquote", children)
            block_nodes.append(node)
        if block_type == BlockType.UNORDERED_LIST:
            children = []
            for line in cleaned_text.split('\n'):
                children.append(text_to_children(line))
            node = ParentNode("ul", children)
            block_nodes.append(node)
        if block_type == BlockType.ORDERED_LIST:
            children = []
            for line in cleaned_text.split('\n'):
                children.append(text_to_children(line))
            node = ParentNode("ol", children)
            block_nodes.append(node)
    block_parent = ParentNode("div", block_nodes)
    return block_parent


# Helper Functions:

def determine_heading_level(block):
    hash_count = 0

    heading_chars = block.split(' ',maxsplit=1)
    print(heading_chars)
    if heading_chars[0][-1] != '#':
        return 0
    for char in line:
        if char == "#":
            hash_count += 1
        else:
            break
    if hash_count == 0 or hash_count > 6:
        return 0
    return hash_count

def text_to_children(text):
    #convert raw text to text nodes:
    children = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def cleaner(text, block_type):
    if block_type == BlockType.HEADING:
        level = determine_heading_level(text)
        cleaned_text = text[level + 1:].strip()
        return cleaned_text
    if block_type == BlockType.PARAGRAPH:
        cleaned_text = text.strip()
        return cleaned_text
    if block_type == BlockType.CODE:
        cleaned_text = text[3:-3].strip()
        return cleaned_text
    if block_type == BlockType.QUOTE:
        cleaned_text = text[1:].strip()
        return cleaned_text
    if block_type == BlockType.UNORDERED_LIST:
        cleaned_text = ''
        for line in text.split('\n'):
            cleaned_line = line[2:].strip()
            cleaned_text += cleaned_line + '\n'
        return cleaned_text
    if block_type == BlockType.ORDERED_LIST:
        cleaned_text = ''
        for line in text.split('\n'):
            cleaned_line = line[3:].strip()
            cleaned_text += cleaned_line + '\n'
        return cleaned_text
    