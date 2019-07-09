//
//  main.cpp
//  DataTypes-Arrays
//
//  Created by Kriti Sharma on 3/21/17.
//  Copyright © 2017 Kriti Sharma. All rights reserved.
//

#include <iostream>
#include <stdio.h>

int main()
{
    int x = 1;
    char y = '1';
    char m = 'z';
    float z = 10.3;
    
    int a = z; // type coercion (typecasting) - one type may be forced to another type if there is a path
    
    int b = y;
    
    int c = m - y;
    

    //every character has been assigned a numeric ID so that it can be printed on the screen
    
    char input;
    int a = 'a';
    int b = 'b';
    
    while (true)
    {
        std::cout << "please enter a letter\n";
        std::cin >> input;
        if (input > a && input < z)
        {
            std::cout << "yes you entered a small case letter\n";
        }
        else
        {
    }
    
    
    return 0;
}
