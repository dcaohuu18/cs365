'''
Dong Cao
CS365 Lab D
helper_functions.py
'''


import numpy as np


def sigmoid(x):
	return 1/(1 + np.exp(-x))


def init_weights_biases(num_input_nodes, num_hidden_nodes, num_output_nodes): # + num_hidden_layers
    weights_biases_dict = {}

    weights_biases_dict['hidden_biases'] = np.zeros((num_hidden_nodes, 1))
    weights_biases_dict['output_biases'] = np.zeros((num_output_nodes, 1))

    weights_biases_dict['hidden_weights'] = np.random.randn(num_hidden_nodes, num_input_nodes)
    weights_biases_dict['output_weights'] = np.random.randn(num_output_nodes, num_hidden_nodes)

    return weights_biases_dict	


def read_file_to_arrays(file_name, delimiter = '\t'):
    with open(file_name, 'r') as inputFile:
        lines_list = inputFile.readlines()
        
        header_list = lines_list[0].split(delimiter)
        header_array = np.array([header.strip() for header in header_list], ndmin = 2)
        header_array = np.transpose(header_array)

        label_list = []
       	feature_list = []

        for line in lines_list[1:]:
            cols = line.split(delimiter)

            label_list.append(float(cols[-1])) #last col is the label
            feature_list.append([float(feature) for feature in cols[:-1]])

        label_array = np.array(label_list, ndmin = 2)
        
        feature_array = np.array(feature_list)
        feature_array = np.transpose(feature_array)
    
    return feature_array, label_array, header_array


if __name__ == '__main__':
    print(sigmoid(10))
    print(init_weights_biases(2,2,1))
    features, labels, headers = read_file_to_arrays('xor.txt')

    print(features)
    print(labels)
    print(headers)