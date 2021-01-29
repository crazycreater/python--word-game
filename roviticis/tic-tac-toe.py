import random as ra
def xogame():  
    global error
    error=False
    global run
    player=input("please choose any character \n\nX  or  O  ").upper()
    #creating dic to store all the user entered values 
    dic={"r1c1":"","r1c2":"","r1c3":"","r2c1":"","r2c2":"","r2c3":"","r3c1":"","r3c2":"","r3c3":""}
    # Assigning character to computer which is opposite to player's character '
    if player =="X":
            computer="O"
            
    else:
            computer="X"
            
    # To print the x o  pattern 
    def Print():
                print("EX: if u want row 1 and column 2 type 'r1c2'")
                print("\n\n")
                print("      {}   |  {}    |  {}   ".format(dic["r1c1"],dic["r1c2"],dic["r1c3"]))
                print("     ―――――――――――――――――")
                print("      {}   |  {}    |  {}   ".format( dic["r2c1"],dic["r2c2"],dic["r2c3"]))
                print("     ―――――――――――――――――")
                print("      {}   |  {}    |  {}   ".format( dic["r3c1"],dic["r3c2"],dic["r3c3"]))
                print("\n\n")
    # check any winners 
    def check(c_player):
                val=""
                global run
                # check vertically 
                for c in range(1,4):
                    val=""
                    for r in range(1,4):
                                 val+=dic["r"+str(r)+"c"+str(c)]
                    
                    if val==3*c_player:
                        print("winner is ",c_player)
                        run=False
                        Print()
                       
                #check horizontal
                for r in range(1,4):
                    val=""
                    for c in range(1,4):
                                 val+=dic["r"+str(r)+"c"+str(c)]
                                
                    if val==3*c_player:
                        print("winner ",c_player)
                        run=False
                        Print()
                       
                val=""
                #check diagonal left to right
                for r,c in enumerate([3,2,1]):
                   
                    val+=dic["r"+str(r+1)+"c"+str(c)]
                   
                if val==3*c_player:
                        print("winner is ",c_player)
                        run=False
                        Print()
                        
                 #check  diagonal  right to left
                val=""
                for r_c in range(1,4):
                        
                        val+=dic["r"+str(r_c)+"c"+str(r_c)]
                       
                if val==3*c_player:
                        print("winner is ",c_player)
                        run=False
                        Print()
                       
    #Assigning  users input to respective row and column 
    def user():
                  global error 
                  if Input in dic:	
                     if dic[Input]=="":
                        dic[Input]=player
                        error=False
                     elif dic[Input]=="X" or "O":
                        print("sorry , choose other box because it is occupied ")
                        error=True
                  else:
                        print("Error:Enter valid input ")
                        error=True
                        
    # Assiging random row and column  for computer
    def comp():
            empty_values=[]
            for  i in  dic:
                if dic[i]=="":
                    empty_values+=[i]
            if empty_values!=[] and not error:
             comp_choice=ra.choice(empty_values)
             dic[comp_choice]=computer
            
              
    #game loop
    run=True
    while run:
               lis=[]
               #calling Print function to print the pattern of x o game 
               Print()
               #getting input from the user to select the place at which he want to place the his character 
               for i in dic.values():
                lis+=[i]
               if ""  not in lis:
                   print("draw ")
                   run=False
                        
               else:
                   #Decide according to character , who has to play first 
                   if player=="X":
                       Input=input("Enter row and column in which you want to place your character  :")
                       user()
                       if not error:
                         comp()
                         check("X")
                         check("O")
                        
                   else:
                       
                         comp()
                         Print()
                         Input=input("Enter row and column in which you want to place your character  :")
                         user()
                         if not error:
                            check("X")
                            check("O")
                    
xogame()
