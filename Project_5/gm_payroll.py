import csv

class Payroll (object):
    def __init__(self):
        self.emp_dict = {}
        self.timecard = {}
        self.receipts = {}
        self.clsf = {}
        self.pymthd = {}
        self.emp_id = {}

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
        return self.emp_dict

    def process_timecards(self):
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
        return self.timecard

    def process_receipts(self):
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
        return self.receipts

    def classification(self):
        for i in self.emp_dict:
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

    def employee_id(self):
        for i in self.emp_dict:
            self.emp_id[i] = self.emp_dict[i][0]
        #print(self.emp_id)
        return self.emp_id

    def find_employee_by_id(self,id):
        if id in self.emp_id:
            print(self.emp_id[id])
        else:
            print("Employee not found")

    def find_employee_id(self,name):
        nam = self.emp_id.values()
        val = nam.index(name)
        ids = self.emp_id.keys()
        id = ids[val]
        return id


    def make_salaried(self,salary,name):
        id = self.find_employee_id(name)
        if id in self.clsf:
            self.clsf[id] = "Salaried"
            print("{}{}".format(name," was successfully changed to be a salaried employee"))
            return self.clsf
        else:
            print("Error- employee not found")

    def make_hourly(self,rate,name):
        id = self.find_employee_id(name)
        if id in self.clsf:
            self.clsf[id] = "Hourly"
            print("{}{}".format(name," was successfully changed to be an hourly employee"))
            return self.clsf
        else:
            print("Error- employee not found")

    def make_commissioned(self,salary,commission,name):
        id = self.find_employee_id(name)
        if id in self.clsf:
            self.clsf[id] = "Commissioned"
            print("{}{}".format(name," was successfully changed to be a commissioned employee"))
            return self.clsf
        else:
            print("Error- employee not found")




def main():
    p = Payroll()
    p.load_employees()
    p.process_timecards()
    p.process_receipts()
    p.classification()
    p.paymethod()
    p.employee_id()
    emp = p.find_employee_by_id('688997')
    emp.make_salaried(45884.99)

if __name__ == "__main__":
    main()