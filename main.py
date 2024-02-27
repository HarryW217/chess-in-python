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
captured_pieces_black = []

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

# check variables / flashing counter
counter = 0

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
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 16, white_locations[i][1] * 100 + 22))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 8, white_locations[i][1] * 100 + 15))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1, 
                                                 100, 100], 2)
    # Black Pieces    
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 16, black_locations[i][1] * 100 + 22))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 8, black_locations[i][1] * 100 + 15))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1, 
                                                 100, 100], 2)
    
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1]+1) not in white_locations and \
        (position[0], position[1]+1) not in black_locations and position[1]<7:
            moves_list.append((position[0],position[1]+1))
        if (position[0], position[1]+2) not in white_locations and \
        (position[0], position[1]+2) not in black_locations and position[1]==1:
            moves_list.append((position[0],position[1]+2))
        if (position[0]+1, position[1]+1) in black_locations:
            moves_list.append((position[0]+1, position[1]+1))
        if (position[0]-1, position[1]+1) in black_locations:
            moves_list.append((position[0]-1, position[1]+1))
    else:
        if (position[0], position[1]-1) not in white_locations and \
        (position[0], position[1]-1) not in black_locations and position[1]>0:
            moves_list.append((position[0],position[1]-1))
        if (position[0], position[1]-2) not in white_locations and \
        (position[0], position[1]-2) not in black_locations and position[1]==6:
            moves_list.append((position[0],position[1]-2))
        if (position[0]-1, position[1]-1) in white_locations:
            moves_list.append((position[0]-1, position[1]-1))
        if (position[0]+1, position[1]-1) in white_locations:
            moves_list.append((position[0]+1, position[1]-1))
    return moves_list

def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies = black_locations
        friends = white_locations
    else:
        friends = black_locations
        enemies = white_locations
    for i in range(4): # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path: 
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list
        
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        friends = white_locations
    else:
        friends = black_locations
    # A Knight can go travel to up to 8 squares, all two squares 
    # in one direction and one in another:
    targets = [(1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2,-1)]
    for i in range(len(targets)):
        target = (position[0]+targets[i][0], position[1]+targets[i][1])
        if target not in friends and 0 <= target[0] <=7 and 0 <= target[1] <=7:
            moves_list.append(target)
    return moves_list

def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies = black_locations
        friends = white_locations
    else:
        friends = black_locations
        enemies = white_locations
    for i in range(4): # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path: 
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_queen(position, color):
    moves_list = check_bishop(position,color)
    second_list = check_rook(position,color)
    for move in second_list:
        moves_list.append(move)
    return moves_list

def check_king(position, color):
    moves_list = []
    if color == 'white':
        friends = white_locations
    else:
        friends = black_locations
    targets = [(0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1)]
    # Note: I have written the for loop slightly differently than in the similar 
    # check_knight function in an effort to experiment with different syntactic approaches!
    for target in targets:
        current_target = (position[0]+target[0], position[1]+target[1])
        if current_target not in friends and 0 <= current_target[0] <=7 and 0 <= current_target[1] <=7:
            moves_list.append(current_target)
    return moves_list

def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1]*100 + 50), 5)

def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825,5 + 50*i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925,5 + 50*i))

# Checks valid moves for just the selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

