#Importing system, mysql and other python files
import sys
import mysql.connector
import Board
import Database.data
import html
import random
#Variables
user1=""
user2=""
option=0
count=0
winner=""
Player1WinCount=0
Player2WinCount=0
DrawCount=0
#Users choice lists
choi1=[]
choi2=[]
T=True
#Definitions for making the tic tac toe board
list1=['1','2','3']
list2=['4','5','6']
list3=['7','8','9']
#Winnsers list as the board
winlist=["123","456","789","147","258","369","159","357"]

#Insering data into the database
def datainsert():

    conDict={'host':'localhost','database':'tictactoe','user':'root','password':''}
    db=mysql.connector.connect(**conDict)
    cursor=db.cursor()
    myText="INSERT INTO history(GameID,Player1,Player1WinCount,Player2,Player2WinCount,TotalDraws) VALUES(%s,%s,%s,%s,%s,%s)"
    myvalues=(GameID,user1,Player1WinCount,user2,Player2WinCount,DrawCount)
    cursor.execute(myText,myvalues)
    db.commit()
    return
    
while T:
    list1=['1','2','3']
    list2=['4','5','6']
    list3=['7','8','9']
    choi1=[]
    choi2=[]
    #Showing main menu
    print("--------------Main Menu--------------")
    print("1. New Game")
    print("2. View History")
    print("3. Read data from a file")
    print("4. Exit")
    #Statement for taking the main menu selections
    print("---------Main Menu Selections---------")
    option=int(input("Enter your Selection : "))
    #Statements and process if the user select 1 from the main menu selection
    if option==1:
        Player1WinCount=0
        Player2WinCount=0
        DrawCount=0
        print()
        #Getting a random range to enter the database
        GameID=random.randint(10,99)
        #Getting players names
        print("-----Player Names-----")
        user1=input("Enter your name : ")
        user2=input("Enter your name : ")
        #Calling tic tac toe board and printing it
        Board.board()
        print("If you want to exit the game press 0")
        #Getting both users choices to fill the board
        while count<6:
            #User1's choices
            if count%2==0:
                print("---------User Selections------------")
                choice=int(input("Enter your choice :"))
                if choice==1:
                    if list1[0]=="B":
                        print("Error Choice")
                        choi1.append('')
                        continue
                    elif list1[0]=='1':
                        list1[0]="A"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==2:
                    if list1[1]=="B":
                        print("Error Choice")
                        choi1.append('')
                        continue
                    elif list1[1]=='2':
                        list1[1]="A"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==3:
                    if list1[2]=="B":
                        print("Error Choice")
                        choi1.append('')
                        continue
                    elif list1[2]=='3':
                        list1[2]="A"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==4:
                    if list2[0]=="B":
                        print("Error Choice")
                        choi1.append('')
                        continue
                    elif list2[0]=='4':
                        list2[0]="A"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==5:
                    if list2[1]=="B":
                        print("Erro Choice")
                        choi1.append('')
                        continue
                    elif list2[1]=='5':
                        list2[1]="A"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==6:
                    if list2[2]=="B":
                        print("Error Choice")
                        choi1.append('')
                        continue
                    elif list2[2]=='6':
                        list2[2]="A"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==7:
                    if list3[0]=="B":
                        print("Error Choice")
                        choi1.append('')
                        continue
                    elif list3[0]=='7':
                        list3[0]="A"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==8:
                    if list3[1]=="B":
                        print("Error Choice")
                        choi1.append('')
                        continue
                    elif list3[1]=='8':
                        list3[1]="A"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==9:
                    if list3[2]=="B":
                        print("Error Choice")
                        choi1.append('')
                        continue
                    elif list3[2]=='9':
                        list3[2]="A"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==0:
                    break
                else:
                    print("Index out of range.Try again...")
                choi1.append(str(choice))
                choi1.sort()
            #User2's choices
            if count%2!=0:
                print("-----------User Selections-----------")
                choice=int(input("Enter your choice :"))
           
                if choice==1:
                    if list1[0]=="A":
                        print("Error Choice")
                        choi2.append('')
                        continue
                    elif list1[0]=='1':
                        list1[0]="B"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==2:
                    if list1[1]=="A":
                        print("Error Choice")
                        choi2.append('')
                        continue
                    elif list1[1]=='2':
                        list1[1]="B"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==3:
                    if list1[2]=="A":
                        print("Error Choice")
                        choi2.append('')
                        continue
                    elif list1[2]=='3':
                        list1[2]="B"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==4:
                    if list2[0]=="A":
                        print("Error Choice")
                        choi2.append('')
                        continue
                    elif list2[0]=='4':
                        list2[0]="B"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==5:
                    if list2[1]=="A":
                        print("Error Choice")
                        choi2.append('')
                        continue
                    elif list2[1]=='5':
                        list2[1]="B"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==6:
                    if list2[2]=="A":
                        print("Error Choice")
                        choi2.append('')
                        continue
                    elif list2[2]=='6':
                        list2[2]="B"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==7:
                    if list3[0]=="A":
                        print("Error Choice")
                        choi2.append('')
                        continue
                    elif list3[0]=='7':
                        list3[0]="B"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==8:
                    if list3[1]=="A":
                        print("Error Choice")
                        choi2.append('')
                        continue
                    elif list3[1]=='8':
                        list3[1]="B"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==9:
                    if list3[2]=="A":
                        print("Error Choice")
                        choi2.append('')
                        continue
                    else:
                        list3[2]="B"
                        print(' | '.join(list1))
                        print(' | '.join(list2))
                        print(' | '.join(list3))
                elif choice==0:
                    break
                else:
                    print("Index out of range. Try again...")
                choi2.append(str(choice))
                choi2.sort()
            print("-----------------------------------")
            print(user1," : ",''.join(choi1))
            print(user2," : ",''.join(choi2))
            win1=''.join(choi1)
            win2=''.join(choi2)
            #Processing the winner and getting inputs to the database
            if win1 in winlist:
                print(user1,"is the winner")
                Player1WinCount+=1
                winner=user1
                choi1.clear()
                choi2.clear()
                count=0
                break
            if win2 in winlist:
                print(user2,"is the winner")
                Player2WinCount+=1
                winner=user2
                choi1.clear()
                choi2.clear()
                count=0
                break   
            count+=1
        #Returning the draw list if both users are unable to win
        #Getting data to the database
        else:
            print("Match Draw")
            DrawCount+=1
            choi1.clear()
            choi2.clear()
            count=0
            
        #Calling the function datainsert()
        datainsert()
        
    #Statements and process if the user select 2 from the main menu selection
    if option==2:
       Database.data.db()

    if option==3:
        html.viewhtmlpage()

    if option==1 or option==2 or option==3:
        T=True
    elif option==4:
        T=False
    else:
        print("Wrong Selection")



