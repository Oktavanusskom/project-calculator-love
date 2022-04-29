print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

joinName = name1 + " " + name2

t = joinName.lower().count("t")
r = joinName.lower().count("r")
u = joinName.lower().count("u")
e = joinName.lower().count("e")
true = t + r + u + e

l = joinName.lower().count("l")
o = joinName.lower().count("o")
v = joinName.lower().count("v")
e = joinName.lower().count("e")
love = l + o + v + e

loveScore = int(str(true) + str(love))

if loveScore < 10 or loveScore > 90:
  print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
  print(f"Your score is {loveScore}, you are alright together.")
else:
  print(f"Your score is {loveScore}.")
