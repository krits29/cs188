#include <iostream>
#include <stdio.h>

int main()
{
    int MyArray[10];   // the array indices start from 0 and go 1 less than the max size
    MyArray[0]= 1;     //the numbers in the square brackets are called indices
    MyArray[1]= 2;
    MyArray[2]= 3;
    MyArray[3]= 4;
    MyArray[4]= 5;
    MyArray[5]= 6;
    MyArray[6]= 7;
    MyArray[7]= 8;
    MyArray[8]= 9;
    MyArray[9]= 10;
    
    std::cout << "MyArray[0]" << MyArray[0] << "\n";
    
    for(int i = 0; i < 10; i++)
    {
        std::cout << "MyArray[ "<< i <<" ] = "<< MyArray[0] << "\n";
    }
    
    
    char twoDArray[10][10];
    for(int i = 0; i < 10; i++) // we are going over all of the rows
    {
        for(int j = 0; j < 10; j++)
        {
            twoDArray[i][j] = ' ';
        }
    }
    
    twoDArray[1][4] = 'x';
    twoDArray[3][5] = 'o';
    
    for(int i = 0; i < 10; i++)
    {
        std::cout << "MyArray[ "<< i <<" ] = "<< MyArray[0] << "\n";
    }
    
    
    for(int i = 0; i < 10; i++) // we are going over all of the rows
    {
        for(int j = 0; j < 10; j++)
        {
            std::cout << "|" << twoDArray[i][j];
        }
        std::cout << "\n-------------------\n";
    }

    return 0;
}
