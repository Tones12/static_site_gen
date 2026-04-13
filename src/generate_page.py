import os
import shutil
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
from htmlnode import HTMLNode, LeafNode, ParentNode
from pathlib import Path



def generate_page(from_path, template_path, dest_path):

    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    markdown_file = open(from_path, 'r')
    markdown = str(markdown_file.read())
    markdown_file.close()
    template_file = open(template_path, 'r')
    template = str(template_file.read())
    template_file.close()

    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()
    
    title = extract_title(markdown)
   
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    
    directory = os.path.dirname(dest_path)
    os.path.isdir(directory) or os.makedirs(directory)
    
    #create new html file in destination path using updated template
    html_file = open(dest_path, 'w')
    html_file.write(template)
    html_file.close()
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    #make list of files and folders in dir_path_content
    dir_list = os.listdir(dir_path_content)
    print(dir_list)
    for item in dir_list:
        dir_path_item = os.path.join(dir_path_content, item)
        dest_dir_path_item = os.path.join(dest_dir_path, item)
        if os.path.isdir(dir_path_item):
            generate_pages_recursive(dir_path_item, template_path, dest_dir_path_item)
        else:
            dest_dir_path_item = Path(dest_dir_path_item).with_suffix('.html')
            generate_page(dir_path_item, template_path, dest_dir_path_item)
    
