# ============================================
# Tic Tac Toe Game
# Author: Muhammad Sohaib Imran
# FAST-NUCES, Lahore | FinTech
# ============================================

import os


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(board):
    """Display the Tic Tac Toe board."""
    print("\n")
    print("  ╔═══╦═══╦═══╗")
    print(f"  ║ {board[0]} ║ {board[1]} ║ {board[2]} ║")
    print("  ╠═══╬═══╬═══╣")
    print(f"  ║ {board[3]} ║ {board[4]} ║ {board[5]} ║")
    print("  ╠═══╬═══╬═══╣")
    print(f"  ║ {board[6]} ║ {board[7]} ║ {board[8]} ║")
    print("  ╚═══╩═══╩═══╝")
    print("\n  Positions:")
    print("  ╔═══╦═══╦═══╗")
    print("  ║ 1 ║ 2 ║ 3 ║")
    print("  ╠═══╬═══╬═══╣")
    print("  ║ 4 ║ 5 ║ 6 ║")
    print("  ╠═══╬═══╬═══╣")
    print("  ║ 7 ║ 8 ║ 9 ║")
    print("  ╚═══╩═══╩═══╝\n")


def check_winner(board, mark):
    """Check if the given mark has won."""
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal
        [2, 4, 6],  # Anti-diagonal
    ]
    for condition in win_conditions:
        if all(board[i] == mark for i in condition):
            return True
    return False


def check_draw(board):
    """Check if the game is a draw."""
    return all(cell in ['X', 'O'] for cell in board)


def get_player_move(board, player, mark):
    """Get and validate player move."""
    while True:
        try:
            move = int(input(f"  🎯 {player} ({mark}), enter position (1-9): "))
            if move < 1 or move > 9:
                print("  ❌ Invalid! Enter a number between 1 and 9.")
            elif board[move - 1] in ['X', 'O']:
                print("  ❌ That position is already taken! Try again.")
            else:
                return move - 1
        except ValueError:
            print("  ❌ Invalid input! Please enter a number.")


def print_score(scores):
    """Display current scores."""
    print(f"\n  📊 SCORES")
    print(f"  ─────────────────────")
    print(f"  {scores['player1_name']} (X) : {scores['player1']}")
    print(f"  {scores['player2_name']} (O) : {scores['player2']}")
    print(f"  Draws              : {scores['draws']}")
    print(f"  ─────────────────────\n")


def play_game(player1, player2, scores):
    """Play a single game of Tic Tac Toe."""
    board = [str(i) for i in range(1, 10)]
    board = [' '] * 9
    current_player = player1
    current_mark = 'X'

    while True:
        clear_screen()
        print("\n" + "=" * 35)
        print("       ❌⭕ TIC TAC TOE ⭕❌")
        print("       Muhammad Sohaib Imran")
        print("=" * 35)
        print_score(scores)
        print_board(board)
        print(f"  Current Turn: {current_player} ({current_mark})")

        # Get move
        move = get_player_move(board, current_player, current_mark)
        board[move] = current_mark

        # Check winner
        if check_winner(board, current_mark):
            clear_screen()
            print("\n" + "=" * 35)
            print("       ❌⭕ TIC TAC TOE ⭕❌")
            print("=" * 35)
            print_board(board)
            print(f"\n  🏆 {current_player} ({current_mark}) WINS!\n")

            if current_mark == 'X':
                scores['player1'] += 1
            else:
                scores['player2'] += 1
            print_score(scores)
            return

        # Check draw
        if check_draw(board):
            clear_screen()
            print("\n" + "=" * 35)
            print("       ❌⭕ TIC TAC TOE ⭕❌")
            print("=" * 35)
            print_board(board)
            print(f"\n  🤝 It's a DRAW!\n")
            scores['draws'] += 1
            print_score(scores)
            return

        # Switch player
        if current_player == player1:
            current_player = player2
            current_mark = 'O'
        else:
            current_player = player1
            current_mark = 'X'


def main():
    """Main game loop."""
    clear_screen()
    print("\n" + "=" * 35)
    print("       ❌⭕ TIC TAC TOE ⭕❌")
    print("       Muhammad Sohaib Imran")
    print("       FAST-NUCES, Lahore")
    print("=" * 35)
    print("\n  Welcome to Tic Tac Toe!\n")

    player1 = input("  Enter Player 1 name: ").strip() or "Player 1"
    player2 = input("  Enter Player 2 name: ").strip() or "Player 2"

    scores = {
        'player1': 0,
        'player2': 0,
        'draws': 0,
        'player1_name': player1,
        'player2_name': player2
    }

    while True:
        play_game(player1, player2, scores)

        again = input("\n  🔄 Play again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            clear_screen()
            print("\n" + "=" * 35)
            print("       ❌⭕ FINAL SCORES ⭕❌")
            print("=" * 35)
            print_score(scores)

            if scores['player1'] > scores['player2']:
                print(f"  🏆 Overall Winner: {player1}!\n")
            elif scores['player2'] > scores['player1']:
                print(f"  🏆 Overall Winner: {player2}!\n")
            else:
                print(f"  🤝 Overall Result: It's a TIE!\n")

            print("  Thanks for playing!")
            print("  — Muhammad Sohaib Imran\n")
            break


if __name__ == "__main__":
    main()
