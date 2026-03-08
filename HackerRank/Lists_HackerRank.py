if __name__ == '__main__':
    N = int(input())
    
    commands = []
    
    for i in range(0, N):
        command = input()
        commands.append(command)
        
    #print(N)

    for i, command in enumerate(commands):
        split_command = command.split()
        commands[i] = split_command

    output = []

    for i, command in enumerate(commands):
        if commands[i][0] == "insert":
            output.insert(int(command[1]), int(command[2]))
        elif commands[i][0] == "print":
            print(output)
        elif commands[i][0] == "remove":
            output.remove(int(command[1]))
        elif commands[i][0] == "append":
            output.append(int(command[1]))
        elif commands[i][0] == "sort":
            output.sort()
        elif commands[i][0] == "pop":
            output.pop()
        elif commands[i][0] == "reverse":
            output.reverse()
    
