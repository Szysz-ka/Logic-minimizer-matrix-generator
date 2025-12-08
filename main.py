def int_to_bin_str(bits:int, num: int):
    return "0"*(bits-len(bin(num)[2:]))+bin(num)[2:]


def matricer(bits: int, one_set: list, zero_set: list):
    cubest = [int_to_bin_str(bits, i) for i in sorted(one_set)]

    cubesf = [int_to_bin_str(bits, i) for i in sorted(zero_set)]

    return [cubest, cubesf]


'''
TO-DO
def truth_tabler(bits: int, functions: list):


#from os import path as pth
filePath = str(input("Enter file path: "))
'''