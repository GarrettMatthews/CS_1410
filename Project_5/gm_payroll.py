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
        print(self.timecard)
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
        print(self.receipts)
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
            return self.emp_id[id]
        else:
            print("Employee not found")

    def find_employee_id(self,name):
        nam = list(self.emp_id.values())
        val = nam.index(name)
        ids = list(self.emp_id.keys())
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
        self.employee_data()

    def make_hourly(self,rate,name):
        id = self.find_employee_id(name)
        if id in self.clsf:
            self.clsf[id] = "Hourly"
            print("{}{}".format(name," was successfully changed to be an hourly employee"))
            return self.clsf
        else:
            print("Error- employee not found")
        self.employee_data()

    def make_commissioned(self,salary,commission,name):
        id = self.find_employee_id(name)
        if id in self.clsf:
            self.clsf[id] = "Commissioned"
            print("{}{}".format(name," was successfully changed to be a commissioned employee"))
            return self.clsf
        else:
            print("Error- employee not found")
        self.employee_data()

    def employee_data(self):
        for i in self.emp_dict:
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
        id = self.find_employee_id(name)
        if id in self.pymthd:
            self.pymthd[id] = "Direct Deposit"
            print("{}{}".format(name, " was successfully changed to Direct Deposit"))
            return self.pymthd
        else:
            print("Error- employee not found")
        self.employee_data()

    def mail_method(self,address,city,state,zip,name):
        id = self.find_employee_id(name)
        if id in self.pymthd:
            self.pymthd[id] = "Mailed Check"
            print("{}{}".format(name, " was successfully changed to Mailed Check"))
            return self.pymthd
        else:
            print("Error- employee not found")
        self.employee_data()

    def add_receipt(self,sale,name):
        id = self.find_employee_id(name)
        if id in self.receipts:
            self.receipts[id].append(sale)
        else:
            self.receipts[id] = [sale]
        return self.receipts

    def add_timecards(self,time,name):
        id = self.find_employee_id(name)
        if id in self.timecard:
            self.timecard[id].append(time)
        else:
            self.timecard[id] = [time]
        return self.timecard

    def issue_payment(self):
        with open ('paylog.txt', 'w') as log:
            for i in self.emp_data():
                if self.emp_data[i][0] == "Hourly":
                    if self.emp_data[i][1] == "Direct Deposit":
                        hours = 0
                        for q in self.timecard[i]:
                            hours += q
                        pay = hours * float(self.emp_data[i][2])
                        log.write("{}{}{}{}{}{}{}{}".format("Check for ",self.emp_id[i] ," for $",pay,
                                                          " deposited successfully into account number ",
                                                        self.emp_data[i][4]," routing number ",self.emp_data[i][3]))
                    elif self.emp_data[i][1] == "Mailed Check":
                        hours = 0
                        for q in self.timecard[i]:
                            hours += q
                        pay = hours * float(self.emp_data[i][6])
                        log.write("{}{}{}{}{}{}{}{}".format("Check for ", self.emp_id[i]," for $",pay,
                                                            " successfully sent to", self.emp_data[i][2],
                                                          self.emp_data[i][3], self.emp_data[i][4], self.emp_data[i][5]))
                    else:
                        log.write("{}{}".format("Error with processing payment for ", self.emp_id[i]))
                elif self.emp_data[i][0] == "Salaried":
                    if self.emp_data[i][1] == "Direct Deposit":
                        pay = float(self.emp_data[i][2]) / 24
                        log.write("{}{}{}{}{}{}{}{}".format("Check for ",self.emp_id[i] ," for $",pay,
                                                          " deposited successfully into account number ",
                                                        self.emp_data[i][4]," routing number ",self.emp_data[i][3]))
                    elif self.emp_data[i][1] == "Mailed Check":
                        pay = float(self.emp_data[i][6]) / 24
                        log.write("{}{}{}{}{}{}{}{}".format("Check for ", self.emp_id[i]," for $",pay,
                                                            " successfully sent to", self.emp_data[i][2],
                                                          self.emp_data[i][3], self.emp_data[i][4], self.emp_data[i][5]))
                    else:
                        log.write("{}{}".format("Error with processing payment for ", self.emp_id[i]))
                elif self.emp_data[i][0] == "Commissioned":
                    if self.emp_data[i][1] == "Direct Deposit":
                        commission = 0
                        for q in self.receipts[i]:
                            sale = float(q)
                            total = sale * (float(self.emp_data[i][3]) * 0.01)
                            commission += total
                        pay = commission + float(self.emp_data[i][2])
                        log.write("{}{}{}{}{}{}{}{}".format("Check for ",self.emp_id[i] ," for $",pay,
                                                          " deposited successfully into account number ",
                                                        self.emp_data[i][4]," routing number ",self.emp_data[i][3]))
                    elif self.emp_data[i][1] == "Mailed Check":
                        commission = 0
                        for q in self.receipts[i]:
                            sale = float(q)
                            total = sale * (float(self.emp_data[i][7]) * 0.01)
                            commission += total
                        pay = commission + float(self.emp_data[i][6])
                        log.write("{}{}{}{}{}{}{}{}".format("Check for ", self.emp_id[i]," for $",pay,
                                                            " successfully sent to", self.emp_data[i][2],
                                                          self.emp_data[i][3], self.emp_data[i][4], self.emp_data[i][5]))
                    else:
                        log.write("{}{}".format("Error with processing payment for ", self.emp_id[i]))



def main():
    p = Payroll()
    p.load_employees()
    p.classification()
    p.paymethod()
    p.employee_id()
    emp = p.find_employee_by_id('522759')
    p.make_hourly(22,emp)
    p.employee_data()
    p.add_receipt(15.67,emp)
    p.add_receipt(16.77,emp)
    p.process_receipts()
    p.add_timecards(8.0,emp)
    p.add_timecards(6.7,emp)
    p.process_timecards()

if __name__ == "__main__":
    main()