def draw_check_and_handle_checkmate():
    is_checked = False
    
    if turn_step < 2: # We have just had black's turn
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    is_checked = True
                    if counter < 15:  
                        pygame.draw.rect(screen, 'dark red', [king_location[0]*100 + 1, king_location[1]*100 + 1, 100, 100], 5)
            
            if is_checked:
                king_cannot_move = False
                invalid_moves_total = 0
                kings_moves = check_king(king_location, 'white') 
                for move in kings_moves: # For every move that the white King can make,
                    for move_list in black_options: # we check every nested moves list in the black options,
                        if move in move_list: # and if the white King's move is in one of these nested lists,
                            invalid_moves_total += 1 # we add 1 to our total of invalid King moves
                            break  # and break the loop to avoid unneccessary iterations for this move. 
                if invalid_moves_total == len(kings_moves): # If the number of invalid moves matches the total number of King moves,
                    king_cannot_move = True # then the King cannot move!
                
                pieces_cannot_attack = True
                king_danger_zones = check_queen(king_location, 'white') 
                # We can try using the check_queen function to get all the positions relative to
                # a King where it might be checked
                attacking_pieces_locations = []
                for zone in king_danger_zones:
                    if zone in black_locations:
                        attacking_pieces_locations.append(zone)
                for i in range(len(white_options)):
                    options = white_options[i]
                    for i in range(len(options)):
                        if options[i] in attacking_pieces_locations:
                            pieces_cannot_attack = False
                            break
                            
                if king_cannot_move and pieces_cannot_attack:
                    draw_game_over('black')
                    
    else: # We have just had white's turn
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    is_checked = True
                    if counter < 15:  
                        pygame.draw.rect(screen, 'dark red', [king_location[0]*100 + 1, king_location[1]*100 + 1, 100, 100], 5)
            
            if is_checked:
                king_cannot_move = False
                invalid_moves_total = 0
                kings_moves = check_king(king_location, 'black')  
                for move in kings_moves:
                    for move_list in white_options:
                        if move in move_list:
                            invalid_moves_total += 1
                            break 
                if invalid_moves_total == len(kings_moves):
                    king_cannot_move = True
                
                pieces_cannot_attack = True
                king_danger_zones = check_queen(king_location, 'black') 
                # We can try using the check_queen function to get all the positions relative to
                # a King where it might be checked
                attacking_pieces_locations = []
                for zone in king_danger_zones:
                    if zone in white_locations:
                        attacking_pieces_locations.append(zone)
                for i in range(len(black_options)):
                    options = black_options[i]
                    for i in range(len(options)):
                        if options[i] in attacking_pieces_locations:
                            pieces_cannot_attack = False
                            break
                            
                if king_cannot_move and pieces_cannot_attack:
                    draw_game_over('white')

  
def draw_game_over(winner):
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))


# Main Game Loop
black_options = check_options(black_pieces, black_locations, 'black') 
white_options = check_options(white_pieces, white_locations, 'white') 

run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill(dark_brown)
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check_and_handle_checkmate()

    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        # If a mouse button is clicked and it is the left mouse button:
            x_coordinate = event.pos[0] // 100
            y_coordinate = event.pos[1] // 100
            click_coordinates = (x_coordinate, y_coordinate)
            if turn_step < 2:
                if click_coordinates in white_locations:
                    selection = white_locations.index(click_coordinates)
                    if turn_step == 0:
                        turn_step = 1
                if click_coordinates in valid_moves and selection != 100:
                    white_locations[selection] = click_coordinates
                    if click_coordinates in black_locations:
                        black_piece_index = black_locations.index(click_coordinates)
                        captured_pieces_white.append(black_pieces[black_piece_index])
                        black_pieces.pop(black_piece_index)
                        black_locations.pop(black_piece_index)
                    black_options = check_options(black_pieces, black_locations, 'black') 
                    white_options = check_options(white_pieces, white_locations, 'white') 
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coordinates in black_locations:
                    selection = black_locations.index(click_coordinates)
                    if turn_step == 2:
                        turn_step = 3
                if click_coordinates in valid_moves and selection != 100:
                    black_locations[selection] = click_coordinates
                    if click_coordinates in white_locations:
                        white_piece_index = white_locations.index(click_coordinates)
                        captured_pieces_black.append(white_pieces[white_piece_index])
                        white_pieces.pop(white_piece_index)
                        white_locations.pop(white_piece_index)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white') 
                    turn_step = 0
                    selection = 100
                    valid_moves = []
    pygame.display.flip()
pygame.quit()