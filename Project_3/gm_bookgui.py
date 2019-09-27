from breezypythongui import EasyFrame
from breezypythongui import EasyDialog



class BookRecommendation(EasyFrame):
    """Shows book reccomendations to the user"""

    def __init__(self):
        """Sets up window, widgets, and data"""
        EasyFrame.__init__(self, title= "Book Recommendations")
        self.addrdrButton = self.addButton(text = "Add Reader", row = 0, column = 0, columnspan = 2,
                                           command= self.addRead)
        self.addbkButton = self.addButton(text = "Add Book", row = 0, column = 3, columnspan = 2,
                                          command = self.addBook)
        self.rtbkButton = self.addButton(text = "Rate Book", row = 1, column = 0, columnspan = 2,
                                         command = self.rateBook)
        self.rmvrdrButton = self.addButton(text = "Remove Reader", row = 1, column = 3, columnspan = 2,
                                           command= self.removeReader)
        self.rcmndButton = self.addButton(text = "Recommend", row = 2, column = 0, columnspan = 2,
                                          command = self.recommend)
        self.rptButton = self.addButton(text = "Report", row =2, column = 3, columnspan = 2, command = self.report)


    def addRead(self):
        text = self.prompterBox(title = "Add Reader", promptString= "Reader Name: ")


    def addBook(self):
        addbookDialog(self,"Add Book")


    def rateBook(self):
        ratebookDialog(self, "Rate Book")

    def removeReader(self):
        rmv = self.prompterBox(title= "Remove Reader", promptString= "Readers Name: ")

    def recommend(self):
        recommendDialog(self, "Readers")

    def report(self):
        reportDialog(self, "Report")

class addbookDialog(EasyDialog):
    def __init__(self, parent,title):
        super().__init__(parent, title)

        def body(self,master):
            self.addLabel(master, text = "Author:", row = 0, column = 0)
            self.addLabel(master, text = "Title:", row = 1, column = 0)
            self.addTextField(master, text = '', row = 0, column = 1)
            self.addTextField(master, text = '', row = 1, column = 1)
            self.apply()

class ratebookDialog(EasyDialog):
    def __init__(self,parent,title):
        super().__init__(parent,title)

        def body(self,parent):
            listPanel = self.addPanel(parent, row=0, column=0)
            listPanel.addListbox(parent, row=0, column=0)
            listPanel.addListbox(parent, row=0, column=2, width=20)
            ratePanel = self.addPanel(parent, row=1, column=0)
            ratePanel.addLabel(parent, text="Enter Rating", row=0, column=0)
            ratePanel.addIntegerField(parent, value=0, row=0, column=1)
            self.apply(parent)

class recommendDialog(EasyDialog):
    def __init__(self, parent, title):
        super().__init__(parent, title)

        def body(self, parent):
            self.addMenuBar(parent, row = 0, column = 0, columnspan= 4)
        def apply(self):
            pass

class reportDialog(EasyDialog):
    def __init__(self, parent, title):
        super(reportDialog, self).__init__(parent, title)

        def body(self, parent):
            self.addTextArea(parent, text = "Your Text Here", row = 0, column = 0)
        def apply(self):
            pass

def main():
    BookRecommendation().mainloop()

if __name__ == "__main__":
    main()