# Author:ogclownwing, Roger Sommer, Traegen Smith
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
import student
import billing

in_state_list = ['1001', '1003']
course_list = ['CSC101', 'CSC102', 'CSC103', 'CSC104']
course_hours = [3, 4, 5, 3]
roster_list = [['1004', '1003'], ['1001'], ['1002'], []]
max_size_list = [3, 2, 1, 3]
student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]


def main():
    print('Welcome to Registration.')
    repeat = 'y'
    while repeat == 'y':
        user = str(input('Enter ID to log in, or 0 to quit: '))
        if user == '0':
            print('Session ended')
            quit()
        else:
            value = login(id=user, s_list=student_list)
        while value == True:
            choice = "-1"
            while choice != "0":
                choice = str(input(
                    'Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: '))
                if choice == "0":
                    repeat = "y"  # NEED TO EXIT LOOP FROM HERE
                    print("Session ended.\n")
                    break
                elif choice == "1":
                    student.add_course(c_list=course_list, r_list=roster_list, id=user, m_list=max_size_list)
                    choice = "-1"
                elif choice == "2":
                    student.drop_course(id=user, c_list=course_list, r_list=roster_list)
                    choice = "-1"
                elif choice == "3":
                    student.list_courses(c_list=course_list, id=user, r_list=roster_list)
                    choice = "-1"
                elif choice == "4":
                    display_tuple = billing.calculate_hours_and_bill(h_list=course_hours, i_s_list=in_state_list,
                                                                     id=user, r_list=roster_list)
                    display_list = list(display_tuple)
                    hours = display_list[0]
                    cost = display_list[1]
                    billing.display_hours_and_bill(cost=cost, hours=hours)
                    choice = "-1"
                else:
                    choice = "-1"
                    repeat = "y"
            break


def login(id, s_list):
    pin = input('Enter PIN: ')
    students = [x[0] for x in s_list]
    if id not in students:
        print('ID or PIN incorrect\n')
        return False
    else:
        while id in [x[0] for x in s_list]:
            index = [x[0] for x in s_list].index(str(id))
            while pin == student_list[index][1]:
                print('ID and pin verified\n')
                return True
            if id not in s_list:
                print('ID or PIN incorrect\n')
            return False


# adapted from answers at
# https://stackoverflow.com/questions/946860/using-pythons-list-index
# -method-on-a-list-of-tuples-or-objects
# pass # temporarily avoid empty function definition

# ------------------------------------------------------------
# This function allows a student to log in.
# It has two parameters: id and s_list, which is the student
# list. This function asks user to enter PIN. If the ID and PIN
# combination is in s_list, display message of verification and
# return True. Otherwise, display error message and return False.
# -------------------------------------------------------------


main()
