from tabulate import tabulate
#################################### Employee database #########################################################

employeeDataBase = [
    {
        'Employee Number' : '001', 
        'Family Name' : 'Alcaff',
        'First Name': 'Wanty',  
        'Sex' : 'Female',
        'Age' : 40, 
        'Position' : 'Internal Manager',
        'Address' : 'Park View Residence, Tangerang'
    },
    {
        'Employee Number' : '002', 
        'Family Name' : 'Zainal',
        'First Name' : 'Sjahrial',
        'Sex' : 'Male',
        'Age' : 45, 
        'Position' : 'Extrnal Manager',
        'Address' : 'Jl. Peta Barat, Jakarta Barat'
    },
    {
        'Employee Number' : '003', 
        'Family Name' : 'Christinawati',
        'First Name' : 'Christinawati',
        'Sex' : 'Female',
        'Age' : 40, 
        'Position' : 'Marketing Manager',
        'Address' : 'Jl. Bawang, Bekasi'
    },
    {
        'Employee Number' : '004', 
        'Family Name' : 'Erlinawati',
        'First Name' : 'Erlinawati', 
        'Sex' : 'Female',
        'Age' : 35, 
        'Position' : 'Sales Representative',
        'Address' : 'Jl. Kelinci, Bekasi '
    },
    {
        'Employee Number' : '005', 
        'Family Name' : 'Mulyono',
        'First Name' : 'Sugeng',
        'Sex' : 'Male',
        'Age' : 30, 
        'Position' : 'Software Engineer',
        'Address' : 'Asyri Green Properties 3 '
    }
]

############################################# Employee Database #########################################################
def dataBase():
    if employeeDataBase == []:
        print('''
              Employee database can not be found!
              ''')
    else:
            print('''--------------------------------------------"Maju Terus Enggan Mundur (MTEM)" Company Employee Database-------------------------------------------- ''')
            print(tabulate(employeeDataBase,headers="keys",tablefmt="fancy_grid"))
            # |Employee Number\t|Name\t\t\t|Sex\t\t|Age\t\t|Position\t\t\t|Address''')
            # for i in range (len(employeeDataBase)):
            #     print(f'''\t\t|{employeeDataBase[i]['Employee Number']}\t\t\t|{employeeDataBase[i]['Name']}\t\t\t|{employeeDataBase[i]['Sex']}\t\t|{employeeDataBase[i]['Age']}\t\t|{employeeDataBase[i]['Position']}\t\t|{employeeDataBase[i]['Address']}''')
        
# #################################### Feature 1: Call Database ######################################################### 
def callDataBase():
    while (True):
        print('''
          Employee database menu:
          1. Employee Database Report 
          2. Search Employee Database
          3. Back to main menu
              ''')
        dataInput = input('''
          Please choose one of the menu (1 to 3): ''')
        if dataInput == '1':
            dataBase()
        elif dataInput == '2':
            inputName = input('''
            Insert employee's First Name: ''').capitalize()
            for i in range (len(employeeDataBase)):
                if (inputName == employeeDataBase[i]['First Name']):
                    print('''
            Employee's name is found! The detail information is:
                          ''') 
                    table = [employeeDataBase[i]]
                    print(tabulate(table,headers="keys",tablefmt="fancy_grid"))
                else:
                    if i == len(employeeDataBase)-1:
                        print(f'''
            Employe's name : {inputName} can not be found!
            Please recheck the spelling!
                              ''')
        elif dataInput == '3':
            print('''
          You will be back to main menu!
          Thank you!''')
            break
        else:
            print('You are incorrectly insert the answer, reinput your answer!')

