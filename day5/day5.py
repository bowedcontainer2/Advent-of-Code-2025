import sys

# Part 1
def solut1():

    ranges = []
    ingredients = []
    before_empty = True
    ans = 0

    for line in sys.stdin:
        if line.strip() == "":
            before_empty = False
            continue
        # Process each non-empty line here
        if before_empty:
            ranges.append(line.strip())
        else:
            ingredients.append(int(line.strip()))

    for ing in ingredients:
        for r in ranges:
            x, y = map(int, r.split('-'))
            if ing in range(x, y + 1):
                ans += 1
                break

    return ans

# print(solut1())

# Part 2
def solut2():

    ranges = []
    ans = 0

    for line in sys.stdin:
        if line.strip() == "":
            break
        ranges.append(line.strip())


    parsed = [list(map(int, r.split('-'))) for r in ranges]

    sorted_ranges = sorted(parsed, key=lambda range: range[0])


    merged_ranges = []

    for x, y in sorted_ranges:
         # if current x is bigger than the last y, then no overlap
        if not merged_ranges or x > merged_ranges[-1][1]:
            merged_ranges.append([x, y])
        else:
            # there is overlap, so we merge. (x is <= last y)
            merged_ranges[-1][1] = max(merged_ranges[-1][1], y)

    for x, y in merged_ranges:
        ans += (y - x + 1)

    return ans




print(solut2())