class Node:   # Класс узла для двоичного дерева
    def __init__(self, data):
        # Инициализация узла с данными
        self.data = data
        self.left = None  # Левый потомок
        self.right = None  # Правый потомок


def build_tree(tree):   # Функция для построения дерева из строки
    stack = []   # Стек для хранения узлов
    i = 0   #Индекс для итерации по строке
    numbers = []  # Список для хранения узлов дерева
    tree = tree.replace(' ', '')  # Удаление пробелов из строки
    comma = False  # Флаг для разделителя ','
    while i < len(tree):
        if tree[i].isdigit() or tree[i] == '-':   # Если символ является цифрой или минусом (для отрицательных чисел)
            number = ''

            while i < len(tree) and (tree[i].isdigit() or tree[i] == '-'):  # Считываем число
                number += tree[i]
                i += 1
            node = Node(number)

            if stack:   # Если стек не пустой, устанавливаем связи между узлами
                parent = stack[-1]
                if comma:
                    parent.right = node
                    comma = False
                elif parent.left is None:
                    parent.left = node
                elif parent.right is None:
                    parent.right = node
            numbers.append(node)

        elif tree[i] == ',':   # Если символ является разделителем ','
            comma = True
            i += 1
        elif tree[i] == '(':   # Если символ является открывающей скобкой '('
            stack += numbers
            i += 1
        elif tree[i] == ')':   # Если символ является закрывающей скобкой ')'
            numbers = []
            stack.pop()
            i += 1
        else:   # Если символ не является цифрой, минусом, ',', '(' или ')'
            i += 1
    return stack[0]   # Возвращаем корень дерева



def add(node, number):   # Функция для добавления узла в дерево
    if number < int(node.data):   # Если число меньше значения текущего узла
        if not node.left:   # Если нет левого потомка, создаем новый узел
            node.left = Node(str(number))
            return
        add(node.left, number)    # Рекурсивно вызываем для левого потомка

    elif number > int(node.data):    # Если число больше значения текущего узла
        if not node.right:   # Если нет правого потомка, также создаем узел
            node.right = Node(str(number))
            return
        add(node.right, number)   # Рекурсивно вызываем для правого потомка


def find_min(node):     # Функция для поиска минимального значения в дереве
    current = node
    while current.left:
        current = current.left
    return current


def delete(node, number):   # Функция для удаления узла из дерева
    if node is None:
        return node

    if int(number) < int(node.data):   # Если число меньше значения текущего узла
        node.left = delete(node.left, number)    # Рекурсивно вызываем для левого потомка
    elif int(number) > int(node.data):  # Если число больше значения текущего узла
        node.right = delete(node.right, number)  # Рекурсивно вызываем для правого потомка
    else:
        # У узла нет детей или только один ребенок
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        # У узла есть два ребенка
        temp = find_min(node.right)  # Найти наименьший узел в правом поддереве
        node.data = temp.data  # Заменить удаляемый узел на наименьший узел
        node.right = delete(node.right, temp.data)  # Удалить наименьший узел из правого поддерева

    return node


def find(node, number):   # Функция для поиска узла с заданным значением
    if not node:
        print("Цифры нет в дереве\n\n")

    elif int(node.data) == int(number):
        print("Цифра есть в дереве\n\n")
        return node

    elif int(number) > int(node.data):
        return find(node.right, number) # Вызываем для правого потомка
    elif int(number) < int(node.data):
        return find(node.left, number)   # Вызываем для левого потомка


def print_tree(node, level=0, prefix="Tree: "):   # Функция для отображения (печати) дерева
    if node:
        print(" " * (level * 4) + prefix + str(node.data))
        if node.left or node.right: # Если есть потомки, вызываем для них:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")


lst = "8 (4 (2 (1, 3), 9 (7,11)), 10 (, 14(13,)))"
# lst = "1 (2 (3 (4 (5 (6 (7 (8, 9), 10), 11), 12), 13), 14), 15)"

root = build_tree(lst)   # Построение дерева
button = 0   # Инициализация переменной для выбора в меню

while 1:
    if button != '3':   # Если выбрана не опция поиска, печатаем дерево
        print(100 * '\n')
        print_tree(root)
    print("Меню:")
    print('Добавить (1)')
    print('Удалить  (2)')
    print('Поиск    (3)')
    print('Выйти    (4)')

    button = input()
    if button == '1':
        print("Введите число, которое хотите добавить")
        add(root, int(input()))

    elif button == '2':
        print("Введите число, которое хотите удалить")
        delete(root, int(input()))

    elif button == '3':
        print("Введите число, которое хотите найти")
        find(root, int(input()))

    elif button == '4':
        break
