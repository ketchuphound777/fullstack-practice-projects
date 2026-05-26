def gate_and(input1, input2):
    """"an AND gate (input A ^ B)"""
    gate1 = input1 and input2
    return bool(gate1)


def gate_not(input1):
    """"an NOT gate (input 1)"""
    gate = input1
    return bool(not input1)


def circuit(a, b, c):
    """"emulates A ^ B ¬(B ^ c)"""
    gate1 = gate_and(b, c)
    gate2 = gate_not(gate1)
    gate3 = gate_and(a, gate2)
    return gate3


print(circuit(0, 0, 0))
print(circuit(0, 0, 1))
print(circuit(0, 1, 0))
print(circuit(0, 1, 0))
print(circuit(1, 0, 0))
print(circuit(1, 0, 1))
print(circuit(1, 1, 0))
print(circuit(1, 1, 1))
