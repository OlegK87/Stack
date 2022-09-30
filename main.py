class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self): # проверка стека на пустоту. Метод возвращает True или False.
        if len(self.stack) == 0:
            return True
        if len(self.stack) != 0:
            return False
    def push(self, item): # добавляет новый элемент на вершину стека. Метод ничего не возвращает.
        self.stack.append(item)
    def pop(self): # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        if self.stack == []:
            return None
        else:
            return self.stack.pop()
    def peek(self):
        if self:
            return self.stack[-1]  # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        else:
            return None
    def size(self): # size возвращает количество элементов в стеке.
        lens = len(self.stack)
        return lens

# Задача 2:

def balanced(string):
    for i in string:
        if i in '([{':
            s.push(i)
        else:
            if s.isEmpty():
                return False
            else:
                if s.peek() + i in braces:
                    s.pop()
                else:
                    return False
    return s.isEmpty() or False

if __name__ == "__main__":
    s = Stack()
    braces = ('()', '[]', '{}')
    result = balanced(input("Введите скобки для проверки на сбалансированность: "))
    if result == True:
        print("Сбалансированно")
    elif result == False:
        print("Несбалансированно")


