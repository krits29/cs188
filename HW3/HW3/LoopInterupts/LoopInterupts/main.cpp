#include <stdio.h>
#include <iostream>

int main()
{
    bool mycondition = true;
    while(mycondition == true/*boolean condition*/)
    {
        int x = 0;
        
        std::cout << "please enter a number\n";
        std::cin >> x;
        
        if(x % 9 == 0)
        {
            std::cout << "the number is divisible by nine\n";
        }
        else
        {
            std::cout << "the number isn't divisible by nine\n";
        }
    }
    
    
    do
    {
        
    } while (mycondition==true/*boolean condition*/);
    
    //LOOP INTERUPTS
    //break - this will throw you out of the loop
    //continue - this will skip the rest of the loop and take you to the beginning of the loop
    
    while (true)
    {
        int x = 0;
        if(x % 9 == 0)
        {
            break;
        }
        
    //CONTINUE statement
    while (false)
    {
        continue;
    }
        
        
    }
    return 0;
    
}
