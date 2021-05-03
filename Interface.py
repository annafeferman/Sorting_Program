from tkinter import *
from tkinter import messagebox as mb
import tkinter.font as font
import SortingProgramInterface as sp

root = Tk()


class Interface:
    background_color = "#3B5975"
    text_color = 'White'
    method_list = ["BubbleSort", "SelectionSort", "InsertionSort", "CocktailSort", "ShellSort"]
    root.title('Сортування масиву')
    root.geometry('800x500+420+30')
    root['bg'] = background_color
    myFont = font.Font(size=14, weight="bold")
    array_length_input_field = Entry()
    array_length_input_label = Label(text='Довжина масиву:', bg=background_color, fg=text_color)
    method_choice_label = Label(text='Оберіть метод сортування', bg=background_color, fg=text_color)
    up_down_choice_label = Label(text='Оберіть тип сортування', bg=background_color, fg=text_color)
    auto_array_input_label = Label(text='Сформуйте масив автоматично', bg=background_color, fg=text_color)
    auto_array_input_button = Button(text="Сформувати\nта сортувати", height=3, width=12, bg="#AFEEEE", activebackground="#48D1CC", font=myFont, command=lambda:auto_array_sort())
    manual_array_input_label = Label(text='Або введіть масив самостійно', bg=background_color, fg=text_color)
    manual_array_input_field = Entry()
    output_label_1 = Text(width=99, bg="#EDFAFA", height=2)
    output_label_2 = Text(width=99, bg="#EDFAFA", height=2)
    output_label_3 = Text(width=99, bg="#EDFAFA", height=2)
    space = Label(bg=background_color)
    array_sort_button = Button(text="Сортувати", height=3, width=10, bg="#AFEEEE", activebackground="#48D1CC", font=myFont, command=lambda:on_sort_clicked())
    output_1_name = Label(text='Вихідний масив: ', bg=background_color, fg=text_color)
    output_2_name = Label(text='Відсортований масив: ', bg=background_color, fg=text_color)
    output_3_name = Label(text='Час виконання програми: ', bg=background_color, fg=text_color)
    restart_button_yes = Button(height=3, width=20, text="Повторити програму", bg="#E0FFFF", activebackground="#AFEEEE", command=lambda:clear())
    restart_button_no = Button(height=3, width=20, text="Завершити програму", bg="#E0FFFF", activebackground="#AFEEEE", command=lambda:quit())
    array_length_input_label.grid(row=1, column=2)
    array_length_input_field.grid(row=2, column=2)
    method_choice_label.grid(row=0, column=0)
    up_down_choice_label.grid(row=0, column=1)
    auto_array_input_label.grid(row=0, column=2)
    auto_array_input_button.grid(row=3, column=2, rowspan=4, pady=8)
    manual_array_input_label.grid(row=0, column=3)
    manual_array_input_field.grid(row=1, column=3)
    array_sort_button.grid(row=2, column=3, rowspan=3, pady=7)
    output_1_name.grid(row=8, column=0)
    output_label_1.grid(row=9, column=0, columnspan=4)
    output_2_name.grid(row=10, column=0)
    output_label_2.grid(row=11, column=0, columnspan=4)
    output_3_name.grid(row=12, column=0)
    output_label_3.grid(row=13, column=0, columnspan=4)
    space.grid(row=14, column=0, columnspan=4)
    restart_button_yes.grid(row=15, column=1, pady=5, columnspan=2)
    restart_button_no.grid(row=16, pady=5, column=1, columnspan=2)
    method_choice_list = Listbox(width=15, height=5)
    method_choice_list.grid(row=1, column=0, rowspan=3)
    for i in method_list:
        method_choice_list.insert(0, i)
    up_down_choice = IntVar()
    up_down_choice.set(0)
    option1 = Radiobutton(root, text="За зростанням", variable=up_down_choice, value=0, bg=background_color, fg=text_color)
    option2 = Radiobutton(root, text="За спаданням", variable=up_down_choice, value=1, bg=background_color, fg=text_color)
    option1.grid(row=1, column=1)
    option2.grid(row=2, column=1)


