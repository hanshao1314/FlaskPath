import datetime
from flask import Flask
from flask import render_template

app=Flask(__name__)


class Calendar:
    """
    当前类实现日历功能
    1、返回列表嵌套列表的日历
    2、安装日历格式打印日历

    # 如果一号是周一，那么第一行1-7           0
    # 如果一号是周二，那么第一行empty+1+1-6   1
    # 如果一号是周三，那么第一行empty+2+1-5   2
    # 如果一号是周四，那么第一行empty+3+1-4   3
    # 如果一号是周五，那么第一行empty+4+1-3   4
    # 如果一号是周六，那么第一行empty+5+1-2   5
    # 如果一号是周日，那么第一行empty+6+1     6
    # 输入1月
    # 得到1月1号是周几
    # []填充7个元素，索引0对应的周一
    # 返回列表
    # day_range 范围在1-31
    """
    def __init__(self,month="now"):
        self.result = []  # ：接受所有的日期，需要是一个嵌套列表，列表当中嵌套的是7元列表

        big_month = [1, 3, 5, 7, 8, 10, 12]  # ：当前大月的天数是31天
        small_month = [4, 6, 9, 11]  # 当前小月的天数是30天

        #获取当前月份
        now = datetime.datetime.now()  #:获取当前的时间
        if month=="now":
            month = now.month  # 获取当前的月份
            first_data = datetime.datetime(now.year, now.month, 1, 0, 0, 0)  # ：获取当前的年、月、日、时、分、秒
        else:
            assert int(month) in range(1,13)
            first_data=datetime.datetime(now.year,month,1,0,0,0,)

        if month in big_month:
            day_range = range(1, 32)  # ：指定大月份的总天数
        elif month in small_month:
            day_range = range(1, 31)  # ：指定小月份的总天数
        else:
            day_range = range(1, 29)

        # 获取指定当月天数
        self.day_range = list(day_range)
        first_week = first_data.weekday()  # 获取当前月份1号是第一周周几

        line1 = []  # 第一行数据
        for e in range(first_week):
            line1.append("empty")
        for d in range(7 - first_week):
            line1.append(str(
                self.day_range.pop(0))+"Django全栈开发"
            )
        self.result.append(line1)

        while self.day_range:   #如果总天数列表有值，就接着循环
            line = []  #每个子列表
            for i in range(7):
                if len(line) < 7 and self.day_range:
                    line.append(str(self.day_range.pop(0)))
                else:
                    line.append("empty")
            self.result.append(line)
    def return_month(self):
        """
        返回列表嵌套列表的日历
        :return:
        """
        return self.result
    def print_month(self):
        """
        安装日历格式打印日历
        :return:
        """
        # 为了展示效果
        print("星期一 星期二 星期三 星期四 星期五 星期六 星期日")
        for line in self.result:
            for day in line:
                day = day.center(6)
                print(day, end=" ")
            print()

if __name__=="__main__":
    cal=Calendar(8)
    cal.print_month()

# @app.route("/")
# def index():
#     return render_template("index.html",name="老边")

# @app.route("/")
# def index():
#     name="老边"
#     return render_template("index.html",**locals())

@app.route("/base/")
def base():
    return render_template("base.html")


@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/index/")
def ex_index():
    return render_template("ex_index.html")

@app.route("/userInfo/")
def userInfo():
    callable=Calendar().return_month()
    return render_template("userInfo.html",**locals())


if __name__=="__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)