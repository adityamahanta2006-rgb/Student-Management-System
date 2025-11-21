import pickle


def set_data():
    print("ENTER STUDENT'S DETAILS")
    rollno = int(input('Enter roll number: '))
    name = input('Enter name: ')
    english = int(input('Enter Marks in English: '))
    maths = int(input('Enter Marks in Maths: '))
    physics = int(input('Enter Marks in Physics: '))
    chemistry = int(input('Enter Marks in Chemistry: '))
    cs = int(input('Enter Marks in CS: '))
    print()
    
    #create a dictionary
    student = {}
    student['rollno'] = rollno
    student['name'] = name
    student['english'] = english
    student['maths'] = maths
    student['physics'] = physics
    student['chemistry'] = chemistry
    student['cs'] = cs
    return student


def display_data(student):
    print('\nSTUDENT DETAILS..')
    print('Roll Number:', student['rollno'])
    print('Name:', student['name'])
    print('English:', student['english'])
    print('Maths:', student['maths'])
    print('Physics:', student['physics'])
    print('Chemistry:', student['chemistry'])
    print('CS:', student['cs'])

def display_data_tabular(student):
    print(student['rollno'], end='\t')
    print(student['name'], end='\t\t')
    print(student['english'], end='\t\t')
    print(student['maths'], end='\t\t')
    print(student['physics'], end='\t\t')
    print(student['chemistry'], end='\t\t')
    print(student['cs'])

def class_result():
    # open file in binary mode for reading
    try:
        infile = open('student.dat', 'rb')
    except FileNotFoundError:
        print('No record found..')
        print('Go to admin menu to create record')
        return

    print('Rollno\tName\t\tEnglish\t\tMaths\t\tPhysics\t\tChemistry\tCS')
    # read to the end of the file
    while True:
        try:
            # reading the object from the file
            student = pickle.load(infile)

            # display the record
            display_data_tabular(student)
        except EOFError:
            break

    # close the file
    infile.close()

def write_record():
    #open file in binary mode for writing.
    outfile = open('student.dat', 'ab')
    
    while(True):
        #serialize the record and writing to file
        pickle.dump(set_data(), outfile)
        ans = input('Wants to enter more record (y/n)?: ')
        if ans in 'nN':
            break

    #close the file
    outfile.close()


def read_records():
    #open file in binary mode for reading
    try:
        infile = open('student.dat', 'rb')
    except FileNotFoundError:
        print('No record found..')
        return

    #read to the end of file.
    while True:
        try:
            #reading the oject from file
            student = pickle.load(infile)

            #display the record
            display_data(student)
        except EOFError:
            break

    #close the file
    infile.close()

def search_record():
    #open file in binary mode for reading
    try:
        infile = open('student.dat', 'rb')
    except FileNotFoundError:
        print('No record..')
        return

    found = False
    print('SEARCH RECORD')
    rollno = int(input('Enter the rollno you want to search: '))
    #read to the end of file.
    while True:
        try:
            #reading the oject from file
            student = pickle.load(infile)
            if student['rollno'] == rollno:
                #display the record
                display_data(student)
                found = True
                break
        except EOFError:
            break
    if found==False:
        print('Record not found!!')

    #close the file
    infile.close()

def delete_record():
    print('DELETE RECORD')

    try:
        infile = open('student.dat', 'rb')
    except FileNotFoundError:
        print('No record found to delete..')
        return

    found = False
    rollno = int(input('Enter roll number:'))

    # Read all records into memory
    records = []
    while True:
        try:
            student = pickle.load(infile)
            if student['rollno'] == rollno:
                display_data(student)
                found = True
            else:
                records.append(student)
        except EOFError:
            break

    infile.close()

    if not found:
        print('Record not Found')
        return
        
    # Rewrite the file without the deleted record
    with open('student.dat', 'wb') as outfile:
        for record in records:
            pickle.dump(record, outfile)

    print("Record found and deleted")



def modify_record():
    print('\nMODIFY RECORD')    
    try:
        infile = open('student.dat', 'rb')
    except FileNotFoundError:
        print('No record found to modify..')
        return

    found = False
    temp_records = []
    rollno = int(input('Enter roll number: '))
    
    while True:
        try:
            student = pickle.load(infile)
            if student['rollno'] == rollno:
                display_data(student)

                print('Name:', student['name'])
                ans = input('Wants to edit(y/n)? ')
                if ans.lower() == 'y':
                    student['name'] = input("Enter the name: ")

                print('English marks:', student['english'])
                ans = input('Wants to edit(y/n)? ')
                if ans.lower() == 'y':
                    student['english'] = int(input("Enter new marks: "))

                print('Maths marks:', student['maths'])
                ans = input('Wants to edit(y/n)? ')
                if ans.lower() == 'y':
                    student['maths'] = int(input("Enter new marks: "))

                print('Physics marks:', student['physics'])
                ans = input('Wants to edit(y/n)? ')
                if ans.lower() == 'y':
                    student['physics'] = int(input("Enter new marks: "))

                print('Chemistry marks:', student['chemistry'])
                ans = input('Wants to edit(y/n)? ')
                if ans.lower() == 'y':
                    student['chemistry'] = int(input("Enter new marks: "))

                print('CS marks:', student['cs'])
                ans = input('Wants to edit(y/n)? ')
                if ans.lower() == 'y':
                    student['cs'] = int(input("Enter new marks: "))

                found = True

            temp_records.append(student)
        except EOFError:
            break

    infile.close()

    if not found:
        print('Record not Found')
        return

    # Rewrite the file without the modified record
    with open('student.dat', 'wb') as outfile:
        for record in temp_records:
            pickle.dump(record, outfile)

    print('Record updated')

def intro():
    print("=" * 80)
    print(" " * 30 + "STUDENT")
    print(" " * 30 + "REPORT CARD")
    print(" " * 30 + "PROJECT")
    print("=" * 80)
    print()

def main_menu():
    print("MAIN MENU")
    print("1. REPORT MENU")
    print("2. ADMIN MENU")
    print("3. EXIT")

def report_menu():
    print("REPORT MENU")
    print("1. CLASS RESULT")
    print("2. STUDENT REPORT CARD")
    print("3. BACK TO MAIN MENU")
    
def admin_menu():
    print("\nADMIN MENU")
    print("1. CREATE STUDENT RECORD")
    print("2. DISPLAY ALL STUDENTS RECORDS")
    print("3. SEARCH STUDENT RECORD ")
    print("4. MODIFY STUDENT RECORD ")
    print("5. DELETE STUDENT RECORD ")
    print("6. BACK TO MAIN MENU")
    
def main():
    intro()
    while(True):
        main_menu()
        choice = input('Enter choice(1-3): ')
        print()

        if choice == '1':
            while True:
                report_menu()
                rchoice = input('Enter choice(1-3): ')
                print()
                if rchoice == '1':
                    class_result()
                elif rchoice == '2':
                    search_record()
                elif rchoice == '3':
                    break
                else:
                    print('Invalid input !!!\n')
                print()
        
        elif choice == '2':
            while True:
                admin_menu()
                echoice = input('Enter choice(1-6): ')
                print()
                if echoice == '1':
                    write_record()
                elif echoice == '2':
                    read_records()
                elif echoice == '3':
                    search_record()
                elif echoice == '4':
                    modify_record()
                elif echoice == '5':
                    delete_record()
                elif echoice == '6':
                    break
                else:
                    print('Invalid input !!!\n')
                
            
        elif choice == '3':
            print('Thanks for using Student Management System')
            break
        else:
            print('Invalid input!!!')
            print()
                            
#call the main function.
main()


