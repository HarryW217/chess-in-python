import pygame
import os

# LeagueSpartan-Bold font file path
script_dir = os.path.dirname(__file__)
font_path = os.path.join(script_dir, 'assets','LeagueSpartan-Bold.otf')

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font(font_path, 20)
big_font = pygame.font.Font(font_path, 50)
timer = pygame.time.Clock()
fps = 60

# Game Variables and Images

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
white_locations = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                   (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
black_locations = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                   (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]
captured_pieces_white = []
captured_pieces_white = []

turn_step = 0 # Keeps track of the phase of each turn
# 0 - White's turn, no selection; 1 - White's turn, piece selected;
# 2 - Black's turn, no selection; 3 - Black's turn, piece selected etc.

selection = 100 # A variable for piece selected, initially a large number not on the board. 

valid_moves = [] # A list for valid moves a piece can make

# Game piece images
# All loaded and scaled for display on the board and captured pieces section
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80,80))
black_queen_small = pygame.transform.scale(black_queen, (45,45))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# check variables/ flashing counter


# RGB values for colors

light_brown = (205, 133, 63)
dark_brown = (101, 67, 33)

def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, light_brown, [600-(column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, light_brown, [700-(column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, 'gray', [800, 0, 200, 800])
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
        status_text = ['White: Select a Piece to Move.', 'White: Select a Destination.',
                       'Black: Select a Piece to Move.', 'Black: Select a Destination.']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (15,825))
        for i in range(9):
            pygame.draw.line(screen, 'black', ((100*i),0),((100*i),800))
            pygame.draw.line(screen, 'black', (0,(100*i)),(800,(100*i)))
            
def draw_pieces():
    # White Pieces
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0]* 100 + 16, white_locations[i][1]*100 + 22))
        else:
            screen.blit(white_images[index], (white_locations[i][0]* 100 + 8, white_locations[i][1]*100 + 15))
    # Black Pieces    
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0]* 100 + 16, black_locations[i][1]*100 + 22))
        else:
            screen.blit(black_images[index], (black_locations[i][0]* 100 + 8, black_locations[i][1]*100 + 15))
    

# Main Game Loop
run = True
while run:
    timer.tick(fps)
    screen.fill(dark_brown)
    draw_board()
    draw_pieces()
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
pygame.quit()