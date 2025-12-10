def int_to_bin_str(bits:int, num: int):
    if num > 2**(bits-1):
        raise FunctionArgumentError(f"{num} jest poza skala")
    else:
        return "0"*(bits-len(bin(num)[2:]))+bin(num)[2:]

class FunctionArgumentError(TypeError):
    pass
    
def matricer(bits: int, one_set: list, zero_set: list):
    cubest = [int_to_bin_str(bits, i) for i in sorted(one_set)]

    cubesf = [int_to_bin_str(bits, i) for i in sorted(zero_set)]

    return [cubest, cubesf]

def dont_care_finder(bits: int, one_set: list, zero_set: list):
    dontcare = []
    for i in range(2**bits):
        if i not in one_set and i not in zero_set:
            dontcare.append(i)
    return dontcare

'''
#functions in functions list formated as so : [value name, bits, one set, zero set]
def truth_tabler(bits: int, functions: list):
    for i, values in enumerate(functions):
        continue
    return 0
'''

oneSet = [2,5,7,9,8,6]
zeroSet = [1,31,18,23]

funkcja1=[6,oneSet,zeroSet]


from os import path as pth
filePath = str(input("Enter file path: "))

with open(filePath,'w') as file:
    for i in matricer(*funkcja1)[0]:
        file.write(f"{i}\n")



