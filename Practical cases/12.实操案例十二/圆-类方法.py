import math

class Circle(object):
    def __init__(self,r):
        self.r=r
        
    def get_area(self):
        return math.pi*math.pow(self.r,2)
    
    def get_circumference(self):
        return math.pi*2*self.r
    
if __name__ == '__main__':
    r = float(input('请输入圆的半径：'))
    x = Circle(r)
    print(f'圆的面积为：{x.get_area():.2f}')
    print(f'圆的周长为：{x.get_circumference():.2f}')