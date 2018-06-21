# -*- coding: UTF8 -*-
#!/usr/bin/python3

# 打印斐波那契数列
def fblq():
    a, b = 0, 1
    while b < 100:
        print(b, end=",")
        a, b = b, a + b

def test_list():
    # 集合支持集合推导式
    a = {x for x in 'asffefewd' if x not in 'ab'}
    print(a)
    set_a = set('fsaffva')
    set_b = set('abgjuk5')
    print('集合set_a中包含元素:', set_a - set_b)
    print('集合set_a或set_b中包含的所有元素:', set_a | set_b)
    print('集合set_a和set_b中都包含了的元素:', set_a & set_b)
    print('不同时包含于set_a和set_b的元素:', set_a ^ set_b)
    set_c = set()
    set_c.add(1)
    set_c.update({3,4,5})
    set_c.update([5,7])
    print(set_c)

def huandai():
    yue_gong = 5108.42
    total_month = 240
    for x in range(1,240):
        yue_gong -= 11.04
        print("第%d个月%d年还贷:%d" %(x, x/12, yue_gong))


if __name__ == '__main__':
    fblq()
    test_list()
    huandai()

