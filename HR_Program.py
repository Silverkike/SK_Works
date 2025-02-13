# Human Resource Program 
with open("hr_system.txt") as file:
    for line in file:
        splitted_line = line.split()
        name = splitted_line[0]
        idn = splitted_line[1]
        job = splitted_line[2]
        salary  = splitted_line[3]
        salary = float(salary)
        if job != "Engineer":
            paycheck = (salary / 12) / 2
            print(f"{name} (ID: {idn}), {job} - ${paycheck:.2f}")
        else:
            paycheck = ((salary / 12) / 2) + 1000
            print(f"{name} (ID: {idn}), {job} - ${paycheck:.2f}")