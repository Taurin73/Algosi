def calculate(exp):
    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
#заполнение стека результатами операций
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            values.append(left / right)

    def priority(operator):
        if operator in ('+', '-'):
            return 1
        if operator in ('*', '/'):
            return 2
        return 0

    operators = []
    values = []
    i = 0
    stack = []
    
# проверки на некорректный ввод(деление на 0, пробел в выражении)

    if '/0' in exp:
        return 'Нельзя делить на 0!'

    if ' ' in exp:
        return 'Пробел в выражении!'
# проверка порядка скобок
    for j in exp:
        if j == ')' and not stack:
            return 'Скобки стоят не верно!'
        elif j == '(':
            stack.append(j)
        elif j == ')' and stack[-1] == '(':
            stack.pop()
    if len(stack) > 0:
        return 'Скобки стоят не верно!'
    

    while i < len(exp):
        if exp[i].isdigit():
            if i == 1 and exp[0] == '-':
                values.append(int(exp[i]) * -1)
                operators.pop()
            else:
                values.append(int(exp[i]))
            i += 1
        elif exp[i] in '+-*/':
            while (operators and operators[-1] in '+-*/' and priority(operators[-1]) >= priority(exp[i])):
                apply_operator(operators, values)
            operators.append(exp[i])
            i += 1
        elif exp[i] == '(':
            operators.append(exp[i])
            i += 1
        elif exp[i] == ')':
            while operators[-1] != '(':
                apply_operator(operators, values) # Считаем выражение в скобках
            operators.pop()
            i += 1
        elif exp[i] == '=':
            while operators:
                apply_operator(operators, values)
            return values[0]
        #print(values)
        #print(operators)

# ввод выражений
expressions = [
    '-2+7*(5/3+9)-5=',
    '2+3*4-5=',
    '(6-2)/2*5=',
    '0/2+7-3*2=',
    '3*2+(8/4)=',
    '5*2-8/4+1=',
    '2+(4*3)/2=',
    '(9-3)*(6/3)=',
    '5*(2+3)-4/2=',
    '7-(4+2/2)*3=',
    '(5/3)*(4-1)=']
for i in expressions:
    print(calculate(i), '==', eval(i[:-1]))

# выражения с ошибками(для примера)
fool_expressions = [
    '2 2+5*(4-7)',
    '2+(4*3))/2=',
    '(6-2)/0*5=']

for i in fool_expressions:
    print(calculate(i))

