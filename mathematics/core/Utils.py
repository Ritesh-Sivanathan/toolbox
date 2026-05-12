def ensure_node(node):

    if (isinstance(node,(int,float))):
        return Constant(node)

    return node


