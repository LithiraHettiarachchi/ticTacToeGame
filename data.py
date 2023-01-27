#Statements for print the game history
#This will works when user insert 2 as the menu selection
def db():
    import mysql.connector
    conDict={'host':'localhost','database':'tictactoe','user':'root','password':''}
    db=mysql.connector.connect(**conDict)
    cursor=db.cursor()
    cursor.execute("SELECT * FROM history")

    data=cursor.fetchall()
    
    for item in data:
        print("GameID :",item[0],"|","Player 1 Name :",item[1],"|","Player1 Win Count :",item[2],"|","Player 2 Name :",item[3],"|","Player 2 Win Count :",item[4],"|","Total Draws :",item[5])
    db.close()
