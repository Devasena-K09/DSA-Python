def evaluate_postfix(tokens):

    stack = []

    for token in tokens:

        if token not in "+-*/":

            stack.append(int(token))

        else:

            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)

            elif token == '-':
                stack.append(a - b)

            elif token == '*':
                stack.append(a * b)

            elif token == '/':
                stack.append(int(a / b))

    return stack[0]


expression = ["2", "1", "+", "3", "*"]

print(evaluate_postfix(expression))
