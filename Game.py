import random

def check_guess(secret_number, guess, num_digits):
    correct_digits = sum(1 for s, g in zip(str(secret_number), str(guess)) if s == g)
    correct_positions = sum(1 for s, g in zip(str(secret_number), str(guess)) if s == g and s == g)
    return correct_digits, correct_positions

def play_round(is_player1_turn, num_digits):
    player_name = "Player 1" if is_player1_turn else "Player 2"
    opponent_name = "Player 2" if is_player1_turn else "Player 1"

    secret_number = random.randint(10**(num_digits-1), (10**num_digits)-1) if is_player1_turn else int(input(f"{player_name}, set your {num_digits}-digit number: "))
    num_guesses = 0

    while True:
        guess = int(input(f"{opponent_name}, guess the number: "))
        num_guesses += 1

        correct_digits, correct_positions = check_guess(secret_number, guess, num_digits)

        if guess == secret_number:
            print(f"{opponent_name}, you guessed it in {num_guesses} tries!")
            return num_guesses
        else:
            print(f"You have {correct_digits} correct digits and {correct_positions} in correct positions.")

def mastermind_game(num_rounds=1, num_digits=4):
    player1_wins = 0
    player2_wins = 0
    ties = 0

    for _ in range(num_rounds):
        player1_guesses = play_round(True, num_digits)
        player2_guesses = play_round(False, num_digits)

        if player1_guesses < player2_guesses:
            print("Player 1 wins the round!")
            player1_wins += 1
        elif player1_guesses > player2_guesses:
            print("Player 2 wins the round!")
            player2_wins += 1
        else:
            print("It's a tie!")
            ties += 1

    print("\nGame Over!")
    print(f"Player 1 wins: {player1_wins}")
    print(f"Player 2 wins: {player2_wins}")
    print(f"Ties: {ties}")

if __name__ == "__main__":
    num_rounds = int(input("Enter the number of rounds: "))
    num_digits = int(input("Enter the number of digits: "))
    mastermind_game(num_rounds, num_digits)
