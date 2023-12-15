import random
import tkinter as tk


class MainFrame(tk.Tk):
    random_numbers_count: int = 5

    checkbox_list: tk.Frame
    selected_numbers_list: tk.Listbox

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = 'Калькулятор рандомных чичел'
        self.__init__ui()

    @property
    def random_number_set(self):
        return [random.randint(1, 99) for _ in range(self.random_numbers_count)]

    def __checkbox_callback(self, number: int):
        assert self.selected_numbers_list, 'Список чисел не создан.'

        number = str(number)

        selected_values = list(self.selected_numbers_list.get(first=0, last=tk.END))

        if number not in selected_values:
            self.selected_numbers_list.insert(tk.END, number)

        else:
            number_index = selected_values.index(number)

            self.selected_numbers_list.delete(
                number_index,
                number_index
            )

        selected_values = list(self.selected_numbers_list.get(first=0, last=tk.END))

        return self.__sum_count(selected_values)

    def __is_honest(self, number: int):
        return number % 2 == 1

    def __sum_count(self, numbers: list[str]):
        numbers = numbers.copy()
        numbers = [int(number) for number in numbers if number.isdigit()]

        number_sum = sum(numbers)
        self.sum_label.configure(
            text=f'Сумма: {number_sum} | {"Четное" if self.__is_honest(number_sum) else "Нечетное"}'
        )

    def __init__ui(self):
        self.checkbox_list = tk.Frame(
            master=self
        )

        self.checkbox_list.pack(side=tk.LEFT)

        self.selected_numbers_list = tk.Listbox(
            master=self
        )
        self.selected_numbers_list.pack(side=tk.RIGHT)

        random_number_set = self.random_number_set

        for random_number in random_number_set:
            checkbox = tk.Checkbutton(
                master=self.checkbox_list,
                text=str(random_number),
                command=lambda number=random_number: self.__checkbox_callback(number)
            )
            checkbox.pack()

        self.sum_label = tk.Label(
            text='Сумма: 0 | Нечетное'
        )

        self.sum_label.pack(side=tk.BOTTOM)


if __name__ == '__main__':
    root = MainFrame()
    root.mainloop()