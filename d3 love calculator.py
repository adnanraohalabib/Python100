name1 = input("What's your name? \n")
name2 = input("What's your partner's name? \n")
name = name1+name2
first_digit, second_digit = 0, 0
for char in name.lower():
    if char in "true":
        first_digit +=1
    if char in "love":
        second_digit += 1

print(f"\n\nCongratulations ! You are {first_digit}{second_digit}% matched with {name2}!!")
