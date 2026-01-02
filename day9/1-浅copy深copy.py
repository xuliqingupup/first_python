import copy


def use_list_copy():
    """
    用list自己的copy
    一种浅copy
    :return:
    """
    a = [1, 2, 3]
    b = a.copy()
    b[0] = 10
    print(a)
    print(b)


def use_copy():
    """
    用copy包中的copy
    copy是浅copy
    针对不可变数据类型.a,b的地址不一样
    :return:
    """
    a = [1, 2, 3]
    b = copy.copy(a)
    b[0] = 10
    print(id(a))
    print(id(b))
    print(a)
    print(b)


def use_copy2():
    """
    浅copy处理不了嵌套的可变数据类型
    最外层的id不一致，但是内层的可变数据类型的id一致
    :return:
    """
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [a, b]
    d = copy.copy(c)
    print(id(c))
    print(id(d))
    print(d)
    print(c)
    # a[0] = 10
    c[0][1] = 10
    print(c)
    print(d)


def use_deepcopy():
    """
    deepcopy可以让两个变量毫无关系
    :return:
    """
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(c))
    print(id(d))
    print("-"*50)
    print(id(c[0]))
    print(id(d[0]))
    print(d)
    print(c)
    # a[0] = 10
    c[0][1] = 10
    print(c)
    print(d)

if __name__ == '__main__':
    # use_list_copy()
    # use_copy()
    # use_copy2()
    use_deepcopy()
