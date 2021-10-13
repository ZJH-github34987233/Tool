import datetime
import sys
import traceback

import Debug.Vision


def remove(rempath):
    import os
    for path, dirnames, filenames in os.walk(rempath):
        for f in filenames:
            os.remove(os.path.join(path, f))
        os.rmdir(rempath)


def getZipDir(dirpath, outFullName):
    import os
    import zipfile
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()
    remove(dirpath)


def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        return path
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return path


class Log:
    def __init__(self, Window):
        self.Windows = mkdir(f'Debug/Log/{Window}')
        self.WindowsID = Window
        self.time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

    def File(self, Type, Connect):
        with open(f'{self.Windows}/{Type}.txt', 'a') as Log:
            Log.write('\n' + f'[{self.time}]' + Connect)
        if Type == 'Log':
            print(f'[{self.time}]' + Connect)

    def Log(self, Connect):
        self.File('Log', Connect)

    def Error(self, location):
        ErrorType = {"Mild": ["<class 'KeyError'>", "<class 'ValueError'>"],
                     "Moderate": ["<class 'Exception'>"],
                     "Severe": ["<class ,'SyntaxError'>"]}
        Error = []
        # 错误分析
        if str(sys.exc_info()[0]) in ErrorType["Mild"]:
            Error.append(f'[轻度错误] 报错内容：{str(sys.exc_info()[1])}')
        elif str(sys.exc_info()[0]) in ErrorType["Moderate"]:
            Error.append(f'[中度错误] 报错内容：{str(sys.exc_info()[1])}')
        elif str(sys.exc_info()[0]) in ErrorType["Severe"]:
            Error.append(f'[严重错误] 报错内容：{str(sys.exc_info()[1])}')
        else:
            Error.append(f'[未知错误] 报错内容：{str(sys.exc_info()[1])}')
        Error.append(str(sys.exc_info()[0]))
        Error.append(str(sys.exc_info()[1]))
        Error.append(traceback.format_exc())
        for i in ['Log', 'Error']:
            self.File(i, location + f'[{Error[1]}]' + Error[0] + '\n' + Error[3] + '\n')

    def Window(self, Type=None, Time=0):
        if Type == 'Open':
            import platform
            self.File('Log',
                      '-' * 20 + f'\n操作系统：{platform.system()}\n系统版本：{platform.platform()} {platform.version()}\n工具版本：{Debug.Vision.Vision().Human_vision()}\n' + '-' * 44)
            Type = '进程已开启'
        elif Type == 'Exit':
            Type = '进程已关闭'
        self.File('Log', f'[{self.WindowsID}]' + Type + '，用时：' + str(Time))
        self.File('Window', f'[{self.WindowsID}]' + Type + '，用时：' + str(Time))
        if Type == '进程已关闭':
            getZipDir(f'Debug/Log/{self.WindowsID}', f'Debug/Log/{self.WindowsID}.zip')
