import random
control=[]
list = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
print("--------------Welcome to Tic-Tac-Toe---------------\n")

coords = {
    "A1":" ", "A2":" ","A3":" ",
    "B1":" ", "B2":" ","B3":" ",
    "C1":" ", "C2":" ","C3":" ",
}

print ("""
        A    B    C

  1       |    |   
      --------------
  2       |    | 
      --------------
  3       |    |   

""")

name = input ("Please Enter Your Name:")

print("Alright ",name,".If you're ready...")

while True:
    pick = input ("Pick a coordination: ")
    pick = pick.upper()
    coords[pick]= "X"
    if pick in control:
        print ("This coordination picked before\n")
        continue
    control.append(pick)
    while True:
        computer = random.choice(list)
        if computer in control:
            pass
        else:
            coords[computer] = "O"
            control.append(computer)
            break

    print("""
          A    B    C

      1    {} | {} | {}
         -------------
      2    {} | {} | {}
         -------------
      3    {} | {} | {}

    """.format(coords['A1'], coords['B1'], coords['C1'], coords['A2'], coords['B2'], coords['C2'], coords['A3'],
               coords['B3'], coords['C3']))

    if coords["A1"]=="X" and coords["A2"]=="X" and coords["A3"]=="X" or \
        coords["B1"] == "X" and coords["B2"] == "X" and coords["B3"] == "X" or \
        coords["C1"] == "X" and coords["C2"] == "X" and coords["C3"] == "X" or \
        coords["A1"]=="X" and coords["B1"]=="X" and coords["C1"]=="X" or \
        coords["A2"]=="X" and coords["B2"]=="X" and  coords["C2"]=="X" or \
        coords["A3"]=="X" and coords["B3"]=="X" and  coords["C3"]=="X" or \
        coords["A1"] == "X" and coords["B2"] == "X" and coords["C3"] == "X" or \
        coords["C1"] == "X" and coords["C2"] == "X" and coords["C3"] == "X" or \
        coords["C1"] == "X" and coords["B2"] == "X" and coords["A3"] == "X":
        print (name,"wins")
        break
    elif coords["A1"]=="O" and coords["A2"]=="O" and coords["A3"]=="O" or \
        coords["B1"] == "O" and coords["B2"] == "O" and coords["B3"] == "O" or \
        coords["C1"] == "O" and coords["C2"] == "O" and coords["C3"] == "O" or \
        coords["A1"]=="O" and coords["B1"]=="O" and coords["C1"]=="O" or \
        coords["A2"]=="O" and coords["B2"]=="O" and  coords["C2"]=="O" or \
        coords["A3"]=="O" and coords["B3"]=="O" and  coords["C3"]=="O" or \
        coords["A1"] == "O" and coords["B2"] == "O" and coords["C3"] == "O" or \
        coords["C1"] == "O" and coords["C2"] == "O" and coords["C3"] == "O" or \
        coords["C1"] == "O" and coords["B2"] == "O" and coords["A3"] == "O":
        print ("Computer wins")
        break