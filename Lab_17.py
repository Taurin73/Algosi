class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(tree):
    stack = []
    i = 0
    numbers = []
    tree = tree.replace(' ', '')
    comma = False
    while i < len(tree):
        if tree[i].isdigit() or tree[i] == '-':
            number = ''

            while i < len(tree) and (tree[i].isdigit() or tree[i] == '-'):
                number += tree[i]
                i += 1
            node = Node(number)

            if stack:
                parent = stack[-1]
                if comma:
                    parent.right = node
                    comma = False
                elif parent.left is None:
                    parent.left = node
                elif parent.right is None:
                    parent.right = node
            numbers.append(node)

        elif tree[i] == ',':
            comma = True
            i += 1
        elif tree[i] == '(':
            stack += numbers
            i += 1
        elif tree[i] == ')':
            numbers = []
            stack.pop()
            i += 1
        else:
            i += 1
    return stack[0]


def add(node, number):
    if number < int(node.data):
        if not node.left:
            node.left = Node(str(number))
            return
        add(node.left, number)

    elif number > int(node.data):
        if not node.right:
            node.right = Node(str(number))
            return
        add(node.right, number)


def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current


def delete(node, number):
    if node is None:
        return node

    if int(number) < int(node.data):
        node.left = delete(node.left, number)
    elif int(number) > int(node.data):
        node.right = delete(node.right, number)
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


def find(node, number):
    if not node:
        print("Цифры нет в дереве\n\n")

    elif int(node.data) == int(number):
        print("Цифра есть в дереве\n\n")
        return node

    elif int(number) > int(node.data):
        return find(node.right, number)
    elif int(number) < int(node.data):
        return find(node.left, number)


def print_tree(node, level=0, prefix="Tree: "):
    if node:
        print(" " * (level * 4) + prefix + str(node.data))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")


lst = "8 (4 (2 (1, 3), 9 (7,11)), 10 (, 14(13,)))"
# lst = "1 (2 (3 (4 (5 (6 (7 (8, 9), 10), 11), 12), 13), 14), 15)"
root = build_tree(lst)
button = 0

while 1:
    if button != '3':
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
