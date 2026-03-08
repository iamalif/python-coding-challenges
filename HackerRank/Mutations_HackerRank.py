def mutate_string(string, position, character):
    
    str = list(string)
    str[position] = character
    str = "".join(str)
    
    return str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)