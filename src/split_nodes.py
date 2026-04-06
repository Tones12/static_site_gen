from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        node_text = node.text
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        markdown_images_extract = extract_markdown_images(node.text)
        if not markdown_images_extract:
            new_nodes.append(node)
            continue
        for i in range(len(markdown_images_extract)):
            if markdown_images_extract[i] == '':
                continue
            image_alt, image_link = markdown_images_extract[i]
            split_node = node_text.split(f"![{image_alt}]({image_link})", 1)
            if len(split_node) > 1:
                node_text = split_node[1]
            if split_node[0]:
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
            new_nodes.append(TextNode(markdown_images_extract[i][0], TextType.IMAGE, markdown_images_extract[i][1]))
        if node_text:
            new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        node_text = node.text
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        markdown_links_extract = extract_markdown_links(node.text)
        if not markdown_links_extract:
            new_nodes.append(node)
            continue
        for i in range(len(markdown_links_extract)):
            if markdown_links_extract[i] == '':
                continue
            anchor_text, link = markdown_links_extract[i]
            split_node = node_text.split(f"[{anchor_text}]({link})", 1)
            if len(split_node) > 1:
                node_text = split_node[1]
            if split_node[0]:
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
            new_nodes.append(TextNode(markdown_links_extract[i][0], TextType.LINK, markdown_links_extract[i][1]))
        if node_text:
            new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes


