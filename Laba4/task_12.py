''' Для начала реализую двусвязный список '''

import gc
import tarfile


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doublo_LinkedList:
    def __init__(self):
        # Инициализируем головной указатель в начале он никуда не указывает
        self.head = None
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
        if (new_node.prev != None):
            new_node.prev.next = new_node
        self.lenght += 1

    # Печать списка (развернут)
    def printList(self):
        cur_node = self.head
        while cur_node.prev != None:
            cur_node = cur_node.prev
            print(cur_node.data)
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
            self.head = self.head.prev
        elif dele.prev == None:
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


    # Получение верхнего элемнта
    def top(self):
        return self.head


line = Doublo_LinkedList()
crowd = None
'''
for i in range (line.lenght):
    print(line.take_elem(i).data, ' i = ', i)'''


#n, m = map(int, input().split())
n, m = 3, 4
com = ['left 2 1', 'right 3 1', 'leave 1', 'name 2']

line.push(1) # 0

for x in range(m):
    command = com[x]
    temp = command.split()
    com_type, I, J = temp[0], (int(temp[1]) if len(temp) > 1 else None), (int(temp[2]) if len(temp) > 2 else None)
    if (com_type == 'left'):
        line.insertBefore(line.rfind_elem(J), I)
    if (com_type == 'right'):
        line.insertAfter(line.rfind_elem(J), I)
    if (com_type == 'leave'):

        line.deleteNode(line.rfind_elem(I))

    if (com_type == 'name'):

        if line.rfind_elem(I).prev == None:
            left = 0
        else:
            left = line.rfind_elem(I).prev.data
        if line.rfind_elem(I).next == None:
            right = 0
        else:
            right = line.rfind_elem(I).next.data
        print(left, right)
for i in range (line.lenght):
    print(line.take_elem(i).data, ' i = ', i)








