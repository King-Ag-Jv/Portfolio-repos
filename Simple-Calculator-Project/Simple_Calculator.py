# Function
import math

def math():
    print("Math testing (Not complete)")
    print("""Note: Enter the first number and operator in the order to calculate
        the result.
        
        Operation list:
        +   : Addition
        -   : Subtraction
        *   : Multiplication
        /   : Division
        ^   : Exponentiation
        
        Note in calculator:
        1. if you want to end the operation, you can type 'enter' after input two numbers with operation
        2. type 'undo' to reenter the number or operator for mistyped number
        3. type 'c' or 'C' to erase all of the number and operators
        4. if you want to square root or cubic root, you can type
        """)

    nlist = []
    oplist = []
    program = True
    calculator = True
    while program:
        while calculator:
            try:
                # Input the value of n
                n = input("Number -> ")
                n = float(n)
                nlist.append(n)
                
                # Enter the operator and whether type 'enter' then the program is
                # ended.
                op = input('Operator -> ')
                if op == "":
                    while True:
                        if len(oplist) >= 1:
                            calculator = False
                            break
                        elif (op == "+") or (op == "-") or (op == "*") or (op == "/") or (op == "^"):
                            break
                        else:
                            op = input("Error.\n")
                else:
                    while True:
                        if (op == "+") or (op == "-") or (op == "*") or (op == "/") or (op == "^"):
                            oplist.append(op)
                            break
                        else:
                            op = input("Wrong operation, please enter the operator again...\n")
            except ValueError:
                mis = True
                if n == "1/2":
                    n = 1/2
                elif n == "1/3":
                    n = 1/3
                else:
                    rooterror = "Not a square root or cubic root."
                    mis = False
                print("Syntax error: the number inputted was not a number.", end="")
                if mis == False:
                    print(rooterror)
                else:
                    print()
                
                
        def operation(calculating):
            strresult = eval(calculating)
            return strresult

        calculate = []
        for j in range(0, len(nlist), 1):
            calculate.append(str(nlist[j]))
            if j < len(nlist) - 1:
                if oplist[j] == "^":
                    calculate.append("**")
                else:
                    calculate.append(oplist[j])
            else:
                break
            

        numbertext = " ".join(calculate)
        result = operation(numbertext)
        print(result)
        while True:
            cont_program = input("Do you want to continue the calculator? y or n...")
            if cont_program.lower() == "y":
                print("Program reset.\n")
                calculator = True
                nlist = []
                oplist = []
                calculate = []
                break
            elif cont_program.lower() == "n":
                print("\nProgram has ended.\nThank you for using our calculator!")
                program = False
                break
            else:
                print("The word does not meet the statement...")
        
        
    return 0

if __name__ == "__main__":
    math()
