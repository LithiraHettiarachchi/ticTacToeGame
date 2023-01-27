def viewhtmlpage():
    import webbrowser
    import mysql.connector
    listhtml=[]

    conDict=mysql.connector.connect(user='root',host='localhost',database='tictactoe',password='')
    selecttable="SELECT * FROM history"
    cursor=conDict.cursor()
    cursor.execute(selecttable)
    data=cursor.fetchall()

    tablehistory="<tr><td>GameID</td><td>Player1</td><td>Player1WinCount</td><td>Player2</td><td>Player2WinCount</td><td>TotalDraws</td></tr>"
    listhtml.append(tablehistory)

    for line in data:
        lineone="<tr><td>%s</td>"%line[0]
        listhtml.append(lineone)
        linetwo="<td>%s</td>"%line[1]
        listhtml.append(linetwo)
        linethree="<td>%s</td>"%line[2]
        listhtml.append(linethree)
        linefour="<td>%s</td>"%line[3]
        listhtml.append(linefour)
        linefive="<td>%s</td>"%line[4]
        listhtml.append(linefive)
        linesix="<td>%s</td></tr>"%line[5]
        listhtml.append(linesix)

    listhtml=''.join(listhtml)
    table='''
    <html>
    <head>
    <title> User History Table</title>
    </head>
    <body>
    <h1><p><center>
    If you want to close this page please click the close button
    </center></p></h1>
    <table>
    %s
    </table>
    </body>
    </html>
    '''%(listhtml)

    filename='20200791 Lithira.html'

    def page(table,filename):
        show=open(filename,"w")
        show.write(table)
        show.close()

    page(table,filename)
    webbrowser.open(filename)

        #cursor.close()
        #conDict.close()
    return

        
        
        
