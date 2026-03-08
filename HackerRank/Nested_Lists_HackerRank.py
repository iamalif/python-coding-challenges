if __name__ == '__main__':
    
    records = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    grades = []
    for record in records:
        grades.append(record[1])
    
    unique_grades = list(set(grades))
    unique_grades.sort()
    
    second_lowest = unique_grades[1]
    
    final_names = []
    for record in records:
        if record[1] == second_lowest:
            final_names.append(record[0])
    
    final_names.sort()
    
    for name in final_names:
        print(name)
