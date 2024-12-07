''''''''''''
'''code'''
''''''''''''

def is_safe(report):
    is_increasing = None
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        
        if diff < 1 or diff > 3:
            return False
        
        if is_increasing is None:
            is_increasing = report[i] < report[i + 1]
        elif is_increasing != (report[i] < report[i + 1]):
            return False
    
    return True

def count_safe_reports(lines):
    safe_count = 0
    
    for line in lines:
        report = list(map(int, line.split()))
        
        if is_safe(report):
            safe_count += 1
    
    return safe_count

''''''''''''
'''input'''
''''''''''''


#Replace with your file path below
fileName = "/home/landen/Python-3.12.3/Programs/AdventOfCode/AOC2TXT.py"

with open(fileName, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

safe_reports = count_safe_reports(lines)
print(safe_reports)




