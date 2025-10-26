def setup() -> tuple[list[str | int], list[str | int]]:
    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")

    return [player_one_name , 1], [player_two_name, 2]

def play_turn(player: list[str | int], board: list[list[int]]) -> None:
        column_number: int = choose_column(player[0]) - 1

        free_spot: int = find_spot(board[column_number])

        while free_spot == -1:
            print("This column is full.")
            column_number: int = choose_column(player[0]) - 1
            free_spot: int = find_spot(board[column_number])

        board[column_number][free_spot] = player[1]

def find_spot(column: list[int]) -> int:
    for i in range(len(column) - 1, -1, - 1):
        if column[i] == 0:
            return i

    return -1

def choose_column(player_name: str) -> int:
    while True:
        try:
            choice = int(input(f"{player_name}, choose a column [1-7]: "))
            if 1 <= choice <= 7:
                return choice
            print("Choose a number between 1 and 7.")
        except ValueError:
            print("Enter a valid integer.")

def check_winner(board: list[list[int]]):
    for r in range(7):
        for c in range(6):
            if board[r][c] == 0:
                continue

            if check_four_consecutive(board, r, c):
                return True

    return False


def check_four_consecutive(board: list[list[int]], x: int, y: int) -> bool:
    target = board[x][y]
    directions: list[tuple[int, int]] = [
        (-1, 0),
        (-1, 1),
        (0, 1),
        (-1, -1)
    ]

    for dr, dc in directions:
        ct: int = 1

        i: int = 1
        while (i < 4 and check_valid_coords(x + dr * i, y + dc * i)
               and board[x + dr * i][y + dc * i] == target):
            ct += 1
            i += 1

        i = 1
        while (i < 4 and check_valid_coords(x - dr * i, y - dc * i)
               and board[x - dr * i][y - dc * i] == target):
            ct += 1
            i += 1

        if ct >= 4:
            return True

    return False

def check_tie(board: list[list[int]]) -> bool:
    return all(cell !=0 for col in board for cell in col)

def draw_board(board: list[list[int]]) -> None:
    for row in zip(*board):
        print(list(row))

def check_valid_coords(x: int, y: int) -> bool:
    return 0 <= x < 7 and 0 <= y < 6

def reset_game(board: list[list[int]]) -> None:
    board.clear()
    board.extend([[0, 0, 0, 0, 0, 0] for _ in range(7)])

def main():
    player_one: list[str|int]
    player_two: list[str|int]
    player_one, player_two = setup()

    board: list[list[int]] = [[0, 0, 0, 0, 0, 0] for _ in range(7)]

    current: list[str|int] = player_one
    other: list[str|int] = player_two

    game_ended: bool = False

    while True:
        play_turn(current, board)

        draw_board(board)

        if check_winner(board):
            print(f"{current[0]} has won! Congratulations!")
            game_ended = True

        if check_tie(board):
            print(f"Game ended. There is a tie!")
            game_ended = True

        current, other = other, current

        if game_ended:
            continue_game: str = input("Would you like to start another game? [Yes]/[No]: ")

            while True:
                if continue_game == "Yes":
                    game_ended = False
                    reset_game(board)
                    current = player_one
                    other = player_two
                    break

                elif continue_game == "No":
                    print("Thanks for playing!")
                    exit()

                continue_game = input("Enter 'Yes' or 'No' please. ")

if __name__ == "__main__":
    main()