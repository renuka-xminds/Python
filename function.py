#1.Write a function to calculate the power of a number raised to another number using recursion

def powerOfNumber(num, exponent):
    if exponent == 0:
        return 1
    
    return num*powerOfNumber(num, exponent-1)


num = int(input("Enter the number: "))
exponent = int(input("Enter the Exponent: "))
print(powerOfNumber(num,exponent))

#2.Print multiplication table of a given number using recursion.

def multiplicationNumber(num, i=1):
    if i <= 10:
        result = num*i
        print(  result)
        multiplicationNumber(num, i+1)


num = int(input("Enter the number: "))
multiplicationNumber(num)

#3.Write a function student_data() which will print student id,name,class,avg of marks using variable length keyword arguments.

def student_data(**data):
    for key, value in data.items():
        print(f"{key}: {value}")


student_data(student_id = 1, name="renuka", std=5, averageMark=50)