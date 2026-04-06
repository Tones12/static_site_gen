from split_nodes import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter


def text_to_textnodes(text):
    if not text:
        raise Exception("No text provided")
    
    #Remove leading and trailing white space
    text = text.strip()

    #Create base TextNode with input text:
    nodes = [TextNode(text, TextType.TEXT)]
    
    #run through split delimiter for each markdown text (excluding images and links)
    delimiter_list = [('**', TextType.BOLD), ('_', TextType.ITALIC), ('`', TextType.CODE)]
    for delimiter in delimiter_list:
        nodes = split_nodes_delimiter(nodes, delimiter[0], delimiter[1])
    
    #run through split nodes for images and links
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes