# Garrett Matthews
# Project 5: Payroll

# I declare that the following source code was written solely by me. I understand that copying any source code,
# in whole or in part, constitutes cheating, and that I will receive a zero on this project if I am found in violation
# of this policy. #

import os
import shutil

class Payroll (object):
    """"Runs the payroll system for Company X"""
    def __init__(self):
        self.emp_dict = {}
        self.timecard = {}
        self.receipts = {}
        self.clsf = {}
        self.pymthd = {}
        self.emp_id = {}
        self.emp_data = {}

    def load_employees(self):
        """Reads the data list from employees.csv and makes a dictionary of lists for each employee"""
        empcsv = open('employees.csv','r')
        emp_temp = []
        empcsv = empcsv.readlines()[1:]
        for line in empcsv:
            for i in line.split(','):
                if line == 0:
                    pass
                else:
                    emp_temp.append(i)
        employee = emp_temp[0::13]
        data_1 = []
        data = []
        for i in emp_temp:
            if i in employee:
                pass
            else:
                data_1.append(i)
        for i in range(26):
            data_temp = data_1[(i * 12):((i + 1) * 12)]
            data.append(data_temp)
        for i in range(len(employee)):
            self.emp_dict[employee[i]] = data[i]
        #print(self.emp_dict)
        for i in self.emp_dict:
            self.emp_dict[i] = [x.replace('\n', '') for x in self.emp_dict[i]]
        return self.emp_dict

    def process_timecards(self):
        """Reads the time cards in and saves them to a dictionary"""
        timecard = open('timecards.txt','r')
        time_temp = []
        time = []
        for line in timecard:
            time_temp.append(line)
        for i in time_temp:
            time.append(i.split(','))
        for i in time:
            for q in range(len(i)):
                if q == 0:
                    pass
                else:
                    i[q] = float(i[q])
        for i in time:
            for q in range(len(i)):
                self.timecard[i[0]] = i[1:]
        #print(self.timecard)
        return self.timecard

    def process_receipts(self):
        """Reads sales receipts and saves them to a dictionary"""
        receipts = open('receipts.txt','r')
        rec_temp = []
        rec = []
        for line in receipts:
            rec_temp.append(line)
        for i in rec_temp:
            rec.append(i.split(','))
        for i in rec:
            for q in range(len(i)):
                if q == 0:
                    pass
                else:
                    i[q] = float(i[q])

        for i in rec:
            for q in range(len(i)):
                self.receipts[i[0]] = i[1:]
        #print(self.receipts)
        return self.receipts

    def classification(self):
        """Takes an employees id, and interprets their pay method for a readable dictionary"""
        for i in self.emp_id:
            if self.emp_dict[i][5] == "1":
                self.clsf[i] = "Hourly"
            elif self.emp_dict[i][5] == "2":
                self.clsf[i] = "Salaried"
            elif self.emp_dict[i][5] == "3":
                self.clsf[i] = "Commissioned"
            else:
                self.clsf[i] = "Error"

        #print(self.clsf)
        return self.clsf

    def paymethod(self):
        """Using an employee's id reads in their pay method into a readable dictionary"""
        for i in self.emp_dict:
            if self.emp_dict[i][6] == "1":
                self.pymthd[i] = "Direct Deposit"
            elif self.emp_dict[i][6] == "2":
                self.pymthd[i] = "Mailed Check"
            else:
                self.pymthd[i] = "Error"
        #print(self.pymthd)
        return self.pymthd

    def employee_id(self):
        """Makes a dictionary associating an employee's name with their id for ease of reading"""
        for i in self.emp_dict:
            self.emp_id[i] = self.emp_dict[i][0]
        #print(self.emp_id)
        return self.emp_id

    def find_employee_by_id(self,id):
        """Using an id, determine an employees name"""
        self.employee_id()
        if id in self.emp_id:
            print(self.emp_id[id])
            return self.emp_id[id]
        else:
            print("Employee not found")

    def find_employee_id(self,name):
        """Using an employees name, find their id"""
        nam = list(self.emp_id.values())
        val = nam.index(name)
        ids = list(self.emp_id.keys())
        id = ids[val]
        return id


    def make_salaried(self,salary,name):
        """Change an employees classification to a salaried employee"""
        id = self.find_employee_id(name)
        if id in self.clsf:
            self.emp_dict[id][5] = "2"
            print("{}{}".format(name," was successfully changed to be a salaried employee"))
            self.emp_dict[id][7] = salary
            self.classification()
            return self.emp_dict
        else:
            print("Error- employee not found")
        self.employee_data()

    def make_hourly(self,rate,name):
        """"Changes an employees classification to an hourly employee"""
        id = self.find_employee_id(name)
        if id in self.clsf:
            self.emp_dict[id][5] = "1"
            print("{}{}".format(name," was successfully changed to be an hourly employee"))
            self.emp_dict[id][8] = rate
            self.classification()
            return self.emp_dict
        else:
            print("Error- employee not found")
        self.employee_data()

    def make_commissioned(self,salary,commission,name):
        """Changes an employees classifcation to a commissioned employee"""
        id = self.find_employee_id(name)
        if id in self.clsf:
            self.emp_dict[id][5] = "3"
            print("{}{}".format(name," was successfully changed to be a commissioned employee"))
            self.emp_dict[id][7] = salary
            self.emp_dict[id][9] = commission
            self.classification()
            return self.emp_dict
        else:
            print("Error- employee not found")
        self.employee_data()

    def employee_data(self):
        """Makes a dictionary of pertinent data about an employee based on their classification and pay method"""
        self.paymethod()
        self.classification()
        for i in self.emp_id:
            if self.clsf[i] == "Salaried":
                if self.pymthd[i] == "Direct Deposit":
                    self.emp_data[i] = [self.clsf[i],self.pymthd[i],self.emp_dict[i][7],self.emp_dict[i][10],
                                         self.emp_dict[i][11]]
                elif self.pymthd[i] == "Mailed Check":
                    self.emp_data[i] = [self.clsf[i],self.pymthd[i],self.emp_dict[i][1],self.emp_dict[i][2],
                                        self.emp_dict[i][3], self.emp_dict[i][4],self.emp_dict[i][7]]
            elif self.clsf[i] == "Hourly":
                if self.pymthd[i] == "Direct Deposit":
                    self.emp_data[i] = [self.clsf[i],self.pymthd[i],self.emp_dict[i][8],self.emp_dict[i][10],
                                         self.emp_dict[i][11]]
                elif self.pymthd[i] == "Mailed Check":
                    self.emp_data[i] = [self.clsf[i],self.pymthd[i],self.emp_dict[i][1],self.emp_dict[i][2],
                                        self.emp_dict[i][3], self.emp_dict[i][4],self.emp_dict[i][8]]
            elif self.clsf[i] == "Commissioned":
                if self.pymthd[i] == "Direct Deposit":
                    self.emp_data[i] = [self.clsf[i],self.pymthd[i],self.emp_dict[i][7],self.emp_dict[i][9],
                                        self.emp_dict[i][10],self.emp_dict[i][11]]
                elif self.pymthd[i] == "Mailed Check":
                    self.emp_data[i] = [self.clsf[i],self.pymthd[i],self.emp_dict[i][1],self.emp_dict[i][2],
                                        self.emp_dict[i][3],self.emp_dict[i][4],self.emp_dict[i][7],self.emp_dict[i][9]]
            else:
                print("Error")
        print(self.emp_data)
        return self.emp_data

    def direct_method(self,routing,account,name):
        """Changes an employees pay method to direct deposit"""
        id = self.find_employee_id(name)
        if id in self.pymthd:
            self.pymthd[id] = "Direct Deposit"
            print("{}{}".format(name, " was successfully changed to Direct Deposit"))
            self.emp_dict[id][10] = routing
            self.emp_dict[id][11] = account
            return self.pymthd, self.emp_dict
        else:
            print("Error- employee not found")
        self.employee_data()

    def mail_method(self,address,city,state,zip,name):
        """Changes an employees pay method to receiving a check in the mail"""
        id = self.find_employee_id(name)
        if id in self.pymthd:
            self.pymthd[id] = "Mailed Check"
            print("{}{}".format(name, " was successfully changed to Mailed Check"))
            self.emp_dict[id][1] = address
            self.emp_dict[id][2] = city
            self.emp_dict[id][3] = state
            self.emp_dict[id][4] = zip
            return self.pymthd, self.emp_dict
        else:
            print("Error- employee not found")
        self.employee_data()

    def add_receipt(self,sale,name):
        """Add receipts of sale connected a specific employee"""
        id = self.find_employee_id(name)
        if id in self.receipts:
            self.receipts[id].append(sale)
        else:
            self.receipts[id] = [sale]
        return self.receipts

    def add_timecard(self,time,name):
        """Add times worked for a specific employee"""
        id = self.find_employee_id(name)
        if id in self.timecard:
            self.timecard[id].append(time)
        else:
            self.timecard[id] = [time]
        return self.timecard

    def issue_payment(self):
        """Pays an employee based on their classification and preferred pay method"""
        with open ('paylog.txt', 'w') as log:
            for i in self.emp_data:
                if self.emp_data[i][0] == "Hourly":
                    if self.emp_data[i][1] == "Direct Deposit":
                        hours = 0
                        for q in self.timecard[i]:
                            hours += q
                        pay = hours * float(self.emp_data[i][2])
                        pay = ("{0:.2f}".format(pay))
                        log.write("{}{}{}{}{}{}{}{}{}{}".format("Check for ",self.emp_id[i] ," for $",pay,
                                                          " deposited successfully into account number ",
                                                        self.emp_data[i][4]," routing number ",self.emp_data[i][3],
                                                              '\n','\n'))
                    elif self.emp_data[i][1] == "Mailed Check":
                        hours = 0
                        for q in self.timecard[i]:
                            hours += q
                        pay = hours * float(self.emp_data[i][6])
                        pay = ("{0:.2f}".format(pay))
                        log.write("{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format("Check for ", self.emp_id[i]," for $",pay,
                                                            " successfully sent to ", self.emp_data[i][2], " ",
                                                          self.emp_data[i][3],", " , self.emp_data[i][4]," ",
                                                                  self.emp_data[i][5],'\n','\n'))
                    else:
                        log.write("{}{}{}{}".format("Error with processing payment for ", self.emp_id[i],'\n','\n'))
                elif self.emp_data[i][0] == "Salaried":
                    if self.emp_data[i][1] == "Direct Deposit":
                        pay = float(self.emp_data[i][2]) / 24
                        pay = ("{0:.2f}".format(pay))
                        log.write("{}{}{}{}{}{}{}{}{}{}".format("Check for ",self.emp_id[i] ," for $",pay,
                                                          " deposited successfully into account number ",
                                                        self.emp_data[i][4]," routing number ",self.emp_data[i][3],
                                                              '\n','\n'))
                    elif self.emp_data[i][1] == "Mailed Check":
                        pay = float(self.emp_data[i][6]) / 24
                        pay = ("{0:.2f}".format(pay))
                        log.write("{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format("Check for ", self.emp_id[i]," for $",pay,
                                                            " successfully sent to ", self.emp_data[i][2], " ",
                                                          self.emp_data[i][3], ", ", self.emp_data[i][4]," ",
                                                                  self.emp_data[i][5],'\n','\n'))
                    else:
                        log.write("{}{}{}{}".format("Error with processing payment for ", self.emp_id[i],'\n','\n'))
                elif self.emp_data[i][0] == "Commissioned":
                    if self.emp_data[i][1] == "Direct Deposit":
                        commission = 0
                        for q in self.receipts[i]:
                            sale = float(q)
                            total = sale * (float(self.emp_data[i][3]) * 0.01)
                            commission += total
                        pay = commission + float(self.emp_data[i][2])
                        pay = ("{0:.2f}".format(pay))
                        log.write("{}{}{}{}{}{}{}{}{}{}".format("Check for ",self.emp_id[i] ," for $",pay,
                                                          " deposited successfully into account number ",
                                                        self.emp_data[i][4]," routing number ",self.emp_data[i][3],
                                                              '\n','\n'))
                    elif self.emp_data[i][1] == "Mailed Check":
                        commission = 0
                        for q in self.receipts[i]:
                            sale = float(q)
                            total = sale * (float(self.emp_data[i][7]) * 0.01)
                            commission += total
                        pay = commission + (float(self.emp_data[i][6]) / 24)
                        pay = ("{0:.2f}".format(pay))
                        log.write("{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format("Check for ", self.emp_id[i]," for $",pay,
                                                            " successfully sent to ", self.emp_data[i][2]," ",
                                                          self.emp_data[i][3],", ", self.emp_data[i][4]," ",
                                                                  self.emp_data[i][5], '\n','\n'))
                    else:
                        log.write("{}{}{}{}".format("Error with processing payment for ", self.emp_id[i],'\n','\n'))

    def run_payroll(self):
        """Runs the issue_payment() program, as well as ensuring all necessary data was initialized"""
        self.employee_id()
        self.classification()
        self.employee_data()
        self.paymethod()
        pay_logfile = "paylog.txt"
        if os.path.exists(pay_logfile):
            os.remove(pay_logfile)
        self.issue_payment()



