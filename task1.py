def task1(arr):
    for number in arr:
        if number == 237:
            break
        if number % 2 == 0:
            print(number)

def task2(number, border):
    if number < border:
        print("Произвольное число меньше пограничного")
    elif number > border:
        print("Произвольное число больше пограничного")
        if number > 3 * border:
            print("Произвольное число больше пограничного более чем в 3 раза")

numbers = [1, 2, 3, 4, 5, 6, 237, 7, 8, 9]
task1(numbers)

num1 = float(input("Введите произвольное число: "))
num2 = float(input("Введите пограничное число: "))
task2(num1, num2)