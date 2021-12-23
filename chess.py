import time
import random
import sys
import pygame as pg
import pieces

size = width,height = 720,480
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (142, 142, 142)
SILVER = (192, 192, 192)
LIGHT = (255, 231, 181)
DARK = (87, 58, 46)
transcript, turn_number = '', 0

def generate_pieces(color):
    if color == 'white':
        prefix = './images/w' 
        return [pieces.Rook(color,prefix+'R.png'), pieces.Knight(color,prefix+'N.png'), pieces.Bishop(color,prefix+'B.png'),
     pieces.Queen(color,prefix+'Q.png'), pieces.King(color,prefix+'K.png'), pieces.Bishop(color,prefix+'B.png'),
     pieces.Knight(color,prefix+'N.png'), pieces.Rook(color,prefix+'R.png')] 
    else: 
        prefix = './images/b'
        return [pieces.Rook(color,prefix+'R.png'), pieces.Knight(color,prefix+'N.png'), pieces.Bishop(color,prefix+'B.png'),
     pieces.King(color,prefix+'K.png'), pieces.Queen(color,prefix+'Q.png'), pieces.Bishop(color,prefix+'B.png'),
     pieces.Knight(color,prefix+'N.png'), pieces.Rook(color,prefix+'R.png')] 
        



def make_pieces(screen, board, flipped):
    num = 0
    for row, pieces in enumerate(board[::(-1 if flipped else 1)]):
        for square, piece in enumerate(pieces[::(-1 if flipped else 1)]):
            if piece:
                image = pg.image.load(piece.path).convert()
                image = pg.transform.scale(image, (50, 50))
                screen.blit(image, (40 + (square * 50), 40 + (row * 50)))

def make_squares(screen):
    color_dict = {True: LIGHT, False: DARK}
    current_color = True
    for row in range(8):
        for square in range(8):
            pg.draw.rect(screen, color_dict[current_color], ((40 + (square * 50)), 40 + (row * 50), 50, 50))
            current_color = not current_color
        current_color = not current_color

def make_coords(screen, font, flipped):
    for row in range(8):
        if flipped:
            font.render_to(screen, (10, 45 + (row * 50)), chr(49 + row))
        else:
            font.render_to(screen, (10, 45 + (row * 50)), chr(56 - row))
    for col in range(8):
        if flipped:
            font.render_to(screen, (45 + (col * 50), 450), chr(72 - col))
        else:
            font.render_to(screen, (45 + (col * 50), 450), chr(65 + col))

def clean_board():
    board = [[None for x in range(8)] for x in range(8)]
    board[0] = generate_pieces("black")
    board[7] = generate_pieces("white")
    board[1] = [pieces.Pawn("black", "./images/bP.png") for square in board[1]]
    board[6] = [pieces.Pawn("white", "./images/wP.png") for square in board[6]]
    return board

def main():
    global transcript, turn_number
    pg.init()
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()
    pg.display.set_caption('Chess')
    pg.display.set_icon(pg.image.load('./images/wK.png').convert())
    pg.display.update()

    playing = True
    turn = 'white'
    check = False
    board_flipped = False
    auto_flip = False
    kings = [(4, 7), (4, 0)]
    promotion = 'queen'
    target_square = None
    target = None
    captures = []
    legal_moves = []

    board = clean_board()

    while True:
        pg.display.update()
        bg = pg.transform.scale(pg.image.load('./images/magnus.jpeg').convert(), size)
        screen.blit(bg, (0, 0))
        COLOR = SILVER if turn == 'white' else BLACK
        make_squares(screen)
        #make_coords(screen, board_flipped)
        make_pieces(screen, board, board_flipped)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()


main()