def triangle_area(base, height):
  area =(0.5)*(base*height)
  return area

print(triangle_area(3,4))#would return 6 and print to console
print(triangle_area(8,11)) #would return 44 and print to console


#Start of LAB
#dictionary food ====key : value

food = {"beef":1.00, "cheese":1.99, "pasta":0.90}
def total_price(food1, food2):
  print(food["beef"])
  total = food[food1] + food[food2]
  return total

goodToGo = True
while (goodToGo):
    input1 = input("pls give us a food")
    if (input1 in food):
        input2 = input("give us a 2nd food")
    else:
          goodToGo = fALSE
    if (input2 in food):
            print ("the Total price is", total_price("pasta", "cheese"))
    else:
            goodToGo = False

#StepIV
shoeInv = {"Jordan13": 1, "Yeezy": 8, "Foamposite": 10, "Airmax": 5, "SB Dunk":20}
print(shoeInv["SB Dunk"])
