#include<iostream>
#define MAX 1000
using namespace std;


//显示菜单界面的函数
void showMenu()
{
	cout << "******************************" << endl
		<< "*****    1.添加联系人    *****" << endl
		<< "*****    2.显示联系人    *****" << endl
		<< "*****    3.删除联系人    *****" << endl
		<< "*****    4.查找联系人    *****" << endl
		<< "*****    5.修改联系人    *****" << endl
		<< "*****    6.清空联系人    *****" << endl
		<< "*****    0.退出通讯录    *****" << endl
		<< "******************************" << endl;
}

//创建联系人结构体
struct Person
{
	//姓名
	string m_Name;
	//性别     1男    2女
	int m_Sex;
	//年龄
	int  m_Age;
	//电话
	string m_Phone;
	//住址
	string m_Addr;
};

//创建通讯录结构体
struct Addressbooks
{
	//通讯录中保存的联系人数组
	struct Person personArray[MAX];

	//通讯录中当前记录联系人个数 
	int m_Size;
};


//1.添加联系人函数
void addPerson(Addressbooks* abs)
{
	//判断通讯录是否已满，如果满了就不再添加
	if (abs->m_Size == MAX)
	{
		cout << "通讯录已满，无法继续添加！" << endl;
		return;
	}
	else
	{
		//添加具体联系人
		//姓名
		string name;
		cout << "请输入姓名：" << endl;
		cin >> name;
		abs->personArray[abs->m_Size].m_Name = name;

		//性别
		cout << "请输入性别：" << endl;
		cout << "1---男" << endl;
		cout << "2---女" << endl;
		int sex = 0;

		while (true)
		{
			//如果输入是1或者2可以退出循环
			//如果输入有误，重新输入
			cin >> sex;
			if (sex == 1 || sex == 2)
			{
				abs->personArray[abs->m_Size].m_Sex = sex;
				break;
			}
			cout << "输入有误，请重新输入" << endl;
		}

		//年龄
		cout << "请输入年龄：" << endl;
		int age = 0;
		cin >> age;
		abs->personArray[abs->m_Size].m_Age = age;

		//电话
		cout << "请输入电话：" << endl;
		string phone;
		cin >> phone;
		abs->personArray[abs->m_Size].m_Phone= phone;

		//住址
		cout << "请输入住址：" << endl;
		string address;
		cin >> address;
		abs->personArray[abs->m_Size].m_Addr = address;

		//更新通讯录中人数
		abs->m_Size++;

		cout << "添加成功！" << endl;
		system("pause");		//请按任意键继续
		system("cls");		//清屏操作
	}
}

//2.显示联系人函数
void showPerson(Addressbooks* abs)
{
	//判断通讯录中的人数是否为0，如果是0，提示记录为空
	//如果不是0，显示联系人信息
	if (abs->m_Size == 0)
	{
		cout << "通讯录为空！" << endl;
	}
	else
	{
		for (int i = 0; i < abs->m_Size; i++)
		{
			cout << "姓名：" << abs->personArray[i].m_Name <<"\t";
			cout << "性别：" << (abs->personArray[i].m_Sex ==1 ? "男":"女")<< "\t";
			cout << "年龄：" << abs->personArray[i].m_Age << "\t";
			cout << "电话：" << abs->personArray[i].m_Phone << "\t";
			cout << "住址：" << abs->personArray[i].m_Addr << endl;
		}
	}
	system("pause");		//请按任意键继续
	system("cls");		//清屏操作
}


//检查联系人是否存在，如果存在返回在数组中的具体位置，不存在返回-1
//参数1：通讯录     参数2：对比姓名
int isExist(Addressbooks* abs, string name)
{
	for (int i = 0; i < abs->m_Size; i++)
	{
		//找到用户输入的姓名了
		if (abs->personArray[i].m_Name == name)
		{
			return i;	//找到了，返回这个人在数组中的下标位置
		}
	}
	return -1;		//如果遍历结束都没找到返回-1
}

//3.删除指定的联系人
void deletePerson(Addressbooks*abs)
{
	cout << "请输入您要删除的联系人" << endl;

	string name;
	cin >> name;

	//ret == -1 未查到
	//ret !=  -1  查到了
	int ret = isExist(abs, name);
	
	if (ret != -1)
	{
		//查到此人，需要进行删除操作
		for (int i = ret; i < abs->m_Size; i++)
		{
			//数据迁移
			abs->personArray[i] = abs->personArray[i + 1];
		}
		abs->m_Size--;	//更新通讯录中的人员数
		cout << "删除成功" << endl;
	}
	else
	{
		cout << "查无此人" << endl;
	}
	system("pause");		//请按任意键继续
	system("cls");		//清屏操作
}

