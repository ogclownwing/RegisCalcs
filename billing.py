def calculate_hours_and_bill(id, i_s_list, r_list, h_list):
    cost = 0
    hours = 0
    for i in range(4):
        if id in r_list[i] and id in i_s_list:
            cost = cost + (h_list[i] * 225)
            hours = hours + h_list[i]
        elif id in r_list[i] and id not in i_s_list:
            cost = cost + (h_list[i] * 850)
            hours = hours + h_list[i]
    return hours, cost


def display_hours_and_bill(hours, cost):
    print("Course load: ", hours, "credit hours")
    print("Cost: $", cost, "\n")
