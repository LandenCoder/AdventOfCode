import re

#Replace with your file path below
fileName = "/home/landen/Python-3.12.3/Programs/AdventOfCode/AOC2TXT.py"

with open(fileName, encoding="utf-8") as file:
    lines = file.readlines()
    #text = []
    #for line in file:
    #    text.append(str(line))
    #print(text)

final_sum = 0

for thing in lines:
    nums_to_multiply = re.findall(r'\d+', thing)
    final_sum += int(nums_to_multiply[0]) * int(nums_to_multiply[1])
    print(re.findall(r'\d+', thing))
    print(int(nums_to_multiply[0]))
    #print(nums_to_multiply)
    #print(int(nums_to_multiply[0]) * int(nums_to_multiply[1]))

print(final_sum)