//4.查找指定的联系人信息
void findPerson(Addressbooks* abs)
{
	cout << "请输入您要查找的联系人" << endl;
	string name;
	cin >> name;

	//判断指定的联系人是否存在在通讯录中
	int ret = isExist(abs, name);
	if (ret != -1)
	{
		cout << "姓名：" << abs->personArray[ret].m_Name << "\t";
		cout << "性别：" << (abs->personArray[ret].m_Sex == 1 ? "男" : "女") << "\t";
		cout << "年龄：" << abs->personArray[ret].m_Age << "\t";
		cout << "电话：" << abs->personArray[ret].m_Phone << "\t";
		cout << "住址：" << abs->personArray[ret].m_Addr << endl;
		
	}
	else
	{
		cout << "查无此人" << endl;
	}
	system("pause");		//请按任意键继续
	system("cls");		//清屏操作
}

//5.修改联系人
void modifyPerson(Addressbooks* abs)
{
	cout << "请输入您要修改的联系人" << endl;
	string name;
	cin >> name;

	//判断指定的联系人是否存在在通讯录中
	int ret = isExist(abs, name);
	if (ret != -1)
	{
		//姓名
		string name;
		cout << "请输入姓名：" << endl;
		cin >> name;
		abs->personArray[ret].m_Name = name;

		//性别
		cout << "请输入性别：" << endl;
		cout << "1---男" << endl;
		cout << "2---女" << endl;
		int sex = 0;

		while (true)
		{
			//如果输入是1或者2可以退出循环
			//如果输入有误，重新输入
			cin >> sex;
			if (sex == 1 || sex == 2)
			{
				abs->personArray[ret].m_Sex = sex;
				break;
			}
			cout << "输入有误，请重新输入" << endl;
		}

		//年龄
		cout << "请输入年龄：" << endl;
		int age = 0;
		cin >> age;
		abs->personArray[ret].m_Age = age;

		//电话
		cout << "请输入电话：" << endl;
		string phone;
		cin >> phone;
		abs->personArray[ret].m_Phone = phone;

		//住址
		cout << "请输入住址：" << endl;
		string address;
		cin >> address;
		abs->personArray[ret].m_Addr = address;
		//年龄

		//电话

		//住址

	}
	else
	{
		cout << "查无此人" << endl;
	}
	system("pause");		//请按任意键继续
	system("cls");		//清屏操作
}


//清空联系人
void cleanPerson(Addressbooks* abs)
{
	abs->m_Size = 0;		//将当前记录联系人数量置为0，做逻辑清空
	cout << "通讯录已经清空" << endl;
	//任意键后清屏
	system("pause");		//请按任意键继续
	system("cls");		//清屏操作
}

int main()
{
	//创建通讯录结构体变量
	Addressbooks abs;

	//初始化通讯录中当前人员个数
	abs.m_Size = 0;

	int select = 0;	//创建用户选择输入的变量
	while (true)
	{
		//调用菜单显示界面函数
		showMenu();

		//提示用户进行选择
		cout << "请问您想要操作什么？请输入对应数字：";

		cin >> select;
		switch (select)
		{
		case 0:
			cout << "已退出通讯录系统，谢谢您的使用！" << endl;
			return 0;
			break;
		case 1:
			cout << "请输入您要添加的联系人信息：" << endl;
			// 添加联系人的代码在此处...
			addPerson(&abs);   //利用地址传递，可以修饰实参
			break;
		case 2:
			cout << "以下是所有的联系人信息：" << endl;
			// 显示联系人的代码在此处...
			showPerson(&abs);
			break;
		case 3:
		//{
		//	cout << "请输入您要删除的联系人名称：" << endl;
		//	// 删除联系人的代码在此处...
		//	cout << "请输入删除联系人姓名：" << endl;
		//	string name;
		//	cin >> name;

		//	if (isExist(&abs, name) == -1)
		//	{
		//		cout << "查无此人" << endl;
		//	}
		//	else
		//	{
		//		cout << "找到此人" << endl;
		//	}
		//	break;
		//}
			deletePerson(&abs);
			break;

		case 4:
			cout << "请输入您要查找的联系人名称：" << endl;
			// 查找联系人的代码在此处...
			findPerson(&abs);
			break;
		case 5:
			// 修改联系人信息
			cout << "请输入要修改的联系人名称：" << endl;
			modifyPerson(&abs);
			break;
		case 6:
			cout << "即将清空所有联系人。" << endl;
			// 清空所有联系人的代码在此处...
			cleanPerson(&abs);
			break;
		default:
			cout << "无效输入，请重新选择。" << endl;
			break;
		}
	}
	return 0;
}