def main():
    p = Payroll()
    p.load_employees()
    p.process_timecards()
    p.process_receipts()
    p.run_payroll()
    # Save copy of payroll file
    shutil.copyfile('paylog.txt', 'paylog1.txt')
    # Change Karina Gay to Salaried and DirectMethod by changing her Employee object:
    emp = p.find_employee_by_id('688997')
    p.make_salaried(45884.99, emp)
    p.direct_method('30417353-K', '465794-3611', emp)
    # Change TaShya Snow to Commissioned and MailMethod; add some receipts
    emp = p.find_employee_by_id('522759')
    p.make_commissioned(50005.50, 25, emp)
    p.mail_method("2624 Hendreit St.", "College", "AK", "99789", emp)
    clas = emp
    p.add_receipt(1109.73, clas)
    p.add_receipt(746.10, clas)
    # Change Rooney Alvarado to Hourly; add some hour entries
    emp = p.find_employee_by_id('165966')
    p.make_hourly(21.53, emp)
    clas = emp
    p.add_timecard(8.0, clas)
    p.add_timecard(8.0, clas)
    p.add_timecard(8.0, clas)
    p.add_timecard(8.0, clas)
    p.add_timecard(8.0, clas)
    # Rerun payroll
    p.run_payroll()


if __name__ == "__main__":
    main()