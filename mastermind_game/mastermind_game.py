import random

list_all_colors = ["red", "black", "white"]


def generate_color():
    list_selected_color = []
    for i in range(4):
        random_color = random.choice(list_all_colors)
        list_selected_color.append(random_color)
    return list_selected_color


def display_instructions():
    print(f"""Hello, I chose 4 colors from the list: {list_all_colors} 
you need to guess what kind of lights and where they are located (colors can be repeated)""")
    users_select = list(map(str, input(f"\n Enter to 4 colors separate them spase: ").split(" ")))
    return users_select


def main():
    list_selected_color = generate_color()
    users_select = display_instructions()
    check_user_select(users_select, list_selected_color)


def check_user_select(users_select, list_selected_color):
    new_list = list_selected_color
    if users_select == list_selected_color:
        print("You win! Graz")
    else:
        count_true = 0  # Правильный цвет в правильной позиции
        for i in range(3):
            if users_select[i] == list_selected_color[i]:
                count_true += 1
        count_guessed_color = 0

        for color in users_select:
            if color in new_list:
                count_guessed_color += 1
                new_list.remove(color)
        count_in_false_place = count_guessed_color - count_true

        print(f" Правильный цвет в правильной позиции: {count_true}\n "
              f"Правильный цвет в неправильной позиции: {count_in_false_place}")


def print_result(count_true, count_in_false_place):
    print(
        f"Правильный цвет в правильной позиции: {count_true}"
        f" Правильный цвет в неправильной позиции: {count_in_false_place}")


main()
