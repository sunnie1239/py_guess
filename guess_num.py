# version 1 猜1~100的一個數
# version 2 加上猜測次數
# version 3 改由使用者設置隨機數起迄
import random

start = input('請輸入起始值:')
end   = input('請輸入終止值:')
start = int(start)
end   = int(end)
r     = random.randint(start, end)  #產生隨機數
count = 0

while True :
	num = input('猜猜數字是多少:')
	num = int(num)
	count += 1 # count = count + 1
	if num == r :
		print('Bingo!!!答案就是', r)
		break
	elif num > r :
		print('答案比', num, '小')
	elif num < r :
		print('答案比', num, '大')

print('總共猜了', count, '次')