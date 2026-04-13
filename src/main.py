from static_folder_to_public import static_folder_to_public_folder
from generate_page import generate_pages_recursive

print('Robot Voice: "Static Site Generator... Initializing..."')

def main():
    if sys.argv[0]:
        basepath = sys.argv[0]
    else:
        basepath = '/'
        
    static_folder_to_public_folder()

    generate_pages_recursive('content', 'template.html', 'public', basepath)

main()
