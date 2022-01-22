import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 31
        self.top = 31
        self.cell_size = 25

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        color = (255, 255, 255)
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, color, (self.left, self.top, self.cell_size, self.cell_size), width=1)
                self.left += self.cell_size
            self.top += self.cell_size
            self.left = 31
        self.left = 31
        self.top = 31

    def notice(self, screen):
        row_number = 1
        column_number = 1
        for i in self.board[1:]:
            for j in i:
                if j == 1:
                    x = 31 + (column_number - 1) * self.cell_size
                    y = 31 + (row_number - 1) * self.cell_size
                    pygame.draw.rect(screen, (100, 255, 100), (x, y, self.cell_size, self.cell_size), width=0)
                column_number += 1
            row_number += 1
            column_number = 1

    def delete_row(self):
        number_of_row = 0
        try:
            for i in range(len(self.board)):
                self.board.remove([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
                number_of_row += 1
        except ValueError:
            pass
        for i in range(number_of_row):
            self.board.insert(0, [0] * 10)
        if number_of_row == 1:
            return 100
        elif number_of_row == 2:
            return 300
        elif number_of_row == 3:
            return 700
        elif number_of_row == 4:
            return 1500
        else:
            return 0

    def end_of_game_checking(self):
        count = 0
        for i in self.board[1:]:
            for j in i:
                if j == 1:
                    count += 1
                    break
        if count == 20:
            return True
        else:
            return False

    def mark_deleted_rows(self):
        numbers = list()
        for count, i in enumerate(self.board):
            if i == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                numbers.append(count)
        return numbers

    def downward_movement_of_shape(self, coordinate_1, coordinate_2, coordinate_3, coordinate_4, shape):
        try:
            coordinates = [coordinate_1, coordinate_2, coordinate_3, coordinate_4]
            coordinates.sort(key=lambda x: int(x[0]), reverse=True)
            if shape not in ['S', 'Z', 'T']:
                if shape == 'I':
                    if self.board[coordinates[0][0] + 1][coordinates[0][1]] == 0:
                        self.board[coordinates[0][0]][coordinates[0][1]] = 0
                        self.board[coordinates[1][0]][coordinates[1][1]] = 0
                        self.board[coordinates[2][0]][coordinates[2][1]] = 0
                        self.board[coordinates[3][0]][coordinates[3][1]] = 0
                        self.board[coordinates[0][0] + 1][coordinates[0][1]] = 1
                        self.board[coordinates[1][0] + 1][coordinates[1][1]] = 1
                        self.board[coordinates[2][0] + 1][coordinates[2][1]] = 1
                        self.board[coordinates[3][0] + 1][coordinates[3][1]] = 1
                    else:
                        return True
                else:
                    if self.board[coordinates[0][0] + 1][coordinates[0][1]] == 0 and \
                            self.board[coordinates[1][0] + 1][coordinates[1][1]] == 0:
                        self.board[coordinates[0][0]][coordinates[0][1]] = 0
                        self.board[coordinates[1][0]][coordinates[1][1]] = 0
                        self.board[coordinates[2][0]][coordinates[2][1]] = 0
                        self.board[coordinates[3][0]][coordinates[3][1]] = 0
                        self.board[coordinates[0][0] + 1][coordinates[0][1]] = 1
                        self.board[coordinates[1][0] + 1][coordinates[1][1]] = 1
                        self.board[coordinates[2][0] + 1][coordinates[2][1]] = 1
                        self.board[coordinates[3][0] + 1][coordinates[3][1]] = 1
                    else:
                        return True
            else:
                if shape == 'S':
                    if self.board[coordinates[0][0] + 1][coordinates[0][1]] == 0 and \
                            self.board[coordinates[1][0] + 1][coordinates[1][1]] == 0 and \
                            self.board[coordinates[3][0] + 1][coordinates[3][1]] == 0:
                        self.board[coordinates[0][0]][coordinates[0][1]] = 0
                        self.board[coordinates[1][0]][coordinates[1][1]] = 0
                        self.board[coordinates[2][0]][coordinates[2][1]] = 0
                        self.board[coordinates[3][0]][coordinates[3][1]] = 0
                        self.board[coordinates[0][0] + 1][coordinates[0][1]] = 1
                        self.board[coordinates[1][0] + 1][coordinates[1][1]] = 1
                        self.board[coordinates[2][0] + 1][coordinates[2][1]] = 1
                        self.board[coordinates[3][0] + 1][coordinates[3][1]] = 1
                    else:
                        return True
                elif shape == 'T':
                    if self.board[coordinates[0][0] + 1][coordinates[0][1]] == 0 and \
                            self.board[coordinates[1][0] + 1][coordinates[1][1]] == 0 and \
                            self.board[coordinates[3][0] + 1][coordinates[3][1]] == 0:
                        self.board[coordinates[0][0]][coordinates[0][1]] = 0
                        self.board[coordinates[1][0]][coordinates[1][1]] = 0
                        self.board[coordinates[2][0]][coordinates[2][1]] = 0
                        self.board[coordinates[3][0]][coordinates[3][1]] = 0
                        self.board[coordinates[0][0] + 1][coordinates[0][1]] = 1
                        self.board[coordinates[1][0] + 1][coordinates[1][1]] = 1
                        self.board[coordinates[2][0] + 1][coordinates[2][1]] = 1
                        self.board[coordinates[3][0] + 1][coordinates[3][1]] = 1
                    else:
                        return True
                else:
                    if self.board[coordinates[0][0] + 1][coordinates[0][1]] == 0 and \
                            self.board[coordinates[1][0] + 1][coordinates[1][1]] == 0 and \
                            self.board[coordinates[2][0] + 1][coordinates[2][1]] == 0:
                        self.board[coordinates[0][0]][coordinates[0][1]] = 0
                        self.board[coordinates[1][0]][coordinates[1][1]] = 0
                        self.board[coordinates[2][0]][coordinates[2][1]] = 0
                        self.board[coordinates[3][0]][coordinates[3][1]] = 0
                        self.board[coordinates[0][0] + 1][coordinates[0][1]] = 1
                        self.board[coordinates[1][0] + 1][coordinates[1][1]] = 1
                        self.board[coordinates[2][0] + 1][coordinates[2][1]] = 1
                        self.board[coordinates[3][0] + 1][coordinates[3][1]] = 1
                    else:
                        return True
        except IndexError:
            return True

    def movement_to_left(self, coordinate_1, coordinate_2, coordinate_3, coordinate_4, shape):
        try:
            if shape == 'I':
                if self.board[coordinate_1[0]][coordinate_1[1] - 1] == 0 and \
                        self.board[coordinate_2[0]][coordinate_2[1] - 1] == 0 and \
                        self.board[coordinate_3[0]][coordinate_3[1] - 1] == 0 and \
                        self.board[coordinate_4[0]][coordinate_4[1] - 1] == 0 and coordinate_1[1] - 1 != -1:
                    self.board[coordinate_1[0]][coordinate_1[1]] = 0
                    self.board[coordinate_2[0]][coordinate_2[1]] = 0
                    self.board[coordinate_3[0]][coordinate_3[1]] = 0
                    self.board[coordinate_4[0]][coordinate_4[1]] = 0
                    self.board[coordinate_1[0]][coordinate_1[1] - 1] = 1
                    self.board[coordinate_2[0]][coordinate_2[1] - 1] = 1
                    self.board[coordinate_3[0]][coordinate_3[1] - 1] = 1
                    self.board[coordinate_4[0]][coordinate_4[1] - 1] = 1
                    coordinate_1 = (coordinate_1[0], coordinate_1[1] - 1)
                    coordinate_2 = (coordinate_2[0], coordinate_2[1] - 1)
                    coordinate_3 = (coordinate_3[0], coordinate_3[1] - 1)
                    coordinate_4 = (coordinate_4[0], coordinate_4[1] - 1)
                    return [coordinate_1, coordinate_2, coordinate_3, coordinate_4]
            elif shape == 'J':
                if self.board[coordinate_1[0]][coordinate_1[1] - 1] == 0 and \
                        self.board[coordinate_2[0]][coordinate_2[1] - 1] == 0 and \
                        self.board[coordinate_4[0]][coordinate_4[1] - 1] == 0 and coordinate_4[1] - 1 != -1:
                    self.board[coordinate_1[0]][coordinate_1[1]] = 0
                    self.board[coordinate_2[0]][coordinate_2[1]] = 0
                    self.board[coordinate_3[0]][coordinate_3[1]] = 0
                    self.board[coordinate_4[0]][coordinate_4[1]] = 0
                    self.board[coordinate_1[0]][coordinate_1[1] - 1] = 1
                    self.board[coordinate_2[0]][coordinate_2[1] - 1] = 1
                    self.board[coordinate_3[0]][coordinate_3[1] - 1] = 1
                    self.board[coordinate_4[0]][coordinate_4[1] - 1] = 1
                    coordinate_1 = (coordinate_1[0], coordinate_1[1] - 1)
                    coordinate_2 = (coordinate_2[0], coordinate_2[1] - 1)
                    coordinate_3 = (coordinate_3[0], coordinate_3[1] - 1)
                    coordinate_4 = (coordinate_4[0], coordinate_4[1] - 1)
                    return [coordinate_1, coordinate_2, coordinate_3, coordinate_4]
            elif shape == 'L':
                if self.board[coordinate_1[0]][coordinate_1[1] - 1] == 0 and \
                        self.board[coordinate_2[0]][coordinate_2[1] - 1] == 0 and \
                        self.board[coordinate_3[0]][coordinate_3[1] - 1] == 0 and coordinate_1[1] - 1 != -1:
                    self.board[coordinate_1[0]][coordinate_1[1]] = 0
                    self.board[coordinate_2[0]][coordinate_2[1]] = 0
                    self.board[coordinate_3[0]][coordinate_3[1]] = 0
                    self.board[coordinate_4[0]][coordinate_4[1]] = 0
                    self.board[coordinate_1[0]][coordinate_1[1] - 1] = 1
                    self.board[coordinate_2[0]][coordinate_2[1] - 1] = 1
                    self.board[coordinate_3[0]][coordinate_3[1] - 1] = 1
                    self.board[coordinate_4[0]][coordinate_4[1] - 1] = 1
                    coordinate_1 = (coordinate_1[0], coordinate_1[1] - 1)
                    coordinate_2 = (coordinate_2[0], coordinate_2[1] - 1)
                    coordinate_3 = (coordinate_3[0], coordinate_3[1] - 1)
                    coordinate_4 = (coordinate_4[0], coordinate_4[1] - 1)
                    return [coordinate_1, coordinate_2, coordinate_3, coordinate_4]
            elif shape == 'O':
                if self.board[coordinate_1[0]][coordinate_1[1] - 1] == 0 and \
                        self.board[coordinate_3[0]][coordinate_3[1] - 1] == 0 and coordinate_1[1] - 1 != -1:
                    self.board[coordinate_1[0]][coordinate_1[1]] = 0
                    self.board[coordinate_2[0]][coordinate_2[1]] = 0
                    self.board[coordinate_3[0]][coordinate_3[1]] = 0
                    self.board[coordinate_4[0]][coordinate_4[1]] = 0
                    self.board[coordinate_1[0]][coordinate_1[1] - 1] = 1
                    self.board[coordinate_2[0]][coordinate_2[1] - 1] = 1
                    self.board[coordinate_3[0]][coordinate_3[1] - 1] = 1
                    self.board[coordinate_4[0]][coordinate_4[1] - 1] = 1
                    coordinate_1 = (coordinate_1[0], coordinate_1[1] - 1)
                    coordinate_2 = (coordinate_2[0], coordinate_2[1] - 1)
                    coordinate_3 = (coordinate_3[0], coordinate_3[1] - 1)
                    coordinate_4 = (coordinate_4[0], coordinate_4[1] - 1)
                    return [coordinate_1, coordinate_2, coordinate_3, coordinate_4]
            elif shape == 'S':
                if self.board[coordinate_1[0]][coordinate_1[1] - 1] == 0 and \
                        self.board[coordinate_4[0]][coordinate_4[1] - 1] == 0 and coordinate_4[1] - 1 != -1:
                    self.board[coordinate_1[0]][coordinate_1[1]] = 0
                    self.board[coordinate_2[0]][coordinate_2[1]] = 0
                    self.board[coordinate_3[0]][coordinate_3[1]] = 0
                    self.board[coordinate_4[0]][coordinate_4[1]] = 0
                    self.board[coordinate_1[0]][coordinate_1[1] - 1] = 1
                    self.board[coordinate_2[0]][coordinate_2[1] - 1] = 1
                    self.board[coordinate_3[0]][coordinate_3[1] - 1] = 1
                    self.board[coordinate_4[0]][coordinate_4[1] - 1] = 1
                    coordinate_1 = (coordinate_1[0], coordinate_1[1] - 1)
                    coordinate_2 = (coordinate_2[0], coordinate_2[1] - 1)
                    coordinate_3 = (coordinate_3[0], coordinate_3[1] - 1)
                    coordinate_4 = (coordinate_4[0], coordinate_4[1] - 1)
                    return [coordinate_1, coordinate_2, coordinate_3, coordinate_4]
            elif shape == 'T':
                if self.board[coordinate_1[0]][coordinate_1[1] - 1] == 0 and \
                        self.board[coordinate_4[0]][coordinate_4[1] - 1] == 0 and coordinate_1[1] - 1 != -1:
                    self.board[coordinate_1[0]][coordinate_1[1]] = 0
                    self.board[coordinate_2[0]][coordinate_2[1]] = 0
                    self.board[coordinate_3[0]][coordinate_3[1]] = 0
                    self.board[coordinate_4[0]][coordinate_4[1]] = 0
                    self.board[coordinate_1[0]][coordinate_1[1] - 1] = 1
                    self.board[coordinate_2[0]][coordinate_2[1] - 1] = 1
                    self.board[coordinate_3[0]][coordinate_3[1] - 1] = 1
                    self.board[coordinate_4[0]][coordinate_4[1] - 1] = 1
                    coordinate_1 = (coordinate_1[0], coordinate_1[1] - 1)
                    coordinate_2 = (coordinate_2[0], coordinate_2[1] - 1)
                    coordinate_3 = (coordinate_3[0], coordinate_3[1] - 1)
                    coordinate_4 = (coordinate_4[0], coordinate_4[1] - 1)
                    return [coordinate_1, coordinate_2, coordinate_3, coordinate_4]
            elif shape == 'Z':
                if self.board[coordinate_1[0]][coordinate_1[1] - 1] == 0 and \
                        self.board[coordinate_3[0]][coordinate_3[1] - 1] == 0 and coordinate_1[1] - 1 != -1:
                    self.board[coordinate_1[0]][coordinate_1[1]] = 0
                    self.board[coordinate_2[0]][coordinate_2[1]] = 0
                    self.board[coordinate_3[0]][coordinate_3[1]] = 0
                    self.board[coordinate_4[0]][coordinate_4[1]] = 0
                    self.board[coordinate_1[0]][coordinate_1[1] - 1] = 1
                    self.board[coordinate_2[0]][coordinate_2[1] - 1] = 1
                    self.board[coordinate_3[0]][coordinate_3[1] - 1] = 1
                    self.board[coordinate_4[0]][coordinate_4[1] - 1] = 1
                    coordinate_1 = (coordinate_1[0], coordinate_1[1] - 1)
                    coordinate_2 = (coordinate_2[0], coordinate_2[1] - 1)
                    coordinate_3 = (coordinate_3[0], coordinate_3[1] - 1)
                    coordinate_4 = (coordinate_4[0], coordinate_4[1] - 1)
                    return [coordinate_1, coordinate_2, coordinate_3, coordinate_4]
        except IndexError:
            return None

    def movement_to_right(self, coordinate_1, coordinate_2, coordinate_3, coordinate_4, shape):
        try:
            if shape == 'I':
                if self.board[coordinate_1[0]][coordinate_1[1] + 1] == 0 and \
                        self.board[coordinate_2[0]][coordinate_1[1] + 1] == 0 and \
                        self.board[coordinate_3[0]][coordinate_1[1] + 1] == 0 and \
                        self.board[coordinate_4[0]][coordinate_1[1] + 1] == 0:
                    self.board[coordinate_1[0]][coordinate_1[1]] = 0
                    self.board[coordinate_2[0]][coordinate_2[1]] = 0
                    self.board[coordinate_3[0]][coordinate_3[1]] = 0
                    self.board[coordinate_4[0]][coordinate_4[1]] = 0
                    self.board[coordinate_1[0]][coordinate_1[1] + 1] = 1
                    self.board[coordinate_2[0]][coordinate_2[1] + 1] = 1
                    self.board[coordinate_3[0]][coordinate_3[1] + 1] = 1
                    self.board[coordinate_4[0]][coordinate_4[1] + 1] = 1
                    coordinate_1 = (coordinate_1[0], coordinate_1[1] + 1)
                    coordinate_2 = (coordinate_2[0], coordinate_2[1] + 1)
                    coordinate_3 = (coordinate_3[0], coordinate_3[1] + 1)
                    coordinate_4 = (coordinate_4[0], coordinate_4[1] + 1)
                    return [coordinate_1, coordinate_2, coordinate_3, coordinate_4]
            elif shape == 'J':
                if self.board[coordinate_1[0]][coordinate_1[1] + 1] == 0 and \
                        self.board[coordinate_2[0]][coordinate_2[1] + 1] == 0 and \
                        self.board[coordinate_3[0]][coordinate_3[1] + 1] == 0:
                    self.board[coordinate_1[0]][coordinate_1[1]] = 0
                    self.board[coordinate_2[0]][coordinate_2[1]] = 0
                    self.board[coordinate_3[0]][coordinate_3[1]] = 0
                    self.board[coordinate_4[0]][coordinate_4[1]] = 0
                    self.board[coordinate_1[0]][coordinate_1[1] + 1] = 1
                    self.board[coordinate_2[0]][coordinate_2[1] + 1] = 1
                    self.board[coordinate_3[0]][coordinate_3[1] + 1] = 1
                    self.board[coordinate_4[0]][coordinate_4[1] + 1] = 1
                    coordinate_1 = (coordinate_1[0], coordinate_1[1] + 1)
                    coordinate_2 = (coordinate_2[0], coordinate_2[1] + 1)
                    coordinate_3 = (coordinate_3[0], coordinate_3[1] + 1)
                    coordinate_4 = (coordinate_4[0], coordinate_4[1] + 1)
                    return [coordinate_1, coordinate_2, coordinate_3, coordinate_4]
            elif shape == 'L':
                if self.board[coordinate_1[0]][coordinate_1[1] + 1] == 0 and \
                        self.board[coordinate_2[0]][coordinate_2[1] + 1] == 0 and \
                        self.board[coordinate_4[0]][coordinate_4[1] + 1] == 0:
                    self.board[coordinate_1[0]][coordinate_1[1]] = 0
                    self.board[coordinate_2[0]][coordinate_2[1]] = 0
                    self.board[coordinate_3[0]][coordinate_3[1]] = 0
                    self.board[coordinate_4[0]][coordinate_4[1]] = 0
                    self.board[coordinate_1[0]][coordinate_1[1] + 1] = 1
                    self.board[coordinate_2[0]][coordinate_2[1] + 1] = 1
                    self.board[coordinate_3[0]][coordinate_3[1] + 1] = 1
                    self.board[coordinate_4[0]][coordinate_4[1] + 1] = 1
                    coordinate_1 = (coordinate_1[0], coordinate_1[1] + 1)
                    coordinate_2 = (coordinate_2[0], coordinate_2[1] + 1)
                    coordinate_3 = (coordinate_3[0], coordinate_3[1] + 1)
                    coordinate_4 = (coordinate_4[0], coordinate_4[1] + 1)
                    return [coordinate_1, coordinate_2, coordinate_3, coordinate_4]
            elif shape == 'O':
                if self.board[coordinate_2[0]][coordinate_2[1] + 1] == 0 and \
                        self.board[coordinate_4[0]][coordinate_4[1] + 1] == 0:
                    self.board[coordinate_1[0]][coordinate_1[1]] = 0
                    self.board[coordinate_2[0]][coordinate_2[1]] = 0
                    self.board[coordinate_3[0]][coordinate_3[1]] = 0
                    self.board[coordinate_4[0]][coordinate_4[1]] = 0
                    self.board[coordinate_1[0]][coordinate_1[1] + 1] = 1
                    self.board[coordinate_2[0]][coordinate_2[1] + 1] = 1
                    self.board[coordinate_3[0]][coordinate_3[1] + 1] = 1
                    self.board[coordinate_4[0]][coordinate_4[1] + 1] = 1
                    coordinate_1 = (coordinate_1[0], coordinate_1[1] + 1)
                    coordinate_2 = (coordinate_2[0], coordinate_2[1] + 1)
                    coordinate_3 = (coordinate_3[0], coordinate_3[1] + 1)
                    coordinate_4 = (coordinate_4[0], coordinate_4[1] + 1)
                    return [coordinate_1, coordinate_2, coordinate_3, coordinate_4]
            elif shape == 'S':
                if self.board[coordinate_2[0]][coordinate_2[1] + 1] == 0 and \
                        self.board[coordinate_3[0]][coordinate_3[1] + 1] == 0:
                    self.board[coordinate_1[0]][coordinate_1[1]] = 0
                    self.board[coordinate_2[0]][coordinate_2[1]] = 0
                    self.board[coordinate_3[0]][coordinate_3[1]] = 0
                    self.board[coordinate_4[0]][coordinate_4[1]] = 0
                    self.board[coordinate_1[0]][coordinate_1[1] + 1] = 1
                    self.board[coordinate_2[0]][coordinate_2[1] + 1] = 1
                    self.board[coordinate_3[0]][coordinate_3[1] + 1] = 1
                    self.board[coordinate_4[0]][coordinate_4[1] + 1] = 1
                    coordinate_1 = (coordinate_1[0], coordinate_1[1] + 1)
                    coordinate_2 = (coordinate_2[0], coordinate_2[1] + 1)
                    coordinate_3 = (coordinate_3[0], coordinate_3[1] + 1)
                    coordinate_4 = (coordinate_4[0], coordinate_4[1] + 1)
                    return [coordinate_1, coordinate_2, coordinate_3, coordinate_4]
            elif shape == 'T':
                if self.board[coordinate_3[0]][coordinate_3[1] + 1] == 0 and \
                        self.board[coordinate_4[0]][coordinate_4[1] + 1] == 0:
                    self.board[coordinate_1[0]][coordinate_1[1]] = 0
                    self.board[coordinate_2[0]][coordinate_2[1]] = 0
                    self.board[coordinate_3[0]][coordinate_3[1]] = 0
                    self.board[coordinate_4[0]][coordinate_4[1]] = 0
                    self.board[coordinate_1[0]][coordinate_1[1] + 1] = 1
                    self.board[coordinate_2[0]][coordinate_2[1] + 1] = 1
                    self.board[coordinate_3[0]][coordinate_3[1] + 1] = 1
                    self.board[coordinate_4[0]][coordinate_4[1] + 1] = 1
                    coordinate_1 = (coordinate_1[0], coordinate_1[1] + 1)
                    coordinate_2 = (coordinate_2[0], coordinate_2[1] + 1)
                    coordinate_3 = (coordinate_3[0], coordinate_3[1] + 1)
                    coordinate_4 = (coordinate_4[0], coordinate_4[1] + 1)
                    return [coordinate_1, coordinate_2, coordinate_3, coordinate_4]
            elif shape == 'Z':
                if self.board[coordinate_2[0]][coordinate_2[1] + 1] == 0 and \
                        self.board[coordinate_4[0]][coordinate_4[1] + 1] == 0:
                    self.board[coordinate_1[0]][coordinate_1[1]] = 0
                    self.board[coordinate_2[0]][coordinate_2[1]] = 0
                    self.board[coordinate_3[0]][coordinate_3[1]] = 0
                    self.board[coordinate_4[0]][coordinate_4[1]] = 0
                    self.board[coordinate_1[0]][coordinate_1[1] + 1] = 1
                    self.board[coordinate_2[0]][coordinate_2[1] + 1] = 1
                    self.board[coordinate_3[0]][coordinate_3[1] + 1] = 1
                    self.board[coordinate_4[0]][coordinate_4[1] + 1] = 1
                    coordinate_1 = (coordinate_1[0], coordinate_1[1] + 1)
                    coordinate_2 = (coordinate_2[0], coordinate_2[1] + 1)
                    coordinate_3 = (coordinate_3[0], coordinate_3[1] + 1)
                    coordinate_4 = (coordinate_4[0], coordinate_4[1] + 1)
                    return [coordinate_1, coordinate_2, coordinate_3, coordinate_4]
        except IndexError:
            return None