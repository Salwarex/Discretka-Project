import random

#2
matrix = []
fromfile = True

def display_matrix(matr):
    for i in matr:
        s = ''
        for j in i:
            s = s + str(j) + ' '
        print(s)

def getMatrixFromFile(filename):
    l = []
    with open(filename, 'r') as f:
        l = [[int(num) for num in line.split(' ')] for line in f]
    return l

if fromfile:
    matrix = getMatrixFromFile(input("Введите название файла: "))
else:
    print('Ввод матрицы')
    print('----')
    print('Правила:')
    print('1. Точки начала графа указываются на вертикальных значениях, точки окончания - на горизонтальных;')
    print('2. Между введенными значениями должен указываться пробел;')
    print('3. Пустые клетки заполняются \"-\"')
    print('4. Главная диагональ должна быть пуста.')

    now = 0
    max = 0
    while True:
        s = input(f'из точки {now + 1}: ')
        arr = s.split()
        arrInt = []
        for s in arr:
            i = 0
            if s != "-":
                i = int(s)
            arrInt.append(i)

        if now == 0:
            matrix.append(arrInt)
            max = len(arrInt) - 1
        else:
            if now >= max:
                matrix.append(arrInt)
                break
            if (len(arrInt) != max + 1) or (arrInt[now] != 0):
                print('ОШИБКА')
                break
            matrix.append(arrInt)
        now += 1


display_matrix(matrix)


start_point = int(input('Введите номер точки истока')) - 1
end_point = int(input('Введите номер точки стока')) - 1

ways = []

temp_way_array = []
deleted_edges = []
blockedPoints = []
def isPointBanned(point):
    if point in blockedPoints:
        return True
    else:
        return False

def nextPoint(point, endPoint, otkat):
    if otkat: temp_way_array.remove(temp_way_array[len(temp_way_array) - 1])

    possible_ways = []
    i = 0
    for x in matrix[point]:
        if x != 0:
            possible_ways.append(i)
        i+=1
    for x in possible_ways:
        if (x in blockedPoints) or (x in temp_way_array) or (x in deleted_edges):
            possible_ways.remove(x)
            print("Удалено", x)

    print(point, possible_ways, blockedPoints,  temp_way_array)

    if point != endPoint:
        if len(possible_ways) == 0:
            if len(temp_way_array) > 0:
                if(not(point in blockedPoints)):
                    blockedPoints.append(point)
                nextPoint(temp_way_array[len(temp_way_array) - 1], endPoint, True)
            else:
                temp_way_array.append(0)
        else:
            nextP = -1
            while nextP == -1:
                i = random.randint(0, len(possible_ways) - 1)
                if (not (isPointBanned(i))):
                    nextP = i

            if (not(point in temp_way_array)):
                temp_way_array.append(point)
            next = possible_ways[nextP]
            nextPoint(next, endPoint, False)
    else:
        temp_way_array.append(point)




nextPoint(start_point, end_point, False)
print("Построенный путь: " + str(temp_way_array))


