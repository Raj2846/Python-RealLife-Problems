"""Text Editor takes character as an input and on undo remove the last character."""

class texteditor:
    def __init__(self):
        self.lst=[]
        self.text=""
        self.output=""
        
    def add_text(self,text):
        self.lst.append(text)
        
    def undo(self):
        self.lst.remove(self.lst[-1])
        
    def get_text(self):
        self.output=self.text.join(self.lst)
        print(self.output)
        
t=texteditor()
t.add_text("A")
t.add_text("B")
t.add_text("C")
t.add_text("D")
t.add_text("E")
t.add_text("F")
t.get_text()
t.undo()
t.get_text()