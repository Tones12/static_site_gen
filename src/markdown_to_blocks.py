def markdown_to_blocks(markdown):
    # take raw markdown string (markdown) as input
    # and return a list of "block" strings.
    raw_blocks = markdown.split(sep='\n\n')
    blocks = []
    
    for block in raw_blocks:
        cleaned_block = block.strip()
    
        if cleaned_block:
            blocks.append(cleaned_block)
    
    return blocks
