#include <iostream>
using namespace std;
/*�����Ķ��巽ʽ��
1.#define �곣��
2.const ���α���
*/
//1.�곣��
#define day 7

int main(){
    //day=14;//�˴�����dayΪ������һ���޸ľͻᱨ��
    cout << "һ���ܹ���" << day << "��" << endl;
    //2.const���α���
    const int month = 12;
    //month=24//�˴�����const���εı���Ҳ��Ϊ������һ���޸ľͻᱨ��
    cout << "һ���ܹ���" << month << "����" << endl;
    system("pause");
    return 0;

}