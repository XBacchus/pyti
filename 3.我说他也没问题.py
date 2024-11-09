"""
小陈在计算机课上编写了一个简单计算器
但是他和普通人不一样，他死都不愿意使用没有美感的if语句
同时，为了满足老师，在程序被奇怪的数据搞垮后
他能在程序中抛出各种可能的错误，以便继续使用程序
请修改他的代码帮他实现这个功能
为了避免核心科技泄露，___需要你补全代码
"""
while True:
    num1 = input()
    operate_signal = input()
    num2 = input()
    
    result = ___(num1 + operate_signal + num2)
    print("result is:" + str(result))