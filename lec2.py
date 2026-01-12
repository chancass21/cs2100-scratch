'''
CS2100
A little starter code
Sample code from lecture
1/8/26
'''

def fahr_to_cell(fahr: float) -> float:
    '''converts fahrennheit to celsius'''
    cell = (fahr - 32) * (5 / 9)
    return cell

CEL_COLD_THRESHOLD = 4
CEL_HOT_THRESHOLD = 36

def main() -> None:
    ''' prompt for temp in fahrenheit, convert to celsius and report '''
    temp_fahr = input("What is the temperature in degrees Fahrenheit?\n")
    
    while not temp_fahr.isdecimal():
        temp_fahr = input("That needs to be a number, try again please.\n")
    
    temp_fahr = float(temp_fahr)
    temp_celsius = fahr_to_cell(temp_fahr)
    print(f"That is {round(temp_celsius, 2)} in celsius!")

    if temp_celsius <= CEL_COLD_THRESHOLD:
        print("brrrrrrrrrr \n")
    elif temp_celsius >= CEL_HOT_THRESHOLD:
        print("whew!\n")
    else:
        print("hot! \n")
