// solve the machineries cannibal problem using searching (artificial intelligence)

#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <algorithm>

using namespace std;

// define the state of the problem
class State {
public:
    vector<int> cannibals;
    vector<int> missionaries;
    int boat;
    int depth;

    State(vector<int> c, vector<int> m, int b, int d) {
        cannibals = c;
        missionaries = m;
        boat = b;
        depth = d;
    }

    // default constructor
    State() {
        cannibals = vector<int>();
        missionaries = vector<int>();
        boat = 0;
        depth = 0;
    }

    // check if the state is valid
    bool isValid() {
        for (int i = 0; i < cannibals.size(); i++) {
            if (cannibals[i] < 0 || missionaries[i] < 0) return false;
            if (cannibals[i] > missionaries[i] && missionaries[i] != 0) return false;
        }
        return true;
    }

    // check if the state is a goal state
    bool isGoal() {
        for (int i = 0; i < cannibals.size(); i++) {
            if (cannibals[i] != 0 || missionaries[i] != 0) return false;
        }
        return true;
    }

    // check if the state is already visited
    bool isVisited(unordered_set<string> &visited) {
        string s = "";
        for (int i = 0; i < cannibals.size(); i++) {
            s += to_string(cannibals[i]) + " ";
        }
        for (int i = 0; i < missionaries.size(); i++) {
            s += to_string(missionaries[i]) + " ";
        }
        s += to_string(boat);
        if (visited.find(s) != visited.end()) return true;
        visited.insert(s);
        return false;
    }

    // print the state
    void print() {
        for (int i = 0; i < cannibals.size(); i++) {
            cout << cannibals[i] << " ";
        }
        cout << "|| ";
        for (int i = 0; i < missionaries.size(); i++) {
            cout << missionaries[i] << " ";
        }
        cout << "|| " << boat << endl;
    }
};

// define the node of the search tree
class Node {
public:
    State state;
    Node *parent;

    Node(State s, Node *p) {
        state = s;
        parent = p;
    }
};

// define the problem
class Problem {
public:
    vector<int> cannibals;
    vector<int> missionaries;
    int boat;

    Problem(vector<int> c, vector<int> m, int b) {
        cannibals = c;
        missionaries = m;
        boat = b;
    }

    // check if the problem is valid
    bool isValid() {
        for (int i = 0; i < cannibals.size(); i++) {
            if (cannibals[i] < 0 || missionaries[i] < 0) return false;
            if (cannibals[i] > missionaries[i] && missionaries[i] != 0) return false;
        }
        return true;
    }

    // check if the problem is solvable
    bool isSolvable() {
        int sumCannibals = 0;
        int sumMissionaries = 0;
        for (int i = 0; i < cannibals.size(); i++) {
            sumCannibals += cannibals[i];
            sumMissionaries += missionaries[i];
        }
        if (sumCannibals > sumMissionaries) return false;
        return true;
    }

    // solve the problem using BFS
    void solve() {
        if (!isValid()) {
            cout << "The problem is not valid." << endl;
            return;
        }
        if (!isSolvable()) {
            cout << "The problem is not solvable." << endl;
            return;
        }
        queue<Node*> q;
        unordered_set<string> visited;
        State initialState(cannibals, missionaries, boat, 0);
        Node *initialNode = new Node(initialState, NULL);
        q.push(initialNode);
        while (!q.empty()) {
            Node *currentNode = q.front();
            q.pop();
            if (currentNode->state.isGoal()) {
                vector<Node*> path;
                Node *temp = currentNode;
                while (temp != NULL) {
                    path.push_back(temp);
                    temp = temp->parent;
                }
                reverse(path.begin(), path.end());
                for (int i = 0; i < path.size(); i++) {
                    path[i]->state.print();
                }
                return;
            }
            vector<State> nextStates = getNextStates(currentNode->state);
            for (int i = 0; i < nextStates.size(); i++) {
                if (!nextStates[i]. isValid() || nextStates[i].isVisited(visited)) continue;
                Node *nextNode = new Node(nextStates[i], currentNode);
                q.push(nextNode);
            }
        }
        cout << "No solution." << endl;
    }
    
    // get the next states of the current state
    vector<State> getNextStates(State currentState) {
        vector<State> nextStates;
        // boat is on the left side
        if (currentState.boat == 0) {
            // move two cannibals
            for (int i = 0; i < currentState.cannibals.size(); i++) {
                vector<int> nextCannibals = currentState.cannibals;
                vector<int> nextMissionaries = currentState.missionaries;
                nextCannibals[i]--;
                nextMissionaries[i]--;
                State nextState(nextCannibals, nextMissionaries, 1, currentState.depth + 1);
                nextStates.push_back(nextState);
            }
            // move one cannibal
            for (int i = 0; i < currentState.cannibals.size(); i++) {
                vector<int> nextCannibals = currentState.cannibals;
                vector<int> nextMissionaries = currentState.missionaries;
                nextCannibals[i]--;
                State nextState(nextCannibals, nextMissionaries, 1, currentState.depth + 1);
                nextStates.push_back(nextState);
            }
            // move one missionary
            for (int i = 0; i < currentState.missionaries.size(); i++) {
                vector<int> nextCannibals = currentState.cannibals;
                vector<int> nextMissionaries = currentState.missionaries;
                nextMissionaries[i]--;
                State nextState(nextCannibals, nextMissionaries, 1, currentState.depth + 1);
                nextStates.push_back(nextState);
            }
        } // boat is on the right side 
        else {
            // move two cannibals
            for (int i = 0; i < currentState.cannibals.size(); i++) {
                vector<int> nextCannibals = currentState.cannibals;
                vector<int> nextMissionaries = currentState.missionaries;
                nextCannibals[i]++;
                nextMissionaries[i]++;
                State nextState(nextCannibals, nextMissionaries, 0, currentState.depth + 1);
                nextStates.push_back(nextState);
            }
            // move one cannibal
            for (int i = 0; i < currentState.cannibals.size(); i++) {
                vector<int> nextCannibals = currentState.cannibals;
                vector<int> nextMissionaries = currentState.missionaries;
                nextCannibals[i]++;
                State nextState(nextCannibals, nextMissionaries, 0, currentState.depth + 1);
                nextStates.push_back(nextState);
            }
            // move one missionary
            for (int i = 0 ; i < currentState.missionaries.size(); i++) {
                vector<int> nextCannibals = currentState.cannibals;
                vector<int> nextMissionaries = currentState.missionaries;
                nextMissionaries[i]++;
                State nextState(nextCannibals, nextMissionaries, 0, currentState.depth + 1);
                nextStates.push_back(nextState);
            }

        }
        return nextStates;
    }
};

int main() {
    vector<int> cannibals = {3, 3, 1};
    vector<int> missionaries = {3, 3, 1};
    int boat = 0;
    Problem problem(cannibals, missionaries, boat);
    problem.solve();
    return 0;
}


/*  //explanation
// how is the problem defined?
// the problem is defined by the number of cannibals and missionaries on each side of the river, and the position of the boat
// how is the problem solved?
// the problem is solved using BFS
// how is the problem solved using BFS?
// the problem is solved using BFS by using a queue to store the nodes, and a set to store the visited states
// how do we know goal is reached?
// we know the goal is reached when the number of cannibals and missionaries on the right side of the river
// is equal to the total number of cannibals and missionaries */