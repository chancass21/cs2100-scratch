'''
    Finished code from class on 3/11/26

    We have a Donut class and a PremiumDonut(Donut) class

    We added a few things to the driver that didn't work,
    until we went back and fixed up the class:
    * sort a list of Donut objects (before we fixed it: TypeError, no < implemented)
    * put Donut objects in a set, or as keys of a dictionary (before we fixed it:
                                unhashable error)
    * make a BagOfDonuts container object, and iterate over it

'''

from lec22 import Donut, PremiumDonut, BagOfDonuts

def main() -> None:
    ''' make some donuts and see what happens '''

    # What's in the menu? Call the Donut class's class method get_menu
    print("======What are possible flavors?======")
    print(Donut.get_menu())

    # Is my coupon code valid? Call the Donut class's static method is_valid_code
    print("\n======Is DONUT20 a valid coupon code?======")
    code = "DONUT20"
    print("Yes!" if Donut.is_valid_code(code) else "no :(")

    # Make two donut objects, one from regular init and one from class method from_menu
    print("\n======Two donuts, two ways======")
    d1 = Donut("glazed", 1.39)
    d2 = Donut.from_menu(1, 1.19)
    print(d1, d2)

    # Make two premium donuts, one from regular init and one from class method from_menu
    # (which flavors are used??)
    print("\n======Making premium donuts!======")
    print(PremiumDonut.get_menu())
    pd1 = PremiumDonut("pride vanilla", 2.99)
    pd2 = PremiumDonut.from_menu(2, 4.99)
    print(pd1, pd2)

    # can I call a donut static method from premium donut?
    print("\n======Is DONUT20 a valid coupon code?======")
    code = "DONUT20"
    print("Yes!" if PremiumDonut.is_valid_code(code) else "No :(")

    # showing the types w/inheritance and class method vs static method
    print("\n======Are you a donut or a PREMIUM donut?======")
    print(f"Asking Donut, class... {Donut.get_type_class()}")
    print(f"Asking Donut, static... {Donut.get_type_static()}")
    print(f"Asking Premium, class... {PremiumDonut.get_type_class()}")
    print(f"Asking Premium, static... {PremiumDonut.get_type_static()}")

    # can i make a list of donuts?
    # can i make a set of donuts? (Possible cliffhanger for next time?)!
    print("\n======Printing a list of donuts======")
    donut_list = [d1, d2, pd2, pd1]
    print([str(d) for d in donut_list])

    print("\n======Can I sort my list of donuts?======")
    sorted_donuts = sorted(donut_list)
    print([str(d) for d in sorted_donuts])

    print("\n======Can I make a set/dictionary of donuts?======")
    donut_set = {d1, d2, pd1, pd2}
    donut_dict = {d1 : "yum", d2 : "also good"}
    print("\nHere are the donuts int he set")
    for d in donut_set:
        print(d)
    print("\nHere are the donuts in the dictionary")
    for key, value in donut_dict.items():
        print(f"{key}...{value}")

    # make a bag of donuts and iterate over it
    print("\n======Making a container BagOfDonuts and iterating======")
    mybag = BagOfDonuts({d1, d2, pd1, pd2})
    for donut in mybag:
        print(donut)
    print(f"That will be ${mybag.get_total_cost()} at the register please!")

if __name__ == "__main__":
    main()
