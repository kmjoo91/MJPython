#define _CRT_SECURE_NO_WARNINGS //strcpy 해결
#include <iostream>
using namespace std;

class Person{
private:
	char* m_name;
	int m_age;
public:
	Person();
	Person(const char* name, const int& age);
	Person(const Person& p);
	~Person();
	void setName(const char* name);
	void setAge(const int& age);
	Person& aging();
	void showInfo() const;
};

Person& Person::aging(){ //레퍼런스 타입이므로 런타임 오류 없음
	this->m_age++;
	return *this;
}

Person::Person()
:m_age(0)
{
	cout << "디폴트 생성자" << endl;
	m_name = new char[strlen("이름없음") + 1];
	strcpy(m_name, "이름없음");
}

Person::Person(const char* name, const int& age)
:m_age(age)
{
	cout << "인자있는 생성자" << endl;
	m_name = new char[strlen(name) + 1];
	strcpy(m_name, name);
}

Person::Person(const Person& p)
	:m_age(p.m_age)
{
	cout << "복사 생성자" << endl;
	m_name = new char[strlen(p.m_name) + 1];
	strcpy(m_name, p.m_name);
}

Person::~Person(){
	cout << "소멸자" << endl;
	delete[] m_name;
}

void Person::setName(const char* name){
	if (m_name != NULL)
		delete[] m_name; //메모리 누수 주의!
	m_name = new char[strlen(name) + 1];
	strcpy(m_name, name);
}

void Person::setAge(const int& age){
	m_age = age;
}


void Person::showInfo() const{
	cout << "주소 : " << this << endl;
	cout << "이름 : " << m_name << endl;
	cout << "나이 : " << m_age << endl;
}
int main(){
	cout << "201111265 김병수" << endl;

	Person std1("홍길동", 20);

	Person std2(std1);
	Person std3 = std1;
	std3.showInfo();

	std3.aging();
	//std2 = std3;
	return 0;
}

//확인하고 지우고 할당