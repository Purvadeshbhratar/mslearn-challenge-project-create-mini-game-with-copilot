# write 'hello world' to the console
print('hello world')

# write a code to create a console minigame Rock, Paper, Scissors where rock beats scissors, scissors beats paper, and paper beats rock take input from user and display if they win  or loss and ask if they want to play again, if they want to play repeat the game or else show their score at end
import random
score = 0
while True:
    print('Enter your choice: rock, paper, scissors')
    user_choice = input().lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print('Invalid input! Please choose rock, paper, or scissors.')
        continue
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f'Computer choice: {computer_choice}')
    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print('You win!')
            score += 1
        else:
            print('You lose!')
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print('You win!')
            score += 1
        else:
            print('You lose!')
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print('You win!')
            score += 1
        else:
            print('You lose!')
    print(f'Score: {score}')
    print('Do you want to play again? (yes/no)')
    play_again = input().lower()
    if play_again == 'no':
        break
print(f'Your final score: {score}')
