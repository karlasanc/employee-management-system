# (global variables)
employee_counter = 0
employees = []

# enter employee info
def get_employee_info(): 
  employee_name = input("\n\tEnter employee name: ")
  employee_ssn = input("\tEnter employee SSN: ")
  employee_phone = input("\tEnter employee phone: ")
  employee_email = input("\tEnter employee email: ")
  employee_salary = input("\tEnter employee salary: ")

  return [employee_name, employee_ssn, employee_phone, employee_email, employee_salary]

# display employee info (formatted)
def display_employee_info(employee_info): 
  name, ssn, phone, email, salary = employee_info
  print("\n\tName: ", name)
  print("\tSSN: ", ssn)
  print("\tPhone: ", phone)
  print("\tEmail: ", email)
  print("\tSalary: ${}".format(salary))

# add employee to system
def add_employee(): 
  global employee_counter
  if employee_counter >= 5:
    print("\nMaxium number of employees reached.")
    return
  employee_info = get_employee_info()
  employees.append(employee_info)
  employee_counter += 1

  print("\n\tEmployee added successfully.")
  print(f"\n\tThere are now {employee_counter} employees in the system.")

  input("\n\tPress Enter to continue...") # pause system for user

# view all employees in system
def view_all_employees():
  for index, employee_info in enumerate(employees, 1):
    print(f"\n\t----- Employee {index}", end="-----")
    display_employee_info(employee_info)
  input("\n\tPress Enter to Return to Main Menu...")

# search employee by SSN
def search_employee(ssn):
  found = False
  for employee_info in employees:
    if ssn in employee_info[1]:
      found = True
      display_employee_info(employee_info)
      break
  if not found:
    print("\n\tEmployee not found.")
  input("\n\tPress Enter to Return to Main Menu...")

# update employee info
def update_employee_info(ssn):
  found_employee = None
  for employee_info in employees:
    if ssn in employee_info[1]:
      found_employee = employee_info
      display_employee_info(found_employee)
      confirm = input("\n\tIs this the employee you want to update? (yes/no): ")
      if confirm == "yes": 
        print("\n\tEnter new employee information:")
        found_employee[0] = input("\n\tEmployee name: ")
        found_employee[2] = input("\tEmployee phone: ")
        found_employee[3] = input("\tEmployee email: ")
        found_employee[4] = input("\tEmployee salary: ")
        print("\n\tEmployee information updated successfully.")
        return
      else: 
        print("\n\tUpdate cancelled.")
        input("\n\tPress enter to return to main menu...")
        return
  print("\n\tEmployee not found with provided SSN.")

  input("\n\tPress enter to return to main menu...")

# export employee info to text file
def export_employee_info():
  with open("employee.txt", "w") as file:  # file outside project folder
    for employee_info in employees:
      file.write(", ".join(employee_info) + "\n")
  print("\n\tEmployee information exported successfully.")
  input("\n\tPress enter to return to main menu...")

# import employee info from text file
def import_employee_info():
  global employee_counter, employees # declare global variables
  try:
    with open("employee.txt", "r") as file: # external file
      lines = file.readlines()
      for line in lines:
        employee_info = line.strip().split(", ")
        employees.append(employee_info)
        employee_counter += 1
      print("\n\tEmployee information imported successfully.")
      input("\n\tPress enter to return to main menu...")
  except FileNotFoundError:
    print("\n\tNo pre-existing employee information found.")
    input("\n\tPress enter to return to main menu...")


# main function
def main():
  global employees, employee_counter #declare global variables

  # continous execution of python script using while loop
  while True:
    #display menu & options
    print("\n" * 5) 
    print("-" * 17, "Employee Management System", "-" * 17)
    print("\n", "\t" * 2, f"There are ({employee_counter}) employees in the system.")

    print("\n\t1. Add new employee")
    print("\t2. View all employees")
    print("\t3. Search employee by SSN")
    print("\t4. Update employee information")
    print("\t5. Export employees' information into a text file")
    print("\t6. Import employees' information into a text file")
    print("\t0. Exit Application")
    print("-" * (36 + len("Employee Management System")))
    print("\n" * 5)

    # request choice from user
    choice = input("\n\tPlease enter your choice: ")
    print("\n" * 20) 

    # check user choice & call appropriate function
    if choice == "1":
      print("\n", "-" * 24, "New Employee","-" * 23)
      add_employee()

    elif choice == "2":
      print("\n", "-" * 19, "Employee Information","-" * 19)
      view_all_employees()

    elif choice == "3":
      print("\n", "-" * 18, "Search Employees by SSN","-" * 18)
      ssn = input("\n\tEnter employee SSN: ")
      search_employee(ssn)

    elif choice == "4":
      print("\n", "-" * 18, "Update Employees Information","-" * 18)
      ssn = input("\n\tEnter employee SSN: ")
      update_employee_info(ssn)

    elif choice == "5":
      print("\n", "-" * 15, "Export Employees Information From File","-" * 15)
      export_employee_info()

    elif choice == "6": 
      print("\n", "-" * 15, "Import Employee Information From File","-" * 15)
      import_employee_info()

    elif choice == "0":
      print("\n", "-" * 15, "End of Program","-" * 15)
      break
    else:
      print("\nInvalid choice. Please enter a valid option.")

# call main function
main()