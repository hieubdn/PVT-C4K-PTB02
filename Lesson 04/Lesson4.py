# Thầy giáo mang kẹo làm quà cho cả lớp nhân dịp lớp có kết quả kiểm tra tốt.
# Túi kẹo có n viên và lớp có m học sinh. Số kẹo được chia đều cho tất cả học sinh trong lớp. 
# Viết chương trình: Nhập n và m vào từ bàn phím.
# đưa ra màn hình số kẹo mỗi học sinh nhận được và số kẹo còn thừa sau khi chia.
n = int(input("Nhập số kẹo hiện tại đang có: "))
m = int(input("Nhập số học viên: "))
a = n//m
b = n%m
print("số kẹo học viên có thể nhận được là: ", a)
print("số kẹo còn thừa lại là: ", b)


# Nhập một số giây từ bàn phím - Viết chương trình chuyển đổi số giây qua Giờ - Phút - giây
s = int(input("Số giây: "))
gio = s // 3600
phut = (s % 3600) // 60
giay = s % 60
print("Chuyển đổi: ", gio, "giờ", phut, "phút", giay, "giây")


# Nhập một số từ bàn phím và tính giá trị tuyệt đối của số đó
n = int(input("Nhập một số: "))
if n < 0:
    b = n * (-1)
    print(b,"là giá trị tuyệt đối của", n)
else:
    print(n, "là giá trị tuyệt đối của", n)


# Xây dựng ứng dụng Math quiz
print("Cùng bạn làm toán")
print("------------------")

# Define the questions and answers as variables
question1 = "Câu 1. 2 luỹ thừa 4 bằng mấy?"
answer1 = 16

question2 = "Câu 2. Căn bậc 3 của 64 là?"
answer2 = 4

question3 = "Câu 3. 78 có chia hết cho 3 không? Bấm Y nếu là Có hoặc N nếu là Không:"
answer3 = "Y"

# Keep track of the score
score = 0

# Ask the user each question and check the answer
print(question1)
user_answer = int(input("Đáp án: "))
if user_answer == answer1:
    print("Chính xác!")
    score += 1
else:
    print("Chưa chính xác!")

print(question2)
user_answer = int(input("Đáp án: "))
if user_answer == answer2:
    print("Chính xác!")
    score += 1
else:
    print("Chưa chính xác!")

print(question3)
user_answer = input("Đáp án: ")
if user_answer == answer3:
    print("Chính xác!")
    score += 1
else:
    print("Chưa chính xác!")

# Print the final score
print("Điểm của bạn là:", score, "trên 3")


# bài tập về nhà 
# Câu 9
a = int(input("Nhập số kẹo: "))
b = int(input("Nhập số em bé: "))
if a % b == 0:
    print("Có")
else:
    print("Không")

# Câu 10
An = float(input("Nhập chiều cao của An: "))
Minh = float(input("Nhập chiều cao của Minh: "))
Lan = float(input("Nhập chiều cao của Lan: "))

if An >= Minh and An >= Lan:
    print("Người cao nhất là An")
elif Minh >= An and Minh >= Lan:
    print("Người cao nhất là MInh")
else: Lan >= Minh and Lan >= An
print ("Người cao nhất là Lan")