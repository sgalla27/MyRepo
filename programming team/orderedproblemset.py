import sys
sys.stdin = open("input.txt")

n = int(sys.stdin.readline())
problems = []

for i in range(n):
    problems.append(int(sys.stdin.readline()))

print(problems)

for i in range(len(problems) - 1):
    if(problems[i] > problems[i+1]):
        if(i == n - 1):
            print(n)

slices
        
