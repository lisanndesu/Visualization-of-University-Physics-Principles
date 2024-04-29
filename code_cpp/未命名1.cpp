#include <stdio.h> 
#include <iostream>

using namespace std;


class Date

{

public:

// ��ȡĳ��ĳ�µ�����

int GetMonthDay(int year, int month)

{

static int days[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

int day = days[month];

if (month == 2 

&&((year % 4 == 0 && year % 100 != 0) || (year%400 == 0)))

{

day += 1;

}

return day;

}



  // ȫȱʡ�Ĺ��캯��

Date(int year = 1900, int month = 1, int day = 1)

{

if(year < 1900

|| month < 1 || month > 12

|| day < 1 || day > GetMonthDay(year ,month) )

{

cout<<"�Ƿ�����"<<endl;

}



_year = year;

_month = month;

_day = day;

}



  // �������캯��

// d2(d1)

Date(const Date& d)

{

this->_year = d._year;

_month = d._month;

_day = d._day;

}



  // ��ֵ���������

// d2 = d3 -> d2.operator=(&d2, d3)

Date& operator=(const Date& d)

{

if (this != &d)

{

this->_year = d._year;

this->_month = d._month;

this->_day = d._day;

}



return *this;

}

   

  // ��������

~Date()

{

// ������

}



void Print()

{

cout<<_year<<"-"<<_month<<"-"<<_day<<endl;

}



  // ����+=����

// d1 += 10

// d1 += -10

Date& operator+=(int day)

{

if (day < 0)

{

return *this -= -day;

}



_day += day;

while (_day > GetMonthDay(_year, _month))

{

_day -= GetMonthDay(_year, _month);

_month++;

if (_month == 13)

{

_year++;

_month = 1;

}

}



return *this;

}



  // ����+����

// d + 10

Date operator+(int day)

{

Date ret(*this);

ret += day;



return ret;

}



  // ����-����

Date operator-(int day)

{

Date ret(*this);

ret -= day;

return ret;

}



   // ����-=����

// d -= 100

// d -= -100

Date& operator-=(int day)

{

if (day < 0)

{

return *this += -day;

}



_day -= day;

while (_day <= 0)

{

--_month;

if (_month == 0)

{

--_year;

_month = 12;

}

_day += GetMonthDay(_year, _month);

}



return *this;

}



  // ǰ��++

// ++d -> d.operator++(&d)

Date& operator++() 

{

*this += 1;

return *this;

}



  // ����++

// d++ -> d.operator++(&d, 0)

Date operator++(int) 

{

Date ret(*this);

*this += 1;

return ret;

}



  // // ����--

Date operator--(int)

{

Date ret(*this);

*this -= 1;

return ret;

}



  // ǰ��--

Date& operator--()

{

*this -= 1;

return *this;

}



// d1 > d2

  // >���������

bool operator>(const Date& d)

{

if (_year > d._year)

{

return true;

}

else if (_year == d._year)

{

if (_month > d._month)

{

return true;

}

else if (_month == d._month)

{

if (_day > d._day)

{

return true;

}

}

}



return false;

}



  // ==���������

bool operator==(const Date& d)

{

return _year == d._year

&& _month == d._month

&& _day == d._day;

}



  // ���渴������������ʵ��

  // >=���������

bool operator >= (const Date& d)

{

return *this > d || *this == d;

}



  // <���������

bool operator < (const Date& d)

{

return !(*this >= d);

}



   // <=���������

bool operator <= (const Date& d)

{

return !(*this > d);

}



  // !=���������

bool operator != (const Date& d)

{

return !(*this == d);

}



// d1 - d2

  // ����-���� ��������

int operator-(const Date& d)

{

int flag = 1;

Date max = *this;

Date min = d;

if (*this < d)

{

max = d;

min = *this;

flag = -1;

}



int day = 0;

while (min < max)

{
