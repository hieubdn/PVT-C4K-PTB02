# ***---Bài tập về nhà---***
# Câu 9
def sum():
    n = int(input("Nhập số n: "))
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum = sum + i
        print('Tổng số lẻ là: ',sum)
# Câu 10
# a = int(input("Nhập số nguyên dương a: "))
# for i in range(1, a+1):
#     if i % 2 == 0:
#         i = i
#         print(i)

# @@@--LESSON 7---@@@
# ----Bài 1----
# n = int(input("Nhập số n: "))
# while n < 100:
#     if n < 0:
#         print("Vui lòng nhập số nguyên dương")
#         break
#     if n > 0:
#         n = n + 1
#         print(n)
# ----Bài 2----
import random  #nhận biến random tư ngoài vào

guesses_taken = 0
number_to_guess = random.randint(1,50)   #Lấy ngẫu nhiên một số nguyên từ 1-50
# random.randint(x,y): Lấy ngẫu nhiên một số nguyên từ X đến Y (với X bé hơn Y)

print("Welcome to the Number Guessing Game!")

while True:
    n = int(input("Take a guess: "))  #Nhập số muốn đoán
    guesses_taken += 1   #Đếm số lần nhập

    if n < number_to_guess:  # So sánh số vừa nhập và giá trị đã random
        print("Too low!")
    elif n > number_to_guess: # So sánh số vừa nhập và giá trị đã random
        print("Too high!")
    else:  #Ngược lại nếu bằng nhau thì in ra....
        print(f"Congratulations! You guessed the number in {guesses_taken} attempts!")
        break