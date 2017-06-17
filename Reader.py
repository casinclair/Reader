
#vowels except y
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

#Dolch preprimer list
preprimer = ["a", "and", "away", "big" , "blue", "can" "come", "down",
            "find", "for", "funny", "go", "help", "here", "i", "in", "is",
            "it", "jump", "little", "look", "make", "me", "my", "not", "one",
            "play", "red", "run", "sand", "see", "the", "three", "to", "two",
            "up", "we", "where", "yellow", "you"]
            
# Dolch primer list
primer = ["all", "am", "are", "at", "ate", "be","black", "brown", "but", "came",
"did", "do", "eat", "four", "get", "good", "have", "he", "into", "like", "must",
"new", "no", "now", "on", "our", "out", "please", "pretty", "ran", "ride", "saw",
"say", "she", "so", "soon", "that", "there", "they", "this", "too", "under", 
"want", "was", "well", "went", "what", "white", "who", "will", "with", "yes"]            

# Initial Consonant Blends and Digraphs
IC = ["bl", "cl", "fl", "gl", "pl", "sc", "sk", "sm", "sl", "sn","sp", "st",
"sw", "sh", "th", "ch", "wh", "br", "cr" , "dr" , "fr" , "gr" , "pr", "tr", "tw"]

#Final Consonant Blends, Digraphs, and Double letters
FC = ["ck", "ft", "lk", "lp", "lt", "mp", "nd", "nt", "sk", "st", "ts", "xt", 
"ch", "sh", "th", "ss", "ck" ,"ff" ,"ll"] 


# Check if a word could be CVC or CVCE 

def check_pattern(text):
    while len(text) >= 3:
        l= [text[0], text[1], text[2]]
        if l[0] in vowels:
            return False
        elif l[1] not in vowels:
            return False
        elif l[2] in vowels:
            return False
        else:
            return True
            
# Check if a word is CVC.
def check_CVC(text):
    pattern = check_pattern(text)
    if pattern == False:
        return False
    elif len(text) != 3:
        return False
    else: 
        return True
        
# Check if a word is CVCE.        
def check_CVCE(text):
    pattern = check_pattern(text)
    if pattern == False:
        return False
    elif len(text) != 4:
        return False
    elif text[3] != "e":
        return False
    else:
        return True

#Check if a word begins with a consonant blend or digraph. If so, read as if one letter
def check_bb (text):
    if len(text) >= 3:
        st= text[0]+text[1]
        if st in IC:
            p = list(text)
            del p[1]
            text = "".join(p)
            return text
        else:
            return text
    else:
            return text
            
#Check if a word ends with a consonant blend, digraph, or double letter. If so, read as if one letter
def check_eb (text):
    if len(text) >= 3:
        end = text[-2]+text[-1]
        if end  in FC:
            p = list(text)
            del p[-1]
            text = "".join(p)
            return text
        else:
            return text
    else:
            return text
# Strip off any punctuation at the end of a word.        
def no_punct(text):
    punct = ["!", ".", "?", ",", ";", ":"]
    if text[-1] in punct:
        p = list(text)
        del p[-1]
        text = "".join(p)
        return text
    else:
        return text
#Check if a word is preprimer, primer, or easily decodable
def check_readable(text):
    word = no_punct(text)
    lc = word.lower()
    merge_start = check_bb(lc)
    merge_end = check_eb(merge_start)
    CVC = check_CVC(merge_end)
    CVCE = check_CVCE(merge_end)
    

    if CVC == True:
        return True
    elif CVCE == True:
        return True
    elif lc.lower() in preprimer:
        return True
    elif lc.lower() in primer:
        return True
    else:
        return False
#Flag words in a text that are not easily decodable, preprimer, or primer
def flag(text):
    words = text.split()
    i = 0
    while i < len(words):
        r = check_readable(words[i])
        if r == False:
            words[i] = "*" + words[i] + "*"
            i += 1
        else:
            i += 1
    text = " ".join(words)
    return text

from Tkinter import *
import ScrolledText


class App:

    #Crete a GUI with a frame, text area, two buttons, and display
    
    def __init__(self, master):
        test= " "
        self.frame = Frame(master, height=60, width=60, bg="#66a4d3")
        self.frame.grid()
        self.Directions = Message(self.frame, text="""Enter your text and press "Submit". Words that a
beginning reader could not read will appear with astericks around them.""")
        self.Directions.grid(row=1, column=1)
        self.textArea = ScrolledText.ScrolledText(self.frame, height=30, width=30, wrap=WORD)
        self.textArea.grid(row=2, column=1)
        self.Enter = Button (self.frame, text = "Submit", command = self.retrieve_text)
        self.Enter.grid(row=3, column=1)
        self.Quit = Button (self.frame, text = "Quit", command=self.frame.quit)
        self.Quit.grid (row=4, column=1)

       #Get the entered text and flag un-readable words.

    def retrieve_text(self):
         words = self.textArea.get(1.0, END)
         test = flag(words)
         self.textArea.insert(END,"\n"+test,*"n")
         self.textArea.tag_config("n", foreground="blue")
        
       
      
       
        

                         
root = Tk()
app = App(root)
root.title("Readability Check")

root.mainloop()
root.destroy()





