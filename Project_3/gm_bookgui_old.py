## The requirments for this project were changed and simplified before I managed to complete this assignment. ##
## The one thing I know I had left was to get report to work after removing a reader##

from breezypythongui import *
from gm_bookrecs import *

class BookRecommendation(EasyFrame):
    """Shows book reccomendations to the user"""

    def __init__(self):
        """Sets up window, widgets, and data"""
        EasyFrame.__init__(self, title= "Book Recommendations")
        self.name = names()
        self.scores = ratings()
        self.rating = bookdict(self.name, self.scores)
        self.books = booktup()

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
        reader = self.prompterBox(title = "Add Reader", promptString= "Reader Name: ")
        self.name.append(reader)
        rate = len(self.scores[1])
        self.rt = []
        for i in range(rate):
            self.rt.append(0)
        self.scores.append(self.rt)
        self.rating[reader] = self.rt



    def addBook(self):
        addbookDialog(self,self.books,self.scores)


    def rateBook(self):
        ratebookDialog(self, self.name, self.books, self.scores, self.rating)

    def removeReader(self):
        rmv = self.prompterBox(title= "Remove Reader", promptString= "Readers Name: ")
        if rmv in self.rating:
            del self.rating[rmv]
        else:
            self.messageBox(title= "Reader Absent", message= "That reader is not in our list")
        if rmv in self.name:
            i = self.name.index(rmv)
            self.name.remove(rmv)
            del self.books[i]
        return self.rating, self.name, self.books


    def recommend(self):
        namelist = self.name
        rcmd = self.prompterBox(title = "Find Recommendations for a Reader", promptString = "Readers Name: ")
        if rcmd in namelist:
            recom = recommend(rcmd)
            recommendDialog(self, recom,rcmd)
        else:
            self.messageBox(title = "Error", message= "That reader is not in our database. Please enter another name")

    def report(self):
        reportDialog(self,self.name,self.rating,self.books,self.scores)

class addbookDialog(EasyDialog):

    def __init__(self, parent,books,score):
        self.books = books
        self.scores = score
        EasyDialog.__init__(self, parent, "Add Book")

    def body(self, master):
        self.addLabel(master, text = "Author:", row = 0, column = 0)
        self.addLabel(master, text = "Title:", row = 1, column = 0)
        self.authorText = self.addTextField(master, text = '', row = 0, column = 1)
        self.titleText = self.addTextField(master, text = '', row = 1, column = 1)


    def apply(self):
        author = self.authorText.getText()
        title = self.titleText.getText()
        book = (author, title)
        self.books.append(book)
        for lst in range(len(self.scores)):
            self.scores[lst].append(0)
        return self.books,self.scores


class ratebookDialog(EasyDialog):
    def __init__(self,parent, name, book, score, rating):
        self.namelist = name
        self.booklist = book
        self.scores = score
        self.rating = rating
        EasyDialog.__init__(self, parent, "Rate Book")

    def body(self,parent):
        labelPanel = self.addPanel(parent, row = 0, column = 0, columnspan = 75, background= '#d9d9d9')
        labelPanel.addLabel( text = "Select Reader:", row = 0, column = 0, background= '#d9d9d9')
        self.readerList = self.addListbox(parent, row=1, column=0, width = 25, height= 10)
        labelPanel.addLabel( text = "Select Book:", row = 0, column = 15, background= '#d9d9d9')
        self.readerList.insert(0,*self.namelist)
        self.bookList = self.addListbox(parent, row=1, column=5, width=50, height = 10)
        self.bookList.insert(0,*self.booklist)
        self.addLabel(parent, text="Enter Rating: ", row= 11, column=0)
        self.ratingValue = self.addIntegerField(parent, value=0, row= 11, column=1)
        self.addLabel(parent, text = "Rating Key: -5: Hated it; -3: Disliked it; -1: Slightly disliked it; 0: Haven't"
                                     "read it; 1: Slightly liked it; 3: Liked it; 5: Loved it", row = 12, column = 0,
                      columnspan= 10)

    def apply(self):
        ratval = self.ratingValue.getNumber()
        reader = self.readerList.getSelectedItem()
        book = self.bookList.getSelectedIndex()
        rt = self.rating[reader]
        rt[book] = ratval
        self.scores[book] = ratval
        return self.rating, self.scores


class recommendDialog(EasyDialog):
    def __init__(self,parent, recom, name):
        self.rec = recom
        self.name = name
        EasyDialog.__init__(self,parent, "Recomendations for " + self.name)


    def body(self, parent):
        self.form = "{}{}".format("Recommendations",'\n')
        for i in range(len(self.rec)):
            self.form += "{}{}".format(self.rec[i],'\n')
        self.outRec = self.addTextArea(parent, text = '', row = 0, column = 0)
        self.outRec["state"] = "normal"
        self.outRec.setText(self.form)
        self.outRec["state"] = "disabled"
    def apply(self):
        pass

class reportDialog(EasyDialog):
    def __init__(self, parent, name, rating,books,scores):
        self.name = name
        self.rating = rating
        self.books = books
        self.scores = scores
        EasyDialog.__init__(self, parent, "Reports")

    def body(self, parent):
        self.form = "{}{}".format("Recommendation Report",'\n')
        for key in self.rating:
            friend = friends(key,self.rating)
            recom = recommend(key,self.rating,self.books)
            self.form +=("{}{}{}".format(key,':',friend) + '\n')
            for i in recom:
                self.form += ("{}{}{}".format('\t',i,'\n'))
        self.reportArea = self.addTextArea(parent, text = '', row = 0, column = 0, height= 100)
        self.reportArea["state"] = "normal"
        self.reportArea.setText(self.form)
        self.reportArea["state"] = "disabled"
    def apply(self):
        pass



def main():
    BookRecommendation().mainloop()

if __name__ == "__main__":
    main()