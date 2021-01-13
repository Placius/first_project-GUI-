from tkinter import *
import random

class Game:
    def __init__(self, root):
        x = int(random.randint(1,100))
        self.find_this_number = x

        self.tries = 1

        menu = Menu(root)
        root.config(menu=menu)

        gameMenu = Menu(menu)
        menu.add_cascade(label="Game", menu=gameMenu)
        gameMenu.add_command(label="New game", command=self.NewGame)
        menu.add_separator()
        gameMenu.add_command(label="Quit", command=menu.quit)

        toolbar = Frame(root)
        self.StartButton = Button(toolbar, text="Start", command=self.Start)
        self.StartButton.pack(side=LEFT, padx=2, pady=2)

        self.TryButton = Button(toolbar, text="Try", command=self.Try)
        self.TryButton.pack(side=LEFT, padx=2, pady=2)

        self.RestartButton = Button(toolbar, text="Restart", command=self.Restart)
        self.RestartButton.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)

        frame = Frame(root)

        self.firstnumber = Label(text="Hier put your number")
        self.firstnumber.pack()
        self.entry_1 = Entry()
        self.entry_1.pack()

        self.TryButton = Button(text="Try", command=self.Try)
        self.TryButton.pack()

        frame.pack()



        self.canvas = Canvas(frame, width=400, height=300)
        self.canvas.pack(anchor=N)
        self.canvas.create_text(198, 50, text="Welcome in my first window game!")
        self.canvas.create_text(198, 80, text="Click Start")

        File1 = "bad.png"
        File2 = "happy.png"

        self.img1 = PhotoImage(file=File1)
        self.img2 = PhotoImage(file=File2)

        status = Label(root, text="Good luck my friend!", bd=1, relief=SUNKEN, anchor=S)
        status.pack(side=BOTTOM, fill=X)

    def NowDoNothing(self):
        return True

    def Start(self):
        self.canvas.delete(ALL)

    def Try(self):
        self.canvas.delete(ALL)
        text = "That was your " + str(self.tries) + " try."
        self.canvas.create_text(198, 80, text=text)

        user_choice = int(self.entry_1.get())

        if user_choice < self.find_this_number:
            self.canvas.create_text(198, 60, text="My number is higher.")
            # self.canvas["background"] = "red"
            self.canvas.create_image(198, 130, image=self.img1)

        elif user_choice > self.find_this_number:
            self.canvas.create_text(198, 60, text="My number is lower.")
            # self.canvas["background"] = "red"
            self.canvas.create_image(198, 130, image=self.img1)

        else:
            self.canvas.create_text(198, 60, text="Congratulations, you win!")
            # self.canvas["background"] = "green"
            self.canvas.create_image(198, 130, image=self.img2)

        self.tries += 1

    def Restart(self):
        self.canvas.delete(ALL)
        self.tries = 1
        self.find_this_number = random.randint(1,100)

    def NewGame(self):
        self.canvas.delete(ALL)
        self.tries = 1
        self.find_this_number = random.randint(1, 100)
        self.canvas.create_text(198, 50, text="Welcome in my first window game!")
        self.canvas.create_text(198, 80, text="Click Start")

root = Tk()
root.title("Find my number...1 - 100")
game = Game(root)
root.mainloop()