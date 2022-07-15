import csv

file_url = 'User_IDs.csv'


def display_menu():
    print(f""" 1) Create a new User ID \n 2) Change a password \n 3) Display all User IDs \n 4) Quit""")
    select = int(input("Enter Selection: "))
    return select


def create_new_user(user_id=None, there_such_id=None):
    if there_such_id == None or there_such_id == True:
        user_id = input("Enter user ID: ")
        there_such_id = validation_id(user_id)

    if there_such_id == True:
        print("Такой айди уже есть!")
        create_new_user()
    elif there_such_id == False:
        password = input("Enter password: ")
        while len(password) < 1:
            password = input("Enter password repeat: ")
        if len(password) >= 1:
            point_for_password = validation_password(password)
            if point_for_password < 3:
                print('password is very weak')
                create_new_user(user_id, there_such_id=False)
            elif point_for_password > 2 and point_for_password < 5:
                print("Your password can update")
                answer = input("Do you want to improve it? y/n: ")
                if answer == "y":
                    create_new_user(user_id, there_such_id=False)
                else:
                    save_to_csv(user_id, password)
            else:
                print("Great password")
                save_to_csv(user_id, password)


def save_to_csv(id, password):
    with open(file_url, mode='a') as file:
        a = f"\n{id},{password}"
        file.write(a)
        print("User created!\n")


def validation_password(password):
    special_sympol = ['!', '@', '$', '%', '*', '<']
    global point_for_password
    point_for_password = 0
    if len(password) > 8:  # checking if the password is longer than 8 characters
        point_for_password += 1
    else:
        pass

    for letter in password:  # checking for uppercase letters
        if letter.isupper() == True:
            point_for_password += 1
            break

    for letter in password:  # checking for lowercase letters
        if letter.isupper() == False:
            point_for_password += 1
            break

    for letter in password:  # checking that the password contains a number
        if letter.isdigit() == True:
            point_for_password += 1
            break

    for letter in password:
        if letter in special_sympol:
            point_for_password += 1
            break
    return point_for_password


def validation_id(user_id):
    global there_such_id
    there_such_id = None
    with open(file_url, mode='r') as file:
        file_read = csv.reader(file)
        array = list(file_read)
        len_list = len(array)
        for i in range(len_list):
            if i == 0:  # skip headers in csv
                pass
            else:
                if str(array[i][0]) == user_id:
                    there_such_id = True
                    break
                else:
                    there_such_id = False
        return there_such_id


def change_password():
    user_id = str(input("Enter user id: "))
    does_id_exist = validation_id(user_id)
    if does_id_exist == True:
        new_password = str(input("Enter new password: "))
        with open(file_url, mode='r') as file:
            file_read = csv.reader(file)
            array = list(file_read)
            new_array = []
            for i in array:
                if str(i[0]) == user_id:
                    a = [user_id, new_password]
                    new_array.append(a)
                else:
                    new_array.append(i)

            with open(file_url, mode="w", encoding='utf-8') as w_file:
                for i in new_array:
                    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
                    file_writer.writerow(i)


def display_all():
    with open(file_url, mode="r", encoding="utf-8") as r_file:
        file_read = csv.reader(r_file)
        array = list(file_read)
        for id in array:
            print(id[0])


def main():
    run_status = True
    while run_status:
        select = display_menu()
        if select == 1:
            create_new_user()
        elif select == 2:
            change_password()
        elif select == 3:
            display_all()
        elif select == 4:
            run_status = False
        else:
            print("Incorect input")


if __name__ == '__main__':
    main()
