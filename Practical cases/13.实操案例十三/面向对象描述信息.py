
class Car(object):
    def __init__(self,type,num):
        self.type=type
        self.num=num 
    def start(self):
        pass
    def stop(self):
        pass
    
class Taxi(Car):
    def __init__(self,type,num,company):
        super().__init__(type,num)  #继承父类的方法
        self.company=company
    def start(self):
        print('乘客您好，我是出租车')
    def stop(self):
        print('乘客您好,目的地到了！')
        
class Taxi(Car):
    def __init__(self,type,num,company):
        super().__init__(type,num)  #继承父类的方法   把父类的type跟num传入
        self.company=company
    def start(self):
        print(f'乘客您好，我是{self.company}公司的，我的车牌是{self.num}，我开的{self.type}')
    def stop(self):
        print('乘客您好,目的地到了！')
        
class FamilyCar(Car):
    def __init__(self,type,num,name):
        super().__init__(type,num)  #继承父类的方法
        self.name=name
    def start(self):
        print(f'叼毛你好，俺是{self.name}，俺滴车牌是{self.num}，我开的{self.type}')
    def stop(self):
        print('叼毛到地了！')
        
        
if __name__ == '__main__':
    taxi=Taxi('上海大众','京A88888','滴滴')
    familycar=FamilyCar('五菱棱光','沪B22222','武大郎')
    taxi.start()
    taxi.stop()
    print('---------------------------------')
    familycar.start()
    familycar.stop()