import textwrap

def wrap(string, max_width):
    
    '''
    str = list(string)
    str_length = len(str)
    lines = int(str_length / int(max_width))
    extra = int(str_length % int(max_width))
    index_counter = 0
    
    for i in range(0, lines):
        final = ""
        for i in range(0, max_width):
            final = final.join(str[index_counter])
            index_counter += 1      
    '''
    
    wrapped = textwrap.fill(string, width=max_width)
    
    return wrapped

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)