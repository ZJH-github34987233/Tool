import time

import Debug.log


def ZHiShu(Int, Windows):
    for i in range(2, int(Int)):
        try:
            FirstTime = time.time()
            if int(Int) % i == 0:
                if int(Int) / i != 1:
                    Other = int(Int) / i
                    Debug.log.Log(Windows).Log(f'[模块][ZHiShu] {Int} 是合数,它的一个因数为{i},另一个为{Other}')
                    FinishTime = time.time()
                    Time = str(FinishTime - FirstTime)
                    Debug.log.Log(Windows).Log('[模块][ZHiShu] 已返回结果,用时：' + Time + '\n')
                    return True
            Debug.log.Log(Windows).Log(f'[模块][ZHiShu] {Int} 不是合数')
            FinishTime = time.time()
            Time = str(FinishTime - FirstTime)
            Debug.log.Log(Windows).Log('[模块][ZHiShu] 已返回结果,用时：' + Time + '\n')
            return False
        except:
            Debug.log.Log(Windows).Error('[模块][ZHiShu]')
