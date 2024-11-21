import argparse

def gen_tree(p_ordering: list, tree_output: list[bool]) -> str:
    """
    Generate a binary decision tree in DOT format with explicit nodes and edges.
    
    :param p_ordering: List of variable names defining the order of decision-making (e.g., ['z1', 'z2', 'z3']).
    :param tree_output: List of Boolean outputs (True/False or 1/0) corresponding to each leaf node.
    :return: String representation of the tree in DOT format.
    """
    # Validate tree output length
    num_ordering = len(p_ordering)
    if len(tree_output) != 2**num_ordering:
        raise ValueError(f"Tree output does not match the amount of ordering. "
                         f"We have {num_ordering} variables, so we need {2**num_ordering} outputs. "
                         f"But we got {len(tree_output)} outputs.")

    # Start generating the DOT tree
    tree = "digraph G {\n"

    # Generate nodes for the decision tree
    node_map = {}  
    for level in range(num_ordering): 
        num_nodes = 2**level 
        tree += f'\t// Level {level}\n'
        for index in range(num_nodes):
            node_name = f"{p_ordering[level]}_{index}"  
            node_map[(level, index)] = node_name  
            tree += f'\t{node_name} [label="{p_ordering[level]}"];\n'

    # Generate leaf nodes for the outputs
    leaf_nodes = []
    for i, output in enumerate(tree_output):
        leaf_node = f"leaf_{i}" 
        leaf_nodes.append(leaf_node)
        label = "1" if output else "0"  
        tree += f'\t{leaf_node} [label="{label}", shape=box];\n'

    # Generate edges
    tree += "// Edges\n"
    for level in range(num_ordering):
        num_nodes = 2**level 
        for index in range(num_nodes):
            current_node = node_map[(level, index)]  
            
            left_child_index = 2 * index  
            right_child_index = 2 * index + 1  

            if level < num_ordering - 1:  
                left_child = node_map[(level + 1, left_child_index)]
                right_child = node_map[(level + 1, right_child_index)]
            else: 
                left_child = leaf_nodes[left_child_index]
                right_child = leaf_nodes[right_child_index]

            tree += f'\t{current_node} -> {left_child} [style=dashed, label="0"];\n'
            tree += f'\t{current_node} -> {right_child} [style=solid, label="1"];\n'

    tree += "}\n"
    return tree

def string_to_file(tree: str, filename: str) -> None:
    """
    Write the string representation of the tree to a file.
    
    :param tree: String representation of the tree in DOT format.
    :param filename: Name of the output file.
    """
    with open(filename, 'w') as file:
        file.write(tree)
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a binary decision tree in DOT format.')
    parser.add_argument('-f', '--file', type=str, help='Output file name.')
    parser.add_argument('ordering', type=str, help='Ordering of decision-making variables (e.g., "z1,z2,z3").')
    parser.add_argument('output', type=str, help='List of Boolean outputs (e.g., "0,1,1,0").')
    args = parser.parse_args()

    p_ordering = args.ordering.split(',')
    tree_output = [bool(int(x)) for x in args.output.split(',')]
    tree = gen_tree(p_ordering, tree_output)
    string_to_file(tree, args.file)
    print(f"Decision tree saved to {args.file}.")
    
    
