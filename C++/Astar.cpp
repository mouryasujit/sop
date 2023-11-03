#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;

struct Node {
    int x, y;
    int cost, heuristic;
    Node(int _x, int _y, int _cost, int _heuristic) : x(_x), y(_y), cost(_cost), heuristic(_heuristic) {}
    bool operator<(const Node& other) const {
        return (cost + heuristic) > (other.cost + other.heuristic);
    }
};

bool isValid(int x, int y, int n, int m) {
    return (x >= 0 && y >= 0 && x < n && y < m);
}

int aStar(vector<vector<int>>& grid, pair<int, int> start, pair<int, int> end) {
    int n = grid.size();
    int m = grid[0].size();
    vector<vector<bool>> visited(n, vector<bool>(m, false));

    priority_queue<Node> pq;
    pq.push({start.first, start.second, 0, abs(end.first - start.first) + abs(end.second - start.second)});

    while (!pq.empty()) {
        Node curr = pq.top();
        pq.pop();

        int x = curr.x;
        int y = curr.y;
        int cost = curr.cost;

        if (x == end.first && y == end.second) {
            return cost;
        }

        if (!visited[x][y]) {
            visited[x][y] = true;

            int dx[] = {-1, 1, 0, 0};
            int dy[] = {0, 0, -1, 1};

            for (int i = 0; i < 4; i++) {
                int newX = x + dx[i];
                int newY = y + dy[i];

                if (isValid(newX, newY, n, m) && !visited[newX][newY]) {
                    pq.push({newX, newY, cost + grid[newX][newY], abs(end.first - newX) + abs(end.second - newY)});
                }
            }
        }
    }

    return -1; // Path not found
}

int main() {
    vector<vector<int>> grid = {
        {1, 3, 1},
        {2, 2, 3},
        {1, 4, 1}
    };

    pair<int, int> start = {0, 0};
    pair<int, int> end = {2, 2};

    int result = aStar(grid, start, end);

    if (result != -1) {
        cout << "Shortest path cost: " << result << endl;
    } else {
        cout << "Path not found." << endl;
    }

    return 0;
}