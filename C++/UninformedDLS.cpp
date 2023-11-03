#include <iostream>
#include <list>
#include <unordered_map>
using namespace std;

class Graph {
    int V;
    unordered_map<int, list<int>> adj;

public:
    Graph(int vertices);
    void addEdge(int u, int v);
    bool DLS(int src, int target, int maxDepth);
    bool IDDFS(int src, int target, int maxDepth);
};

Graph::Graph(int vertices) {
    V = vertices;
}

void Graph::addEdge(int u, int v) {
    adj[u].push_back(v);
}

bool Graph::DLS(int src, int target, int maxDepth) {
    if (src == target)
        return true;

    if (maxDepth <= 0)
        return false;

    for (int& neighbor : adj[src]) {
        if (DLS(neighbor, target, maxDepth - 1))
            return true;
    }

    return false;
}

bool Graph::IDDFS(int src, int target, int maxDepth) {
    for (int i = 0; i <= maxDepth; i++) {
        if (DLS(src, target, i))
            return true;
    }
    return false;
}

int main() {
    Graph g(7);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 5);
    g.addEdge(2, 6);

    int target = 6;
    int maxDepth = 2;
    int src = 0;

    if (g.DLS(src, target, maxDepth))
        cout << "Target is reachable from source within max depth" << endl;
    else
        cout << "Target is NOT reachable from source within max depth" << endl;

    return 0;
}