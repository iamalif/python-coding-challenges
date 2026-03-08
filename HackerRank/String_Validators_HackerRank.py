if __name__ == '__main__':
    s = input()
    
    # Alphanumeric checker /// DONE
    print(any(char.isalnum() for char in s))
        
    # Alphabetical checker
    print(any(char.isalpha() for char in s))
        
    # Digit checker /// DONE
    digit_checker = list(s)
    digit_checker_result = False
    for digit in digit_checker:
        if digit.isdigit():
            digit_checker_result = True
            break
        else:
            digit_checker_result = False
    print(digit_checker_result)
    
    # Lower checker
    print(any(char.islower() for char in s))
    
    # Upper checker
    print(any(char.isupper() for char in s))    
    
