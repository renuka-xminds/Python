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


