from static_folder_to_public import static_folder_to_public_folder
from generate_page import generate_pages_recursive
import sys

print('Robot Voice: "Static Site Generator... Initializing..."')

def main():
    
    if len(sys.argv) > 1:
        basepath = {sys.argv[1]}
    else:
        basepath = '/'
    
    static_folder_to_public_folder()

    generate_pages_recursive('content', 'template.html', 'docs', basepath)

main()
