def triangle_area(base, height):
  area =(0.5)*(base*height)
  return area

print(triangle_area(3,4))#would return 6 and print to console
print(triangle_area(8,11)) #would return 44 and print to console


#Start of LAB
#dictionary food ====key : value

#food = {"beef":1.00, "cheese":1.99, "pasta":0.90}
#def total_price(food1, food2):
  #print(food["beef"])
  #total = food[food1] + food[food2]
  #return total

#goodToGo = True
#while (goodToGo):
    #input1 = input("pls give us a food")
    #if (input1 in food):
        #input2 = input("give us a 2nd food")
    #else:
          #goodToGo = fALSE
    #if (input2 in food):
            #print ("the Total price is", total_price("pasta", "cheese"))
            #else:
            #goodToGo = False

#StepIV
#shoeInv = {"Jordan13": 10, "Yeezy": 80, "Foamposite": 10, "Airmax": 5, "SB Dunk":20}
#print(shoeInv["SB Dunk"])

#def clearanceSale(d, updater):
  #d1 = {"Jordan13": d["Jordan13"] /updater }
  #shoeInv.update("Jordan13", shoeInv["Jordan13"] /updater)
  #d.update( d1)

 
  #d2 = {"Yeezy": d["Yeezy"] /updater }
  #d.update( d2)
  #(shoeInv["Foamposite"] /updater)
  #d3 = {"Foamposite": d["Foamposite"] /updater }
  #d.update( d3)
  #(shoeInv["Airmax"] /updater)
  #d4 = {"Airmax": d["Airmax"] /updater }
  #d.update( d4)
  #(shoeInv["SB Dunk"] /updater)
  #d5 = {"SB Dunk": d["SB Dunk"] /updater }
  #d.update( d5)

  #return (d)

#print(clearanceSale(shoeInv,5)) #answer = 4

#STepVI
nba_player = {"Curry" : 30, "Lebron": 23, "Duran": 7, "Oubre": 12, "Harden": 13}

def largestJerseyNumber(nba_player) :  
    largestjerseyNum = 0

    for x in range(5):
    #if (nba_player["Curry"]) > (nba_player["Lebron"] ):
    print("x is", x)

    print( nba_player["Curry"])
    if (nba_player["Curry"]) > (nba_player["Lebron"] ):
        largestjerseyNum = nba_player["Curry"]

    if (nba_player["Curry"]) > (nba_player["Lebron"] ):
        largestjerseyNum = nba_player["Curry"]
      else:
            largestjerseyNum = nba_player["Duran"]

    print (largestjerseyNum)
  #read in 1sr jersey number, 


  #compare to 2nd jersey number
  #if 1st > 2nd
  #largest = 1st


