class Element:
    def __init__(self, key="", value=0):
        """
        Конструктор класса Element. Создает элемент хэш-таблицы.
        key: Ключ элемента.
        value: Значение элемента.
        """
        self.key = key
        self.value = value

class HashMap:
    N = 10  # Размер хэш-таблицы по умолчанию

    def __init__(self):
        """
        Конструктор класса HashMap. Создает хэш-таблицу с наложением.
        """
        self.size = self.N  # Размер хэш-таблицы
        self.table = [Element("", 0) for _ in range(self.N)]  # Инициализация списка элементов

    def hash(self, s):
        """
        Хэш-функция для вычисления индекса элемента в хэш-таблице.
        s: Ключ для хэширования.
        """
        h = 0
        k = 1
        for c in s:
            h += ord(c) * k
            k *= 3
        return h % self.N  # Возвращает индекс элемента в таблице по значению хэша

    def add(self, s):
        """
        Метод добавления элемента в хэш-таблицу с наложением.
        s: Ключ элемента для добавления.
        """
        h = self.hash(s)
        while self.table[h].key != "" and self.table[h].key != s and h < (self.size - 1):
            # Поиск свободного слота для нового элемента
            h += 1
        if self.table[h].key == "":
            # Добавление элемента, если слот пустой
            self.table[h] = Element(s, 1)
        elif self.table[h].key == s:
            # Увеличение счетчика, если ключ совпадает
            self.table[h].value += 1
        else:
            # Увеличение размера хэш-таблицы и добавление нового элемента
            self.size += 1
            self.table.append(Element(s, 1))

    def write(self):
        """
        Метод записи элементов из хэш-таблицы в строку.
        Возвращает строку со всеми ключами и их значениями.
        """
        tmp = ""
        for i in range(len(self.table)):
            if self.table[i].value:
                tmp += self.table[i].key + ' ' + str(self.table[i].value) + '\n'
        return tmp

if __name__ == "__main__":
    # Пример использования хэш-таблицы с наложением
    with open("input13.txt", "r") as in_file, open("output13.txt", "w") as out_file:
        table = HashMap()
        for line in in_file:
            for word in line.split():
                table.add(word)
        out_file.write(table.write())


f = open('output13.txt', 'r')

for i in range(6):
    print(f.readline())
