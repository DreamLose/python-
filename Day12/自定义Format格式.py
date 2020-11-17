
formatDic = {
    "ymd":"{0.year}{0.mon}{0.day}",
    "y-m-d":"{0.year}-{0.mon}-{0.day}"
}

class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day
    def __format__(self, format_spec):
        print("我开始执行")
        print(format_spec)
        if not format_spec:
            format_spec = "ymd"
        fm = formatDic[format_spec]
        return fm.format(self)


da = Date('2020','11','17')
# x = "{0.year}-{0.mon}-{0.day}".format(da)
# print(x)
print(format(da,'ymd'))