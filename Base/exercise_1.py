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


if __name__ == "__main__":
    find_daffodils_nums()
