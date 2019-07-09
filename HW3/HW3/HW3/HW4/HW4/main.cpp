//
//  main.cpp
//  HW4
//
//  Created by Kriti Sharma on 3/21/17.
//  Copyright © 2017 Kriti Sharma. All rights reserved.
//

#include <iostream>
#include <stdio.h>

int main()
{
    bool mycondition = true;
    while(mycondition == true)
    {
    int a = 0;
    int b = 0;
    int c = 0;
    int d = 0;
    
    std::cout << "please enter a multiplication sequence of four numbers\n enter your first number\n";
    std::cin >>a;
    
    std::cout << "please enter your second number\n";
    std::cin >>b;
    
    std::cout << "please enter your third number\n";
    std::cin >>c;
    
    std::cout<<"plese enter the last number\n";
    std::cin >>d;
        
    if((b = 2*a), (c = 3*a), (d = 4*a))
    {
        std::cout << "Wuhoo! Your list was in sequence\n";
    }
    else
    {
        std::cout << "Sorry. Your list wasn't in a sequence. Try again\n";
    }
        
    }
    
    
    return 0;
}
