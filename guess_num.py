import random

r = random.randint(1, 100)  #抓出一個數
while True :
	num = input('猜猜數字是多少:')
	num = int(num)
	if num == r :
		print('Bingo!!!答案就是', r)
		break
	elif num > r :
		print('答案比', num, '小')
	elif num < r :
		print('答案比', num, '大')