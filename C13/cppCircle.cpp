/* 定义了圆类的C++程序 */
#include <iostream>
const double PI = 3.14159;  // 圆周率
class Circle    // 圆
{
private:
    double r;   // 半径

public:
    Circle(double r_)   // 构造器
    {
        r = r_;
    }
    double area()       // 计算面积
    {
        return PI * r * r;
    }
    double perimiter()  // 计算周长
    {
        return 2 * PI * r;
    }
};
int main()
{
    double r;
    std::cout << "请输入圆的半径：";
    std::cin >> r;
    Circle c = Circle(r);
    std::cout << "圆的面积为：" << c.area() << std::endl;
    std::cout << "圆的周长为：" << c.perimiter() << std::endl;
}
