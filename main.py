import random

total_equations = 100

equations = []
signs = ['+', '-', '/', '*']

base_nums = int(input('How many values to calculate? '))-1
count_nums = base_nums
count = 0
y = 0

while 0 < total_equations:
    while count != count_nums:
            equations.append(random.randint(1, 10))
            equations.append(random.choice(signs))
            count_nums = count_nums - 1
    equations.append(1)
    print(" ".join(map(str,equations)))
    equations = []
    count_nums = base_nums
    total_equations = total_equations - 1

# while count < total_equations:

