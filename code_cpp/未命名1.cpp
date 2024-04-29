#include <stdio.h> 
#include <iostream>

using namespace std;


class Date

{

public:

// 获取某年某月的天数

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



  // 全缺省的构造函数

Date(int year = 1900, int month = 1, int day = 1)

{

if(year < 1900

|| month < 1 || month > 12

|| day < 1 || day > GetMonthDay(year ,month) )

{

cout<<"非法日期"<<endl;

}



_year = year;

_month = month;

_day = day;

}



  // 拷贝构造函数

// d2(d1)

Date(const Date& d)

{

this->_year = d._year;

_month = d._month;

_day = d._day;

}



  // 赋值运算符重载

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

   

  // 析构函数

~Date()

{

// 清理工作

}



void Print()

{

cout<<_year<<"-"<<_month<<"-"<<_day<<endl;

}



  // 日期+=天数

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



  // 日期+天数

// d + 10

Date operator+(int day)

{

Date ret(*this);

ret += day;



return ret;

}



  // 日期-天数

Date operator-(int day)

{

Date ret(*this);

ret -= day;

return ret;

}



   // 日期-=天数

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



  // 前置++

// ++d -> d.operator++(&d)

Date& operator++() 

{

*this += 1;

return *this;

}



  // 后置++

// d++ -> d.operator++(&d, 0)

Date operator++(int) 

{

Date ret(*this);

*this += 1;

return ret;

}



  // // 后置--

Date operator--(int)

{

Date ret(*this);

*this -= 1;

return ret;

}



  // 前置--

Date& operator--()

{

*this -= 1;

return *this;

}



// d1 > d2

  // >运算符重载

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



  // ==运算符重载

bool operator==(const Date& d)

{

return _year == d._year

&& _month == d._month

&& _day == d._day;

}



  // 下面复用上面两个的实现

  // >=运算符重载

bool operator >= (const Date& d)

{

return *this > d || *this == d;

}



  // <运算符重载

bool operator < (const Date& d)

{

return !(*this >= d);

}



   // <=运算符重载

bool operator <= (const Date& d)

{

return !(*this > d);

}



  // !=运算符重载

bool operator != (const Date& d)

{

return !(*this == d);

}



// d1 - d2

  // 日期-日期 返回天数

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
