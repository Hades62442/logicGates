def AND(a,b):
    return (a and b)

def OR(a,b):
    return (a or b)

def XOR(a,b):
    return (a!=b)

def NOT(a):
    return (not a)

def NAND(a,b):
    return not (AND(a,b))

def NOR(a,b):
    return not (OR(a,b))

def XNOR(a,b):
    return (a == b)


def test():
    print(f"Input A\tInput B\tAND\tOR\tXOR\tNAND\tNOR\tXNOR")
    a = False
    b = False
    print(f"{a}\t{b}\t{AND(a,b)}\t{OR(a,b)}\t{XOR(a,b)}\t{NAND(a,b)}\t{NOR(a,b)}\t{XNOR(a,b)}")
    b = True
    print(f"{a}\t{b}\t{AND(a,b)}\t{OR(a,b)}\t{XOR(a,b)}\t{NAND(a,b)}\t{NOR(a,b)}\t{XNOR(a,b)}")
    a = True
    b = False
    print(f"{a}\t{b}\t{AND(a,b)}\t{OR(a,b)}\t{XOR(a,b)}\t{NAND(a,b)}\t{NOR(a,b)}\t{XNOR(a,b)}")
    b = True
    print(f"{a}\t{b}\t{AND(a,b)}\t{OR(a,b)}\t{XOR(a,b)}\t{NAND(a,b)}\t{NOR(a,b)}\t{XNOR(a,b)}")

test()