import random

r = random.randint(1, 100)  #抓出一個數
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