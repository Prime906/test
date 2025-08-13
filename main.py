import numpy as np

inputs = [ 28,85 ]
weights =[ 0.5, 0.5]
bias = -30

weighted_inputs = [inputs[i]* [i] for i in range(len(inputs))]
total_input = sum(weighted_inputs) + bias

def sigmoid(x):
    return 1/(1 + np.exp(-x))

activated_output = sigmoid(total_input)
print("Chance of rain", activated_output)