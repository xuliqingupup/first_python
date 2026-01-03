# 正则表达式和re模块配合使用
# 用于找出适配的字符串（符合标准）
import re


def str_match():
    s = 'xujingupup.com'
    res = re.match('xujingupup', s)
    print(res.group())


def use_single_match():
    """
    # '.'可以匹配任意的字符，除了‘\n’
    # '[]'可以匹配其中列举的字符
    # '\d'可以匹配数字
    # '\s'匹配空格
    # '\w'匹配字母，数字，下划线，汉字
    对应的大写匹配除对应小写匹配内容以外的字符
    :return:
    """
    # ez版本
    ret = re.match('.', 'M')
    print(ret.group())
    ret = re.match('t.o', 'too')
    print(ret.group())
    # 匹配【】中的字符
    # 匹配数字0-9
    ret = re.match("[0-35-9]hellopython", '3hellopython')
    print(ret.group())
    ret = re.match("[0-35-9]hellopython", '7hellopython')
    print(ret.group())
    print('-' * 50)
    # /d的使用
    ret = re.match(r"复制体\d号准备战斗", '复制体4号准备战斗')
    print(ret.group())


def use_multiple_match():
    """
    # '*'匹配前一个字符0次或者无限次，即可有可无
    # '+'匹配前一个字符1次或者无限次，即至少一次
    # '?'匹配前一个字符出现 1 次或者 0 次，即要么有 1 次，要么没有
    # ‘{m}'匹配前一个字符出现m次
    # ’{m,n}'匹配前一个字符出现，m-n次，默认贪婪
    :return:
    """
    ret = re.match(".*", "M")
    print(ret.group())
    ret = re.match(".*", "plsnevergiveup")
    print(ret.group())
    ret = re.match(".*", "lloveu")
    print(ret.group())
    print('-' * 50)
    names = ["name1", "__name__", "2_name", "_name"]
    for name in names:
        ret = re.match(r"[a-zA-Z_]\w*", name)
        if ret:
            print(f'{ret.group()}是合法格式')
        else:
            print(f'{name}是非法格式')
    print('-' * 50)
    ret = re.match(r"[1-9]?[0-9]", "7")
    print(ret.group())

    ret = re.match(r"[1-9]?\d", "33")
    print(ret.group())

    ret = re.match(r"[1-9]?\d$", "09")
    if ret:
        print(ret.group())
    else:
        print('错啦')
    print('-' * 50)
    ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
    print(ret.group())
    ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s*34455ff66")
    print(ret.group())


def match_start_end():
    """
    '^'小帽子匹配开头
    '$'小老鼠匹配结尾

    :return:
    """
    # 匹配@163.com
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
    for email in email_list:
        ret = re.match(r"\w{5,20}@163.com$", email)
        if ret:
            print(f'{ret.group()}是正确的', end='')
            print(email)

        else:
            print(f'{email}是不符合规范的')
    ret = re.match(r"[1-9]?\d$", "49")
    if ret:
        print(ret.group())
    else:
        print('不是0-99之间')


def split_group():
    """
    匹配分组
    :return:
    """
    # 匹配0-100
    ret = re.match(r"[1-9]?\d$|100", '100')
    print(ret.group())
    ret = re.match(r"[1-9]?\d$|100", '20')
    print(ret.group())
    print('-' * 50)
    ret = re.match(r"[1-9]$|[1-9][0-9]", "11")
    if ret:
        print(ret.group())
    else:
        print('不是1-99之间')
    print('-' * 50)
    ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@qq.com")
    print(ret.group())
    ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@126.com")
    print(ret.group())
    print('-' * 50)
    # [^-]代表没有遇到斜杠就一直匹配下去
    ret = re.match(r"([^-]+)-(\d+)", "010-12345678")
    print(ret.group())  # 默认是全部输出
    print(ret.group(1))
    print(ret.group(2))
    print('-' * 50)
    # 能够完成对正确的字符串的匹配
    ret = re.match(r"<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</htmla>")
    print(ret.group())
    ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
    print(ret.group())
    print('-' * 50)
    labels = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h1>www.cskaoyan.com</h2></html>"]
    for label in labels:
        ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)  # 要用括号(\w*)表示出分组才能用后面的\2或者\1
        # '.'表示任意字符 \w表示[A-Za-z_0-9]和汉字
        if ret:
            print(f"{ret.group()} 是符合要求的标签")
        else:
            print(f"{label} 不符合要求")
    print('-' * 50)
    # 另一种分组方式更适合后期的维护
    # (?P<自己命名的名字>这里加需要匹配字符的正则表达式)这就是一个分组前缀，
    for label in labels:
        ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", label)
        if ret:
            print("%s 是符合要求的标签" % ret.group())
        else:
            print("%s 不符合要求" % label)


def add(x):
    result = x.group()
    return str(int(result) + 100)


def other_func():
    """
    search sub findall split
    :return:
    """
    ret = re.search(r"\d+", "访问数9999，订阅量888")
    print(ret.group())
    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
    print(ret)
    print('-' * 50)
    ret = re.sub(r"\d+", '998', "python = 997")
    print(ret)
    ret = re.sub(r"\d+", lambda x: str(int(x.group()) + 100), "python = 997")
    print(ret)
    ret = re.sub(r"\d+", add, "python = 997")
    print(ret)
    print('-' * 50)
    # sub只替换前两个
    text = "apple apple apple apple"
    pattern = r"apple"
    replacement = "orange"

    new_text = re.sub(pattern, replacement, text, count=3)
    print(new_text)


def find_second_match(pattern, text):
    matches = re.finditer(pattern, text)
    try:
        next(matches)  # 跳过第一个匹配项
        second_match = next(matches)  # 获取第二个匹配项
        return second_match.group()
    except StopIteration:
        return None


def use_findall():
    s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'
    ret_s = re.sub(r'年|月', r'/', s)
    ret_s = re.sub(r'日', r' ', ret_s)
    ret_s = re.sub(r'时|分', r':', ret_s)
    print(ret_s)
    # findall 内部的设计机制，在分组前面加?:
    pattern = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
    ret = pattern.findall(ret_s)
    print(ret)
    pattern1 = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
    # 如果不在(0[0-9]|1[0-9]|2[0-4])这个分组中加？:   那么只会输出这个分组的内容 ，反之如果加了就是输出整个字符串
    # search 没问题
    ret1 = pattern1.search(ret_s)
    print(ret1.group())


def use_sub():
    long_text = """<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>
    """
    # print(long_text)
    ret = re.sub(r'<[^>]*>|&nbsp;|\n|\s', '', long_text)
    print(ret)


def use_split():
    ret = re.split(r":| ", "info:xiaoZhang 33 shandong")
    print(ret)


if __name__ == '__main__':
    # str_match()
    # use_single_match()
    # use_multiple_match()
    # match_start_end()
    # split_group()
    # other_func()
    # use_findall()
    # use_sub()
    use_split()
