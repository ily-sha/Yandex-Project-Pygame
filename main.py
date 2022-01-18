import pygame

from classes import Board

from functions import get_shape_type

pygame.init()
size = width, height = 512, 640
screen = pygame.display.set_mode(size)
game_window = False
settings_window = False
start_window = True
start_of_start_window = False
PUSH_SHAPE = None
shape_is_active = False
upload_shapes = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_window:
                if button_polygon.collidepoint(event.pos):
                    start_window = False
                    game_window = True
                    start_of_start_window = True
        elif event.type == PUSH_SHAPE:
            if shape_is_active:
                pass
            else:
                shape = get_shape_type()
                shape = 'I'
                shape_is_active = True
                print(shape)
                if shape == 'I':
                    board.board[0][4] = 1
                    board.board[1][4] = 1
                    board.board[2][4] = 1
                    board.board[3][4] = 1
                    coordinate_1 = (0, 4)
                    coordinate_2 = (1, 4)
                    coordinate_3 = (2, 4)
                    coordinate_4 = (3, 4)
                upload_shapes = True
    if start_window:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (100, 255, 100), (16, 16, 480, 608), width=1)
        pygame.draw.rect(screen, (100, 255, 100), (21, 21, 470, 598), width=1)
        font = pygame.font.SysFont('staypixelregular', 79)
        text = font.render('tetris', 0, (100, 255, 100), (0, 0, 0))
        screen.blit(text, (161, 160))

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

        button_polygon = [(221, 306), (221, 313), (214, 313), (214, 320), (207, 320)]
        button_polygon += [(207, 350), (214, 350), (214, 357), (221, 357), (221, 364)]
        button_polygon += [(291, 364), (291, 357), (298, 357), (298, 350), (305, 350)]
        button_polygon += [(305, 320), (298, 320), (298, 313), (291, 313), (291, 306)]

        font = pygame.font.SysFont('staypixelregular', 19)
        text = font.render('play!', 0, (100, 255, 100), (0, 0, 0))
        screen.blit(text, (236, 327))
    if game_window:
        screen.fill((0, 0, 0))
        color = (100, 255, 100)
        pygame.draw.rect(screen, color, (16, 16, 480, 608), width=1)

        # надпись 'score'

        font = pygame.font.SysFont('staypixelregular', 37)
        text = font.render('score:', 0, color, (0, 0, 0))
        screen.blit(text, (296, 31))

        # надпись со значением 'score'

        font = pygame.font.SysFont('staypixelregular', 29)
        text = font.render('aaaaaa', 0, color, (0, 0, 0))
        screen.blit(text, (296, 76))

        # надпись 'hi-score'

        font = pygame.font.SysFont('staypixelregular', 37)
        text = font.render('hi-score:', 0, color, (0, 0, 0))
        screen.blit(text, (296, 115))

        # надпись со значением 'hi - score'

        font = pygame.font.SysFont('staypixelregular', 29)
        text = font.render('aaaaaa', 0, color, (0, 0, 0))
        screen.blit(text, (296, 160))

        # надпись 'level'

        font = pygame.font.SysFont('staypixelregular', 37)
        text = font.render('level:', 0, color, (0, 0, 0))
        screen.blit(text, (296, 462))

        # надпись со значением 'level'

        font = pygame.font.SysFont('staypixelregular', 29)
        text = font.render('aaaaaa', 0, color, (0, 0, 0))
        screen.blit(text, (296, 507))

        if start_of_start_window:
            board = Board(10, 20)
            board.board.append([0] * 10)
            start_of_start_window = False
            PUSH_SHAPE = pygame.USEREVENT + 1
            pygame.time.set_timer(PUSH_SHAPE, 1500)
        board.render(screen)
        if upload_shapes:
            board.notice(screen)
    pygame.display.flip()
    if start_window:
        button_polygon = pygame.draw.polygon(screen, (0, 0, 0), button_polygon)

pygame.quit()