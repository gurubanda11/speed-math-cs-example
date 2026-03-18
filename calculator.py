
calulation= input("which calculation do you want to do? (1. add, 2. subtract, 3. multiply, 4. divide): ")
firstinput= input("enter a number: ")
secondinput= input("enter another number: ")

if calulation == "add" or calulation == "1":
    print(float(firstinput) + float(secondinput))
elif calulation == "subtract" or calulation == "2":
    print(float(firstinput) - float(secondinput)) 
elif calulation == "multiply"or calulation == "3":
    print(float(firstinput) * float(secondinput))
elif calulation == "divide" or calulation == "4":
    print (float(firstinput) / float(secondinput))
elif secondinput  == "0" and calulation == "divide" or calulation == "4":
    print("Undefined")