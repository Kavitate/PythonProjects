employees = []
count = 0

def export_emp(employees):
  fopen = open("EmployeeDatabase.txt", "a")
  for employee in employees:
    for i in employee:
      fopen.write(i+" ")
    fopen.write("\n")
  fopen.close()

def import_emp(fname):
  temp = []
  fopen = open(fname,"r")
  for line in fopen:
    line = line.strip()
    if len(line) != 0:
      line = line.split()
      temp.append(line)
  fopen.close()
  return temp

def Add_Employee():
  global count
  Employee = []
  count += 1
  print('Enter name of employee: ',end='')
  Employee.append(input())
  print('Enter employee SSN: ',end='')
  Employee.append(input())
  print('Enter employee phone number: ',end='')
  Employee.append(input())
  print('Enter employee email: ',end='')
  Employee.append(input())
  print('Enter employee salary: $',end='')
  Employee.append(input())
  employees.append(Employee)
  import os
  os.system('cls' if os.name == 'nt' else "printf '\033c'")

def view_all_Employees(employees):
  for i in employees:
    print('---------------------------- '+i[0]+' ---------------------------------------')
    print('SSN: ', i[1])
    print('Phone: ', i[2])
    print('Email: ', i[3])
    print('Salary: ', i[4])
    print('------------------------------------------------------------------------')

def search_Employee(ssn):
  findIdex = 0
  for i in employees:
    if(i[1]==ssn):
      return findIdex
    findIdex+=1
  return-1

def main():
  global count
  global employees
while(True):
  print("------------------------ Employee Management System ----------------------------\n")
  print('Enter -1 to exit')
  print('\nThere are (',count,') employees in the database.')
  print('--------------------------------------------------------------------------------')
  print('1. Add new employee.\n')
  print('2. View all employees.\n')
  print('3. Search employee by SSN.\n')
  print('4. Edit employee information.\n')
  print('5. Export employees information into a text file.\n')
  print('6. Import employees information from a text file.')
  print('---------------------------------------------------------------------------------\n')
  print('Please enter your option number: ', end="")
  a=int(input())
  import os
  os.system('cls' if os.name == 'nt' else "printf '\033c'")
  if(a==-1):
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    quit()
  elif (a==1):
    Add_Employee()
    print()
  elif(a==2):
    view_all_Employees(employees)
    print()
    input("Press ENTER to return to the main menu.")
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
  elif(a==3):
    ssn=input("Enter Employee SSN: ")
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    empIndex=search_Employee(ssn)
    if(empIndex>=0):
      print("---------------------------- "+employees[empIndex][0]+" ---------------------------------------")
      print('SSN:',employees[empIndex][1])
      print('Phone:',employees[empIndex][2])
      print('Email:',employees[empIndex][3])
      print('Salary:',employees[empIndex][4])
      print("------------------------------------------------------------------------\n")
      input("Press ENTER to return to the main menu.")
      import os
      os.system('cls' if os.name == 'nt' else "printf '\033c'")
    else:
      import os
      os.system('cls' if os.name == 'nt' else "printf '\033c'")
      print("Employee "+ssn+" not found.\n")
      input("Press ENTER to return to the main menu.")
      import os
      os.system('cls' if os.name == 'nt' else "printf '\033c'")
  elif(a==4):
    ssn=input("Enter the SSN of the employee you would like to update: ")
    empIndex=search_Employee(ssn)
    if(empIndex>=0):
      employees[empIndex][0]=input("Enter updated name: ")
      employees[empIndex][2]=input("Enter updated phone number: ")
      employees[empIndex][3]=input("Enter updated email address: ")
      employees[empIndex][4]=input("Enter updated salary: $")
      print("\nEmployee information has been updated successfully.\n")
      input("Press ENTER to return to the main menu.")
      import os
      os.system('cls' if os.name == 'nt' else "printf '\033c'")
    else:
      import os
      os.system('cls' if os.name == 'nt' else "printf '\033c'")
      print("Employee with "+ssn+" is not found.\n")
      input("Press ENTER to return to the main menu.")
      import os
      os.system('cls' if os.name == 'nt' else "printf '\033c'")
  elif(a==5):
    export_emp(employees)
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Data Successfully Exported.\n")
    input("Press ENTER to return to the main menu.")
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
  elif(a==6):
    employees = import_emp("EmployeeDatabase.txt")
    count = count + len(employees)
    print("Data Successfully Loaded.\n")
    input("Press ENTER to return to the main menu.")
  else:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print('Invalid option.\n')
    input("Press ENTER to return to the main menu.")
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

main ()
