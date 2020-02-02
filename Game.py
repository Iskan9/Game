import random
from tkinter import Frame, Label, Button

size = 400
N = 4

# цвет клеток
color_cell = {2: "lavender blush", 4: "lemon chiffon", 8: "sandy brown", 16: "coral", 32: "salmon1",
              64: "tomato",  128: "orange", 256: "dark orange", 512: "gold2", 1024: "gold3",
              2048: "gold", 4096: "yellow2", 8192: "yellow", 16384: "chocolate1",
              32768: "chocolate2", 65536: "chocolate3"}

# цвет непосредственно чисел
color_num = {2: "gray40", 4: "gray40", 8: "snow", 16: "snow", 32: "snow", 64: "snow", 128: "snow",
             256: "snow", 512: "snow", 1024: "snow",2048: "snow",
             4096: "misty rose", 8192: "misty rose", 16384: "misty rose", 32768: "misty rose",
             65536: "misty rose", 131072: "misty rose"}


def add_two(mat):
    a = random.randrange(0, len(mat))  # случайное число из диапазона [0, len(mat))
    b = random.randrange(0, len(mat))
    while(mat[a][b] != 0):
        a = random.randrange(0, len(mat))
        b = random.randrange(0, len(mat))
    mat[a][b] = 2
    return mat


