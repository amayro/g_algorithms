import hashlib


def task_section(task):
    print(f'\n{"":-^10} №{task} {"":-^10}')


# №1 ------------------------------------------------------------------------------------
task_section(1)
"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
string = "beep boop beer!"
print("Исходная строка: " + string)


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right


def make_haffman_tree(node, code=""):
    if isinstance(node, str):
        return {node: code}

    l, r = node.children()

    result = {}
    result.update(make_haffman_tree(l, code + "0"))
    result.update(make_haffman_tree(r, code + "1"))

    return result


frequencies = {}
for char in string:
    if char not in frequencies:
        frequencies[char] = 0

    frequencies[char] += 1

tree = frequencies.items()

while len(tree) > 1:
    tree = sorted(tree, reverse=True, key=lambda x: x[1])
    char1, count1 = tree[-1]
    char2, count2 = tree[-2]
    tree = tree[:-2]
    tree.append((Node(char1, char2), count1 + count2))

code_table = make_haffman_tree(tree[0][0])

coded = []
for char in string:
    coded.append(code_table[char])

print(f"Закодированная строка: {''.join(coded)}")


# №2 ------------------------------------------------------------------------------------
task_section(2)
"""
2. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

# s = input("Введите строку из маленьких латинских букв: ")
s = "beep"
N = len(s)
r = set()

for i in range(N):
    if i == 0:
        N = len(s) - 1
    else:
        N = len(s)
    for j in range(N, i, -1):
        print(s[i:j])
        r.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
print(r)

print(f"Количество различных подстрок в строке '{s}' равно {len(r)}")
