'''
Dong Cao
CS365 Lab D
compare_exp.py
'''


from helper_functions import sigmoid, init_weights_biases, read_file_to_arrays, print_result_table
from neural_network import forward_propagate, find_loss, backprop, update_weights_biases
import numpy as np
import argparse


def train_network(weights_biases_dict, feature_array, label_array, num_hidden_nodes, num_output_nodes, epochs, learning_rate):
    for i in range(epochs):
        forward_prop_outputs = forward_propagate(feature_array, weights_biases_dict)

        gradients_dict = backprop(feature_array, label_array, forward_prop_outputs, weights_biases_dict)
        
        weights_biases_dict = update_weights_biases(weights_biases_dict, gradients_dict, learning_rate)

    loss = find_loss(forward_prop_outputs['output_layer_outputs'], label_array)
    print('final loss = {}'.format(loss))

    return weights_biases_dict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file_name", help="Input file name", type=str)
    parser.add_argument("-hn", "--num_hidden_nodes", metavar='', help='Number of hidden nodes', type=int, required=True)
    parser.add_argument("-on", "--num_output_nodes", metavar='', help='Number of output nodes', type=int, required=True)
    parser.add_argument("-lr", "--learning_rate", metavar='', help='Learning rate', type =float, required=True)
    parser.add_argument("-ep", "--epochs", metavar='', help='Number of epochs', type=int, required=True)
    args = parser.parse_args()

    feature_array, label_array, header_array = read_file_to_arrays(args.input_file_name)

    num_input_nodes = np.size(feature_array, 0) # get the num of rows/features
    first_weights_biases = init_weights_biases(num_input_nodes, args.num_hidden_nodes, args.num_output_nodes)

    print("\nlearning rate = {}, epochs = {}:".format(args.learning_rate, args.epochs))

    final_weights_biases = train_network(first_weights_biases, feature_array, label_array, 
                                        args.num_hidden_nodes, args.num_output_nodes, 
                                        args.epochs, args.learning_rate)

    output_vals = forward_propagate(feature_array, final_weights_biases)
    output_layer_outputs = output_vals['output_layer_outputs']

    print_result_table(args.input_file_name, output_layer_outputs)

    compare = input("\nDo you want to use another learning rate or number of epochs (y/n)? ")

    while compare != 'n':
        if compare == 'y':
            try:
                args.learning_rate = float(input("new learning rate = "))
                args.epochs = int(input("new number of epochs = "))

                print("\nlearning rate = {}, epochs = {}:".format(args.learning_rate, args.epochs))

                final_weights_biases = train_network(first_weights_biases, feature_array, label_array, 
                                                    args.num_hidden_nodes, args.num_output_nodes, 
                                                    args.epochs, args.learning_rate)

                output_vals = forward_propagate(feature_array, final_weights_biases)
                output_layer_outputs = output_vals['output_layer_outputs']

                print_result_table(args.input_file_name, output_layer_outputs)
        
            except ValueError:
                print("Invalid input: learning rate must be a float and number of epochs must be an integer!")

        else:
            print("Invalid input: only accepts 'y' or 'n'!")

        compare = input("\nDo you want to use another learning rate or number of epochs (y/n)? ")


if __name__ == '__main__':
	main()