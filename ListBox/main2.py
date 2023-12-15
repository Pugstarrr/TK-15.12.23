import tkinter as tk
from tkinter import ttk

def update_selection():
    selected_numbers.clear()
    for number, var in zip(numbers, check_vars):
        if var.get():
            selected_numbers.append(number)
            numbers_list.insert(tk.END, number)
        else:
            try:
                idx = selected_numbers.index(number)
                selected_numbers.remove(number)
                numbers_list.delete(idx)
            except ValueError:
                pass
    update_sum()

def update_sum():
    total_sum = sum(selected_numbers)
    sum_label.config(text=f"Сумма: {total_sum}")

# Создаем главное окно
root = tk.Tk()
root.title("Чекбоксы и сумма чисел")

# Списки для хранения чисел и переменных чекбоксов
numbers = [15, 29, 44, 67, 88]
check_vars = []
selected_numbers = []


# Фреймы для размещения элементов
left_frame = ttk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

right_frame = ttk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

num = tk.Listbox(left_frame)
num.pack(pady=10)

# Создаем чекбоксы в левом фрейме
for number in numbers:
    var = tk.BooleanVar()
    check_vars.append(var)
    chk = ttk.Checkbutton(num, text=str(number), variable=var, command=update_selection)
    chk.pack(anchor='w')

# Список для отображения выбранных чисел в правом фрейме
numbers_list = tk.Listbox(right_frame)
numbers_list.pack(pady=1)

# Метка для отображения суммы
sum_label = ttk.Label(right_frame, text="Сумма: 0")
sum_label.pack(pady=1)

root.mainloop()