#include <iostream>
#include <stdio.h>

int main()
{
    int MyArray[11];   // the array indices start from 0 and go 1 less than the max size
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
    MyArray[10]= 11;
    
    char etchAsketch[11][11];
    for(int i = 0; i < 11; i++) // we are going over all of the rows
    {
        for(int j = 0; j < 10; j++)
        {
            etchAsketch[i][j] = ' ';
        }
    }
    
    etchAsketch[10][0]= 'x';
    
    for(int i = 0; i < 11; i++) // we are going over all of the rows
    {
        for(int j = 0; j < 10; j++)
        {
            std::cout << "|" << etchAsketch[i][j];
        }
        std::cout << "\n-------------------\n";
    }
    

    for(int i = 0; 1 < 11;)
    {
        for(int j = 0; j < 10; j++)
        {
        char direction;
        std::cout << "Which direction would you like the dot to move: 'U' (up), 'D' (down), 'L' (left), or 'R' (right)\n";
        std::cin >> direction;
        
        if(direction == 'L')
        {
            for(int i = 0; i < 11; i++) // we are going over all of the rows
            {
                for(int j = 0; j < 10; j++)
                {
                    etchAsketch[i][j] = ' ';
                }
            }
            
            etchAsketch[10][0]= 'x';
            
            for(int i = 0; i < 11; i++) // we are going over all of the rows
            {
                for(int j = 0; j < 10; j++)
                {
                    std::cout << "|" << etchAsketch[i][j];
                }
                std::cout << "\n-------------------\n";
            }
            
        }
        else if(direction == 'U')
        {
            for(int i = 0; i < 11; i++) // we are going over all of the rows
            {
                for(int j = 0; j < 10; j++)
                {
                    etchAsketch[i][j] = ' ';
                }
            }
            
            etchAsketch[9][0]= 'x';
            etchAsketch[10][0] = 'x';
            
            for(int i = 0; i < 11; i++) // we are going over all of the rows
            {
                for(int j = 0; j < 10; j++)
                {
                    std::cout << "|" << etchAsketch[i][j];
                }
                std::cout << "\n---------------------\n";
            }
            std::cout << "Which direction would you like the dot to move\n";
            std::cin >> direction;
            if (direction == 'U')
            {
                for(int i = 0; i < 11; i++) // we are going over all of the rows
                {
                    for(int j = 0; j < 10; j++)
                    {
                        etchAsketch[i][j] = ' ';
                    }
                }
                
                etchAsketch[10][0]= 'x';
                etchAsketch[9][0]= 'x';
                etchAsketch[8][0]= 'x';
                
                for(int i = 0; i < 11; i++) // we are going over all of the rows
                {
                    for(int j = 0; j < 10; j++)
                    {
                        std::cout << "|" << etchAsketch[i][j];
                    }
                    std::cout << "\n---------------------\n";
                }
                
            }
            
            else if (direction == 'R')
            {
                for(int i = 0; i < 11; i++) // we are going over all of the rows
                {
                    for(int j = 0; j < 10; j++)
                    {
                        etchAsketch[i][j] = ' ';
                    }
                }
                
                etchAsketch[10][0]= 'x';
                etchAsketch[9][1]= 'x';
                etchAsketch[9][0]= 'x';
                
                for(int i = 0; i < 11; i++) // we are going over all of the rows
                {
                    for(int j = 0; j < 10; j++)
                    {
                        std::cout << "|" << etchAsketch[i][j];
                    }
                    std::cout << "\n---------------------\n";
                }
                
            }
            
        }
        else if(direction == 'R')
        {
            for(int i = 0; i < 11; i++) // we are going over all of the rows
            {
                for(int j = 0; j < 10; j++)
                {
                    etchAsketch[i][j] = ' ';
                }
            }
            
            etchAsketch[10][1]= 'x';
            etchAsketch[10][0]= 'x';
            
            for(int i = 0; i < 11; i++) // we are going over all of the rows
            {
                for(int j = 0; j < 10; j++)
                {
                    std::cout << "|" << etchAsketch[i][j];
                }
                std::cout << "\n---------------------\n";
            }
            
        }
        else if (direction == 'D')
        {
            for(int i = 0; i < 11; i++) // we are going over all of the rows
            {
                for(int j = 0; j < 10; j++)
                {
                    etchAsketch[i][j] = ' ';
                }
            }
            
            etchAsketch[10][0]= 'x';
            
            for(int i = 0; i < 11; i++) // we are going over all of the rows
            {
                for(int j = 0; j < 10; j++)
                {
                    std::cout << "|" << etchAsketch[i][j];
                }
                std::cout << "\n---------------------\n";
            }
            
        }
        else
        {
            std::cout << "sorry that is not a valid direction to move; choose up, down, right, or left\n\n";
        }
            
        }
    }
        
    
    
    return 0;
}
