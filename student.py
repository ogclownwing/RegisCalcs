def add_course(id, c_list, r_list, m_list):
    course_adder = input("Enter course you want to add: ")
    i = 0
    if course_adder == "CSC101":
        i = 0
    elif course_adder == "CSC102":
        i = 1
    elif course_adder == "CSC103":
        i = 2
    elif course_adder == "CSC104":
        i = 3
    m_list = m_list[i]
    r_list = r_list[i]
    if course_adder not in c_list:
        print("Course not found.\n")
        return
    elif course_adder in c_list and m_list <= len(r_list):
        print("Course is full.\n")
        return
    elif id in r_list:
        print("You are already enrolled in that course.\n")
        return
    else:
        r_list.append(id)
        print("Course added.\n")


def drop_course(id, c_list, r_list):
    course_dropper = input("Enter course you want to drop: ")
    i = 0
    if course_dropper == "CSC101":
        i = 0
    elif course_dropper == "CSC102":
        i = 1
    elif course_dropper == "CSC103":
        i = 2
    elif course_dropper == "CSC104":
        i = 3
    r_list = r_list[i]
    if course_dropper not in c_list:
        print("Course not found.\n")
        return
    elif id not in r_list:
        print("You are not enrolled in that course.\n")
        return
    else:
        r_list.remove(id)
        print("Course dropped.\n")


def list_courses(id, c_list, r_list):
    counter = 0
    for i in range(4):
        if id in r_list[i]:
            counter = counter + 1
            print(c_list[i])
        else:
            continue
    if counter == 0:
        print("No courses are registered\n")
    print("Total number: ", counter, "\n")
