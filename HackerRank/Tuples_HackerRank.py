# Enter your code here. Read input from STDIN. Print output to STDOUT
input1 = int(input())
input2 = input()

input_list = map(int, input2.split())
input_tuple = tuple(input_list)

print(hash(input_tuple))
