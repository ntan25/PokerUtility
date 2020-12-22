numbers = [1, 2, 3, 4, 5, 6, 7, 8]

x = 2
numbers.remove(x)


i = 0
j = 0
k = 0
straightfour = 0
straightthree = 0

while i < len(numbers):
    a = numbers[i]
    numbers.pop(i)
    while j < len(numbers):
        b = numbers[j]
        numbers.pop(j)
        while k < len(numbers):
            c = numbers[k]
            if a == x + 1 and b == i + 1 and c == j + 1:
                straightfour += 1
            elif a == x + 1 and b == i + 1:
                straightthree += 1
                k += 1
        numbers.insert(j, b)
        j += 1
    numbers.insert(i, a)
    i += 1

print("straightfour = " + straightfour)
print("straightthree = " + straightthree)