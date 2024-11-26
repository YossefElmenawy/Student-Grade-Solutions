import random
words = ["coding","apple","movie","orange"]
word = random.choice(words)
letters = list(word)
# print(letters)
random.shuffle(letters)
# print(letters)
scrambled_words = "".join(letters)
print("scrambled word is : ",scrambled_words)
attempts = 5
while attempts > 0:
    guess = input(f"enter the word, (you have onle {attempts} attempts): ")
    if guess.lower() == word.lower():
        print("Right amswer!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Wrong answer, please try again!")
        else:
            print("you have lost, the word was",word)    
