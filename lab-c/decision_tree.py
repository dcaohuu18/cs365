'''
Dong Cao
CS365 Lab C
decision_tree.py
'''


from helper_functions import Node, read_file, importance, print_tree, count_nodes
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


#########################################################
# Accuracy Testing:


def classify_example(example, des_tree_root):
    if des_tree_root.classification != None:
        return des_tree_root.classification
    
    for child in des_tree_root.children_list:
        if example[child.attribute] == child.att_value:
            return classify_example(example, child)


def training_set_accuracy(yes_exs, no_exs, des_tree_root):
    correct = 0 
    
    for ex in yes_exs:
        if classify_example(ex, des_tree_root) == 'yes':
            correct += 1

    for ex in no_exs:
        if classify_example(ex, des_tree_root) == 'no':
            correct += 1    
    
    return correct/(len(yes_exs)+len(no_exs))


def test_set_accuracy(yes_exs, no_exs, attributes): # leave-one-out cross-validation
    correct = 0

    for i in range(len(yes_exs)):
        curtailed_yes_exs = copy.deepcopy(yes_exs[:i]) + copy.deepcopy(yes_exs[i+1:]) # this takes a lot of time!
        
        root = Node(curtailed_yes_exs, no_exs)
        build_decision_tree(root, curtailed_yes_exs, no_exs, attributes, curtailed_yes_exs, no_exs)
        
        if classify_example(yes_exs[i], root) == 'yes':
            correct += 1

    for i in range(len(no_exs)):
        curtailed_no_exs = copy.deepcopy(no_exs[:i]) + copy.deepcopy(no_exs[i+1:])
        
        root = Node(yes_exs, curtailed_no_exs)
        build_decision_tree(root, yes_exs, curtailed_no_exs, attributes, yes_exs, curtailed_no_exs)
        
        if classify_example(no_exs[i], root) == 'no':
            correct += 1
    
    return correct/(len(yes_exs)+len(no_exs))


#########################################################


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help ="Enter input file name", type = str)
    args = parser.parse_args()
    
    yes_exs, no_exs, attributes = read_file(args.file_name)

    root = Node(yes_exs, no_exs)
    build_decision_tree(root, yes_exs, no_exs, attributes, yes_exs, no_exs) # expand the decision tree
    
    print_tree(root)

    print("number of nodes is: {}".format(count_nodes(root)))

    print("training_set_accuracy is: {:.2%}".format(training_set_accuracy(yes_exs, no_exs, root)))

    run_cross_val = input("Do you want to run leave-one-out cross-validation (y/n)? ")

    if run_cross_val == 'y':
        print("test_set_accuracy is: {:.2%}".format(test_set_accuracy(yes_exs, no_exs, attributes)))

    elif run_cross_val != 'n':
        print("Invalid input! Please enter either 'y' or 'n'.")


if __name__ == '__main__':
    main()