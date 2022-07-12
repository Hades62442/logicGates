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


def test(a,b):
    print(f"{AND(a,b)}\t{OR(a,b)}\t{XOR(a,b)}\t{NAND(a,b)}\t{NOR(a,b)}\t{XNOR(a,b)}")

a = False
b = False
test(a,b)
b = True
test(a,b)
a = True
b = False
test(a,b)
b = True
test(a,b)