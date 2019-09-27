from breezypythongui import EasyFrame
from breezypythongui import EasyDialog
import tkinter


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
        self.rmvrdrButton = self.addButton(text = "Remove Reader", row = 1, column = 3, columnspan = 2)
        self.rcmndButton = self.addButton(text = "Recommend", row = 2, column = 0, columnspan = 2)
        self.rptButton = self.addButton(text = "Report", row =2, column = 3, columnspan = 2)


    def addRead(self):
        text = self.prompterBox(title = "Add Reader", promptString= "Reader Name: ")


    def addBook(self):
        EasyDialog.__init__(self, title= "Add Book")
        body(self)
        inputPanel = self.addPanel(self, row = 0, column = 0)
        inputPanel.authorLabel = inputPanel.addLabel(self, text = "Author: ", row = 0, column = 0)
        inputPanel.titleLabel = inputPanel.addLabel(self, text = "Title: ", row = 1, column = 0)
        inputPanel.authorField = inputPanel.addTextField(self, text = "", row = 0, column = 1)
        inputPanel.titleField = inputPanel.addTextField(self, text = "", row = 1, column = 1)
        buttonPanel = self.addPanel(self, row = 1, column = 0)
        buttonPanel.apply()
        buttonPanel.cancelButton = buttonPanel.addButton(self, text = "Cancel", row = 0, column = 1)

    def rateBook(self):
        EasyDialog.__init__(self, title = "Rate Book")
        body(self)
        listPanel = self.addPanel(self, row = 0, column = 0)
        listPanel.addListbox(self, row = 0, column = 0)
        listPanel.addListbox(self, row = 0, column = 2, width = 20)
        ratePanel = self.addPanel(self, row = 1, column = 0)
        ratePanel.addLabel(self, text = "Enter Rating", row = 0, column = 0)
        ratePanel.addIntegerField(self, value = 0, row = 0, column = 1)
        buttonPanel = self.addPanel(self, row = 2, column = 0)
        buttonPanel.apply()
        buttonPanel.cancelButton = buttonPanel.addButton(self, text="Cancel", row=0, column=1)


def main():
    BookRecommendation().mainloop()

if __name__ == "__main__":
    main()