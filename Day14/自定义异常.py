class PreExcetption(BaseException):
    def __init__(self,msg):
        self.mag=msg
# raise PreExcetption('自己定制的异常')
# raise TypeError('类型错误')
# print('自己定制的异常')
print(PreExcetption('自己定制的异常'))

