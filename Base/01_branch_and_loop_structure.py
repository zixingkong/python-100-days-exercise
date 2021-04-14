from random import randint


# 1.寻找水仙花数
# **说明**：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
# 它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：1<sup>3</sup> + 5<sup>3</sup> + 3<sup>3</sup> = 153

def find_daffodils_nums():
	for i in range(100, 1000):
		single = i % 10
		hundred = i // 100
		mid = i // 10
		ten = mid % 10
		num = single ** 3 + hundred ** 3 + ten ** 3
		if num == i:
			print(i)


# 2.将一个整数反转
def reverse_num(num):
	num = int(input('num = '))
	reversed_num = 0
	while num > 0:
		reversed_num = reversed_num * 10 + num % 10
		num //= 10
	print(reversed_num)


# 3：百钱百鸡问题。
# 百钱百鸡是我国古代数学家[张丘建](https://baike.baidu.com/item/%E5%BC%A0%E4%B8%98%E5%BB%BA/10246238)在《算经》一书中
# 提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？翻译成现代文是：公鸡5元一只，母鸡3元一只，
# 小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少

def hundred_buy_chicken():
	for x in range(1, 21):
		for y in range(1, 34):
			z = 100 - x - y
			if 100 == x * 5 + 3 * y + z // 3 and z % 3 == 0:
				print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')


# 4.CRAPS赌博游戏
# CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
# 简化后的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
# 玩家如果摇出其他点数则玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
# 其他点数玩家继续摇骰子，直到分出胜负。
def craps():
	result = True
	while result:
		first_num = randint(1, 6)
		second_num = randint(1, 6)
		first = first_num + second_num
		if first == 7 or first == 11:
			print('')


if __name__ == "__main__":
	# find_daffodils_nums
	# find_daffodils_nums()
	hundred_buy_chicken()
