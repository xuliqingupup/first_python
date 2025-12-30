def open_r():
    f = open('text1.txt', mode='r', encoding='utf8')
    text = f.read()
    print(text)
    f.close()


def open_w():
    """
    读写文件，没有就创建，有就覆盖(如果进行写操作的话)
    :return: 
    """
    f = open('text2.txt', mode='w+', encoding='utf8')
    f.write('hellomyhandsome')
    f.close()


if __name__ == '__main__':
# open_r()
    open_w()
