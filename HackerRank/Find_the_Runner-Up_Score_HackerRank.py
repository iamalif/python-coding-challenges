if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    elems = list(arr)
    
    winner = max(elems)
    
    while winner in elems:
        elems.remove(winner)
    
    runner_up = max(elems)
    
    print(runner_up)
