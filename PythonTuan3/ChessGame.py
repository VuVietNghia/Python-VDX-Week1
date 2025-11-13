# MINI CHESS GAME - CONSOLE VERSION (~120 lines)
import copy

# Ký tự quân cờ
PIECES = {
    'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
    'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
}


# Bàn cờ ban đầu
def init_board():
    return [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]


# In bàn cờ
def print_board(board):
    print("  a b c d e f g h")
    for i in range(8):
        row = str(8 - i) + " "
        for j in range(8):
            piece = board[i][j]
            row += PIECES.get(piece, '·') + " "
        print(row + str(8 - i))
    print("  a b c d e f g h")


# Chuyển tọa độ alge (e2) -> (row, col)
def alg_to_coord(alg):
    col = ord(alg[0]) - ord('a')
    row = 8 - int(alg[1])
    return row, col


# Kiểm tra trong bàn cờ
def on_board(r, c):
    return 0 <= r < 8 and 0 <= c < 8


# Tìm vị trí vua
def find_king(board, color):
    king = 'K' if color == 'white' else 'k'
    for r in range(8):
        for c in range(8):
            if board[r][c] == king:
                return r, c


# Kiểm tra xem vua có bị chiếu không
def is_in_check(board, color):
    kr, kc = find_king(board, color)
    opponent = 'black' if color == 'white' else 'white'
    return is_attacked(board, kr, kc, opponent)


# Kiểm tra ô (r,c) có bị tấn công bởi đối thủ không
def is_attacked(board, r, c, by_color):
    directions = {
        'P': [(-1, -1), (-1, 1)] if by_color == 'white' else [(1, -1), (1, 1)],
        'N': [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)],
        'K': [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)],
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        'Q': [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    }
    piece_map = {'white': 'PRNBQK', 'black': 'prnbqk'}
    for pr, pc in [(r, c) for r in range(8) for c in range(8)]:
        piece = board[pr][pc]
        if piece in piece_map[by_color]:
            dirs = directions.get(piece.upper(), [])
            for dr, dc in dirs:
                nr, nc = pr + dr, pc + dc
                if piece.upper() in 'RQB':
                    while on_board(nr, nc) and board[nr][nc] == '.':
                        nr += dr;
                        nc += dc
                    if on_board(nr, nc) and (nr, nc) == (r, c) and board[nr][nc] != '.':
                        if board[nr][nc].islower() if by_color == 'white' else board[nr][nc].isupper():
                            continue
                        return True
                elif piece.upper() == 'P':
                    if (nr, nc) == (r, c):
                        return True
                elif (nr, nc) == (r, c):
                    return True
    return False


# Kiểm tra nước đi hợp lệ (cơ bản)
def is_valid_move(board, move, color):
    if len(move) != 4: return False
    r1, c1 = alg_to_coord(move[0:2])
    r2, c2 = alg_to_coord(move[2:4])
    piece = board[r1][c1]
    if not piece or (color == 'white' and piece.islower()) or (color == 'black' and piece.isupper()):
        return False
    if board[r2][c2] != '.' and ((color == 'white') == board[r2][c2].isupper()):
        return False

    # Simulate move
    temp = copy.deepcopy(board)
    temp[r2][c2] = temp[r1][c1]
    temp[r1][c1] = '.'
    if is_in_check(temp, color):
        return False
    return True


# Thực hiện nước đi
def make_move(board, move):
    r1, c1 = alg_to_coord(move[0:2])
    r2, c2 = alg_to_coord(move[2:4])
    board[r2][c2] = board[r1][c1]
    board[r1][c1] = '.'


# Kiểm tra chiếu hết / hòa
def is_game_over(board, color):
    has_move = False
    for r1 in range(8):
        for c1 in range(8):
            piece = board[r1][c1]
            if piece != '.' and ((color == 'white') == piece.isupper()):
                for r2 in range(8):
                    for c2 in range(8):
                        move = f"{chr(c1 + 97)}{8 - r1}{chr(c2 + 97)}{8 - r2}"
                        if is_valid_move(board, move, color):
                            temp = copy.deepcopy(board)
                            make_move(temp, move)
                            if not is_in_check(temp, color):
                                has_move = True
    to
    in_check = is_in_check(board, color)
    return (in_check and not has_move, not in_check and not has_move)


# === MAIN GAME ===
board = init_board()
turn = 'white'
move_count = 1

print("🎉 MINI CHESS GAME - Nhập nước đi kiểu: e2e4")
print("Gõ 'quit' để thoát\n")

while True:
    print_board(board)
    check_status = " (Đang bị chiếu!)" if is_in_check(board, turn) else ""
    print(f"\nLượt {move_count}: {'Trắng' if turn == 'white' else 'Đen'} đi{check_status}")

    move = input("Nước đi: ").strip().lower()
    if move == 'quit':
        print("Bye!")
        break
    if len(move) != 4 or not move[0:2].isalnum() or not move[2:4].isalnum():
        print("❌ Sai định dạng! Dùng kiểu: e2e4")
        continue
    if not is_valid_move(board, move, turn):
        print("❌ Nước đi không hợp lệ!")
        continue

    make_move(board, move)
    checkmate, stalemate = is_game_over(board, 'black' if turn == 'white' else 'white')

    if checkmate:
        print_board(board)
        print(f"🎉 CHIẾU HẾT! {'Trắng' if turn == 'black' else 'Đen'} thắng!")
        break
    if stalemate:
        print_board(board)
        print("🤝 HÒA CỜ! Không bên nào đi được.")
        break

    turn = 'black' if turn == 'white' else 'white'
    move_count += (turn == 'white')