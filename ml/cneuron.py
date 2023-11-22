def step_function(n):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1
    
def neuron(inputs, weight=1, bias=1):
    summation = sum(input * weight for input in inputs) + bias
    forward_propagation = step_function(summation)
    return forward_propagation

def main():
    ZEROONEONEONE = [
        (0, [0,0]),
        (1, [1,0]),
        (1, [0,1]),
        (1, [1,1])
    ]
    ONEZEROZEROONE = [
        (1, [0,0]),
        (0, [1,0]),
        (0, [0,1]),
        (1, [1,1])
    ]
    ZEROZEROZEROONE = [
        (0, [0,0]),
        (0, [1,0]),
        (0, [0,1]),
        (1, [1,1])
    ]
    print("OR GATE")
    for outcome in ZEROONEONEONE:
        expected = outcome[0]
        inputs = outcome[1]
        decision = neuron(inputs, 1, 0)
        if decision == expected:
            print(decision, expected, "correct")
        else:
            print("wrong")
    print("")
    print("AND GATE")
    for outcome in ZEROZEROZEROONE:
        expected = outcome[0]
        inputs = outcome[1]
        layer0 = neuron(inputs, 2, -2), neuron(inputs, -1, 2)
        layer1 = neuron(layer0, 1, 100), neuron(inputs, -1, 50)
        decision = neuron(layer1, 2 ,0)
        if decision == expected:
            print(decision, expected, "correct")
        else:
            print("wrong")
    print("")

    print("success")

# main()
