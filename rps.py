import random

def play_round(player_choice):
  """Plays a single round of Rock, Paper, Scissors."""

  # Validate player's choice
  if player_choice.lower() not in ["rock", "paper", "scissors"]:
    return "Invalid choice. Please choose from rock, paper, or scissors."

  # Computer's random choice
  computer_choice = random.choice(["rock", "paper", "scissors"])

  # Determine the winner
  if player_choice.lower() == computer_choice:
    return f"It's a tie! You both chose {player_choice.lower()}."
  elif (
      (player_choice.lower() == "rock" and computer_choice == "scissors")
      or (player_choice.lower() == "paper" and computer_choice == "rock")
      or (player_choice.lower() == "scissors" and computer_choice == "paper")
  ):
    return f"You win! {player_choice.lower()} beats {computer_choice}."
  else:
    return f"You lose! {computer_choice} beats {player_choice.lower()}."


def main():
  """Main function to run the Rock, Paper, Scissors game."""

  while True:
    player_choice = input("Choose rock, paper, or scissors: ")
    result = play_round(player_choice)
    print(result)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
      break

if __name__ == "__main__":
  main()