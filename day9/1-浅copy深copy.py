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
    print("-" * 50)
    print(id(c[0]))
    print(id(d[0]))
    print(d)
    print(c)
    # a[0] = 10
    c[0][1] = 10
    print(c)
    print(d)


class Hero:
    def __init__(self, name, blood):
        self.name = name
        self.blood = blood
        self.equipment = ['鞋子', '指环']


def use_copy_own_obj():
    """
    实际对于自定义对象的练习
    :return:
    """
    old_hero = Hero('蚂蚁', 90)
    new_hero = copy.deepcopy(old_hero)
    new_hero.blood = 80  # 新对象修改后，原对象不会受到任何影响
    new_hero.equipment.append('药水')
    print(old_hero.blood)
    print(old_hero.equipment)


if __name__ == '__main__':
    # use_list_copy()
    # use_copy()
    # use_copy2()
    # use_deepcopy()
    use_copy_own_obj()
