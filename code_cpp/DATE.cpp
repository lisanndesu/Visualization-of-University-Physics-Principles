#include <iostream>
using namespace std;

class Date;

ostream& operator<<(ostream& out, Date& obj);


class Date

{

	public:
	
	// 获取某年某月的天数
	
	int GetMonthDay(int year, int month)
	{
		if(month<1||month>12)
		{
			cout<<"输入有误";
			exit(1);
		}
		int days[13] = {-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		if (month==2 && (year%4==0 && year%100!=0 ||year%400==0))
		{
			return 29;
		}
		return days[month];
	}
	  // 全缺省的构造函数
	
	Date(int year = 1900, int month = 1, int day = 1){
		_year = year;
		_month = month;
		_day = day;
	}
	  // 拷贝构造函数
	
	// d2(d1)
	
	Date(const Date& d){
		_year = d._year;
		_month = d._month;
		_day = d._day;
	}
	
	  // 赋值运算符重载
	
	// d2 = d3 -> d2.operator=(&d2, d3)
	
	Date& operator=(const Date& d)
	{
		_year = d._year;
		_month = d._month;
		_day = d._day;
	}
	
	
	
	  // 析构函数
	
	~Date(){
	};
	
	
	
	  // 日期+=天数
	
	void operator+=(int day)
	{
		_day+=day;
		while(_day>GetMonthDay(_year, _month))
		{
			_day-=GetMonthDay(_year, _month);
			_month++;
			if (_month>12)
			{
				_year++;
				_month = 1;
			}
		}
//		cout<<"进入+=operator"<<*this<<endl;
	}
	
	
	
	  // 日期+天数
	
	Date operator+(int day)
	{
		Date obj = *this;
		obj+=day;
		return obj;
	}
	
	
	
	  // 日期-天数
	
	Date operator-(int day)
	{
		Date obj = *this;
		obj-=day;
		return obj;
	}
	
	
	
	   // 日期-=天数
	
	Date& operator-=(int day)
	{
		_day -= day;
		while(_day<1)
		{
			_month--;
			if(_month<1)
			{
				_month = 12;
				_year--;
			}
			
			_day+=GetMonthDay(_year, _month);
		}
	}
	
	
	
	  // 前置++
	
	Date& operator++(int)
	{
		cout<<"进入++"<<endl;
		*this+=1;
		Date obj = *this-1;
		return obj;
	}
	
	
	
	  // 后置++
	
	Date& operator++()
	{
		cout<<"进入++"<<endl;
		*this+=1;
		return *this;
	}
	
	
	
	  // 后置--
	
	Date operator--(int)
	{
		*this-=1;
		return *this+1;
	}
	
	
	
	  // 前置--
	
	Date& operator--()
	{
		*this-=1;
		return *this;
	}
	
	
	
	  // >运算符重载
	
	bool operator>( Date& d)
	{
		if(_year > d.gety())
		{
			return true;
		}
		if(this->_year==d.gety())
		{
			if(this->_month>d.getm())
			{

				return true;
			}
			else if(this->_month==d.getm())
			{
				if(this->_day>d.getd())
				{
					cout<<"d"<<endl;
					return true;
				}
			}
		}
		return false;
	}
	
	
	
	  // ==运算符重载
	
	bool operator==( Date& d)
	{
		if(_year==d.gety()||_month==d.getm()||_day==d.getd())
		{
			return true;
		}
		return false;
	}
	
	
	
	  // >=运算符重载
	
	bool operator >= ( Date& d)
	{
		if(*this<d)
		{
			return false;
		}
		return true;
	}
	
	   
	
	  // <运算符重载
	
	bool operator < ( Date& d)
	{
		if(*this > d||*this==d)
		{
			return false;
		}
		return true;
	}
	
	
	
	   // <=运算符重载
	
	bool operator <= ( Date& d)
	{
		if(*this<d||*this==d)
		{
			return true;
		}
		return false;
	}
	
	
	
	  // !=运算符重载
	
	bool operator != (Date& d)
	{
		return !(*this==d);
	}
	
	
	
	  // 日期-日期 返回天数
	  
	int gety()
	{
		return _year;
	}
	
	int getm()
	{
		return _month;
	}
	
	int getd()
	{
		return _day;
	}
	int operator-(const Date& d);
	private:
	int _year;
	int _month;
	int _day;
};

ostream& operator<<(ostream& out, Date& obj)
{
	cout<<obj.gety()<<"年"<<obj.getm()<<"月"<<obj.getd()<<"日";
	return out;
}

int main()
{
	Date *obj = new Date(2024, 4, 19);
	cout<<*obj<<endl;
	Date *obj1 = new Date(*obj);
	cout<<*obj1<<endl;
	*obj1+=100;
	cout<<*obj1<<endl;

	Date obj2=*obj1+100;
	cout<<obj2<<endl;
	
	Date obj3 = obj2-100;
	cout<<obj3<<endl;
	
	cout<<(obj3>obj2)<<endl;
	cout<<++obj3<<endl;
	
	
	
	return 0;
}
