import csv

class Payroll (object):
    def __init__(self):
        pass

    def load_employees(self):
        """Reads the data list from employees.csv and makes a dictionary of lists for each employee"""
        self.emp_dict = {}
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
        for i in range(len(employee)):
            employee[i] = int(employee[i])
        for i in range(26):
            data_temp = data_1[(i * 12):((i + 1) * 12)]
            data.append(data_temp)
        for i in range(len(employee)):
            self.emp_dict[employee[i]] = data[i]
        print(self.emp_dict)

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
                    i[q] = int(i[q])
                else:
                    i[q] = float(i[q])
        self.timecard = {}
        for i in time:
            for q in range(len(i)):
                self.timecard[i[0]] = i[1:]

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
                    i[q] = int(i[q])
                else:
                    i[q] = float(i[q])
        self.receipts = {}
        for i in rec:
            for q in range(len(i)):
                self.receipts[i[0]] = i[1:]
        print(self.receipts)


def main():
    p = Payroll()
    #p.load_employees()
    #p.process_timecards()
    p.process_receipts()

if __name__ == "__main__":
    main()