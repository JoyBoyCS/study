#include<iostream>
#define MAX 1000
using namespace std;


//��ʾ�˵�����ĺ���
void showMenu()
{
	cout << "******************************" << endl
		<< "*****    1.�����ϵ��    *****" << endl
		<< "*****    2.��ʾ��ϵ��    *****" << endl
		<< "*****    3.ɾ����ϵ��    *****" << endl
		<< "*****    4.������ϵ��    *****" << endl
		<< "*****    5.�޸���ϵ��    *****" << endl
		<< "*****    6.�����ϵ��    *****" << endl
		<< "*****    0.�˳�ͨѶ¼    *****" << endl
		<< "******************************" << endl;
}

//������ϵ�˽ṹ��
struct Person
{
	//����
	string m_Name;
	//�Ա�     1��    2Ů
	int m_Sex;
	//����
	int  m_Age;
	//�绰
	string m_Phone;
	//סַ
	string m_Addr;
};

//����ͨѶ¼�ṹ��
struct Addressbooks
{
	//ͨѶ¼�б������ϵ������
	struct Person personArray[MAX];

	//ͨѶ¼�е�ǰ��¼��ϵ�˸��� 
	int m_Size;
};


//1.�����ϵ�˺���
void addPerson(Addressbooks* abs)
{
	//�ж�ͨѶ¼�Ƿ�������������˾Ͳ������
	if (abs->m_Size == MAX)
	{
		cout << "ͨѶ¼�������޷�������ӣ�" << endl;
		return;
	}
	else
	{
		//��Ӿ�����ϵ��
		//����
		string name;
		cout << "������������" << endl;
		cin >> name;
		abs->personArray[abs->m_Size].m_Name = name;

		//�Ա�
		cout << "�������Ա�" << endl;
		cout << "1---��" << endl;
		cout << "2---Ů" << endl;
		int sex = 0;

		while (true)
		{
			//���������1����2�����˳�ѭ��
			//�������������������
			cin >> sex;
			if (sex == 1 || sex == 2)
			{
				abs->personArray[abs->m_Size].m_Sex = sex;
				break;
			}
			cout << "������������������" << endl;
		}

		//����
		cout << "���������䣺" << endl;
		int age = 0;
		cin >> age;
		abs->personArray[abs->m_Size].m_Age = age;

		//�绰
		cout << "������绰��" << endl;
		string phone;
		cin >> phone;
		abs->personArray[abs->m_Size].m_Phone= phone;

		//סַ
		cout << "������סַ��" << endl;
		string address;
		cin >> address;
		abs->personArray[abs->m_Size].m_Addr = address;

		//����ͨѶ¼������
		abs->m_Size++;

		cout << "��ӳɹ���" << endl;
		system("pause");		//�밴���������
		system("cls");		//��������
	}
}

//2.��ʾ��ϵ�˺���
void showPerson(Addressbooks* abs)
{
	//�ж�ͨѶ¼�е������Ƿ�Ϊ0�������0����ʾ��¼Ϊ��
	//�������0����ʾ��ϵ����Ϣ
	if (abs->m_Size == 0)
	{
		cout << "ͨѶ¼Ϊ�գ�" << endl;
	}
	else
	{
		for (int i = 0; i < abs->m_Size; i++)
		{
			cout << "������" << abs->personArray[i].m_Name <<"\t";
			cout << "�Ա�" << (abs->personArray[i].m_Sex ==1 ? "��":"Ů")<< "\t";
			cout << "���䣺" << abs->personArray[i].m_Age << "\t";
			cout << "�绰��" << abs->personArray[i].m_Phone << "\t";
			cout << "סַ��" << abs->personArray[i].m_Addr << endl;
		}
	}
	system("pause");		//�밴���������
	system("cls");		//��������
}


//�����ϵ���Ƿ���ڣ�������ڷ����������еľ���λ�ã������ڷ���-1
//����1��ͨѶ¼     ����2���Ա�����
int isExist(Addressbooks* abs, string name)
{
	for (int i = 0; i < abs->m_Size; i++)
	{
		//�ҵ��û������������
		if (abs->personArray[i].m_Name == name)
		{
			return i;	//�ҵ��ˣ�����������������е��±�λ��
		}
	}
	return -1;		//�������������û�ҵ�����-1
}

//3.ɾ��ָ������ϵ��
void deletePerson(Addressbooks*abs)
{
	cout << "��������Ҫɾ������ϵ��" << endl;

	string name;
	cin >> name;

	//ret == -1 δ�鵽
	//ret !=  -1  �鵽��
	int ret = isExist(abs, name);
	
	if (ret != -1)
	{
		//�鵽���ˣ���Ҫ����ɾ������
		for (int i = ret; i < abs->m_Size; i++)
		{
			//����Ǩ��
			abs->personArray[i] = abs->personArray[i + 1];
		}
		abs->m_Size--;	//����ͨѶ¼�е���Ա��
		cout << "ɾ���ɹ�" << endl;
	}
	else
	{
		cout << "���޴���" << endl;
	}
	system("pause");		//�밴���������
	system("cls");		//��������
}

