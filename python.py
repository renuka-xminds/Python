print('Hello world')

a = 10
b = 5
print(a+b)
print(a-b)
print(a%b)
print(a*b)

#Sum of first N natural numbers using while loop
number = int(input("Enter a number: "))
sum = 0
i = 1
while i <= number:
    sum = sum+i
    i +=1

print(sum)

"""Input mark of a student in 5 subject and print the total mark and grade of the student
avg is greater than 90 the A grade
avg>=80 B grade
avg>=70 grade C
avg>=60 grade D
otherwise grade F"""

mark = int(input("enter the mark: "))
avg = mark/5
if avg > 90:
    print("Grade A" , mark)
elif avg >= 80:
    print("Grade B" , mark)
elif avg >= 70:
    print("Grade C" , mark)
elif avg >= 60:
    print("Grade D" , mark)
else:
    print("Failed")



#Define a calculator using match-case

firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

operation = input("Enter the operation: ")

match operation:
    case '+':
        print(firstNumber+secondNumber)

    case '-':
        print(firstNumber-secondNumber)
    
    case '*':
        print(firstNumber*secondNumber)
    
    case '/':
        print(firstNumber/secondNumber)


"""1.Create a list containing marks of a student
Find the total and average of marks
 Find the maximum mark"""

sum = 0
mark = [32.5, 33.0, 31.8, 2]
for i in mark:
    sum = sum + i
#sum and average of mark
print("sum of mark =", sum)
print("average of mark =", sum/len(mark))

#descending order
mark.sort(reverse=True)
print(mark)

#highest 3 marks
print(mark[0:3])

"""Next create a todo list
Add new task
remove task
insert a task in a position"""

todoList = ["log check", "testing"]
print(todoList)
#adding item
todoList.append("bug fixing")
print(todoList)
#removing item
todoList.remove("testing")
print(todoList)

#adding testing after bug fixing

todoList.insert(2, "testing")
print(todoList)









