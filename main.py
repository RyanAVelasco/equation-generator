import random
import colored
from colored import stylize

total_equations = int(input('How many equations do you want? '))
base_nums = int(input('How many values to calculate? '))-1

equations = []
signs = ['+', '-', '/', '*']
count_nums = base_nums
count = 0
question_nums = 1

while 0 < total_equations:
    while count != count_nums:
            equations.append(random.randint(1, 10))
            equations.append(random.choice(signs))
            count_nums = count_nums - 1
    equations.append(1)
    print()
    print(stylize("[ Question", colored.fg("45")), \
        stylize(question_nums, colored.fg("45")), \
        stylize("]", colored.fg("45")), \
        " ".join(map(str,equations)))
    print(stylize("================================", colored.fg("7")))
    equations = []
    count_nums = base_nums
    question_nums = question_nums + 1
    total_equations = total_equations - 1

# while count < total_equations:

