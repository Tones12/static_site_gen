import os
import shutil
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
from htmlnode import HTMLNode, LeafNode, ParentNode


def generate_page(from_path, template_path, dest_path):

    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    markdown_file = open(from_path, 'r')
    markdown = str(markdown_file.read())
    markdown_file.close()
    template_file = open(template_path, 'r')
    template = str(template_file.read())
    template_file.close()

    html_nodes = markdown_to_html_node(markdown)
    html = html_nodes.to_html()
    title = extract_title(markdown)
    template.replace("{{ Title }}", title)
    template.replace("{{ Content }}", html)
    os.path.isdir(dest_path) or os.makedirs(dest_path)
    #create new html file in destination path using updated template
    html_file = open(os.path.join(dest_path, "index.html"), 'w')
    html_file.write(template)
    html_file.close()
    

    
