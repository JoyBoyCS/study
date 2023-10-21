
#jack#20#男#90
class Student(object):
    def __init__(self,stu_name,stu_age,stu_gander,stu_score):
        self.stu_name=stu_name
        self.stu_age=stu_age
        self.stu_gander=stu_gander
        self.stu_score=stu_score
        
    def show(self):
        print(self.stu_name,self.stu_age,self.stu_gander,self.stu_score)
             
if __name__ == '__main__':
    print('请输入5为学员的信息：（姓名#年龄#性别#成绩）')
    lst=[]
    for i in range(0,5):
        a=input(f'请输入第{i+1}位学员的信息：')
        lst1=a.split('#')
        #创建学生对象
        stu=Student(lst1[0],int(lst1[1]),lst1[2],float(lst1[3]))
        lst.append(stu)
    #遍历列表
    for item in lst:
        item.show()