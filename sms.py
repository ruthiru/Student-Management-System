
c_pass = c_defer = c_fail = 0
credit_range = [0, 20, 40, 60, 80, 100, 120]


def credit_pass():
    global c_pass
    try:
        c_pass = int(input("Please enter your credits at pass: "))
    except ValueError:
        print("Integer required")
        credit_pass()
    else:
        if c_pass not in credit_range:
            print("Out of range")
            credit_pass()


def credit_defer():
    global c_defer
    try:
        c_defer = int(input("Please enter your credits at defer: "))
    except ValueError:
        print("Integer required")
        credit_defer()
    else:
        if c_defer not in credit_range:
            print("Out of range")
            credit_defer()


def credit_fail():
    global c_fail
    try:
        c_fail = int(input("Please enter your credits at fail: "))
    except ValueError:
        print("Integer required")
        credit_fail()
    else:
        if c_fail not in credit_range:
            print("Out of range")
            credit_fail()


def total():
    credit_pass()
    credit_defer()
    credit_fail()

    if 120 != (c_pass + c_defer + c_fail):
        print("Total incorrect")
        total()


Next_student = True
Pro = Tra = Ret = Exc = 0
List = [[], [], [], []]

while True:
    global y
    y=int(input("Enter number '1' for Student login,Enter number '2' for Staff login : "))
    if y==1:
        print("--Student Version--")
        break
    elif y==2:
        print("--Staff Version--")
        break
    while y not in [1,2]:
        print("invalid Data\n")
        y=int(input("Enter number '1' for Student login,Enter number '2' for Staff login : "))
        







while Next_student:
    total()
    if c_pass == 120:
        print("Progression Outcome:Progress")
        Pro = Pro + 1
        List[0].append([c_pass, c_defer, c_fail])
    elif c_pass == 100:
        print("Progression Outcome:Progress (module trailer)")
        Tra = Tra + 1
        List[1].append([c_pass, c_defer, c_fail])
    elif 60 <= (c_pass + c_defer):
        print("Progression Outcome: Do not Progress - module retriever")
        Ret = Ret + 1
        List[2].append([c_pass, c_defer, c_fail])
    else:
        print("Progression Outcome: Exclude")
        Exc = Exc + 1
        List[3].append([c_pass, c_defer, c_fail])
        
    if y == "staff":
            


        x = input("Would you like to enter another set of data?\n"
            " Enter 'y' for yes or 'q' to quit and view results:")

        while x.lower() not in ["y", "q"]:
           print("invalid Data")
        x = input("Would you like to enter another set of data?\n"
                " Enter 'y' for yes or 'q' to quit and view results:")

        

        if x.lower() == "q":

            print("-" * 50, "\nHistogram")
            print("Progress   ", Pro, ":", "*" * Pro)
            print("Trailer    ", Tra, ":", "*" * Tra)
            print("Retriever  ", Ret, ":", "*" * Ret)
            print("Excluded   ", Exc, ":", "*" * Exc)
            print("Outcome in total", "\n", "_" * 50)

            f = open("pyth_cw.txt", "w")
            for i in List:
                for z in i:
                    if i == List[0]:
                        print("progress -", z[0], ",", z[1], ",", z[2])
                        f.write("progress - " + str(z[0]) + "," + str(z[1]) + "," + str(z[2]) + "\n")
                    elif i == List[1]:
                        print("Progress (module trailer) -", z[0], ",", z[1], ",", z[2])
                        f.write("Progress (module trailer) - " + str(z[0]) + "," + str(z[1]) + "," + str(z[2]) + "\n")
                    elif i == List[2]:
                        print("Module Retriever -", z[0], ",", z[1], ",", z[2])
                        f.write("Module Retriever - " + str(z[0]) + "," + str(z[1]) + "," + str(z[2]) + "\n")
                    elif i == List[3]:
                        print("Exclude -", z[0], ",", z[1], ",", z[2])
                        f.write("Exclude - " + str(z[0]) + "," + str(z[1]) + "," + str(z[2]) + "\n")
            f.close()
            
            break
    
    







