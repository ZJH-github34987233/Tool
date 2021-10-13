import time

import Debug.log


class Fence:
    def __init__(self, Windows):
        self.Windows = Windows

    def encrypt(self, Original, Key):
        try:
            FirstTime = time.time()
            Fence = []
            Finally = ''
            for i in range(0, len(Original)):
                O = Original[i]  # 确认字符
                Fence.append(O)  # 添加字符
                Debug.log.Log(self.Windows).Log(
                    f'[模块][Fence][encrypt] 已将原文第{i}个字符（{O}）添加入列表Fence（{Fence}）中')  # 日志输出
                if len(Fence) == Key:  # 分隔成特定宽度的字符串
                    while Fence != []:
                        Finally = Finally + Fence.pop(0)
                    Debug.log.Log(self.Windows).Log('[模块][Fence][encrypt] 已合并剩余字符与处理后的密文')  # 日志输出
                    Finally = Finally + ' '  # 添加分隔符
                    Debug.log.Log(self.Windows).Log(
                        '[模块][Fence][encrypt] 已在字符串Finally中添加分隔符')  # 日志输出
            Debug.log.Log(self.Windows).Log(
                '[模块][Fence][encrypt] 处理后的字符串为：' + Finally + str(Fence))  # 日志输出
            lists = Finally.split(' ')  # 分隔
            Debug.log.Log(self.Windows).Log(
                '[模块][Fence][encrypt] 已将字符串Finally分隔为：' + str(lists))  # 日志输出
            C = ''  # 初始化
            Finally = ''  # 初始化
            for o in range(0, Key):
                for Code in lists:
                    C = Code[o:o + 1]  # 储存lists每组数据的字符
                    Finally = Finally + C
            Debug.log.Log(self.Windows).Log('[模块][Fence][encrypt] 已获取到结果：' + Finally)  # 日志输出
            while not Fence == []:
                Finally = Finally
                Finally = Finally + Fence.pop(0)  # 尝试合并剩余与Finally
            Debug.log.Log(self.Windows).Log(
                '[模块][Fence][encrypt] 已将剩余的字符添加入字符串Finally,Finally为：' + Finally)  # 日志输出
        except:
            Debug.log.Log(self.Windows).Error('[模块][Fence][encrypt]')  # 日志输出
            return
        else:
            FinishTime = time.time()
            Time = str(FinishTime - FirstTime)
            Debug.log.Log(self.Windows).Log(
                '[模块][Fence][encrypt] 已返回结果,用时：' + Time + '\n')  # 日志输出
            return Finally

    def decrypt(self, PassWord, Key):
        FirstTime = time.time()
        Finally = ''
        More = ''
        for i in PassWord:
            if len(Finally) != len(PassWord) - len(PassWord) % Key:
                Finally += i
            else:
                More += i
        Finally = self.encrypt(Finally, len(Finally) // Key) + More

        FinishTime = time.time()
        Time = str(FinishTime - FirstTime)
        Debug.log.Log(self.Windows).Log('[模块][Fence][decrypt] 已返回结果,用时：' + Time + '\n')  # 日志输出
        return Finally
