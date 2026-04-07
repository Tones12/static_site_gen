import re
from enum import Enum
from markdown_to_blocks import markdown_to_blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block):
    lines = block.split('\n')

    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    if len(block) >= 6 and block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    if all(line.startswith('>') for line in lines):
        return BlockType.QUOTE
    if all(line.startswith('- ') or line.startswith('* ') for line in lines):
        return BlockType.UNORDERED_LIST
    
    is_ordered = True
    for i, line in enumerate(lines, 1):
        if not line.startswith(f"{i}. "):
            is_ordered = False
            break
    if is_ordered:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
