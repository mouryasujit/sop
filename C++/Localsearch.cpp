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

// Simulated Anealing
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

double objectiveFunction(double x) {
    return x * x;  
}

double simulatedAnnealing(double initialX, double temperature, double coolingRate, int maxIterations) {
    double currentX = initialX;
    double bestX = currentX;
    double currentObjective = objectiveFunction(currentX);
    double bestObjective = currentObjective;

    for (int iteration = 0; iteration < maxIterations; ++iteration) {
        double candidateX = currentX + (rand() / (RAND_MAX / 2.0) - 1.0);  // Random perturbation
        double candidateObjective = objectiveFunction(candidateX);

        double acceptanceProbability = exp((currentObjective - candidateObjective) / temperature);

        if (candidateObjective < currentObjective || (rand() / static_cast<double>(RAND_MAX)) < acceptanceProbability) {
            currentX = candidateX;
            currentObjective = candidateObjective;

            if (currentObjective < bestObjective) {
                bestX = currentX;
                bestObjective = currentObjective;
            }
        }

        temperature *= 1.0 - coolingRate;
    }

    return bestX;
}

int main() {
    srand(static_cast<unsigned>(time(nullptr)));

    double initialX = 5.0; 
    double initialTemperature = 100.0;
    double coolingRate = 0.003;
    int maxIterations = 10000;

    double result = simulatedAnnealing(initialX, initialTemperature, coolingRate, maxIterations);

    cout << "Optimal solution: " << result << endl;
    cout << "Objective value: " << objectiveFunction(result) << endl;

    return 0;
}
