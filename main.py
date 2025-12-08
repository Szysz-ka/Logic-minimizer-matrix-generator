def intToBinStr(bits:int, num: int):
    return "0"*(bits-len(bin(num)[2:]))+bin(num)[2:]


def matricer(bits: int, oneSet: list, zeroSet: list):
    cubesT = [intToBinStr(bits, i) for i in sorted(oneSet)]

    cubesF = [intToBinStr(bits, i) for i in sorted(zeroSet)]

    return [cubesT, cubesF]

print(matricer(4, [0, 1, 2, 3], [4,7,16]))