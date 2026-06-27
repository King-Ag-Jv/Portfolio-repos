# Debugging

import time

print("Ageng Super Market")
print()
print("Enter the date: ")
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

while True:
    try:
        monthcurrent = int(input("Month: "))
        while monthcurrent>12:
            print("U typed more than 12, there's 12 months a year...")
            monthcurrent = int(input("Month: "))
        break
    except ValueError:
        print("Please enter it again...")

month_a = month[monthcurrent-1]
print()
print("Month entered: ")
print(month_a)
print()
    
while True:
    try:
        datecurrent = int(input("Date: "))
        while (datecurrent <= 0) or (datecurrent >= 33):
            datecurrent = input("the date entered was out of range of the exact date, please enter it again\nDate: ")
        if (month_a == month[0]) or (month_a == month[2]) or (month_a == month[4]) or (month_a == month[6]) or (month_a == month[7]) or (month_a == month[9]) or (month_a == month[11]):
            while datecurrent >= 32:
                print("The month you have entered was", month_a, ". The date entered was more than 31, please enter it again")
                datecurrent = int(input("Date: "))
        else:
            if (month_a == month[3]) or (month_a == month[5]) or (month_a == month[8]) or (month_a == month[10]):
                while datecurrent >= 31:
                    print("The month you have entered was", month_a, ". The date entered was more than 30, please enter it again")
                    datecurrent = int(input("Date: "))
            else:
                        if month_a == month[1]:
                            while datecurrent >= 30:
                                print("The date you have entered was", month_a, ". The date entered was more than 29, please enter it again")
                                datecurrent = int(input("Date: "))
        break
    except ValueError:
        print("Please enter it again...")
        
    

strdate = str(datecurrent)

if (datecurrent in range(1,11)) or (datecurrent >= 20):
    if strdate[-1] == '1':
        date_last = strdate + "st"
    else:
        if strdate[-1] == '2':
            date_last = strdate + "nd"
        else:
            if strdate[-1] == '3':
                date_last = strdate + "rd"
            else:
                date_last = strdate + "th"
else:
  if datecurrent in range(11,20):
      date_last = strdate + "th"
      
while True:
    try:
        yearcrnt = int(input("Year: "))
        while (yearcrnt < 1400) or (yearcrnt > 2200):
            print("u've entered out of the range, please enter it again")
            yearcrnt = int(input("Year: "))
        break
    
    except ValueError:
        print(f"Please enter it again.")
        
str_yearcrnt = str(yearcrnt)
crntdate = " ".join([date_last, month_a, str_yearcrnt])
print("\ncurrent date:", crntdate)

time.sleep(0.8)
print()
print()
time.sleep(0.8)
for j in range(1,61):
    print("-", end="")
    if j == 60:
        print()

print()
# shopping list:

currency = "USD"


shopping = {    "Egg":2,
                "Rice":30,
                "Flour":4,
                "Milk":5,
                "Detergent":5,
                "Salt":2,   
                "Water Bottle": 4,  
}


# ITEMS LISTS:
Items = ("Egg",
         "Rice",
         "Flour",
         "Milk",
         "Detergent",
         "Salt",
         "Water Bottle:")

vegg = "Egg"
vrice = "Rice" # discount 10%
vflour = "Flour"
vmilk = "Milk"
vdetergent = "Detergent"
vsalt = "Salt"

    # discounts: rice = 10%
    
# 1st item list:
"""
writeitems = f"Items:\n{vegg} = {shopping[vegg]} {currency}\n{vrice} = {shopping[vrice]} {currency}\n{vflour} = {shopping[vflour]} {currency}\n{vmilk} = {shopping[vmilk]} {currency}\n{vdetergent} = {shopping[vdetergent]} {currency}\n{vsalt} = {shopping[vsalt]} {currency} \n\n"

time.sleep(0.8)
print(writeitems)
"""

# 2nd item list:
"""
print("Items:")
for j in range(0, len(Items)):
    print(f"{Items[j]} = {shopping[Items[j]]} {currency}")
"""

# 3rd item list:
print("Items:")
for j in range(0, len(Items)):
    print(f"{j + 1}. {Items[j]}", end="")
    countchar = len(Items[j])
    countindent = 12 - countchar
    for l in range(0, countindent):
        if (l > 0) and (l < countindent):
            print(" ", end="")
        if (l == countindent - 1):
            print(f"= {shopping[Items[j]]} {currency}", end="")
    print()
        
print("\n")
    # Making the operation in cashier:
    # Calculating the results of dis thing...
    
# make a function to calculate the items:



