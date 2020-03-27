'''
Dong Cao
CS365 Lab C
decision_tree.py
'''


from helper_functions import Node, read_file, importance, print_tree
import argparse
import copy


def build_decision_tree(root, yes_exs, no_exs, attributes, pa_yes_exs, pa_no_exs):
    if yes_exs == [] and no_exs == []: # empty box
        if len(pa_yes_exs) > len(pa_no_exs):
            root.classification = 'yes' # plurality value of parent examples
        else:
            root.classification = 'no'
        return # stop expanding further 

    elif yes_exs == []:
        root.classification = 'no'
        return 

    elif no_exs == []:
        root.classification = 'yes'
        return 

    elif attributes == {}:
        if len(yes_exs) > len(no_exs):
            root.classification = 'yes' # plurality value of current examples
        else:
            root.classification = 'no'
        return # stop expanding further

    else: # expand further
        attribute_keys = list(attributes.keys())
        A = attribute_keys[0] # most important attribute 
        max_gain, children = importance(A, attributes[A], yes_exs, no_exs)

        for att in attribute_keys[1:]:
            temp_gain, temp_chil = importance(att, attributes[att], yes_exs, no_exs)

            if temp_gain > max_gain:
                max_gain, children = temp_gain, temp_chil
                A = att # most important attribute

        root.children_list = children

        child_attributes = copy.deepcopy(attributes)
        del child_attributes[A]

        for child in root.children_list:
            build_decision_tree(child, child.yes_exs, child.no_exs, child_attributes, yes_exs, no_exs)

        return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help ="Enter input file name", type = str)
    args = parser.parse_args()
    
    yes_exs, no_exs, attributes = read_file(args.file_name)

    root = Node(yes_exs, no_exs)
    build_decision_tree(root, yes_exs, no_exs, attributes, yes_exs, no_exs) # expand the decision tree
    
    print_tree(root)


if __name__ == '__main__':
	main()