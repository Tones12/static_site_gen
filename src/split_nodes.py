from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        split_node = extract_markdown_images(node.text)
        for i in range(len(split_node)):
            if split_node[i] == '':
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_node[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_node[i], text_type))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        split_node = node.text.split(sep=delimiter)
        if len(split_node) % 2 == 0:
            raise Exception("Missing closing delimiter. Invalid Markdown syntax.")
        for i in range(len(split_node)):
            if split_node[i] == '':
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_node[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_node[i], text_type))
    return new_nodes
