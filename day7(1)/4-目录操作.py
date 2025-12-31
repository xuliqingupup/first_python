import os


def use_rename():
    """
    相对路径
    :return:
    """
    # os.rename('dir1/file1.py', 'dir1/file2.py')
    os.remove('dir1/file2.py')


def use_dir_func():
    filelist = os.listdir('.')
    print(type(filelist))
    print(filelist)
    print(os.getcwd())
    os.chdir('dir1')
    f = open('file1', mode='w', encoding='utf-8')
    f.close()


def dir_dfs(current_path, width):
    """
    文件的深度优先遍历
    :return:
    """
    filelist = os.listdir(current_path)
    for filename in filelist:
        # print(' ' * width, filename)
        new_path = os.path.join(current_path, filename)
        print(new_path)
        if os.path.isdir(new_path):
            dir_dfs(new_path, width + 4)


def use_stat(file_path):
    """
    文件大小
    :param file_path:
    :return:
    """
    file_info = os.stat(file_path)
    print('size{},uid{},mode{:x},mtime{}'.format(file_info.st_size, file_info.st_uid,
                                                 file_info.st_mode, file_info.st_mtime))
    from time import strftime
    from time import gmtime
    gm_time = gmtime(file_info.st_mtime)
    # 把秒数转为字符串时间
    print(strftime("%Y-%m-%d %H:%M:%S", gm_time))


if __name__ == '__main__':
    # use_rename()
    # use_dir_func()
    # dir_dfs('.', 0)
    use_stat('dir1/file1')