def current_pozition_game(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 16384:
                return 'win'

    for i in range(len(mat) - 1): # проверка на существование элементов, подлежащих слиянию
        for j in range(len(mat[0]) - 1):
            if mat[i][j] == mat[i + 1][j] or mat[i][j + 1] == mat[i][j]:
                return 'Ничего не происходит'
    for i in range(len(mat)):  # если есть хоть один элемент нулевой, значит игра еще не проиграна
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'Ничего не происходит'
    for k in range(len(mat) - 1):  # проверяем наличие сливающихся элементов в  последней строке
        if mat[len(mat) - 1][k] == mat[len(mat) - 1][k + 1]:
            return 'Ничего не происходит'

    for j in range(len(mat) - 1):  # проверяем наличие сливающихся элементов в  последнем столбце
        if mat[j][len(mat) - 1] == mat[j + 1][len(mat) - 1]:
            return 'Ничего не происходит'
    return 'lose'


def merge_left(mat):  # функция слияния
    flag = False
    for i in range(len(mat)):
        for j in range(len(mat) - 1):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                flag = True
                mat[i][j] *= 2
                mat[i][j + 1] = 0
    return (mat, flag)


def merge_right(mat):  # функция слияния
    flag = False
    for i in range(len(mat)):
        for j in range(1, len(mat)):
            if mat[i][-j] == mat[i][-j - 1] and mat[i][-j] != 0:
                flag = True
                mat[i][-j] *= 2
                mat[i][-j-1] = 0
    return (mat, flag)


def merge_up(mat): # функция слияния
    flag = False
    for i in range(len(mat)-1):
        for j in range(len(mat)):
            if mat[i][j] == mat[i+1][j] and mat[i][j] != 0:
                flag = True
                mat[i][j] *= 2
                mat[i+1][j] = 0
    return (mat, flag)


def merge_down(mat):  # функция слияния
    flag = False
    for i in range(1, len(mat)):
        for j in range(len(mat)):
            if mat[-i][j] == mat[-i-1][j] and mat[-i][j] != 0:
                flag = True
                mat[-i][j] *= 2
                mat[-i-1][j] = 0
    return (mat, flag)


def transfer0_right(mat):  # перенос нулей вправо
    flag = False
    new = [[0] * len(mat) for _ in range(len(mat))]
    for i in range(len(mat)):
        row_non_zero = [mat[i][j] for j in range(len(mat[i])) if mat[i][j] != 0]
        count_0 = len(mat[i]) - len(row_non_zero)
        for k in range(count_0):
            row_non_zero.append(0)  # вставить в конец позицию 0
        new[i] = row_non_zero
    if mat != new:
        flag = True
    return (new, flag)


def transfer0_left(mat):  # перенос нулей влево
    flag = False
    new = [[0] * len(mat) for _ in range(len(mat))]
    for i in range(len(mat)):
        row_non_zero = [mat[i][j] for j in range(len(mat[i])) if mat[i][j] != 0]
        count_0 = len(mat[i]) - len(row_non_zero)
        for k in range(count_0):
            row_non_zero.insert(0, 0)  # вставить в нулевую позицию 0
        new[i] = row_non_zero
    if mat != new:
        flag = True
    return (new, flag)


def transfer0_down(mat):  # перенос нулей вверх
    flag = False
    new = [[0] * len(mat) for _ in range(len(mat))]
    for i in range(len(mat)):
        row_non_zero = [mat[j][i] for j in range(len(mat[i])) if mat[j][i] != 0]
        count_0 = len(mat[i]) - len(row_non_zero)
        for k in range(count_0):
            row_non_zero.append(0)  # вставить в конец  0
        for r in range(len(new)):
            new[r][i] = row_non_zero[r]
    if mat != new:
        flag = True
    return (new, flag)


def transfer0_up(mat):  # перенос нулей вниз
    flag = False
    new = [[0] * len(mat) for _ in range(len(mat))]
    for i in range(len(mat)):
        row_non_zero = [mat[j][i] for j in range(len(mat[i])) if mat[j][i] != 0]
        count_0 = len(mat[i]) - len(row_non_zero)
        for k in range(count_0):
            row_non_zero.insert(0, 0)  # вставить в начало  0
        for r in range(len(new)):
            new[r][i] = row_non_zero[r]
    if mat != new:
        flag = True
    return (new, flag)


def up(game):  # возврат матрицы после сдвига вверх
    game, flag0 = transfer0_down(game)
    game, flag1 = merge_up(game)
    game, flag2 = transfer0_down(game)
    flag = flag1 or flag2 or flag0
    return (game, flag)


def down(game):  # возврат матрицы после сдвига вниз
    game, flag0 = transfer0_up(game)
    game, flag1 = merge_down(game)
    game, flag2 = transfer0_up(game)
    flag = flag1 or flag2 or flag0
    return (game, flag)


def left(game):  # возврат матрицы после сдвига влево
    game, flag0 = transfer0_right(game)
    game, flag1 = merge_left(game)
    game, flag2 = transfer0_right(game)
    flag = flag1 or flag2 or flag0
    return (game, flag)


def right(game):  # возврат матрицы после сдвига вправо
    game, flag0 = transfer0_left(game)
    game, flag1 = merge_right(game) # слияние
    game, flag2 = transfer0_left(game) # опять сдвигаем нули
    flag = flag1 or flag2 or flag0
    return (game, flag)


class Game(Frame):
    def __init__(self):
        Frame.__init__(self) # явно вызывает метод __init__() из класса Frame

        self.grid()
        self.master.title('2048 Iskan')
        self.master.bind("<Key>", self.action)

        self.matrix = [[0]*N for _ in range(N)]
        self.matrix = add_two(self.matrix)
        self.matrix = add_two(self.matrix)


        self.action = {"w": up, "s": down, "a": left, "d": right, "ц": up, "ы": down, "ф": left, "в": right}

        self.game_cells = [[0]*N for _ in range(N)]
        self.playing_field()  # пользовательские функции
        self.update_game()  # пользовательские функции
        self.mainloop()


    def playing_field(self):
        background = Frame(self, bg="seashell4", width=size, height=size)
        background.grid()

        for i in range(N):
            for j in range(N):
                cell = Frame(background, bg="seashell3", width=size / N, height=size / N)
                cell.grid(row=i, column=j, padx=5, pady=5)
                tm = Label(master=cell, bg="seashell3", font=("Verdana", 40, "bold"), width=5, height=2)
                tm.grid()
                self.game_cells[i][j] = tm


    def update_game(self):
        for i in range(N):
            for j in range(N):
                if self.matrix[i][j] == 0:
                    self.game_cells[i][j].config(text='', bg="seashell3")
                else:
                    tmp=self.matrix[i][j]
                    self.game_cells[i][j].config(text=str(tmp), bg=color_cell[tmp], fg=color_num[tmp])
        self.update_idletasks()


    def action(self, event):
        try:
            key = event.char
            self.matrix, flag = self.action[key](self.matrix)
            # если kye='d', тогда  comman['d] - это right, только лишь название функции  но не ее вызов.
            # А action[key](matrix) это уже вызов
            if flag:
                self.matrix = add_two(self.matrix)  # добавили двойку
                self.update_game()  # обновили
                flag = False

                if current_pozition_game(self.matrix) == 'win':
                    self.game_cells[1][1].config(text="You", bg="gray30")
                    self.game_cells[1][2].config(text="Win!", bg="gray30")

                if current_pozition_game(self.matrix) == 'lose':
                    self.game_cells[1][1].config(text="You", bg="gray30")
                    self.game_cells[1][2].config(text="Lose!", bg="gray30")
        except KeyError:
            pass

Iskan = Game()


