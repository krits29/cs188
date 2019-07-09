#include <iostream>
#include <stdio.h>
#include "MyHeader.h"

void printMyName ();

void printMyName ()   //this is a function signature - telling computer that a definition for this will be provided later
{
    std::cout <<"My name is Kriti!!\n";
}

int main()
{
    printMyName();
    SampleFunction();;
    
    return 0;
}

