#include <iostream>
#include <stdio.h>

int MyGlobalVariable = 0;

int main()
{
    int FrontGear = 0;
    int RearGear = 0;
    int RPM = 0;
    int speed = 0;
    int diameter = 0;
    
    std::cout << "please set the front gear of the bicycle (it must be 1, 2, or 3)\n";
    std::cin >>FrontGear;
    std::cout << "please set the rear gear of the bicycle (it must be 1, 2, 3, 4, 5, 6, or 7)\n";
    std::cin >>RearGear;
    std::cout << "now enter the average rotations per minute that the bike travels at\n";
    std::cin >>RPM;
    std::cout << "please enter the diameter of the wheel of the bicycle\n";
    std::cin >>diameter;
    
    speed = (RPM*3.1415*diameter)/60;
    
    std::cout << "the speed of the bicycle is << speed << /n";
    
    return 0;
}
