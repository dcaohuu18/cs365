'''
Dong Cao
CS365 Lab C
helper_functions.py
'''


class Node:
    def __init__(self, yes_exs, no_exs, attribute = None, att_value = None):
        self.yes_exs = yes_exs
        self.no_exs = no_exs
        self.children_list = []
        self.attribute = attribute
        self.att_value = att_value
        self.classification = None 


#########################################################


import math


def read_file(file_name):    
    yes_exs = []
    no_exs = []

    with open(file_name, 'r') as inputFile:
        lines_list = inputFile.readlines()
        attributes_list = lines_list[0].split('\t')[:-1] # we don't need the last column (the classification attribute)
        attributes_dict = {attribute: set() for attribute in attributes_list}
        
        for line in lines_list[1:]:
            values = line.split('\t')
            classification = values[-1].strip()
            del values[-1] # we no longer need the last column

            if classification == 'yes':
                example = {}

                for att, val in zip(attributes_list, values):
                    attributes_dict[att].add(val)
                    example[att] = val
                
                yes_exs.append(example)

            else:
                example = {}

                for att, val in zip(attributes_list, values):
                    attributes_dict[att].add(val)
                    example[att] = val
                
                no_exs.append(example)

    return yes_exs, no_exs, attributes_dict

def entropy(q):
    if q != 0 and q != 1: 
        return -(q*math.log(q, 2) + (1-q)*math.log(1-q, 2))
    
    elif q == 0:
        return -((1-q)*math.log(1-q, 2))
    
    elif q == 1:
        return -(q*math.log(q, 2))


def importance(attribute, att_values, yes_exs, no_exs): # actually split the tree
    children_nodes = []

    for val in att_values: # split 
        child_yes_exs = [ex for ex in yes_exs if ex[attribute] == val] # can we go through all the examples just once?
        child_no_exs = [ex for ex in no_exs if ex[attribute] == val]
        children_nodes.append(Node(child_yes_exs, child_no_exs, attribute, val))

    remainder = 0

    for child in children_nodes:
        try:
            child_entropy = entropy(len(child.yes_exs)/(len(child.yes_exs)+len(child.no_exs)))
        except ZeroDivisionError: # empty box
            continue

        remainder += (len(child.yes_exs)+len(child.no_exs))/(len(yes_exs)+len(no_exs)) * child_entropy

    info_gain = entropy(len(yes_exs)/(len(yes_exs)+len(no_exs))) - remainder

    return info_gain, children_nodes 


def print_tree(root, level = 0):
    identation = (level-1)*"    "

    if root.classification == None:
        if level != 0: # not the root
            print(identation + "|{att} = {val}".format(att=root.attribute, val=root.att_value))
        
        for child in root.children_list:
            print_tree(child, level+1)
    
    else:
        print(identation + "|{att} = {val}: {class_}".format(att=root.attribute, val=root.att_value, class_=root.classification))

'''
outlook = sunny
|  humidity = high: no
|  humidity = normal: yes
outlook = overcast: yes
outlook = rainy
|  windy = TRUE: no
|  windy = FALSE: yes
'''

if __name__ == '__main__':
	read_file('titanic2.txt')