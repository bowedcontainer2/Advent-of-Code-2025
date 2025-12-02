import sys

def solut():

    filtered_input = sys.stdin.read().splitlines()
    
    current = 50
    
    ans = 0
    
    for item in filtered_input:
        dir = item[0]
        
        if dir == "R":
            number = int(item[1:])
            init_ticks = number // 100
            ans += init_ticks
            simple_move = number - (init_ticks * 100)
            current_move = current + simple_move

            if current != 0 and current_move > 100:
                ans += 1
            current = current_move % 100
        else:
            number = int(item[1:])
            init_ticks = number // 100
            ans += init_ticks
            simple_move = number - (init_ticks * 100)
            current_move = current - simple_move
            
            if current != 0 and current_move < 0:
                ans += 1
            current = current_move % 100

        if current == 0:
            ans += 1

        
    return ans
    
print(solut())
