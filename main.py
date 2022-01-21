import pygame

import sqlite3

from classes import Board

from functions import get_shape_type

import sprites

from pympler import muppy

all_objects = muppy.get_objects()

pygame.init()
size = width, height = 512, 640
screen = pygame.display.set_mode(size)
game_window = False
start_window = True
level = 'easy'
score = '0'
bang_start = None
clock = pygame.time.Clock()
fps = 40
start_of_start_window = False
display_bangs = False
numbers_of_deleted_rows = None
note_about_deleted_rows = 0
number_of_bangs = None
hotkeys_is_ok = False
push_shape_fast_event_use = False
delete_rows_event_use = False
end_of_game = False
hi_score_changed = False
play_button_is_pressed = False
wait_press_play_button = False
HOLD_PLAY_BUTTON = None
END_OF_GAME = None
PUSH_SHAPE = None
PUSH_SHAPE_FAST = None
DELETE_ROWS = None
shape_is_active = False
hotkeys_is_no = True
upload_shapes = False
play_button_polygon = None
play_button_polygon_list = list()
easy_button_rect = None
medium_button_rect = None
hard_button_rect = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == END_OF_GAME:
            pygame.time.set_timer(PUSH_SHAPE, 0)
            if push_shape_fast_event_use:
                pygame.time.set_timer(PUSH_SHAPE_FAST, 0)
            if delete_rows_event_use:
                pygame.time.set_timer(DELETE_ROWS, 0)
            pygame.time.set_timer(END_OF_GAME, 0)
            hotkeys_is_ok = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_window:
                if play_button_polygon.collidepoint(event.pos):
                    HOLD_PLAY_BUTTON = pygame.USEREVENT + 1
                    pygame.time.set_timer(HOLD_PLAY_BUTTON, 20)
                    play_button_is_pressed = True
                    wait_press_play_button = True
                elif easy_button_rect.collidepoint(event.pos):
                    level = 'easy'
                elif medium_button_rect.collidepoint(event.pos):
                    level = 'medium'
                elif hard_button_rect.collidepoint(event.pos):
                    level = 'hard'
        elif event.type == HOLD_PLAY_BUTTON:
            if not pygame.mouse.get_pressed()[0]:
                if not wait_press_play_button:
                    play_button_is_pressed = False
                    pygame.time.set_timer(HOLD_PLAY_BUTTON, 0)
                    start_window = False
                    game_window = True
                    start_of_start_window = True
                else:
                    play_button_is_pressed = False
                    wait_press_play_button = False
                    pygame.time.set_timer(HOLD_PLAY_BUTTON, 375)
        elif event.type == PUSH_SHAPE:
            if shape_is_active:
                stop = board.downward_movement_of_shape(coordinate_1, coordinate_2, coordinate_3, coordinate_4, shape)
                coordinate_1 = (coordinate_1[0] + 1, coordinate_1[1])
                coordinate_2 = (coordinate_2[0] + 1, coordinate_2[1])
                coordinate_3 = (coordinate_3[0] + 1, coordinate_3[1])
                coordinate_4 = (coordinate_4[0] + 1, coordinate_4[1])
                if stop:
                    shape_is_active = False
                    numbers_of_deleted_rows = board.mark_deleted_rows()
                    if len(numbers_of_deleted_rows) != 0:
                        DELETE_ROWS = pygame.USEREVENT + 4
                        pygame.time.set_timer(DELETE_ROWS, 375)
                        delete_rows_event_use = True
                        display_bangs = True
                        bang_start = True
                        number_of_bangs = 20
                        note_about_deleted_rows += len(numbers_of_deleted_rows)
            else:
                shape = get_shape_type()
                shape_is_active = True
                if shape == 'I':
                    board.board[0][4] = 1
                    board.board[1][4] = 1
                    board.board[2][4] = 1
                    board.board[3][4] = 1
                    coordinate_1 = (0, 4)
                    coordinate_2 = (1, 4)
                    coordinate_3 = (2, 4)
                    coordinate_4 = (3, 4)
                elif shape == 'J':
                    board.board[0][4] = 1
                    board.board[1][4] = 1
                    board.board[2][4] = 1
                    board.board[2][3] = 1
                    coordinate_1 = (0, 4)
                    coordinate_2 = (1, 4)
                    coordinate_3 = (2, 4)
                    coordinate_4 = (2, 3)
                elif shape == 'L':
                    board.board[0][4] = 1
                    board.board[1][4] = 1
                    board.board[2][4] = 1
                    board.board[2][5] = 1
                    coordinate_1 = (0, 4)
                    coordinate_2 = (1, 4)
                    coordinate_3 = (2, 4)
                    coordinate_4 = (2, 5)
                elif shape == 'O':
                    board.board[0][4] = 1
                    board.board[0][5] = 1
                    board.board[1][4] = 1
                    board.board[1][5] = 1
                    coordinate_1 = (0, 4)
                    coordinate_2 = (0, 5)
                    coordinate_3 = (1, 4)
                    coordinate_4 = (1, 5)
                elif shape == 'S':
                    board.board[0][5] = 1
                    board.board[0][6] = 1
                    board.board[1][5] = 1
                    board.board[1][4] = 1
                    coordinate_1 = (0, 5)
                    coordinate_2 = (0, 6)
                    coordinate_3 = (1, 5)
                    coordinate_4 = (1, 4)
                elif shape == 'T':
                    board.board[0][4] = 1
                    board.board[0][5] = 1
                    board.board[0][6] = 1
                    board.board[1][5] = 1
                    coordinate_1 = (0, 4)
                    coordinate_2 = (0, 5)
                    coordinate_3 = (0, 6)
                    coordinate_4 = (1, 5)
                elif shape == 'Z':
                    board.board[0][4] = 1
                    board.board[0][5] = 1
                    board.board[1][5] = 1
                    board.board[1][6] = 1
                    coordinate_1 = (0, 4)
                    coordinate_2 = (0, 5)
                    coordinate_3 = (1, 5)
                    coordinate_4 = (1, 6)
            if hotkeys_is_no:
                hotkeys_is_ok = True
                hotkeys_is_no = False
        elif event.type == PUSH_SHAPE_FAST:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                stop = board.downward_movement_of_shape(coordinate_1, coordinate_2, coordinate_3, coordinate_4, shape)
                coordinate_1 = (coordinate_1[0] + 1, coordinate_1[1])
                coordinate_2 = (coordinate_2[0] + 1, coordinate_2[1])
                coordinate_3 = (coordinate_3[0] + 1, coordinate_3[1])
                coordinate_4 = (coordinate_4[0] + 1, coordinate_4[1])
                if stop:
                    shape_is_active = False
                    pygame.time.set_timer(PUSH_SHAPE_FAST, 0)
                    push_shape_fast_event_use = False
                    numbers_of_deleted_rows = board.mark_deleted_rows()
                    if len(numbers_of_deleted_rows) != 0:
                        DELETE_ROWS = pygame.USEREVENT + 4
                        pygame.time.set_timer(DELETE_ROWS, 375)
                        delete_rows_event_use = True
                        display_bangs = True
                        bang_start = True
                        number_of_bangs = 20
                        note_about_deleted_rows += len(numbers_of_deleted_rows)
                if level == 'easy':
                    if note_about_deleted_rows > 11:
                        pygame.time.set_timer(PUSH_SHAPE, 200)
                    elif note_about_deleted_rows > 9:
                        pygame.time.set_timer(PUSH_SHAPE, 250)
                    elif note_about_deleted_rows > 7:
                        pygame.time.set_timer(PUSH_SHAPE, 350)
                    elif note_about_deleted_rows > 5:
                        pygame.time.set_timer(PUSH_SHAPE, 450)
                    elif note_about_deleted_rows > 3:
                        pygame.time.set_timer(PUSH_SHAPE, 550)
                    else:
                        pygame.time.set_timer(PUSH_SHAPE, 600)
                elif level == 'medium':
                    if note_about_deleted_rows > 10:
                        pygame.time.set_timer(PUSH_SHAPE, 200)
                    elif note_about_deleted_rows > 7:
                        pygame.time.set_timer(PUSH_SHAPE, 250)
                    elif note_about_deleted_rows > 4:
                        pygame.time.set_timer(PUSH_SHAPE, 350)
                    elif note_about_deleted_rows > 2:
                        pygame.time.set_timer(PUSH_SHAPE, 450)
                    else:
                        pygame.time.set_timer(PUSH_SHAPE, 500)
                else:
                    if note_about_deleted_rows > 8:
                        pygame.time.set_timer(PUSH_SHAPE, 200)
                    elif note_about_deleted_rows > 5:
                        pygame.time.set_timer(PUSH_SHAPE, 250)
                    elif note_about_deleted_rows > 2:
                        pygame.time.set_timer(PUSH_SHAPE, 350)
                    else:
                        pygame.time.set_timer(PUSH_SHAPE, 400)
            else:
                pygame.time.set_timer(PUSH_SHAPE_FAST, 0)
                push_shape_fast_event_use = False
        elif event.type == DELETE_ROWS:
            plus_score = board.delete_row()
            score = str(int(score) + plus_score)
            pygame.time.set_timer(DELETE_ROWS, 0)
            delete_rows_event_use = False
        elif event.type == pygame.KEYDOWN and hotkeys_is_ok:
            if event.key == pygame.K_a:
                data = board.movement_to_left(coordinate_1, coordinate_2, coordinate_3, coordinate_4, shape)
                if data is not None:
                    coordinate_1 = data[0]
                    coordinate_2 = data[1]
                    coordinate_3 = data[2]
                    coordinate_4 = data[3]
            elif event.key == pygame.K_d:
                data = board.movement_to_right(coordinate_1, coordinate_2, coordinate_3, coordinate_4, shape)
                if data is not None:
                    coordinate_1 = data[0]
                    coordinate_2 = data[1]
                    coordinate_3 = data[2]
                    coordinate_4 = data[3]
            elif event.key == pygame.K_s:
                PUSH_SHAPE_FAST = pygame.USEREVENT + 3
                push_shape_fast_event_use = True
                stop = board.downward_movement_of_shape(coordinate_1, coordinate_2, coordinate_3, coordinate_4, shape)
                coordinate_1 = (coordinate_1[0] + 1, coordinate_1[1])
                coordinate_2 = (coordinate_2[0] + 1, coordinate_2[1])
                coordinate_3 = (coordinate_3[0] + 1, coordinate_3[1])
                coordinate_4 = (coordinate_4[0] + 1, coordinate_4[1])
                if stop:
                    shape_is_active = False
                    if level == 'easy':
                        if note_about_deleted_rows > 11:
                            pygame.time.set_timer(PUSH_SHAPE, 200)
                        elif note_about_deleted_rows > 9:
                            pygame.time.set_timer(PUSH_SHAPE, 250)
                        elif note_about_deleted_rows > 7:
                            pygame.time.set_timer(PUSH_SHAPE, 350)
                        elif note_about_deleted_rows > 5:
                            pygame.time.set_timer(PUSH_SHAPE, 450)
                        elif note_about_deleted_rows > 3:
                            pygame.time.set_timer(PUSH_SHAPE, 550)
                        else:
                            pygame.time.set_timer(PUSH_SHAPE, 600)
                    elif level == 'medium':
                        if note_about_deleted_rows > 10:
                            pygame.time.set_timer(PUSH_SHAPE, 200)
                        elif note_about_deleted_rows > 7:
                            pygame.time.set_timer(PUSH_SHAPE, 250)
                        elif note_about_deleted_rows > 4:
                            pygame.time.set_timer(PUSH_SHAPE, 350)
                        elif note_about_deleted_rows > 2:
                            pygame.time.set_timer(PUSH_SHAPE, 450)
                        else:
                            pygame.time.set_timer(PUSH_SHAPE, 500)
                    else:
                        if note_about_deleted_rows > 8:
                            pygame.time.set_timer(PUSH_SHAPE, 200)
                        elif note_about_deleted_rows > 5:
                            pygame.time.set_timer(PUSH_SHAPE, 250)
                        elif note_about_deleted_rows > 2:
                            pygame.time.set_timer(PUSH_SHAPE, 350)
                        else:
                            pygame.time.set_timer(PUSH_SHAPE, 400)
                else:
                    pygame.time.set_timer(PUSH_SHAPE_FAST, 150)
                    if level == 'easy':
                        if note_about_deleted_rows > 11:
                            pygame.time.set_timer(PUSH_SHAPE, 200)
                        elif note_about_deleted_rows > 9:
                            pygame.time.set_timer(PUSH_SHAPE, 250)
                        elif note_about_deleted_rows > 7:
                            pygame.time.set_timer(PUSH_SHAPE, 350)
                        elif note_about_deleted_rows > 5:
                            pygame.time.set_timer(PUSH_SHAPE, 450)
                        elif note_about_deleted_rows > 3:
                            pygame.time.set_timer(PUSH_SHAPE, 550)
                        else:
                            pygame.time.set_timer(PUSH_SHAPE, 600)
                    elif level == 'medium':
                        if note_about_deleted_rows > 10:
                            pygame.time.set_timer(PUSH_SHAPE, 200)
                        elif note_about_deleted_rows > 7:
                            pygame.time.set_timer(PUSH_SHAPE, 250)
                        elif note_about_deleted_rows > 4:
                            pygame.time.set_timer(PUSH_SHAPE, 350)
                        elif note_about_deleted_rows > 2:
                            pygame.time.set_timer(PUSH_SHAPE, 450)
                        else:
                            pygame.time.set_timer(PUSH_SHAPE, 500)
                    else:
                        if note_about_deleted_rows > 8:
                            pygame.time.set_timer(PUSH_SHAPE, 200)
                        elif note_about_deleted_rows > 5:
                            pygame.time.set_timer(PUSH_SHAPE, 250)
                        elif note_about_deleted_rows > 2:
                            pygame.time.set_timer(PUSH_SHAPE, 350)
                        else:
                            pygame.time.set_timer(PUSH_SHAPE, 400)
    if start_window:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (100, 255, 100), (16, 16, 480, 608), width=1)
        pygame.draw.rect(screen, (100, 255, 100), (21, 21, 470, 598), width=1)
        font = pygame.font.SysFont('staypixelregular', 79)
        text = font.render('tetris', 0, (100, 255, 100), (0, 0, 0))
        screen.blit(text, (161, 160))

        if play_button_is_pressed:

            # верхняя поверхность кнопки

            color = (100, 255, 100)

            pygame.draw.rect(screen, color, (221, 321, 70, 7))

            pygame.draw.rect(screen, color, (214, 328, 7, 7))
            pygame.draw.rect(screen, color, (291, 328, 7, 7))

            pygame.draw.rect(screen, color, (207, 335, 7, 30))
            pygame.draw.rect(screen, color, (298, 335, 7, 30))

            pygame.draw.rect(screen, color, (214, 365, 7, 7))
            pygame.draw.rect(screen, color, (291, 365, 7, 7))

            pygame.draw.rect(screen, color, (221, 372, 70, 7))

            # боковая поверхность кнопки

            pygame.draw.rect(screen, color, (207, 365, 7, 15))
            pygame.draw.rect(screen, color, (298, 365, 7, 15))

            pygame.draw.rect(screen, color, (214, 380, 7, 7))
            pygame.draw.rect(screen, color, (291, 380, 7, 7))

            pygame.draw.rect(screen, color, (221, 387, 70, 7))

            # плоскость под кнопкой

            pygame.draw.rect(screen, color, (305, 357, 7, 7))
            pygame.draw.rect(screen, color, (200, 357, 7, 7))

            pygame.draw.rect(screen, color, (312, 364, 7, 30))
            pygame.draw.rect(screen, color, (194, 364, 7, 30))

            pygame.draw.rect(screen, color, (305, 394, 7, 7))
            pygame.draw.rect(screen, color, (200, 394, 7, 7))

            pygame.draw.rect(screen, color, (207, 401, 98, 7))

            play_button_polygon_list = [(221, 306), (221, 313), (214, 313), (214, 320), (207, 320)]
            play_button_polygon_list += [(207, 350), (214, 350), (214, 357), (221, 357), (221, 364)]
            play_button_polygon_list += [(291, 364), (291, 357), (298, 357), (298, 350), (305, 350)]
            play_button_polygon_list += [(305, 320), (298, 320), (298, 313), (291, 313), (291, 306)]

            font = pygame.font.SysFont('staypixelregular', 19)
            text = font.render('play!', 0, (100, 255, 100), (0, 0, 0))
            screen.blit(text, (236, 342))
        else:

            # верхняя поверхность кнопки

            color = (100, 255, 100)

            pygame.draw.rect(screen, color, (221, 306, 70, 7))

            pygame.draw.rect(screen, color, (214, 313, 7, 7))
            pygame.draw.rect(screen, color, (291, 313, 7, 7))

            pygame.draw.rect(screen, color, (207, 320, 7, 30))
            pygame.draw.rect(screen, color, (298, 320, 7, 30))

            pygame.draw.rect(screen, color, (214, 350, 7, 7))
            pygame.draw.rect(screen, color, (291, 350, 7, 7))

            pygame.draw.rect(screen, color, (221, 357, 70, 7))

            # боковая поверхность кнопки

            pygame.draw.rect(screen, color, (207, 350, 7, 30))
            pygame.draw.rect(screen, color, (298, 350, 7, 30))

            pygame.draw.rect(screen, color, (214, 380, 7, 7))
            pygame.draw.rect(screen, color, (291, 380, 7, 7))

            pygame.draw.rect(screen, color, (221, 387, 70, 7))

            # плоскость под кнопкой

            pygame.draw.rect(screen, color, (305, 357, 7, 7))
            pygame.draw.rect(screen, color, (200, 357, 7, 7))

            pygame.draw.rect(screen, color, (312, 364, 7, 30))
            pygame.draw.rect(screen, color, (194, 364, 7, 30))

            pygame.draw.rect(screen, color, (305, 394, 7, 7))
            pygame.draw.rect(screen, color, (200, 394, 7, 7))

            pygame.draw.rect(screen, color, (207, 401, 98, 7))

            play_button_polygon_list = [(221, 306), (221, 313), (214, 313), (214, 320), (207, 320)]
            play_button_polygon_list += [(207, 350), (214, 350), (214, 357), (221, 357), (221, 364)]
            play_button_polygon_list += [(291, 364), (291, 357), (298, 357), (298, 350), (305, 350)]
            play_button_polygon_list += [(305, 320), (298, 320), (298, 313), (291, 313), (291, 306)]

            font = pygame.font.SysFont('staypixelregular', 19)
            text = font.render('play!', 0, (100, 255, 100), (0, 0, 0))
            screen.blit(text, (236, 327))

        if level == 'easy':
            pygame.draw.rect(screen, color, (108, 537, 75, 25), width=3)
            pygame.draw.rect(screen, color, (108, 559, 75, 10), width=3)
            pygame.draw.rect(screen, color, (98, 579, 95, 2))
            pygame.draw.rect(screen, color, (98, 554, 2, 25))
            pygame.draw.rect(screen, color, (191, 554, 2, 25))
            pygame.draw.rect(screen, color, (98, 554, 10, 2))
            pygame.draw.rect(screen, color, (181, 554, 10, 2))

            font = pygame.font.SysFont('staypixelregular', 17)
            text = font.render('easy', 0, (100, 255, 100), (0, 0, 0))
            screen.blit(text, (131, 543))

            easy_button_rect = pygame.Rect(108, 537, 75, 25)
        else:
            pygame.draw.rect(screen, color, (108, 527, 75, 25), width=3)
            pygame.draw.rect(screen, color, (108, 549, 75, 20), width=3)
            pygame.draw.rect(screen, color, (98, 579, 95, 2))
            pygame.draw.rect(screen, color, (98, 554, 2, 25))
            pygame.draw.rect(screen, color, (191, 554, 2, 25))
            pygame.draw.rect(screen, color, (98, 554, 10, 2))
            pygame.draw.rect(screen, color, (181, 554, 10, 2))

            font = pygame.font.SysFont('staypixelregular', 17)
            text = font.render('easy', 0, (100, 255, 100), (0, 0, 0))
            screen.blit(text, (131, 533))

            easy_button_rect = pygame.Rect(108, 527, 75, 25)

        if level == 'medium':
            pygame.draw.rect(screen, color, (218, 537, 75, 25), width=3)
            pygame.draw.rect(screen, color, (218, 559, 75, 10), width=3)
            pygame.draw.rect(screen, color, (208, 579, 95, 2))
            pygame.draw.rect(screen, color, (208, 554, 2, 25))
            pygame.draw.rect(screen, color, (301, 554, 2, 25))
            pygame.draw.rect(screen, color, (208, 554, 10, 2))
            pygame.draw.rect(screen, color, (291, 554, 10, 2))

            font = pygame.font.SysFont('staypixelregular', 17)
            text = font.render('medium', 0, (100, 255, 100), (0, 0, 0))
            screen.blit(text, (230, 543))

            medium_button_rect = pygame.Rect(218, 537, 75, 25)
        else:
            pygame.draw.rect(screen, color, (218, 527, 75, 25), width=3)
            pygame.draw.rect(screen, color, (218, 549, 75, 20), width=3)
            pygame.draw.rect(screen, color, (208, 579, 95, 2))
            pygame.draw.rect(screen, color, (208, 554, 2, 25))
            pygame.draw.rect(screen, color, (301, 554, 2, 25))
            pygame.draw.rect(screen, color, (208, 554, 10, 2))
            pygame.draw.rect(screen, color, (291, 554, 10, 2))

            font = pygame.font.SysFont('staypixelregular', 17)
            text = font.render('medium', 0, (100, 255, 100), (0, 0, 0))
            screen.blit(text, (230, 533))

            medium_button_rect = pygame.Rect(218, 527, 75, 25)

        if level == 'hard':
            pygame.draw.rect(screen, color, (328, 537, 75, 25), width=3)
            pygame.draw.rect(screen, color, (328, 559, 75, 10), width=3)
            pygame.draw.rect(screen, color, (318, 579, 95, 2))
            pygame.draw.rect(screen, color, (318, 554, 2, 25))
            pygame.draw.rect(screen, color, (411, 554, 2, 25))
            pygame.draw.rect(screen, color, (318, 554, 10, 2))
            pygame.draw.rect(screen, color, (401, 554, 10, 2))

            font = pygame.font.SysFont('staypixelregular', 17)
            text = font.render('hard', 0, (100, 255, 100), (0, 0, 0))
            screen.blit(text, (350, 543))

            hard_button_rect = pygame.Rect(328, 537, 75, 25)
        else:
            pygame.draw.rect(screen, color, (328, 527, 75, 25), width=3)
            pygame.draw.rect(screen, color, (328, 549, 75, 20), width=3)
            pygame.draw.rect(screen, color, (318, 579, 95, 2))
            pygame.draw.rect(screen, color, (318, 554, 2, 25))
            pygame.draw.rect(screen, color, (411, 554, 2, 25))
            pygame.draw.rect(screen, color, (318, 554, 10, 2))
            pygame.draw.rect(screen, color, (401, 554, 10, 2))

            font = pygame.font.SysFont('staypixelregular', 17)
            text = font.render('hard', 0, (100, 255, 100), (0, 0, 0))
            screen.blit(text, (350, 533))

            hard_button_rect = pygame.Rect(328, 527, 75, 25)

    if game_window:
        screen.fill((0, 0, 0))
        color = (100, 255, 100)
        pygame.draw.rect(screen, color, (16, 16, 480, 608), width=1)

        # надпись 'score'

        font = pygame.font.SysFont('staypixelregular', 37)
        text = font.render('score:', 0, color, (0, 0, 0))
        screen.blit(text, (296, 31))

        # надпись со значением 'score'

        font = pygame.font.SysFont('vcrosdmonorusbyd', 23)
        text = font.render(score, 0, color, (0, 0, 0))
        screen.blit(text, (296, 76))

        # надпись 'hi-score'

        font = pygame.font.SysFont('staypixelregular', 37)
        text = font.render('hi-score:', 0, color, (0, 0, 0))
        screen.blit(text, (296, 115))

        # надпись со значением 'hi - score'

        con = sqlite3.connect('hi-scores.db')
        cur = con.cursor()
        if level == 'easy':
            hi_score = str(cur.execute('SELECT easy FROM hi_scores').fetchone()[0])
        elif level == 'medium':
            hi_score = str(cur.execute('SELECT medium FROM hi_scores').fetchone()[0])
        else:
            hi_score = str(cur.execute('SELECT hard FROM hi_scores').fetchone()[0])
        if int(score) > int(hi_score):
            if level == 'easy':
                cur.execute('''UPDATE hi_scores
                               SET easy = ?''', (int(score),))
            elif level == 'medium':
                cur.execute('''UPDATE hi_scores
                               SET medium = ?''', (int(score),))
            else:
                cur.execute('''UPDATE hi_scores
                               SET hard = ?''', (int(score),))
            con.commit()
            hi_score_changed = True
            hi_score = score

        font = pygame.font.SysFont('vcrosdmonorusbyd', 23)
        text = font.render(hi_score, 0, color, (0, 0, 0))
        screen.blit(text, (296, 160))

        # надпись 'level'

        font = pygame.font.SysFont('staypixelregular', 37)
        text = font.render('level:', 0, color, (0, 0, 0))
        screen.blit(text, (296, 462))

        # надпись со значением 'level'

        font = pygame.font.SysFont('staypixelregular', 29)
        text = font.render(level, 0, color, (0, 0, 0))
        screen.blit(text, (296, 507))

        if hi_score_changed and not end_of_game:

            font = pygame.font.SysFont('staypixelregular', 37)
            text = font.render('wow, you', 0, color, (0, 0, 0))
            screen.blit(text, (296, 263))

            font = pygame.font.SysFont('staypixelregular', 37)
            text = font.render('have a new', 0, color, (0, 0, 0))
            screen.blit(text, (296, 308))

            font = pygame.font.SysFont('staypixelregular', 37)
            text = font.render('hi-score!!!', 0, color, (0, 0, 0))
            screen.blit(text, (296, 353))

        if end_of_game:
            font = pygame.font.SysFont('staypixelregular', 37)
            text = font.render('ooh, you', 0, color, (0, 0, 0))
            screen.blit(text, (296, 284))

            font = pygame.font.SysFont('staypixelregular', 37)
            text = font.render('have lost...', 0, color, (0, 0, 0))
            screen.blit(text, (296, 329))

            pygame.draw.rect(screen, color, (108, 546, 75, 25), width=3)
            pygame.draw.rect(screen, color, (108, 568, 75, 20), width=3)
            pygame.draw.rect(screen, color, (98, 598, 95, 2))
            pygame.draw.rect(screen, color, (98, 573, 2, 25))
            pygame.draw.rect(screen, color, (191, 573, 2, 25))
            pygame.draw.rect(screen, color, (98, 573, 10, 2))
            pygame.draw.rect(screen, color, (181, 573, 10, 2))

            font = pygame.font.SysFont('staypixelregular', 17)
            text = font.render('easy', 0, (100, 255, 100), (0, 0, 0))
            screen.blit(text, (131, 552))

        if start_of_start_window:
            board = Board(10, 20)
            board.board.append([0] * 10)
            PUSH_SHAPE = pygame.USEREVENT + 2
            if level == 'easy':
                pygame.time.set_timer(PUSH_SHAPE, 600)
            elif level == 'medium':
                pygame.time.set_timer(PUSH_SHAPE, 500)
            else:
                pygame.time.set_timer(PUSH_SHAPE, 400)
            start_of_start_window = False
        board.render(screen)
        board.notice(screen)
        if display_bangs:
            if number_of_bangs >= 1:
                if bang_start:
                    for i in numbers_of_deleted_rows:
                        y = 19 + (i - 1) * 25
                        for j in range(10):
                            x = 19 + j * 25
                            sprites.Bang(x, y)
                    bang_start = False
                    number_of_bangs -= 1
                else:
                    sprites.bangs.update()
                    number_of_bangs -= 1
                sprites.bangs.draw(screen)
            else:
                for item in sprites.bangs:
                    item.kill()
                display_bangs = False
                number_of_bangs = None
                bang_start = None
                numbers_of_deleted_rows = None
        if board.end_of_game_checking():
            end_of_game = True
            END_OF_GAME = pygame.USEREVENT + 5
            pygame.time.set_timer(END_OF_GAME, 1)
    pygame.display.flip()
    if start_window:
        play_button_polygon = pygame.draw.polygon(screen, (0, 0, 0), play_button_polygon_list)
    clock.tick(fps)

pygame.quit()