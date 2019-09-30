# Garrett Matthews
# Project 3: Book Recommendations GUI

# I declare that the following source code was written solely by me. I understand that copying any source code,
# in whole or in part, constitutes cheating, and that I will receive a zero on this project if I am found in violation
# of this policy. #

# Importing necessary modules #
from breezypythongui import *
from gm_bookrecs import *

# Making the class
class BookRecommendation(EasyFrame):
    """Shows book reccomendations to the user"""
    # Initializing the window #
    def __init__(self):
        """Sets up window, widgets, and data"""
        EasyFrame.__init__(self, title= "Book Recommendations")
        self.name = names()
        self.scores = ratings()
        self.rating = bookdict(self.name, self.scores)
        self.books = booktup()

        self.friendsButton = self.addButton(text = "Friends", row = 0, column = 0, columnspan = 2,
                                            command = self.friends)
        self.rcmndButton = self.addButton(text = "Recommend", row = 0, column = 2, columnspan = 2,
                                          command = self.recommend)
        self.rptButton = self.addButton(text = "Report", row =0, column = 4, columnspan = 2, command = self.report)

    def friends(self):
        """Calls the friends dialog upon button push"""
        friendsDialog(self, self.name, self.rating)

    def recommend(self):
        """Implements the recommendations command upon button push"""
        namelist = self.name
        rcmd = self.prompterBox(title = "Find Recommendations for a Reader", promptString = "Readers Name: ")
        if rcmd in namelist:
            recom = recommend(rcmd)
            recommendDialog(self, recom,rcmd)
        else:
            self.messageBox(title = "Error", message= "That reader is not in our database. Please enter another name")

    def report(self):
        """Generates a report based on the readers and their ratings"""
        reportDialog(self,self.name,self.rating,self.books,self.scores)


class friendsDialog(EasyDialog):
    """Dialog for inputting readers name and number of friends to look at"""
    def __init__(self, parent, name, dict):
        self.namelist = name
        self.dict = dict
        EasyDialog.__init__(self,parent, "Friends")

    def body(self, parent):
        self.addLabel(parent, text = "Readers Name:", row = 0, column = 0)
        self.readName = self.addTextField(parent, text = '', row = 0, column = 1)
        self.addLabel(parent, text = "Number of friends to find:", row = 1, column = 0)
        self.friendNumber = self.addIntegerField(parent, value= 2, row = 1, column = 1)

    def apply(self):
        numb = self.friendNumber.getValue()
        name = self.readName.getText()
        if int(numb) > 0:
            if name in self.namelist:
                friendreportDialog(self,name, int(numb), self.dict)
            else:
                self.messageBox(title="Error", message= "That is not a valid reader. Please enter another reader.")
        else:
            self.messageBox(title="Error", message="Number of friends must be a positive number greater than 0.")


class friendreportDialog(EasyDialog):
    """Dialog to display the friends of a reader"""
    def __init__(self, parent, name, numb, dict):
        self.name = name
        self.numb = numb
        self.dict = dict
        EasyDialog.__init__(self,parent, "Friends of" + self.name)

    def body(self, parent):
        self.friendReport = self.addTextArea(parent,text= "", row= 0, column = 0, height= 10)
        self.friends = friends(self.name, self.dict, self.numb)
        self.form = "{}{}{}".format("Friends of:", self.name, '\n')
        x = 0
        for i in self.friends:
            x += 1
            self.form += "{}{}{}{}".format(x,') ', i,'\n')
        self.friendReport["state"] = "normal"
        self.friendReport.setText(self.form)
        self.friendReport["state"] = "disabled"

    def apply(self):
        pass


class recommendDialog(EasyDialog):
    """Dialog to display recommendations of books for a reader"""
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
    """Dialog to display the report for all readers"""
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