'''
Dong Cao
CS365 Lab D
neural_network.py
'''


from helper_functions import sigmoid, init_weights_biases, read_file_to_arrays
import numpy as np
import argparse


def forward_propagate(feature_array, weights_biases_dict):
    hidden_layer_values = np.dot(weights_biases_dict['hidden_weights'], feature_array) + weights_biases_dict['hidden_biases']
    hidden_layer_outputs = sigmoid(hidden_layer_values)

    output_layer_values = np.dot(weights_biases_dict['output_weights'], hidden_layer_outputs) + weights_biases_dict['output_biases']
    output_layer_outputs = sigmoid(output_layer_values)

    output_vals = {
    'hidden_layer_outputs': hidden_layer_outputs,
    'output_layer_outputs': output_layer_outputs
    }

    return output_vals


# Use binary cross-entropy to calculate the loss
def find_loss(output_layer_outputs, labels):
    num_examples = labels.shape[1] # The number of examples is the number of columns in label_array

    loss = (-1 / num_examples) * np.sum(np.multiply(labels, np.log(output_layer_outputs)) +
                                        np.multiply(1-labels, np.log(1-output_layer_outputs)))
    return loss


def backprop(feature_array, labels, output_vals, weights_biases_dict, verbose=False):
    if verbose:
        print()
    # We get the number of examples by looking at how many total
    # labels there are. (Each example has a label.)
    num_examples = labels.shape[1]
    
    # These are the outputs that were calculated by each
    # of our two layers of nodes that calculate outputs.
    hidden_layer_outputs = output_vals["hidden_layer_outputs"]
    output_layer_outputs = output_vals["output_layer_outputs"]

    # These are the weights of the arrows coming into our output
    # node from each of the hidden nodes. We need these to know
    # how much blame to place on each hidden node.
    output_weights = weights_biases_dict["output_weights"]

    # This is how wrong we were on each of our examples, and in
    # what direction. If we have four training examples, there
    # will be four of these.
    # This calculation works because we are using binary cross-entropy,
    # which produces a fairly simple calculation here.
    raw_error = output_layer_outputs - labels
    if verbose:
        print("raw_error", raw_error)
    
    # This is where we calculate our gradient for each of the
    # weights on arrows coming into our output.
    output_weights_gradient = np.dot(raw_error, hidden_layer_outputs.T)/num_examples
    if verbose:
        print("output_weights_gradient", output_weights_gradient)
    
    # This is our gradient on the bias. It is simply the
    # mean of our errors.
    output_bias_gradient = np.sum(raw_error, axis=1, keepdims=True)/num_examples
    if verbose:
        print("output_bias_gradient", output_bias_gradient)
    
    # We now calculate the amount of error to propegate back to our hidden nodes.
    # First, we find the dot product of our output weights and the error
    # on each of four training examples. This allows us to figure out how much,
    # for each of our training examples, each hidden node contributed to our
    # getting things wrong.
    blame_array = np.dot(output_weights.T, raw_error)
    if verbose:
        print("blame_array", blame_array)
    
    # hidden_layer_outputs is the actual values output by our hidden layer for
    # each of the four training examples. We square each of these values.
    hidden_outputs_squared = np.power(hidden_layer_outputs, 2)
    if verbose:
        print("hidden_layer_outputs", hidden_layer_outputs)
        print("hidden_outputs_squared", hidden_outputs_squared)
    
    # We now multiply our blame array by 1 minus the squares of the hidden layer's
    # outputs.
    propagated_error = np.multiply(blame_array, 1-hidden_outputs_squared)
    if verbose:
        print("propagated_error", propagated_error)
    
    # Finally, we compute the magnitude and direction in which we
    # should adjust our weights and biases for the hidden node.
    hidden_weights_gradient = np.dot(propagated_error, feature_array.T)/num_examples
    hidden_bias_gradient = np.sum(propagated_error, axis=1, keepdims=True)/num_examples
    if verbose:
        print("hidden_weights_gradient", hidden_weights_gradient)
        print("hidden_bias_gradient", hidden_bias_gradient)
    
    # A dictionary that stores all of the gradients
    # These are values that track which direction and by
    # how much each of our weights and biases should move
    gradients = {"hidden_weights_gradient": hidden_weights_gradient,
                 "hidden_bias_gradient": hidden_bias_gradient,
                 "output_weights_gradient": output_weights_gradient,
                 "output_bias_gradient": output_bias_gradient}

    return gradients


def update_weights_biases(weights_biases_dict, gradients, learning_rate):
    updated_weights_biases = {}
    
    new_hidden_weights = weights_biases_dict['hidden_weights']-learning_rate*gradients['hidden_weights_gradient']
    updated_weights_biases['hidden_weights'] = new_hidden_weights

    new_hidden_biases = weights_biases_dict['hidden_biases']-learning_rate*gradients['hidden_bias_gradient']
    updated_weights_biases['hidden_biases'] = new_hidden_biases

    new_output_weights = weights_biases_dict['output_weights']-learning_rate*gradients['output_weights_gradient']
    updated_weights_biases['output_weights'] = new_output_weights

    new_output_biases = weights_biases_dict['output_biases']-learning_rate*gradients['output_bias_gradient']
    updated_weights_biases['output_biases'] = new_output_biases

    # >> can make a for loop to do this
    
    return updated_weights_biases


def train_network(feature_array, label_array, num_hidden_nodes, num_output_nodes, epochs, learning_rate):
    num_input_nodes = np.size(feature_array, 0) # get the num of rows 
    weights_biases_dict = init_weights_biases(num_input_nodes, num_hidden_nodes, num_output_nodes)

    for i in range(epochs):
        forward_prop_outputs = forward_propagate(feature_array, weights_biases_dict)
        
        if (i+1)%100 == 0: # report loss every 100 epochs 
            loss = find_loss(forward_prop_outputs['output_layer_outputs'], label_array)
            print('Epoch {}: {}\n'.format(i+1, loss))

        gradients_dict = backprop(feature_array, label_array, forward_prop_outputs, weights_biases_dict)
        
        weights_biases_dict = update_weights_biases(weights_biases_dict, gradients_dict, learning_rate)

    return weights_biases_dict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file_name", help="Input file name", type=str)
    parser.add_argument("-hn", "--num_hidden_nodes", metavar='', help='Number of hidden nodes', type=int, required=True)
    parser.add_argument("-on", "--num_output_nodes", metavar='', help='Number of output nodes', type=int, required=True)
    parser.add_argument("-lr", "--learning_rate", metavar='', help='Learning rate (between 0 & 1)', type =float, required=True)
    parser.add_argument("-ep", "--epochs", metavar='', help='Number of epochs', type=int, required=True)
    args = parser.parse_args()

    feature_array, label_array, header_array = read_file_to_arrays(args.input_file_name)

    weights_biases_dict = train_network(feature_array, label_array, 
                                        args.num_hidden_nodes, args.num_output_nodes, 
                                        args.epochs, args.learning_rate)


if __name__ == '__main__':
	main()