def main_cashier():

    cashier_bool = True
    true_false = str()
    texti = "Item:"
    buying_list = dict()
    item_bought = list()
    i = 0

    while cashier_bool:
    
        gud = None
        order_number = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"]
        item_order = order_number[i] + " " + texti
        
        if i == 6:
            cashier_bool = False
            print("You have already input too many things in here!!! (jk :D:D)\n\n")
            
            
            
    # Input the items:
        gud = str(input(f"{order_number[i]}\n\nNote: the items cannot written twice that also change the value of quantity of the item:...\nEnter the {item_order} "))
        
        """
        while (gud != Items[0]) and (gud != Items[1]) and (gud != Items[2]) and (gud != Items[3]) and (gud != Items[4]) and (gud != Items[5]):
            print(f"The item you input was '{gud}', please enter correctly or i will kill u :-(")
            del gud
            gud = input(f"Enter the {item_order}: ")
        """
        correction = 0
        while True:
            if (gud.capitalize() == Items[correction]):
                break
            else:
                correction = correction + 1
                if correction > len(Items) - 1:
                    print(f"The item you input was '{gud}', please enter correctly or I will kill u :-(")
                    del gud
                    gud = input(f"Enter the {item_order}: ")
                    correction = 0

        gud = gud.capitalize()
        while True:
            try:
                quantity = int(input("Enter the items quantity: "))
                if (quantity <= 0) or (quantity > 99):
                    while True:
                        try:
                            print("You entered too low or too high, Please enter it again or u die...")
                            del quantity
                            quantity = input("Enter the items quantity: ")
                            break
                        except ValueError:
                                print("Please enter the quantities again... : ")
                
                break
            except ValueError:
                print("There was an error occured, please enter it again...")
            
        
        if (gud != None) and (quantity != None):
            buying_list.update({gud: quantity})
            item_bought.append(gud)
            del gud
            del quantity
    
        if len(buying_list) == i + 1:
            i = i + 1
        
        
    # Making the cashier more complexcities :)
    
        true_false = input("Do you want to continue to insert the items again? (Type anything if yes, otherwise type 'No' or 'no' to stop)\n")
        if (true_false == "No") or (true_false == "no") or (true_false == "NO"):
            cashier_bool = False
        elif (true_false == "Yes") or (true_false == "yes") or (true_false == "YES"):
            cashier_bool = True
        else:
            wek = True
            while wek:
                true_false = input("wat u doing?\n")
                if (true_false == "YES") or (true_false == "Yes") or(true_false == "yes") or (true_false == "NO") or (true_false == "No") or (true_false == "no"):
                    wek = False
                
        print("\n")

    if cashier_bool == False:
        
        disc_list = []
        discstring_list = []
        item_costs_list = []
        

        # checking the items that has discount

        def find_discount(item_discount):
            match item_discount:
                case "Rice": return 10/100
                case "Pill": return 995/1000
                case _: return 0
                
                
        def discount_string(discstring):
            match discstring:                    
                case 0.1: return "10%"
                case 0.995: return "99.5%"
                case _: return "0%"

        print("List of items entered:")
        for j in range(0, i): 
            

            var_disc = find_discount(item_bought[j])
        
            disc_list.append(var_disc)
            discstring_list.append(discount_string(var_disc))
            
            
            # calculate the results:
            item_costs = (1 - disc_list[j])*(buying_list[item_bought[j]]*shopping[item_bought[j]])
            item_costs_list.append(item_costs)
            
            
            indent = " "*3
            str_j = str(j+1)
            str_one_item_cost = str(shopping[item_bought[j]])
            str_quantityofitem = str(buying_list[item_bought[j]])
            str_item_costs = str(item_costs_list[j])
            
            print(indent.join([f"{str_j}. {item_bought[j]} ({str_one_item_cost} {currency}) : {str_quantityofitem} (Quantities).\n", f"Total: {str_one_item_cost} x {str_quantityofitem} - discount ({discstring_list[j]}) = {str_item_costs} {currency}"]))
            time.sleep(1)
        
        
        # prefix the list in item_costs_list that are missing to make the return function can return an output
        # make a variable named k with integer value '5'
        k = len(shopping) - 1
        item_missing = k + 1 - i
        
        # making zero value if it has no input named 'zl'
        blank_value = [0]
        
        if i <= 5:
            item_costs_list[(k - item_missing + 1):k] = blank_value*item_missing
                        

    return (sum(item_costs_list[0:k]))


# Resulting the end of the cashier
total = main_cashier() # this also call the function as the result of the cashier goods

time.sleep(0.9)
print()
for k in range(1, 71):
    print("~", end="")
    if k == 70:
        print("\n")

print("The date of customer entered: {}\nThe total in the cashier is: {} {}".format(crntdate, total, currency))

input("\n\nEnter anything to continue...\n")
time.sleep(0.9)
print("\n")
for j in range(1, 71):
    print("-", end="")
    if j == 70:
        print("\n")

time.sleep(1.2)
line = 70
wawa = ["...THANKS...", "...FOR...", "...ENTER TO OUR CASHIER...", "   ^_^   "]
for i in wawa:
    sentence_count = line - len(i)
    if sentence_count % 2 == 1:
        text_rounding = sentence_count + 1
    else:
        text_rounding = sentence_count
    for j in range(0, text_rounding):
        print("~", end="")
        if j == text_rounding/2:
            print(i, end="")
    print()
