### How to run:
From the command line, run ```python3 neural_network.py --help``` to see what arguments are required and how to specify them. 
An example call is ```python3 neural_network.py -hn 2 -on 1 -lr 0.3 -ep 10000 xor.txt```. 

### What each file does:
* ```helper_functions.py```
  * ```sigmoid()```
  * ```init_weights_biases()```
  * ```read_file_to_array()```
* ```neural_network.py``` includes the algorithm of training the neural network:
  * ```forward_propagate()```
  * ```backprop()```
  * ```train_network()```
  * ```main()``` handles input from the terminal...
