import random

"""
Rock-Paper-Scissors Game
A simple command-line game where a user plays against the computer.
"""

# Dictionary mapping numerical choices to game actions
ACTIONS: dict[int, str] = {0: "Rock", 1: "Paper", 2: "Scissors"}

# Dictionary defining which action defeats which
VICTORIES: dict[str, str] = {
    "Rock": "Scissors",  # Rock beats Scissors
    "Paper": "Rock",  # Paper beats Rock
    "Scissors": "Paper",  # Scissors beat Paper
}


def get_user_selection(actions: dict[int, str]) -> str:
    """Prompts the user to select an action and returns the corresponding string."""
    choices = [f"{actions[action]}[{action}]" for action in actions]
    choices_str = ", ".join(choices)
    while True:
        try:
            selection = int(
                input(f"Enter a choice ({choices_str}): ")
            )  # Prompt user for input
            if selection in actions:
                return actions[selection]  # Return corresponding action
            else:
                print(
                    f"Invalid selection. Enter a value in range [0, {len(actions) - 1}]"
                )
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_computer_selection(actions: dict[int, str]) -> str:
    """Randomly selects an action for the computer."""
    selection = random.randint(0, len(actions) - 1)  # Generate random choice
    return actions[selection]


def get_determine_winner(
    victories: dict[str, str], user_action: str, computer_action: str
) -> str:
    """Determines the winner of the game based on user and computer actions."""
    if user_action == computer_action:
        return f"Both players selected {user_action}. It's a tie!"  # Case for a tie
    elif victories[user_action] == computer_action:
        return f"{user_action} beats {computer_action}! You win!"  # User wins
    else:
        return f"{computer_action} beats {user_action}! You lose."  # Computer wins


if __name__ == "__main__":
    while True:
        user_selection = get_user_selection(ACTIONS)  # Get user's choice
        print(f"You selected: {user_selection}")

        computer_selection = get_computer_selection(ACTIONS)  # Get computer's choice
        print(f"Computer selected: {computer_selection}")

        determine_winner = get_determine_winner(
            VICTORIES, user_selection, computer_selection
        )
        print(determine_winner)  # Display game result

        # Ask the user if they want to play again
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing!")  # Exit message
            break