//4.����ָ������ϵ����Ϣ
void findPerson(Addressbooks* abs)
{
	cout << "��������Ҫ���ҵ���ϵ��" << endl;
	string name;
	cin >> name;

	//�ж�ָ������ϵ���Ƿ������ͨѶ¼��
	int ret = isExist(abs, name);
	if (ret != -1)
	{
		cout << "������" << abs->personArray[ret].m_Name << "\t";
		cout << "�Ա�" << (abs->personArray[ret].m_Sex == 1 ? "��" : "Ů") << "\t";
		cout << "���䣺" << abs->personArray[ret].m_Age << "\t";
		cout << "�绰��" << abs->personArray[ret].m_Phone << "\t";
		cout << "סַ��" << abs->personArray[ret].m_Addr << endl;
		
	}
	else
	{
		cout << "���޴���" << endl;
	}
	system("pause");		//�밴���������
	system("cls");		//��������
}

//5.�޸���ϵ��
void modifyPerson(Addressbooks* abs)
{
	cout << "��������Ҫ�޸ĵ���ϵ��" << endl;
	string name;
	cin >> name;

	//�ж�ָ������ϵ���Ƿ������ͨѶ¼��
	int ret = isExist(abs, name);
	if (ret != -1)
	{
		//����
		string name;
		cout << "������������" << endl;
		cin >> name;
		abs->personArray[ret].m_Name = name;

		//�Ա�
		cout << "�������Ա�" << endl;
		cout << "1---��" << endl;
		cout << "2---Ů" << endl;
		int sex = 0;

		while (true)
		{
			//���������1����2�����˳�ѭ��
			//�������������������
			cin >> sex;
			if (sex == 1 || sex == 2)
			{
				abs->personArray[ret].m_Sex = sex;
				break;
			}
			cout << "������������������" << endl;
		}

		//����
		cout << "���������䣺" << endl;
		int age = 0;
		cin >> age;
		abs->personArray[ret].m_Age = age;

		//�绰
		cout << "������绰��" << endl;
		string phone;
		cin >> phone;
		abs->personArray[ret].m_Phone = phone;

		//סַ
		cout << "������סַ��" << endl;
		string address;
		cin >> address;
		abs->personArray[ret].m_Addr = address;
		//����

		//�绰

		//סַ

	}
	else
	{
		cout << "���޴���" << endl;
	}
	system("pause");		//�밴���������
	system("cls");		//��������
}


//�����ϵ��
void cleanPerson(Addressbooks* abs)
{
	abs->m_Size = 0;		//����ǰ��¼��ϵ��������Ϊ0�����߼����
	cout << "ͨѶ¼�Ѿ����" << endl;
	//�����������
	system("pause");		//�밴���������
	system("cls");		//��������
}

int main()
{
	//����ͨѶ¼�ṹ�����
	Addressbooks abs;

	//��ʼ��ͨѶ¼�е�ǰ��Ա����
	abs.m_Size = 0;

	int select = 0;	//�����û�ѡ������ı���
	while (true)
	{
		//���ò˵���ʾ���溯��
		showMenu();

		//��ʾ�û�����ѡ��
		cout << "��������Ҫ����ʲô���������Ӧ���֣�";

		cin >> select;
		switch (select)
		{
		case 0:
			cout << "���˳�ͨѶ¼ϵͳ��лл����ʹ�ã�" << endl;
			return 0;
			break;
		case 1:
			cout << "��������Ҫ��ӵ���ϵ����Ϣ��" << endl;
			// �����ϵ�˵Ĵ����ڴ˴�...
			addPerson(&abs);   //���õ�ַ���ݣ���������ʵ��
			break;
		case 2:
			cout << "���������е���ϵ����Ϣ��" << endl;
			// ��ʾ��ϵ�˵Ĵ����ڴ˴�...
			showPerson(&abs);
			break;
		case 3:
		//{
		//	cout << "��������Ҫɾ������ϵ�����ƣ�" << endl;
		//	// ɾ����ϵ�˵Ĵ����ڴ˴�...
		//	cout << "������ɾ����ϵ��������" << endl;
		//	string name;
		//	cin >> name;

		//	if (isExist(&abs, name) == -1)
		//	{
		//		cout << "���޴���" << endl;
		//	}
		//	else
		//	{
		//		cout << "�ҵ�����" << endl;
		//	}
		//	break;
		//}
			deletePerson(&abs);
			break;

		case 4:
			cout << "��������Ҫ���ҵ���ϵ�����ƣ�" << endl;
			// ������ϵ�˵Ĵ����ڴ˴�...
			findPerson(&abs);
			break;
		case 5:
			// �޸���ϵ����Ϣ
			cout << "������Ҫ�޸ĵ���ϵ�����ƣ�" << endl;
			modifyPerson(&abs);
			break;
		case 6:
			cout << "�������������ϵ�ˡ�" << endl;
			// ���������ϵ�˵Ĵ����ڴ˴�...
			cleanPerson(&abs);
			break;
		default:
			cout << "��Ч���룬������ѡ��" << endl;
			break;
		}
	}
	return 0;
}