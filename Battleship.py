from tkinter import Button,Label,Tk,font,messagebox,Message
from random import randrange

count = 0
def Play():
    global  count
    count = 0
    wincount = 25

    def Ship_verify(ship):
        for i in ship[0]:
            if i in ship[1] or i in ship[2]:
                return False
        for i in ship[1]:
            if i in ship[2]:
                return False
        return True

    def Ship_init():
        ship = []
        for i in range(3):
            a = randrange(2,7)
            b = randrange(2,7)
            temp = tuple([a,b])
            ship.append(temp)

        for i in range(3):
            temp = randrange(1,5)
            if temp == 1:
                temploc = list(ship[i])
                ship[i] = [tuple(temploc), tuple([temploc[0]-1,temploc[1]]), tuple([temploc[0]+1,temploc[1]]) ]
            elif temp == 2:
                temploc = list(ship[i])
                ship[i] = [tuple(temploc), tuple([temploc[0],temploc[1] - 1]) , tuple([temploc[0],temploc[1]+1])]
            elif temp == 3:
                temploc = list(ship[i])
                ship[i] = [tuple(temploc), tuple([temploc[0]+1 ,temploc[1]-1]) , tuple([temploc[0]-1,temploc[1]+1])]
            else:
                temploc = list(ship[i])
                ship[i] = [tuple(temploc), tuple([temploc[0]-1 ,temploc[1]-1]) , tuple([temploc[0]+1,temploc[1]+1])]

        if Ship_verify(ship):
            return ship
        else:
            return Ship_init()

    master = Tk()
    master.title("Radar")

    ship = Ship_init()
    print(ship)
    drowned = []

    def clicked(x,y):
        global count
        count=count + 1
        temp = tuple([x,y])
        for i in range(3):
            if temp in ship[i]:
                messagebox.showinfo("Hit","Ship is Hit",parent = master)
                Buttons[7*(x-1)+y-1].configure(text = "X",fg = 'red',font = ('arial',16,'bold'))
                ship[i].remove(temp)


        for i in range(3):
            if ship[i]==[] and i not in drowned:
                messagebox.showinfo("Kill","Ship %(this)d is Drowned."%{'this':i+1},parent = master,)
                drowned.append(i)

        if ship == [[],[],[]]:
            messagebox.showinfo("You Won","All ships are destroyed.",parent = master)
            master.destroy()

        MissileLabels.configure(text="Missiles Remaining = %(this)d " % {'this': wincount - count})


        if count==wincount:
            messagebox.showinfo("You Lost","You have no missiles left.\nYour ship was Drowned.",parent = master)
            master.destroy()

        print(x,y)


    Buttons = []
    for i in range(7):
        for j in range(7):
            Buttons.append(Button(master,text = '%(x)d%(y)d'%{'x':i+1,'y':j+1},bg="lightgreen",fg="blue",command = lambda a=i+1,b=j+1: clicked(a,b),font = ('arial',15,'bold'),relief = 'raised',activeforeground ='red',activebackground = 'yellow'))
            Buttons[(i)*7 + (j)].grid(row = i,column = j)

    MissileLabels = Label(master,text = "Missiles Remaining = %(this)d"%{'this':wincount-count},width = 33,height = 3,bg = 'cyan',fg = 'black',font = ('arial',15,'bold'))
    MissileLabels.grid(row = 7,column = 0 , columnspan = 7)
    master.configure(bg = 'white')
    master.mainloop()

#Instructions
def Instructions():
    Instruct = Tk()
    Instruct.title("How to Play")

    message = 'Captain!!!, First Officer Jones Reporting.\nEnemy Ships have started attacking us.\nOur Radars are jammed and so are theirs.\nWe do have limited missiles and we need to face our enemy soon or our Motherland will be in grave danger.\nIntelligence report has informed there are three Enemy Battleships.\nCaptain, it is up to you to save us.\nGod Help us.\n\nYou need to predict enemy ships locations and annihilate them before they destroy you.To destroy a ship, you need to hit it in three locations.\nAll the best, Captain.'
    Messagedisp = Message(Instruct,text = message,font = ('arial',20),fg = 'black',bg = 'white')
    Messagedisp.pack()

Main = Tk()
Main.title("Battleship")
Main.configure(bg = 'indigo')

AllButtonsColor = 'black'
Active = 'white'
ButtonsFont =('arial',18,'bold')


PlayLabel = Button(Main,command = Play,height = 5, width = 30,text = "Play",bg = AllButtonsColor,fg='orange',font = ButtonsFont,activebackground = Active)
PlayLabel.grid(row = 0 , column = 0)

InstructLabel = Button(Main,command = Instructions,height = 5 ,width =30, text = "How to Play",fg = 'lightgreen',bg = AllButtonsColor,font = ButtonsFont,activebackground = Active)
InstructLabel.grid(row = 1, column = 0)

QuitLabel = Button(Main,command = lambda:Main.destroy(), height = 5 ,width = 30,text = "Quit",fg = 'red',bg = AllButtonsColor,font = ButtonsFont,activebackground = Active)
QuitLabel.grid(row = 3, column = 0)

Main.mainloop()
