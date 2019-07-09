#include <iostream>
#include <stdio.h>

int ParticleOne = 0;
int ParticleTwo = 0;

void printGameboard()
{
    
}

void Colision()
{
    
}

void OutOfBounds()
{
    
}


int main()
{
    ParticleOne = 1;
    ParticleTwo = 2;
    int distance = 0;
    
    std::cout << "please enter the particle you want to move '1 = Partice One' and '2 = Particle Two\n";
    std::cin >> ParticleOne;
    std::cin >> ParticleTwo;
    
    
    bool mycondition = true;
    while (mycondition ==true)
    {
        char direction = 0;
        
        std::cout << "please enter the direction you want the particle to move (x or y) \n";
        std::cin >> direction;
        
        if (direction == 'x' || 'y')
            return true;
        else
        {
        std::cout << "that is not a valid direction. please enter x or y\n";
        }
    }
    
    std::cout << "please enter a distance the particle should travel in that direction\n";
    std::cin >> distance
    
    
    return 0;
}
