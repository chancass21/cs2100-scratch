''' 
    CS2100
    A little starter code 
    Sample code from lecture
    1/8/26
'''

def main() -> None:
    ''' prompt for temp in fahrenheit, convert to celsius and report '''

    temp_fahr = float(input("What is the temperature in degrees Fahrenheit?\n"))
    temp_celsius = (temp_fahr - 32) * (5 / 9)
    print(f"That is {temp_celsius} in celsius!")

if __name__ == "__main__":
    main()
