### How to run:
From the command line, run ```python3 neural_network.py --help``` to see what arguments are required and how to specify them. 
An example call is ```python3 neural_network.py -hn 2 -on 1 -lr 0.3 -ep 15000 xor.txt```. 

### What each file does:
* ```helper_functions.py``` includes functions that support the neural network training:
  * ```sigmoid()```: a sigmoid function that acts as the activation function and that squashes the given x value to a value between 0 and 1.
  * ```init_weights_biases()``` initiates a dictionary of weights and biases for the hidden and output layers given the number of nodes in each layer. The weights and biases are stored in numpy arrays. 
  * ```read_file_to_array()``` takes the name of the input file and returns three numpy arrays: ```feature_array```, ```label_array```, and ```header_array```.
  * ```print_result_table()``` prints out the features, labels, and the network's outputs in a tabular format. 
* ```neural_network.py``` includes the algorithm of training the neural network:
  * ```forward_propagate()``` returns the outputs of the nodes in the hidden and output layers using forward propagation.
  * ```find_loss()``` calculates the loss (error) of the network's predictions using the Binary Cross-Entropy Loss function. 
  * ```backprop()``` does back propagation and returns a dictionary of gradients for the weights and biases. 
  * ```update_weights_biases()``` uses the gradients returned by ```backprop()``` and the given learning rate to update the weights and biases. 
  * ```train_network()``` puts everything together. It first calls ```init_weights_biases()```. It then repeatedly calls ```forward_propagate()```, ```backprop()```, and ```update_weights_biases()``` a number of times (= the given number of epochs) to better the network. It also reports the loss every 100 epochs by calling ```find_loss()```. 
  * ```main()``` handles input from the terminal, calls ```train_network()```, classifies the examples by calling ```forward_propagate()```, and prints out the result.
