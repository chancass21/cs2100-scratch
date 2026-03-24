'''
    Starter code for class on 3/9/26

    We have a Donut class and a PremiumDonut(Donut) class

    In the driver, we'll...
    * Call the class method get_menu() to see what flavors there are
    * Call the static method is_valid_code() to validate our coupon
    * create a donut using init
    * create a donut using the class method from_menu
    * create a premium donut using init
    * create a premium donut using the class method from_menu
    * compare what happens with _type and class vs static in super vs sub class
'''


from lec21_start import Donut, PremiumDonut

def main() -> None:
    ''' make some donuts '''

    # What's in the menu? Call the Donut class's class method get_menu
    print("======What are possible flavors?======")
    print(Donut.get_menu())
    print(PremiumDonut.get_menu())

    # Is my coupon code valid? Call the Donut class's static method is_valid_code
    print("\n======Is DONUT20 a valid coupon code?======")
    code = "DONUT20"
    print("Yes!" if Donut.is_valid_code(code) else "No :(")

    # Make two donut objects, one from regular init and one from class method from_menu
    print("\n======Two donuts, two ways======")
    d1 = Donut("jelly", 1.39)
    d2 = Donut.from_menu(0, 1.89)
    print(d1, d2)

    # Make two premium donuts, one from regular init and one from class method from_menu
    # (which flavors are used??)
    print("\n======Making premium donuts!======")
    pd1 = PremiumDonut("pride vanilla", 4.99)
    pd2 = PremiumDonut.from_menu(2, 3.99)
    print(pd1, pd2)

    # can I call a donut static method from premium donut?
    print("\n======Is DONUT20 a valid coupon code?======")
    code = "DONUT20"
    # print("Yes!" if PremiumDonut.is_valid_code(code) else "No :(")

    # showing the types w/inheritance and class method vs static method
    print("\n======Are you a donut or a PREMIUM donut?======")
    print(f"Asking Donut, class... {Donut.my_type_cls()}")
    print(f"Asking Donut, static... {Donut.my_type_static()}")
    print(f"Asking Premium, class... {PremiumDonut.my_type_cls()}")
    print(f"Asking Premium, static... {PremiumDonut.my_type_static()}")

    # can i make a list of donuts?
    # can i make a set of donuts? (Possible cliffhanger for next time?)!
    donut_list = [d1, d2, pd1, pd2]
    print([str(d) for d in donut_list])

    # can't make a set, or a dictionary :( Wednesday we'll talk about why
    # error message: unhashable!
    #donut_dict = {d1 : "yum", d2: "also good", pd1 : "delicious"}
    #donut_set = {d1, d2, pd1, pd2}


if __name__ == "__main__":
    main()
