import sys

# Part 1

def solut1():

    filtered_input = sys.stdin.read().strip().split(",")

    ans = 0

    for item in filtered_input:
        start, end = item.split("-")
        start = int(start)
        end = int(end)
        for num in range(start, end + 1):
            num_str = str(num)
            if len(num_str) % 2 == 0:
                middle = len(num_str) // 2
                first_half = num_str[:middle]
                second_half = num_str[middle:]
                if first_half == second_half:
                    ans += num

    return ans

print(solut1())

# Part 2 

def solut2():

    filtered_input = sys.stdin.read().strip().split(",")

    ans = 0

    found = []

    for item in filtered_input:
        start, end = item.split("-")
        start = int(start)
        end = int(end)
        for num in range(start, end + 1):
            num_str = str(num) # 11
            for i in range(1, len(num_str) + 1):
                if len(num_str) % i == 0: 
                    block_length = len(num_str) // i
                    if block_length != len(num_str):
                        block = num_str[:block_length] # get first block
                        for j in range(block_length, len(num_str), block_length):
                            curr_subset = num_str[j:j+block_length]
                            if block != curr_subset:
                                break
                            elif j == len(num_str) - block_length:
                                if num not in found:
                                    found.append(num)
                                    ans += num

    return ans

             

print(solut2())