# ################################## Feature 2: Add Employee Database ##################################################### 
def addDataBase():
    while(True):
        existancy = []
        print('''
              Add employee database menu
              1. Add employee database
              2. Back to main menu''')
        dataInput = input('''
          Please choose one of the menu (1 to 2): ''')
        if dataInput == '1':
            employeeNumber = str(input('''
              Insert the employee number: '''))
            for i in range (len(employeeDataBase)):
                if (employeeNumber == employeeDataBase[i]['Employee Number']):
                        existancy =[employeeNumber]
                        print(f'''
                Employee Number is already exist.
                The last employee number is {employeeDataBase[len(employeeDataBase)-1]['Employee Number']} ''')
                else:
                    if existancy == [] and i == len(employeeDataBase)-1:
                        employeeFamilyName = input('Insert the employee family name: ').capitalize()
                        employeeFirstName = input('Insert the employee first name: ').capitalize()
                        employeeGender = input('Insert the employee gender (Male/Female): ').capitalize()
                        employeeAge = int(input('Insert the employee age: '))
                        employeePosition = input('Insert the employee position: ').capitalize
                        employeeAddress = (input('Insert the employee Adress: ')).capitalize
                        print('''
            Detail of new employee database:''')
                        table = [
                            {'Employee Number' : employeeNumber, 
                             'Family Name' : employeeFamilyName,
                             'First Name': employeeFirstName,  
                             'Sex' : employeeGender,
                             'Age' : employeeAge , 
                             'Position' : employeePosition,
                             'Address' : employeeAddress
                             }
                             ]
                        print(tabulate(table,headers="keys",tablefmt="fancy_grid"))
                        # \t|Employee Number\t!Name\t|Sex\t\t|Age\t\t|Position\t\t\t|Address
                        # \t|{employeeNumber}\t\t\t|{employeeName}\t\t|{employeeGender}\t\t|{employeeAge}\t\t|{employeePosition}\t\t|{employeeAddress}''')
                        while (True):
                            confirmation = input('Are you sure input the new employee database?(Yes/No): ')
                            if confirmation == 'Yes':
                                employeeDataBase.append({
                                'Employee Number' : employeeNumber, 
                                'Family Name' : employeeFamilyName,
                                'First Name' : employeeFirstName, 
                                'Sex' : employeeGender,
                                'Age' : employeeAge,
                                'Position' : employeePosition,
                                'Address' : employeeAddress    
                                })
                                break
                            elif confirmation == 'No':
                                print('''
                                New employee database is not added
                                You will be back to "Add employee database menu"      ''')
                                break
                            else:
                                print('You are incorrectly insert the answer, reinput your answer!')
                        dataBase()
                    #     for i in range (len(employeeDataBase)):
                    #         print(f'''
                    # \t|Employee Number\t|Name\t\t|Sex\t\t|Age\t\t|Position\t\t\t|Address
                    # \t|{employeeDataBase[i]['Employee Number']}\t\t\t|{employeeDataBase[i]['Name']}\t\t\t|{employeeDataBase[i]['Sex']}\t\t|{employeeDataBase[i]['Age']}\t\t|{employeeDataBase[i]['Position']}\t\t|{employeeDataBase[i]['Address']}
                    #             ''')
        elif dataInput == '2':
            print('''
          You will be back to main menu!
          Thank you!''')
            break
        else:
            print('You are incorrectly insert the answer, reinput your answer!')

