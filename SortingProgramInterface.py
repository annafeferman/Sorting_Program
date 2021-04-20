from random import randint  # randint для заполнения массива
import timeit  # timeit для рассчета времени выполнения


class DataValidation:

    def validate_array_length(self, text):
        try:
            res = int(text)
            if res <= 0:
                return False
            return res
        except(TypeError, ValueError):
            return False

    def validate_array(self, text):
        delimeter = " "
        split_array = text.split(delimeter)
        res_array = []
        try:
            for number in split_array:
                array_element = int(number)
                res_array.append(array_element)
            return res_array
        except(TypeError, ValueError):
            return False

    def auto_array_input(self, length):
        old_list = []
        for i in range(length):
            old_list.append(randint(0, 100))
        return old_list


class ArraySort:

    def bubbleSort(self, my_list, up_down):
        last_item = len(my_list) - 1
        for k in range(last_item):  # вложенным циклом перебираем все элементы массива
            for j in range(last_item - k):
                if (up_down == 0 and my_list[j] > my_list[j + 1]) or (up_down == 1 and my_list[j] < my_list[j + 1]):
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        return my_list

    def selectionSort(self, my_list, up_down):
        for i in range(len(my_list)):
            min_index = i
            for j in range(i + 1, len(my_list)):
                if (up_down == 0 and my_list[j] < my_list[min_index]) or (
                        up_down == 1 and my_list[j] > my_list[min_index]):
                    min_index = j
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
        return my_list

    def insertionSort(self, my_list, up_down):
        for i in range(1, len(my_list)):
            k = my_list[i]  # присваиваем ключу значение номера элемента
            min_index = i - 1  # начинаем отсчет с минимального номера
            while (up_down == 0 and min_index >= 0 and my_list[min_index] > k) or (
                    up_down == 1 and min_index >= 0 and my_list[
                min_index] < k):  # сравниваем значение элемента с прерыдущим
                my_list[min_index + 1] = my_list[min_index]  # меняем, если он больше
                min_index -= 1
            my_list[min_index + 1] = k
        return my_list

    def cocktailSort(self, my_list, up_down):
        for i in range(len(my_list) // 2):
            swap = False  # присваем значенрие фолз в начале каждой итерации
            for j in range(1 + i, len(my_list) - i):
                if (up_down == 0 and my_list[j] < my_list[j - 1]) or (
                        up_down == 1 and my_list[j] > my_list[j - 1]):  # используем bubble sort
                    my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
                    swap = True
            if not swap:  # если ничего не изменилось, прерываем цикл (элементы отсортированы)
                break
            swap = False
            for j in range(len(my_list) - i - 1, i, -1):  # проходим цикл без последнего элемента
                if (up_down == 0 and my_list[j] < my_list[j - 1]) or (
                        up_down == 1 and my_list[j] > my_list[j - 1]):  # так как он уже на своем месте
                    my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]  # меняем нужные элементы местами
                    swap = True
            if not swap:  # если ничего не изменилось, прерываем цикл
                break
        return my_list

    def shellSort(self, my_list, up_down):
        n = len(my_list)
        gap = n // 2  # устанавливаем базовый шаг, деля длину массива на 2, потом он будет уменьшатся
        while gap > 0:  # цикл выполняется до тех пор, пока окончательно не уменьшится шаг
            for i in range(gap, n):
                temp = my_list[i]  # добавляем элемент, который уже отсортирован, во временную переменную
                j = i  # добавляем отсортированные элементы на нужную позицию
                while (up_down == 0 and j >= gap and my_list[j - gap] > temp) or (
                        up_down == 1 and j >= gap and my_list[j - gap] < temp):
                    my_list[j] = my_list[j - gap]  # меняем элементы местами
                    j -= gap

                my_list[j] = temp  # возвращаем значения из временной переменной на нужное место
            gap //= 2
        return my_list


def ExecutionTime():
    execution_time = int(timeit.timeit(number=100000) * 10000)/10000
    result = str(execution_time) + " seconds"
    return result