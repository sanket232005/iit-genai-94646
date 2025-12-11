number = input("Enter Number Sepereted by commas : ")
num =[int(x) for x in number.split(",")]
print(num)

even = 0
odd = 0
for n in num:
    if n % 2 == 0:
        even += 1
    else :
        odd += 1

print("Even Number :", even)        
print("Odd Number :", odd)        
