import math
import re

class LatheDetail:

    def __init__(self ,material, drawing , detail_length, width ,height):

        self.material           = material
        self.drawing            = drawing
        self.detail_length      = detail_length
        self.width              = width
        self.height             = height


    def weight(self): #detai weight calculation

        list_of_keys1 = ["aluminum", "copper", "steel"]
        list_of_values1 = [2.6989, 8.92, 7.8]
        d1 = dict(zip(list_of_keys1, list_of_values1))
        material_density = d1.get(self.material)
        mat_weight = math.ceil(int(self.detail_length)*int(self.width)*int(self.height)/1000*material_density/1000)
        return mat_weight

    def price(self): #price calculation

        list_of_keys = ["aluminum", "copper", "steel","engine","bearing","flange"]
        list_of_values = [100, 500, 200,3,1,1.5]
        d = dict(zip(list_of_keys, list_of_values)) # making a dictionary from material type and its price for 1 kg and work complexity
        material_price_for_1_kg = d.get(self.material)
        work_complexity = d.get(self.drawing)
        final_price = material_price_for_1_kg*self.weight()*work_complexity
        return material_price_for_1_kg, work_complexity,final_price


    def display_info(self): #display all the information about the order< that customer had already made and price display
        print("\nInfo about order:\n")
        print("\tMaterial:",self.material, "\n\tMaterial price for 1 kg: " ,"₴",self.price()[0],
              "\n\tMaterial weight: ",self.weight(),"kg""\n\tDrawing: " ,self.drawing,"\n\tPrice multiplier: ",self.price()[1])
        print("\nPrice:")
        print("\t","₴",self.price()[2])


#--------------------------------------------------- input+input error detection --------------------------------------

while True:

    print("\nHi user, first indicate a material for your detail.\nAvailable material are: aluminum, copper, steel.")
    a=input("\nMaterial:")

    lookfor = re.compile("aluminum|copper|steel")
    res = re.match(lookfor, a)

    if res == None:
        print("\n\tWrong value. Reenter the value correctly")
        continue

    else:
        break

while True:

    print("\nIndicate a type of the drawing.\nAvailable drawings are: engine, bearing, flange.")
    b=input("\ndrawing:")

    lookforb = re.compile("engine|bearing|flange")
    resb = re.match(lookforb, b)

    if resb == None:
        print("\n\tWrong value. Reenter the value correctly")
        continue

    else:
        break

while True:

    print("\nIndicate a detail length in mm.")
    c=input("\ndetail length:")

    lookforc = re.compile("\d+")
    resc = re.match(lookforc, c)

    if resc == None:
        print("\n\tWrong value. Reenter the value correctly")
        continue

    else:
        break

while True:

    print("\nIndicate a detail width in mm.")
    d=input("\ndetail width:")

    lookford = re.compile("\d+")
    resd = re.match(lookforc, d)

    if resd == None:
        print("\n\tWrong value. Reenter the value correctly")
        continue

    else:
        break

while True:

    print("\nIndicate a detail width in mm.")
    e=input("\ndetail width:")

    lookfore = re.compile("\d+")
    rese = re.match(lookforc, e)

    if rese == None:
        print("\n\tWrong value. Reenter the value correctly")
        continue

    else:
        break

order = LatheDetail(a,b,c,d,e)
order.weight()
order.display_info()
order.price()