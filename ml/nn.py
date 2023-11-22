def sigmoid(x):
    """Sigmoid activation function."""
    return 1 / (1 + (2.718281828459045 ** -x)) # Using 2.718281828459045 for e's value.
def sigmoid_derivative(x):
    """Derivative of the sigmoid function."""
    return x * (1 - x)
def chatgpt():
    # Training dataset for an OR gate
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    expected_output = [[0], [1], [1], [1]]

    epochs = 10000
    lr = 0.1
    inputLayerNeurons, outputLayerNeurons = 2, 1

    # Random weights and bias initialization
    weights = [[4000.9], [-100]]
    bias = 0.3

    for _ in range(epochs):
        for i in range(len(inputs)):
            # Forward Propagation
            weighted_sum = sum([a*b for a,b in zip(inputs[i], [w[0] for w in weights])]) + bias
            predicted_output = sigmoid(weighted_sum)

            # Backpropagation
            # Using mean squared error loss function
            error = expected_output[i][0] - predicted_output
            d_predicted_output = error * sigmoid_derivative(predicted_output)
            
            # Update weights and bias
            for j in range(inputLayerNeurons):
                weights[j][0] += lr * d_predicted_output * inputs[i][j]
            bias += lr * d_predicted_output

    # Testing
    print("Results after training:")
    for i in range(len(inputs)):
        weighted_sum = sum([a*b for a,b in zip(inputs[i], [w[0] for w in weights])]) + bias
        print(inputs[i], "=>", sigmoid(weighted_sum))

class gates:
    @classmethod
    def OR(cls):
        inputs = [[0,0],[0,1],[1,0],[1,1]]
        outputs = [[0],[1],[1],[1]]
        return inputs, outputs
    @classmethod
    def XOR(cls):
        inputs = [[0,0],[0,1],[1,0],[1,1]]
        outputs = [[0],[1],[1],[0]]
        return inputs, outputs
    @classmethod
    def AND(cls):
        inputs = [[0,0],[0,1],[1,0],[1,1]]
        outputs = [[0],[0],[0],[1]]
        return inputs, outputs 

def call_function_by_name(function_name):
    return globals()[function_name]()

def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Both vectors should be of the same length.")
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result

def main(gate):
    inputs, output = getattr(globals()["gates"](), gate)() 
    weights = [3, -3] 
    learning_rate = 0.1
    bias = [0.1, 0.5]
    # sit in for epochs...
    while True:
        # getting each input to be parsed by a neuron
        for i in range(len(inputs)):
            # neuron part
            if i > 1:
                biased = bias[0]
                biased_position = 0
            else: 
                biased = bias[1]
                biased_position = 1
            weighted_sum = dot_product(inputs[i], weights) + biased
            # run it through the activation function
            perdicted_output = sigmoid(weighted_sum)
            
            # backpropagation
            error = output[i][0]
            nudge_derivative_perdicted_output = error * sigmoid_derivative(perdicted_output)
            print(nudge_derivative_perdicted_output, f"Is how much the weight is nudged by...\n\n")
            
            # now with the backpropagation we can apply error to the weight or bias
            for j in range(len(inputs[0])):
                weights[j] += learning_rate * nudge_derivative_perdicted_output
            bias[biased_position] += learning_rate * nudge_derivative_perdicted_output

        print("Results after training:")
        for i in range(len(inputs)):
            if i > 1:
                biased = bias[0]
                biased_position = 0
            else: 
                biased = bias[1]
                biased_position = 1
            weighted_sum = dot_product(inputs[i], weights) + biased
            print(inputs[i], "=>", sigmoid(weighted_sum))
        input("continue?....")

main("OR")
