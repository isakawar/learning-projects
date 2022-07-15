import sqlite3
from tkinter import *

db = sqlite3.connect("gallery.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Artists(
ArtistID INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT NOT NULL,
Address TEXT NOT NULL,
Town TEXT,
County TEXT,
Postcode TEXT)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Pieces(
PieceID INTEGER PRIMARY KEY AUTOINCREMENT,
ArtistID INTEGER NOT NULL,
Title TEXT NOT NULL,
Medium TEXT,
Price INTEGER NOT NULL)""")


def add_artist():
    name = str(artistname.get())
    adress = str(artistadd.get())
    town = str(artisttown.get())
    country = str(artistcounty.get())
    postcode = str(artistpostcode.get())
    cursor.execute("""INSERT INTO Artists(Name,Address,Town,County,Postcode) VAlUES(?,?,?,?,?)""",
                   [name, adress, town, country, postcode])
    db.commit()
    clear_artist_input()


def add_piece():
    artist_id = int(artname.get())
    title = str(arttitle.get())
    choise_medium = medium.get()
    price = artprice.get()

    cursor.execute("""INSERT INTO Pieces(ArtistID,Title,Medium,Price) VALUES(?,?,?,?)""",
                   [artist_id, title, choise_medium, price])
    db.commit()
    clear_piece_input()


def clear_artist_input():
    artistname.delete(0, END)
    artistadd.delete(0, END)
    artisttown.delete(0, END)
    artistcounty.delete(0, END)
    artistpostcode.delete(0, END)
    artistname.focus()
    print("чисто")


def clear_piece_input():
    artname.delete(0, END)
    arttitle.delete(0, END)
    medium.set(["--------"])
    artprice.delete(0, END)
    artname.focus()


def view_all_artist():
    cursor.execute("SELECT * FROM Artists")
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ", " + str(x[4]) + ", " + x[
            5] + "\n"
        outputwindow.insert(END, newrecord)


def viewart():
    cursor.execute("SELECT * FROM Pieces")
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ",  ₤" + str(x[4]) + "\n"
        outputwindow.insert(END, newrecord)


def sear_artist_by_id():
    artist_id = searchartist.get()
    cursor.execute("""SELECT * FROM Artists WHERE artistid = ?""", [artist_id])
    for x in cursor.fetchall():
        artist_by_id = f"{str(x[0])}, {str(x[1])}, {str(x[2])}, {str(x[3])}, {str(x[4])} \n"
        outputwindow.insert(END, artist_by_id)


def clear_output():
    outputwindow.delete(0, END)


def search_piece_by_medium():
    choise = medium2.get()
    cursor.execute("""SELECT * FROM Pieces WHERE Medium = ?""", [choise])
    for x in cursor.fetchall():
        piece_by_medium = f"{str(x[0])}, {str(x[1])}, {str(x[2])}, {str(x[3])}, {str(x[4])} \n"
        outputwindow.insert(END, piece_by_medium)


def search_piece_by_price():
    inp_min = selectmin.get()
    inp_max = selectmax.get()
    cursor.execute("""SELECT * FROM Pieces WHERE Price >=? and Price <= ? """, [inp_min, inp_max])
    for x in cursor.fetchall():
        piece_by_price = f"{str(x[0])}, {str(x[1])}, {str(x[2])}, {str(x[3])}, ₤{str(x[4])} \n"
        outputwindow.insert(END, piece_by_price)


def sold_piece():
    id_piece = soldpiece.get()
    cursor.execute("""SELECT * FROM Pieces WHERE PieceID = ?""", [id_piece])
    for x in cursor.fetchall():
        piece_by_price = f"{str(x[0])}, {str(x[1])}, {str(x[2])}, {str(x[3])}, ₤{str(x[4])} \n"

        with open('SoldetPiece.csv', mode='a') as file:
            file.write(f"{piece_by_price}\n")

    cursor.execute("""DELETE FROM Pieces WHERE PieceID = ?""", [id_piece])
    db.commit()
    soldpiece.delete(0, END)


window = Tk()
window.title("Art")
window.geometry("1220x600")
title1 = Label(text="Enter new details: ")
title1.place(x=20, y=10, width=200, height=25)
artistnamelbl = Label(text="Name: ")
artistnamelbl.place(x=30, y=40, width=80, height=25)
artistname = Entry(text="")
artistname.place(x=110, y=40, width=200, height=25)
artistname.focus()
artistaddlbl = Label(text="Address: ")
artistaddlbl.place(x=310, y=40, width=80, height=25)
artistadd = Entry(text="")
artistadd.place(x=390, y=40, width=200, height=25)
artisttownlbl = Label(text="Town: ")
artisttownlbl.place(x=590, y=40, width=80, height=25)
artisttown = Entry(text="")
artisttown.place(x=670, y=40, width=100, height=25)
artistcountylbl = Label(text="County: ")
artistcountylbl.place(x=770, y=40, width=80, height=25)
artistcounty = Entry(text="")
artistcounty.place(x=850, y=40, width=100, height=25)
artistpostcodelbl = Label(text="Postcode: ")
artistpostcodelbl.place(x=950, y=40, width=80, height=25)
artistpostcode = Entry(text="")
artistpostcode.place(x=1030, y=40, width=100, height=25)
addbtn = Button(text="Add Artist", command=add_artist)
addbtn.place(x=110, y=80, width=130, height=25)
clearbtn = Button(text="Clear Artist", command=clear_artist_input)
clearbtn.place(x=250, y=80, width=130, height=25)
artnamelbl = Label(text="Artist ID: ")
artnamelbl.place(x=30, y=120, width=80, height=25)
artname = Entry(text="")
artname.place(x=110, y=120, width=50, height=25)
arttitlelbl = Label(text="Title: ")
arttitlelbl.place(x=200, y=120, width=80, height=25)
arttitle = Entry(text="")
arttitle.place(x=280, y=120, width=280, height=25)
artmediumlbl = Label(text="Medium: ")
artmediumlbl.place(x=590, y=120, width=80, height=25)

types_art = ["--------", "Oil", "Watercolour", "Ink", "Acrylic"]
medium = StringVar()
medium.set(types_art[0])
artmedium = OptionMenu(window, medium, *types_art)

artmedium.place(x=670, y=120, width=100, height=25)
artpricelbl = Label(text="Price:")
artpricelbl.place(x=770, y=120, width=80, height=25)
artprice = Entry(text="")
artprice.place(x=850, y=120, width=100, height=25)
addartbtn = Button(text="Add Piece", command=add_piece)
addartbtn.place(x=110, y=150, width=130, height=25)
clearartbtn = Button(text="Clear Piece", command=add_piece)
clearartbtn.place(x=250, y=150, width=130, height=25)
outputwindow = Listbox()
outputwindow.place(x=10, y=200, width=1000, height=350)

clearoutputwindow = Button(text="Clear Output", command=clear_output)
clearoutputwindow.place(x=1020, y=200, width=155, height=25)
viewallartists = Button(text="View All Artists", command=view_all_artist)
viewallartists.place(x=1020, y=230, width=155, height=25)
viewallart = Button(text="View All Art", command=viewart)
viewallart.place(x=1020, y=260, width=155, height=25)
searchartist = Entry(text="")
searchartist.place(x=1020, y=300, width=50, height=25)
searchartistbtn = Button(text="Search by Artist", command=sear_artist_by_id)
searchartistbtn.place(x=1075, y=300, width=100, height=25)
medium2 = StringVar(window)
searchmedium = OptionMenu(window, medium2, "Oil", "Watercolour", "Ink", "Acrylic")
searchmedium.place(x=1020, y=330, width=100, height=25)
searchmediumbtn = Button(text="Search", command=search_piece_by_medium)
searchmediumbtn.place(x=1125, y=330, width=50, height=25)
minlbl = Label(text="Min:")
minlbl.place(x=1020, y=360, width=75, height=25)
maxlbl = Label(text="Max:")
maxlbl.place(x=1100, y=360, width=75, height=25)
selectmin = Entry(text="")
selectmin.place(x=1020, y=380, width=75, height=25)
selectmax = Entry(text="")
selectmax.place(x=1100, y=380, width=75, height=25)
searchpricebtn = Button(text="Search by Price", command=search_piece_by_price)
searchpricebtn.place(x=1020, y=410, width=155, height=25)
soldpiece = Entry(text="")
soldpiece.place(x=1020, y=450, width=50, height=25)
soldbtn = Button(text="Sold", command=sold_piece)
soldbtn.place(x=1075, y=450, width=100, height=25)

window.mainloop()
db.close()
