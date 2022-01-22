import random

words = ["book","tree","python","bag","cook","red","man","eeg"]

#i = random.randint(0, len(words)-1)
#word = words[i]

word = random.choice(words) #cloch
joon= 10

while joon > 0 :
    print('- ' * len(word)) # -----

    user_character = input() # s

    if user_character in word:
        print('yes')

    else:
        joon = joon -1
        print('No')

