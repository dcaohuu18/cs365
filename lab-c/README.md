### How to run:
From the command line, run ```python3 decision_tree.py <datafile.txt>```. The three datasets available in the directory are ```tennis.txt```, ```pets.txt```, and ```titanic2.txt```. After printing out the decision tree and the training set accuracy, it will prompt you to decide whether to calculate the test set accuracy (leave-one-out cross-validation) or finish the execution.

### What each file does:
* ```helper_functions.py``` includes the class ```Node``` and functions that support the decision tree building:
  * ```read_file()``` returns two lists of examples (yes and no) and a dictionary of attributes and their possible values, given the file name of the dataset.
  * ```importance()``` splits the examples on the given attribute and returns the information gain and the children nodes resulting from this split. 
  * ```print_tree()``` takes the tree's root as input and recursively prints out the tree. 
  * ```count_nodes()``` takes the tree's root as input and returns the tree's number of nodes.
* ```decision_tree.py``` includes the algorithm of building the decision tree and methods of accuracy testing:
  * ```build_decision_tree()``` takes the root, examples, and attributes as input and recursively constructs the tree by adding children nodes.
  * ```training_set_accuracy()``` takes the root and examples as input and returns the training set accuracy.
  * ```test_set_accuracy()``` takes the examples and attributes as input and returns the test set accuracy.
  * ```main()``` handles input from the terminal and calls the three functions above.
