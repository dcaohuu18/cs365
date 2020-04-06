### How to run:
From the command line, run ```python3 decision_tree.py <datafile.txt>```. The three datasets available in the directory are ```tennis.txt```, ```pets.txt```, and ```titanic2.txt```. After printing out the decision tree and the training set accuracy, it will prompt you to decide whether to calculate the test set accuracy (leave-one-out cross-validation) or finish the execution.

### What each file does:
* ```helper_functions.py``` includes the class ```Node``` and functions that support the decision tree building:
  * ```read_file()```
  * ```importance()```
  * ```print_tree()```
  * ```count_nodes()```
* ```decision_tree.py``` includes the algorithm of building the decision tree and methods of accuracy testing:
  * ```build_decision_tree()```
  * ```training_set_accuracy()```
  * ```test_set_accuracy()```
  * ```main()```
