// Hill Climbing
#include <iostream>
#include <cmath>
#include <random>

using namespace std;

double objectiveFunction(double x) {
    return -x * x; 
}

double hillClimbing(double initialX, double stepSize, int maxIterations) {
    double currentX = initialX;
    double currentObjective = objectiveFunction(currentX);

    for (int iteration = 0; iteration < maxIterations; ++iteration) {
        double neighborX = currentX + stepSize;
        double neighborObjective = objectiveFunction(neighborX);

        if (neighborObjective > currentObjective) {
            currentX = neighborX;
            currentObjective = neighborObjective;
        } else {
            break; 
        }
    }

    return currentX;
}

int main() {
    double initialX = 2.0;  
    double stepSize = 0.1;  
    int maxIterations = 100; 

    double result = hillClimbing(initialX, stepSize, maxIterations);

    cout << "Optimal solution: " << result << endl;
    cout << "Objective value: " << objectiveFunction(result) << endl;

    return 0;
}

