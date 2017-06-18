from Tkinter import *
import ScrolledText
from Reader import *


class App:

    def __init__(self, master):
        """ Crete a GUI with a frame, text area, two buttons, and display """
        test = " "
        self.frame = Frame(master, height=60, width=60, bg="#66a4d3")
        self.frame.grid()
        self.Directions = Message(self.frame, text="""Enter your text and press
        "Submit". Words that a beginning reader could not read will appear with
        astericks around them.""")
        self.Directions.grid(row=1, column=1)
        self.textArea = ScrolledText.ScrolledText(self.frame, height=30,
                                                  width=30, wrap=WORD)
        self.textArea.grid(row=2, column=1)
        self.Enter = Button(self.frame, text="Submit",
                            command=self.retrieve_text)
        self.Enter.grid(row=3, column=1)
        self.Quit = Button(self.frame, text="Quit", command=self.frame.quit)
        self.Quit.grid(row=4, column=1)

    def retrieve_text(self):
        """ Get the entered text and flag un-readable words. """
        words = self.textArea.get(1.0, END)
        test = flag(words)
        self.textArea.insert(END, "\n"+test, *"n")
        self.textArea.tag_config("n", foreground="blue")


root = Tk()
app = App(root)
root.title("Readability Check")

root.mainloop()
root.destroy()