def on_sort_clicked():
    flag = validate_data_manual()
    selected_method = Interface.method_choice_list.curselection()
    selected_up_down = Interface.up_down_choice.get()
    array = sp.DataValidation.validate_array(sp.DataValidation, Interface.manual_array_input_field.get())
    if flag:
        Interface.output_label_1.insert(0.0, Interface.manual_array_input_field.get())
        if selected_method == (4,):
            Interface.output_label_2.insert(0.0, sp.ArraySort.bubbleSort(sp.ArraySort, array, selected_up_down))
        elif selected_method == (3,):
            Interface.output_label_2.insert(0.0, sp.ArraySort.selectionSort(sp.ArraySort, array, selected_up_down))
        elif selected_method == (2,):
            Interface.output_label_2.insert(0.0, sp.ArraySort.insertionSort(sp.ArraySort, array, selected_up_down))
        elif selected_method == (1,):
            Interface.output_label_2.insert(0.0, sp.ArraySort.cocktailSort(sp.ArraySort, array, selected_up_down))
        elif selected_method == (0,):
            Interface.output_label_2.insert(0.0, sp.ArraySort.shellSort(sp.ArraySort, array, selected_up_down))
        Interface.output_label_3.insert(0.0, sp.ExecutionTime())
    else:
        if_mistake()


def auto_array_sort():
    selected_method = Interface.method_choice_list.curselection()
    selected_up_down = Interface.up_down_choice.get()
    array_length = sp.DataValidation.validate_array_length(sp.DataValidation, Interface.array_length_input_field.get())
    array = sp.DataValidation.auto_array_input(sp.DataValidation, array_length)
    flag = validate_data_auto()
    if flag:
        Interface.output_label_1.insert(0.0, array)
        if selected_method == (4,):
            Interface.output_label_2.insert(0.0, sp.ArraySort.bubbleSort(sp.ArraySort, array, selected_up_down))
        elif selected_method == (3,):
            Interface.output_label_2.insert(0.0, sp.ArraySort.selectionSort(sp.ArraySort, array, selected_up_down))
        elif selected_method == (2,):
            Interface.output_label_2.insert(0.0, sp.ArraySort.insertionSort(sp.ArraySort, array, selected_up_down))
        elif selected_method == (1,):
            Interface.output_label_2.insert(0.0, sp.ArraySort.cocktailSort(sp.ArraySort, array, selected_up_down))
        elif selected_method == (0,):
            Interface.output_label_2.insert(0.0, sp.ArraySort.shellSort(sp.ArraySort, array, selected_up_down))
        Interface.output_label_3.insert(0.0, sp.ExecutionTime())
    else:
        if_mistake()


def validate_data_manual():
    array_valid = sp.DataValidation.validate_array(sp.DataValidation, Interface.manual_array_input_field.get())
    array = sp.DataValidation.validate_array(sp.DataValidation, Interface.manual_array_input_field.get())
    sel_m = Interface.method_choice_list.curselection()
    if sel_m == (0, ) or sel_m == (1, ) or sel_m == (2, ) or sel_m == (3, ) or sel_m == (4, ):
        method_is_selected = True
    else:
        method_is_selected = False
    if array and array_valid and method_is_selected:
        flag = True
    else:
        flag = False
    return flag


def validate_data_auto():
    length_valid = sp.DataValidation.validate_array(sp.DataValidation, Interface.array_length_input_field.get())
    sel_m = Interface.method_choice_list.curselection()
    if sel_m == (0, ) or sel_m == (1, ) or sel_m == (2, ) or sel_m == (3, ) or sel_m == (4, ):
        method_is_selected = True
    else:
        method_is_selected = False
    if length_valid and method_is_selected:
        flag = True
    else:
        flag = False
    return flag


def if_mistake():
    mb.showerror("Error", "You must have input something wrong... \n Try again!")


def clear():
    Interface.array_length_input_field.delete(0, END)
    Interface.manual_array_input_field.delete(0, END)
    Interface.output_label_1.delete(0.0, END)
    Interface.output_label_2.delete(0.0, END)
    Interface.output_label_3.delete(0.0, END)


def quit():
    root.destroy()


root.mainloop()
