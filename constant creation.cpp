#include <iostream>
using namespace std;
/*常量的定义方式：
1.#define 宏常量
2.const 修饰变量
*/
//1.宏常量
#define day 7

int main(){
    //day=14;//此处报错，day为常量，一旦修改就会报错
    cout << "一周总共有" << day << "天" << endl;
    //2.const修饰变量
    const int month = 12;
    //month=24//此处报错，const修饰的变量也称为常量，一旦修改就会报错
    cout << "一年总共有" << month << "个月" << endl;
    system("pause");
    return 0;

}