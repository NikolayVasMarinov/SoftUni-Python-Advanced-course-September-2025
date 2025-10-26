def setup() -> tuple[list[str], list[str]]:
    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")

    player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'? ")

    while player_one_sign not in ["X", "O"]:
        print("Choose either 'X' or 'O'")
        player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'? ")

    player_two_sign = "O" if player_one_sign == "X" else "X"

    return [player_one_name, player_one_sign], [player_two_name, player_two_sign]

def play_turn(current_player: list[str], current_board: list[list[str]]) -> None:
    choice = choose_position(current_player[0])

    row = (choice - 1) // 3
    column = (choice - 1) % 3

    while not current_board[row][column] == " ":
        print("Choose an empty spot")
        choice = choose_position(current_player[0])

        row = (choice - 1) // 3
        column = (choice - 1) % 3

    current_board[row][column] = current_player[1]

def draw_board(board: list[list[str]]) -> None:
   for row in board:
       print("|", " | ".join(row), "|")

def choose_position(player_name: str) -> int:
    while True:
        try:
            choice = int(input(f"{player_name}, choose a position [1-9]: "))
            if 1 <= choice <= 9:
                return choice
            print("Choose a number between 1 and 9.")
        except ValueError:
            print("Enter a valid integer.")

def check_if_won(board: list[list[str]], sign: str) -> bool:
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)):
            return True

        if all(board[j][i] == sign for j in range(3)):
            return True

    if all(board[i][i] == sign for i in range(3)):
        return True

    if all(board[i][2 - i] == sign for i in range(3)):
        return True

    return False

def is_board_full(board: list[list[str]]) -> bool:
    return all(cell != " " for row in board for cell in row)

def main():
    player_one: list[str]
    player_two: list[str]
    player_one, player_two = setup()

    board: list[list[str]] = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    current: list[str]
    other: list[str]
    if player_one[1] == "X":
        current = player_one
        other = player_two
    else:
        current = player_two
        other = player_one

    while True:
        play_turn(current, board)

        draw_board(board)

        if check_if_won(board, current[1]):
            print(f"{current[0]} has won! Congratulations!")
            break

        if is_board_full(board):
            print(f"Tie between {current[0]} and {other[0]}!")
            break

        current, other = other, current

if __name__ == "__main__":
    main()