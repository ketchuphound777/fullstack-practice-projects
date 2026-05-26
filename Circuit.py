def gate_and(input1, input2):
    """ an AND gate (input1 ^ input2) """
    gate1 = input1 and input2
    return bool(gate1)


def gate_or(input1, input2):
    """ an OR gate (input1 v input2) """
    gate1 = input1 or input2
    return bool(gate1)


def gate_xor(input1, input2):
    """ an XOR gate ((input1 ^ ~input2) v (~input1 ^ input2)) """
    gate1 = input1 and not input2
    gate2 = input2 and not input1
    return bool(gate1 or gate2)


def gate_nand(input1, input2):
    """ a NAND gate (~(input1 ^ input2)) """
    gate1 = not (input1 and input2)
    return bool(gate1)


def gate_nor(input1, input2):
    """ a NOR gate (~(input1 v input2)) """
    gate1 = not (input1 or input2)
    return bool(gate1)


def gate_not(input1):
    """ a NOT gate (~input1) """
    return bool(not input1)


def circuit(a, b, c, d):
    """emulates (~A ^ B ^ C ^ D) v (A ^ ~B ^ C ^ D) v (A ^ B ^ ~C ^ D) v (A ^ B ^ C ^ ~D)"""
    gate1 = gate_not(a)  # A
    gate2 = gate_and(gate1, b)  # ~A ^ B
    gate3 = gate_and(gate2, c)  # ~A ^ B ^ C
    gate4 = gate_and(gate3, d)  # ~A ^ B ^ C ^D (Term 1)

    gate5 = gate_not(b)  # ~B
    gate6 = gate_and(a, gate5)  # A ^ B
    gate7 = gate_and(gate6, c)  # A ^ B ^ C
    gate8 = gate_and(gate7, d)  # A ^ B ^ C ^ D (Term 2)

    gate9 = gate_not(c)  # ~C
    gate10 = gate_and(a, b)  # A ^ B
    gate11 = gate_and(gate10, gate9)  # A ^ B ^ ~C
    gate12 = gate_and(gate11, d)  # A ^ B ^ ~C ^ D (Term 3)

    gate13 = gate_not(d)  # ~D
    gate14 = gate_and(a, b)  # A ^ B
    gate15 = gate_and(gate14, c)  # A ^ B ^ C
    gate16 = gate_and(gate15, gate13)  # A ^ B ^ C ^ ~D

    gate17 = gate_or(gate4, gate8)  # Term1 V Term2
    gate18 = gate_or(gate12, gate16)  # Term3 V Term4
    gate19 = gate_or(gate17, gate18)  # (Term1 V Term2) V (Term3 V Term4)

    return gate19


print(circuit(0, 0, 0, 0))
print(circuit(0, 0, 0, 1))
print(circuit(0, 0, 1, 0))
print(circuit(0, 0, 1, 1))
print(circuit(0, 1, 0, 0))
print(circuit(0, 1, 0, 1))
print(circuit(0, 1, 1, 0))
print(circuit(0, 1, 1, 1))
print(circuit(1, 0, 0, 0))
print(circuit(1, 0, 0, 1))
print(circuit(1, 0, 1, 0))
print(circuit(1, 0, 1, 1))
print(circuit(1, 1, 0, 0))
print(circuit(1, 1, 0, 1))
print(circuit(1, 1, 1, 0))
print(circuit(1, 1, 1, 1))
