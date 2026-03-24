''' 
    CS2100
    A little starter code 
    Sample code from lecture
    1/8/26

    Some notes for what we added:
        Conversion math got moved into functions, that way we can convert multiple things, code can be reused!
        We always write a docstring for every function and at the top of every file

        round(xx, 2) -- a float XX, and a # of decimal places to round to
        
        CONSTANT -- varialbe named in ALL_CAPS, never change these
        
        validate user input -- use a while loop to re-prompt until they enter the right thing
        
        what can this data type do? -- in Python interactive mode, try help(str) 
        
        string methods -- 
            "hello".upper() returns HELLO
            "he!!o".replace("!", "") retuerns heo
            "43".isdecimal() returns true
        
        Conditionals: if/elif/else
            Handy shortcut: x = y if condition else z
                            (if condition is true, then x = y. Otherwise, x = z)

        What might we do next?
        Test the functions and make sure they work!
'''

CEL_COLD_THRESHOLD = 4
CEL_HOT_THRESHOLD = 30

def fahr_to_cel(fahr: float) -> float:
    ''' convert given fahrenheit temp to celsius
        parameters:
            fahr (float) - starting temp in fahr
        returns:
            float - ending tmp in celsius
    '''
    cel = (fahr - 32) * (5 / 9)
    return cel

def cel_to_fahr(cel: float) -> float:
    ''' convert given celsius to fahrenheit 
        parameters:
            cel (float), the starting temp in degrees celsius
        returns:
            float, the converted temp in degrees fahrenheit
    '''
    fahr = cel * (9 / 5) + 32
    return fahr

def main() -> None:
    ''' temperature conversion program
        prompt user for what unit to start with, F or C, validating it's one of the two
        prompt user for what the starting temp is, validate it's a decimal for conversion
        convert from F to C, or C to F, and report the result
       '''

    start_unit = input("What unit to start with F or C?\n")
    start_unit = start_unit.upper()
    while start_unit != "F" and start_unit != "C":
        start_unit = input("Must be F or C, please enter again.\n").upper()

    temp_str = input(f"What is the temp in {start_unit}?\n")
    while not temp_str.replace(".", "").isdecimal():
        temp_str = input("That needs to be a number, try again please\n")
    temp_start = float(temp_str)

    if start_unit == "F":
        temp_converted = fahr_to_cel(temp_start)
    else:
        temp_converted = cel_to_fahr(temp_start)

    # report converted temp to the user, along with some hot/cold commentary
    print(f"That is {round(temp_converted, 2)} in {'C' if start_unit == 'F' else 'F'}!")
    hot = temp_start >= CEL_HOT_THRESHOLD if start_unit == "C" else \
          temp_converted >= CEL_HOT_THRESHOLD
    cold = temp_start <= CEL_COLD_THRESHOLD if start_unit == "C" else \
          temp_converted <= CEL_COLD_THRESHOLD
    if cold:
        print("brrrrr! Put on a jacket :(")
    elif hot:
        print("whew!!! T-shirt and short day :(")
    else:
        print("...comfy :)")

if __name__ == "__main__":
    main()
