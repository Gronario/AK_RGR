from Lathe import *

def main():

    while True:

        # --------------------------------------------------- input+input error detection --------------------------------------

        while True:

            print(
                "\nHi user, first indicate a material for your detail.\nAvailable material are: aluminum, copper, steel.")
            a = input("\nMaterial:")

            lookfor = re.compile("aluminum|copper|steel")
            res = re.match(lookfor, a)

            if res == None:
                print("\n\tWrong value. Reenter the value correctly")
                continue

            else:
                break

        while True:

            print("\nIndicate a type of the drawing.\nAvailable drawings are: engine, bearing, flange.")
            b = input("\ndrawing:")

            lookforb = re.compile("engine|bearing|flange")
            resb = re.match(lookforb, b)

            if resb == None:
                print("\n\tWrong value. Reenter the value correctly")
                continue

            else:
                break

        while True:

            print("\nIndicate a detail length in mm.")
            c = input("\ndetail length:")

            lookforc = re.compile("\d+")
            resc = re.match(lookforc, c)

            if resc == None:
                print("\n\tWrong value. Reenter the value correctly")
                continue

            else:
                break

        while True:

            print("\nIndicate a detail width in mm.")
            d = input("\ndetail width:")

            lookford = re.compile("\d+")
            resd = re.match(lookforc, d)

            if resd == None:
                print("\n\tWrong value. Reenter the value correctly")
                continue

            else:
                break

        while True:

            print("\nIndicate a detail height in mm.")
            e = input("\ndetail width:")

            lookfore = re.compile("\d+")
            rese = re.match(lookforc, e)

            if rese == None:
                print("\n\tWrong value. Reenter the value correctly")
                continue

            else:
                break

        order = LatheDetail(a, b, c, d, e)
        order.weight()
        order.display_info()
        order.price()

        stop=input("Press Enter to exit the program or press 0 to start program again: ")
        if stop == "0":
            break

main()