# ################################## Feature 3: Update employee Database ##################################################### 
def updateDataBase():
    while (True):
        print('''
              Update employee database menu
              1. Update employee database
              2. Back to main menu''')
        dataInput = input('''
          Please choose one of the menu (1 to 2): ''')
        if dataInput == '1':
            dataBase()
            employeeNumber = input('Input Employee Number that will be changed: ')
            for i in range (len(employeeDataBase)):
                if (employeeNumber == employeeDataBase[i]['Employee Number']):
                    print(f'''
                Employee Number is found!''')
                    condition = input(f'''
                Are you sure to change the employee database with employee number {employeeNumber}?(Yes/No): 
                                        ''')
                    if condition == 'Yes':
                        print('''
                                Employee database information : 
                                1. Employee Number
                                2. Employee Family Name
                                3. Employee First Name
                                4. Employee Gender
                                5. Employee Age
                                6. Employee Position
                                7. Employee Address
                                 ''')
                        dataInput = input('''
                                   Please choose one of the menu (1 to 6): 
                                   ''')
                        if dataInput == '1':
                            newEmployeeNumber = input('''
                                                      Insert new Employee Number: 
                                                      ''')
                            decission = input('''
                                  Are you sure to change the employee number?(Yes/No): 
                                  ''')
                            if decission == 'Yes':
                                employeeDataBase[i]['Employee Number'] = newEmployeeNumber
                            elif decission == 'No':
                                print('''
                                      Update employee data Number is canceled
                                      ''')
                            else:
                                print('You are incorrectly insert the answer, reinput your answer!')
                                break
                        elif dataInput == '2':
                            newEmployeeFamilyName = input('''
                                                      Insert new Employee Family Name: 
                                                      ''')
                            decission = input('''
                                  Are you sure to change the employee Family name?(Yes/No): 
                                  ''')
                            if decission == 'Yes':
                                employeeDataBase[i]['Family Name'] = newEmployeeFamilyName
                            elif decission == 'No':
                                print('''
                                      Update employee data Family Name is canceled
                                      ''')
                            else:
                                print('You are incorrectly insert the answer, reinput your answer!')
                                break
                        elif dataInput == '3':
                            newEmployeeFirstName = input('''
                                                      Insert new Employee First Name: 
                                                      ''')
                            decission = input('''
                                  Are you sure to change the employee First name?(Yes/No): 
                                  ''')
                            if decission == 'Yes':
                                employeeDataBase[i]['First Name'] = newEmployeeFirstName
                            elif decission == 'No':
                                print('''
                                      Update employee data First Name is canceled
                                      ''')
                            else:
                                print('You are incorrectly insert the answer, reinput your answer!')
                                break    
                        elif dataInput == '4':
                            newEmployeeGender = input('''
                                                      Insert new Employee Gender: 
                                                      ''')
                            decission = input('''
                                  Are you sure to change the employee gender?(Yes/No): 
                                  ''')
                            if decission == 'Yes':
                                employeeDataBase[i]['Sex'] = newEmployeeGender
                            elif decission == 'No':
                                print('''
                                      Update employee data Gender is canceled
                                      ''')
                            else:
                                print('You are incorrectly insert the answer, reinput your answer!')
                                break
                        elif dataInput == '5':
                            newEmployeeAge = int(input('''
                                                      Insert new Employee Age: 
                                                      '''))
                            decission = input('''
                                  Are you sure to change the employee age?(Yes/No): 
                                  ''')
                            if decission == 'Yes':
                                employeeDataBase[i]['Age'] = newEmployeeAge
                            elif decission == 'No':
                                print('''
                                      Update employee data Age is canceled
                                      ''')
                            else:
                                print('You are incorrectly insert the answer, reinput your answer!')
                                break
                        elif dataInput == '6':
                            newEmployeePosition = int(input('''
                                                      Insert new Employee Position: 
                                                      '''))
                            decission = input('''
                                  Are you sure to change the employee Position?(Yes/No): 
                                  ''')
                            if decission == 'Yes':
                                employeeDataBase[i]['Position'] = newEmployeePosition
                            elif decission == 'No':
                                print('''
                                      Update employee data Position is canceled
                                      ''')
                            else:
                                print('You are incorrectly insert the answer, reinput your answer!')
                                break     
                        elif dataInput == '7':
                            newEmployeeAddress = int(input('''
                                                      Insert new Employee Address: 
                                                      '''))
                            decission = input('''
                                  Are you sure to change the employee Address?(Yes/No): 
                                  ''')
                            if decission == 'Yes':
                                employeeDataBase[i]['Address'] = newEmployeeAddress
                            elif decission == 'No':
                                print('''
                                      Update employee data Address is canceled
                                      ''')
                            else:
                                print('You are incorrectly insert the answer, reinput your answer!')
                                break
                        else:
                            print('''
                                  You are incorrectly insert the answer, reinput your answer!
                                  ''')
                    elif condition == 'No':
                        print('''The process is canceled!
                              You will be back to "Update employee database menu"): 
                              ''')
                        break
                    else:
                        print('You are incorrectly insert the answer, reinput your answer!')
            dataBase()       
        elif dataInput == '2':
            print('''
          You will be back to main menu!
          Thank you!''')
            break
        else:
            print('You are incorrectly insert the answer, reinput your answer!')

# ################################## Feature 4: Update employee Database ##################################################### 
def deleteDatabase():
    while (True):
        print('''
              Delete employee database menu
              1. Delete employee database
              2. Back to main menu''')
        dataInput = input('''
          Please choose one of the menu (1 to 2): ''')
        if dataInput == '1':
            dataBase()
            employeeNumber = input('Input Employee Number that will be changed: ')
            for i in range (len(employeeDataBase)):
                if (employeeNumber == employeeDataBase[i]['Employee Number']):
                    print(f'''
                Employee Number is found!''')
                    condition = input(f'''
                Are you sure to delete the employee database with employee number {employeeNumber}?(Yes/No): 
                                        ''')
                    if condition == 'Yes':
                        del employeeDataBase[i]
                    elif condition == 'No':
                        print(('''The process is canceled!
                              You will be back to "Delete employee database menu"): 
                              '''))
                        break
                    else:
                        print('You are incorrectly insert the answer, reinput your answer!')
            dataBase()
        elif dataInput == '2':
             print('''
          You will be back to main menu!
          Thank you!''')
             break
        else:
            print('You are incorrectly insert the answer, reinput your answer!')

#################################################### Main Menu #############################################################               
def mainMenu():
    while(True):
        print('''
            ---------------------Welcome to "Maju Terus Enggan Mundur (MTEM)" Company--------------------- 
            Features:
            1. Employee Database 
            2. Add Employee Database 
            3. Update Employee Database 
            4. Delete Employee Database
            5. Exit''')
        dataInput = input('''
            Please choose one of the features (1 to 5): ''')
        if dataInput == '1':
            callDataBase()  
        elif dataInput == '2':
            addDataBase()
        elif dataInput == '3':
            updateDataBase()
        elif dataInput == '4':
            deleteDatabase()
        elif dataInput == '5':
            print('''
                  Thank you for coming''')
            break
        else:
            print('''
                ---------------------You are incidently input incorrect number---------------------
                ----------------------Please reinput the correct number (1 to 5)-------------------
                ''')

print(mainMenu())
