num1 = float (input("entr a number: "))
num2 = float (input("entr a number: "))
opr = input (" :(/, *, -, +)")

if opr == '+':
    result = num1 + num2
elif opr == '-':
    result = num1 - num2
elif opr == '*':
    result = num1 * num2
elif opr == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero!"
else:
    result = "Invalid operation!"

print("Result:", result)
