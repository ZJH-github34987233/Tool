import time

import Debug.log


class Solution:  # 罗马数字转化
    def __init__(self, Windows):
        self.Windows = Windows

    def RomanToInt(self, s):
        FirstTime = time.time()
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }  # 罗马数字
        if s == "":
            Debug.log.Log(self.Windows).Log('[模块][Solution][RomanToInt] 已返回结果\n')  # 日志输出
            return 0
        index = len(s) - 2
        sum = ROMAN[s[-1]]
        while index >= 0:
            if ROMAN[s[index]] < ROMAN[s[index + 1]]:
                sum -= ROMAN[s[index]]
            else:
                sum += ROMAN[s[index]]
            index -= 1
        FinishTime = time.time()
        Time = str(FinishTime - FirstTime)
        Debug.log.Log(self.Windows).Log('[模块][Solution][RomanToInt] 已返回结果,用时：' + Time + '\n')  # 日志输出
        return sum

    def parse(self, digit, index):
        NUMS = {
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
        }
        ROMAN = {
            'I': ['I', 'X', 'C', 'M'],
            'V': ['V', 'L', 'D', '?'],
            'X': ['X', 'C', 'M', '?']
        }
        s = NUMS[digit]
        Debug.log.Log(self.Windows).Log('[模块][Solution][parse] 已返回结果\n')  # 日志输出
        return s.replace('X', ROMAN['X'][index]).replace('I', ROMAN['I'][index]).replace('V', ROMAN['V'][index])

    def intToRoman(self, num):
        FirstTime = time.time()
        s = ''
        index = 0
        while num != 0:
            digit = num % 10
            if digit != 0:
                s = self.parse(digit, index) + s
            num = num // 10
            index += 1
        FinishTime = time.time()
        Time = str(FinishTime - FirstTime)
        Debug.log.Log(self.Windows).Log('[模块][Solution][intToRoman] 已返回结果,用时：' + Time + '\n')  # 日志输出
        return s
