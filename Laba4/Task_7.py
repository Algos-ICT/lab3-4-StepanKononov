import gc


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Doublo_LinkedList:
    def __init__(self):
        # Инициализируем головной указатель в начале он никуда не указывает
        self.head = None
        self.tail = None
        self.lenght = 0

    # Поместить в конец списка
    def push(self, new_data):
        # Создаем новый элемент списка с указанным значением
        new_node = Node(new_data)

        # Так-как это последний элемент
        new_node.next = None

        # Если список  был пустым
        if self.head is None:
            new_node.prev = None
            self.tail = new_node
        else:
            self.head.next = new_node
            new_node.prev = self.head
        # Перемещаем указатель на текущий элемент
        self.head = new_node
        self.lenght += 1

    # Вставить после определенного эхлемента
    def insertAfter(self, prev_node, new_data):

        # Проверим что предыдущий элемент сущствует
        if prev_node is None:
            print("This node doesn't exist in DLL")
            return

        # Создаём новый элемент списка
        new_node = Node(new_data)

        # Задаём след элем как след после prev_node
        new_node.next = prev_node.next
        # Задаем предыдущий элемент для текущего
        new_node.prev = prev_node

        # Задаем предыдущему элементу след как текущий
        prev_node.next = new_node

        # Если мы не добавляли в конец тогда указываем след элементу указатель на текущий
        if new_node.next is not None:
            new_node.next.prev = new_node
        else:
            self.head = new_node
        self.lenght += 1

    # Вставить перед определенного эхлемента
    def insertBefore(self, next_node, new_data):
        # Проверим что "след" элемент сущствует
        if next_node is None:
            print("This node doesn't exist in DLL")
            return

        # Создаём новый элемент списка
        new_node = Node(new_data)

        # Задаём след элем как след после prev_node
        new_node.next = next_node
        # Задаем предыдущий элемент для текущего
        new_node.prev = next_node.prev

        next_node.prev = new_node

        # Подвязывваем пердыдущий элемент если он есть к текущему
        if new_node.prev is not None:
            new_node.prev.next = new_node
        # Обновляем хвост
        if new_node.prev is None:
            self.tail = new_node
        self.lenght += 1

    # Печать списка (развернут)
    def printList(self):
        if self.is_empty():
            return
        cur_node = self.head
        it_first_iter = True
        while cur_node.prev != None:
            if it_first_iter:
                print(cur_node.data, '<-- head')
                it_first_iter= False
            else:
                print(cur_node.data)
            cur_node = cur_node.prev
        print(cur_node.data, '<-- tail')

    # Получение элемнта по индексу
    def take_elem(self, index):
        if index >= self.lenght:
            print("List index out of range")
            return
        cur_node = self.head
        iterables = self.lenght - 1 - index
        for i in range(iterables):
            cur_node = cur_node.prev
        return cur_node
    # Удаление элемента
    def deleteNode(self, dele):

        # Base Case
        if self.head is None or dele is None:
            return
        # If node to be deleted is head node
        if self.head == dele:
            # Если удаляем последний элемент из списка
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.prev

        elif dele.prev == None:
            self.tail = dele.next
            dele.next.prev = None

        else:
            dele.prev.next = dele.next
            dele.next.prev = dele.prev

        self.lenght -= 1
        gc.collect()
    # Поиск элемента по значению (возвращает первое правое вхождение)
    def rfind_elem(self, elem_data):
        cur_node = self.head
        while cur_node.data != elem_data:
            cur_node = cur_node.prev
        return cur_node

    def is_empty(self):
        return self.head == None

    # Получение верхнего элемнта
    def top(self):
        return self.head
    def down(self):
        return self.tail

stack = Doublo_LinkedList()
#temp = input()
commands = '89+17-*'
for elem in commands:
    if elem in '+-*':
        a = stack.head.prev.data
        b = stack.head.data
        stack.deleteNode(stack.head)
        stack.deleteNode(stack.head)
        if elem == '+':
            result = a + b
        elif elem == '-':
            result = a - b
        else:
            result = a * b
        stack.push(result)
    else:
        stack.push(int(elem))
print(stack.tail.data)
