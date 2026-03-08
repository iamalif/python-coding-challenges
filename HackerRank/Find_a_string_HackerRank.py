def count_substring(string, sub_string):
    
    main_str = string
    sub_str = sub_string
    start = 0
    counter = 0

    while True:
        position = main_str.find(sub_str, start)
        
        if position == -1:
            break

        counter += 1
        start = position +1
    
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)