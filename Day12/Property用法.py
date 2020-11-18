class Goods:
     def __init__(self):
         # 商品原始价格
         self.original_price = 100
         # 商品折扣
         self.discount = 0.8
     @property
     def price(self):
         # 实际价格 =  原价 * 折扣
         return self.original_price * self.discount
     @price.setter
     def price(self,val):
         self.original_price = val
     @price.deleter
     def price(self):
         del self.original_price

obj = Goods()
print(obj.price)
obj.price = 200
print(obj.price)
del obj.price