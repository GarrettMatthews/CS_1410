import os
import shutil

class Payroll (object):
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

    def employee_id(self):
        for i in self.emp_dict:
            self.emp_id[i] = self.emp_dict[i][0]
            #print(i)
        #print(self.emp_id)
        return self.emp_id

    def make_salaried(self, salary, name):
        id = self.find_employee_id(name)
        if id in self.clsf:
            self.emp_dict[id][5] = "2"
            print("{}{}".format(name, " was successfully changed to be a salaried employee"))
            self.emp_dict[id][7] = salary
            self.classification()
            return self.emp_dict
        else:
            print("Error- employee not found")
        self.employee_data()

    def employee_data(self):
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

    def classification(self):
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
        for i in self.emp_dict:
            if self.emp_dict[i][6] == "1":
                self.pymthd[i] = "Direct Deposit"
            elif self.emp_dict[i][6] == "2":
                self.pymthd[i] = "Mailed Check"
            else:
                self.pymthd[i] = "Error"
        #print(self.pymthd)
        return self.pymthd



def main():
    p = Payroll()
    p.load_employees()
    p.employee_id()
    p.classification()
    p.paymethod()
    p.employee_data()
    #p.make_salaried("5","688997")


if __name__ == "__main__":
    main()