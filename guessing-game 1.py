#Guess the Secret Number 
#Done in Python 3
#originally written in Nov. 2018



secret = 1 #the secret number is previously selected
#User inserts a number to guess between 0 and 9
guess = int(input("Please type your guess number between 0 and 9: "))
print ("your guess is")
print (guess)


if secret == guess: #We compare the guess and the secret number only allowing the user to type numbers between 0 and 9
    print ("You have guessed the Number!! Congratulations.")
elif guess < 0:
    print ("Please choose a number between 0 and 9")
elif guess > 9:
    print ("Please choose a number between 0 and 9")
else:
    print ("Sorry, wrong guess. Try again.")
