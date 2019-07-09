#include <iostream>
#include <stdio.h>

int myGlobalVariable = 30;

void myPrintingFunction()
{   //stuff between is called the body
    std::cout << "What is amazing and five letters????\nme (Kriti)\n";
}

int Add(int a, int b)
{
    int x = a + b;
    return x;
}

int aChecker(char charInput)
{
    if (charInput == 'a')
        return true;
    else
        return false;
}

int main()
{
    int x = 10;
    
    x = 20;
    
    int y = 0;
    
    myPrintingFunction(); //invoking a function
    int z = Add(x, y);    //invoking a function
    
    {
        int mylocal = 30;
    }
    
    return 0;
}