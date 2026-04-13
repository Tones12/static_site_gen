class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""
        
        to_print = ""
        for k, v in self.props.items():
            to_print += f' {k}="{v}"'
        return to_print

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Error: Value not set")
        if not self.tag:
            return str(self.value)
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Error: Tag not set")
        if not self.children:
            return ValueError("Error: Children not set")
        message = ''
        for child in self.children:
            message += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>' + message + f'</{self.tag}>'

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"