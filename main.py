def AND(a,b):
    return (a and b)

def OR(a,b):
    return (a or b)

def XOR(a,b):
    return int(a!=b)

def NOT(a):
    return int(not a)

def NAND(a,b):
    return int(not (AND(a,b)))

def NOR(a,b):
    return int(not (OR(a,b)))

def XNOR(a,b):
    return int(a == b)


def test():
    print(f"Input A\tInput B\tAND\tOR\tXOR\tNAND\tNOR\tXNOR")
    a = 0
    b = 0
    print(f"{a}\t{b}\t{AND(a,b)}\t{OR(a,b)}\t{XOR(a,b)}\t{NAND(a,b)}\t{NOR(a,b)}\t{XNOR(a,b)}")
    b = 1
    print(f"{a}\t{b}\t{AND(a,b)}\t{OR(a,b)}\t{XOR(a,b)}\t{NAND(a,b)}\t{NOR(a,b)}\t{XNOR(a,b)}")
    a = 1
    b = 0
    print(f"{a}\t{b}\t{AND(a,b)}\t{OR(a,b)}\t{XOR(a,b)}\t{NAND(a,b)}\t{NOR(a,b)}\t{XNOR(a,b)}")
    b = 1
    print(f"{a}\t{b}\t{AND(a,b)}\t{OR(a,b)}\t{XOR(a,b)}\t{NAND(a,b)}\t{NOR(a,b)}\t{XNOR(a,b)}")

#test()

def decToBin(n):
    return int(bin(n).replace("0b", ""))

def binToDec(n):
    return int(str(n), 2)

#print(decToBin(12), binToDec(10001))

def adder(a,b,c):
    carry = OR(AND(a,b),AND(XOR(a,b),c))
    sum = XOR(XOR(a,b),c)
    return sum, carry

'''
print(f"Input A\tInput B\tCarry In\tSum\tCarry")
print(f"0\t0\t0\t\t{adder(0, 0, 0)[0]}\t{adder(0, 0, 0)[1]}")
print(f"0\t1\t0\t\t{adder(0, 1, 0)[0]}\t{adder(0, 1, 0)[1]}")
print(f"1\t0\t0\t\t{adder(1, 0, 0)[0]}\t{adder(1, 0, 0)[1]}")
print(f"1\t1\t0\t\t{adder(1, 1, 0)[0]}\t{adder(1, 1, 0)[1]}")
print(f"0\t0\t1\t\t{adder(0, 0, 1)[0]}\t{adder(0, 0, 1)[1]}")
print(f"0\t1\t1\t\t{adder(0, 1, 1)[0]}\t{adder(0, 1, 1)[1]}")
print(f"1\t0\t1\t\t{adder(1, 0, 1)[0]}\t{adder(1, 0, 1)[1]}")
print(f"1\t1\t1\t\t{adder(1, 1, 1)[0]}\t{adder(1, 1, 1)[1]}")
'''

def fourBitAdder(num1, num2, carryIn):
    # data handling
    bin1 = str(decToBin(num1)).zfill(4)
    bin2 = str(decToBin(num2)).zfill(4)

    bin1Bits, bin2Bits = [], []
    for bit in bin1:
        bin1Bits.append(int(bit))

    for bit in bin2:
        bin2Bits.append(int(bit))

    # 4-bit adder algorithm
    adder1 = adder(bin1Bits[3], bin2Bits[3], carryIn)
    adder2 = adder(bin1Bits[2], bin2Bits[2], adder1[1])
    adder3 = adder(bin1Bits[1], bin2Bits[1], adder2[1])
    adder4 = adder(bin1Bits[0], bin2Bits[0], adder3[1])

    carry = adder4[1]
    sum = [adder4[0], adder3[0], adder2[0], adder1[0]]

    # convert sum from binary to dec
    s = [str(integer) for integer in sum] # convert list into string ([1, 1, 0, 1] -> "1101")
    s = "".join(s)

    sum = binToDec(s)

    print(f"Process: {num1} + {num2}\nResult: Total is {sum}, carry is {bool(carry)}")


fourBitAdder(6, 7, 0)
fourBitAdder(10, 2, 0)
fourBitAdder(8, 10, 0)
fourBitAdder(1, 1, 0)
fourBitAdder(8, 8, 0)
fourBitAdder(15, 9, 0)