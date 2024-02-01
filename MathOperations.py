import random
import time

MIN_NUM = 2
MAX_NUM = 10
OPERATORS = ["+", "-", "*"]
TOTAL_TRIES = 3


def generate_problem():
    left = random.randint(MIN_NUM, MAX_NUM)
    right = random.randint(MIN_NUM, MAX_NUM)
    operator = random.choice(OPERATORS)

    expr = str(left) + ' ' + operator + ' ' + str(right)
    answ = eval(expr)
    return expr, answ

input("Press enter to start")
start_time = time.time()
wrong = 0

for i in range(TOTAL_TRIES):
    expr, answ = generate_problem()
    while True:
        guess = input('Problem #' + str(i+1) + ": " + expr + " = ")
        if guess == str(answ):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("Nice work, you finished in ", total_time,  'with ', wrong,  'wrong answers')
