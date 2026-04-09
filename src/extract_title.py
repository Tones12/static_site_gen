from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from markdown_to_html_node import determine_heading_level

def extract_title(markdown):
    #pull the h1 header from the mardown text and return it
    #if there is no h1 header raise an exception
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            level = determine_heading_level(block)
            if level == 1:
                return block[1:].strip()
    raise Exception("No h1 header found")
            
    
