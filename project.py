name = input('Enter the name: ')
if name == 'shubham':
    print('Hello')
else:
    print('Sorry, wrong name')

password = input('Enter the password: ')
if password == 'python':
    print('*******************************************************************************************************')
    print('*                                 Welcome Python Project                                           *****')     
    print('********************************************************************************************************')
else:
    print('Wrong password')

print('Please select a project:')
print('1. Calculator')
print('2. Speed Test')


abc = int(input('Enter the number: '))

if abc == 1:
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    ch = int(input("Enter Choice(1-4): "))

    if ch == 1:
        a = int(input("Enter A: "))
        b = int(input("Enter B: "))
        c = a + b
        print("Sum =", c)
    elif ch == 2:
        a = int(input("Enter A: "))
        b = int(input("Enter B: "))
        c = a - b
        print("Difference =", c)
    elif ch == 3:
        a = int(input("Enter A: "))
        b = int(input("Enter B: "))
        c = a * b
        print("Product =", c)
    elif ch == 4:
        a = int(input("Enter A: "))
        b = int(input("Enter B: "))
        c = a / b
        print("Quotient =", c)

elif abc == 2:
    print('Welcome to Speed Test')
    # Add your speed test logic here

import random
import time

def generate_question():
    op1 = random.randint(1, 11)
    op2 = random.randint(1, 11)
    operand = random.choice(['+', '-', '*', '/'])
    if operand == '+':
        answer = op1 + op2
    elif operand == '-':
        answer = op1 - op2
    elif operand == '*':
        answer = op1 * op2
    elif operand == '/':
        answer = op1 / op2
    question = f"{op1} {operand} {op2}"
    return question, answer

def play_game():
    name = input('Enter your name: ')
    if name == 'shubham':
        print('Name is correct.')
    else:
        print('Wrong name, but don\'t worry. Please continue studying.')
    no_of_questions = int(input('How many questions do you want to answer? '))
    correct = 0
    start_time = time.time()
    for _ in range(no_of_questions):
        question, answer = generate_question()
        print(question)
        user_ans = float(input('What is your answer? '))
        if user_ans == answer:
            correct += 1
            print('You are correct!')
        else:
            print('You are wrong!')
    end_time = time.time()
    print(f"You got {correct} answers correct.")
    print('You used {:.3f} seconds.'.format(end_time - start_time))

play_game()


