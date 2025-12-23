import sys
import math

def solut1():

    input_data = []

    for line in sys.stdin:
        input_data.append(line.strip().split())

    operations = input_data[-1] # list of operations
    nums = [list(map(int, row)) for row in input_data[:-1]] # 2d array of the nums

    columns = list(zip(*nums)) # transpose to get columns

    result = []
    for i in range(len(operations)):
        if operations[i] == '+':
            result.append(sum(columns[i]))
        elif operations[i] == '*':
            result.append(math.prod(columns[i]))

    return sum(result)


print(solut1())