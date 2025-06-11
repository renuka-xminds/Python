Q1 = """ Is python is case sensitive ?
a. yes
b. no
"""

Q2 = """ Which of the following is not a key ?
a. eval
b. asset
c. local
"""


questions = { Q1:"a", Q2:"a"}

name = input("Enter your name: ")

print("hello" ,name)
score = 0
for i in questions:
    print(i)
    ans = input("choose the option: ")
    if ans == questions[i]:
        print("correct answer, you got 1 point")
        score = score + 1
        print("current score", score)
    else:
        print("You are wrong, you lost 1 point")
        score = score -1
        print("current score", score)

print("Final score is: ", score)