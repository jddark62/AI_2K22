# solve the 8 puzzle problem using uninformed heuristic search algorithms

from queue import PriorityQueue
import sys
import time
import math
import random

class Puzzle(object):
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def solve(self, method):
        if method == "bfs":
            return self.bfs()
        elif method == "dfs":
            return self.dfs()
        elif method == "astar":
            return self.astar()
        elif method == "idastar":
            return self.idastar()
        else:
            print("invalid method")
            return None

    def bfs(self):
        start = time.time()
        fringe = [self.initial]
        expanded = 0
        while fringe:
            node = fringe.pop(0)
            expanded += 1
            if node.state == self.goal:
                end = time.time()
                return (node, expanded, end - start)
            fringe.extend(node.expand())
        return None

    def dfs(self):
        start = time.time()
        fringe = [self.initial]
        expanded = 0
        while fringe:
            node = fringe.pop()
            expanded += 1
            if node.state == self.goal:
                end = time.time()
                return (node, expanded, end - start)
            fringe.extend(node.expand())
        return None

    def astar(self):
        start = time.time()
        fringe = PriorityQueue()
        fringe.put(self.initial)
        expanded = 0
        while not fringe.empty():
            node = fringe.get()
            expanded += 1
            if node.state == self.goal:
                end = time.time()
                return (node, expanded, end - start)
            for child in node.expand():
                fringe.put(child)
        return None

    def idastar(self):
        start = time.time()
        bound = self.initial.manhattan()
        fringe = [self.initial]
        expanded = 0
        while fringe:
            node = fringe.pop()
            expanded += 1
            if node.manhattan() > bound:
                fringe.append(node)
                continue
            if node.state == self.goal:
                end = time.time()
                return (node, expanded, end - start)
            for child in node.expand():
                fringe.append(child)
            bound = min(n.manhattan() for n in fringe)
        return None
    
class Node(object):
    def __init__(self, state, parent, operator, depth, cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def expand(self):
        nodes = []
        nodes.append(self.move_up())
        nodes.append(self.move_down())
        nodes.append(self.move_left())
        nodes.append(self.move_right())
        return [node for node in nodes if node is not None]

    def move_up(self):
        if self.state.index(0) < 3:
            return None
        else:
            new_state = self.state[:]
            index = new_state.index(0)
            new_state[index], new_state[index - 3] = new_state[index - 3], new_state[index]
            return Node(new_state, self, "Up", self.depth + 1, self.depth + 1 + self.manhattan())

    def move_down(self):
        if self.state.index(0) > 5:
            return None
        else:
            new_state = self.state[:]
            index = new_state.index(0)
            new_state[index], new_state[index + 3] = new_state[index + 3], new_state[index]
            return Node(new_state, self, "Down", self.depth + 1, self.depth + 1 + self.manhattan())

    def move_left(self):
        if self.state.index(0) % 3 == 0:
            return None
        else:
            new_state = self.state[:]
            index = new_state.index(0)
            new_state[index], new_state[index - 1] = new_state[index - 1], new_state[index]
            return Node(new_state, self, "Left", self.depth + 1, self.depth + 1 + self.manhattan())

    def move_right(self):
        if self.state.index(0) % 3 == 2:
            return None
        else:
            new_state = self.state[:]
            index = new_state.index(0)
            new_state[index], new_state[index + 1] = new_state[index + 1], new_state[index]
            return Node(new_state, self, "Right", self.depth + 1, self.depth + 1 + self.manhattan())

    def manhattan(self):
        distance = 0
        for i in range(9):
            if self.state[i] != 0:
                distance += abs(i % 3 - self.state[i] % 3) + abs(i // 3 - self.state[i] // 3)
        return distance
    
    def print_path(self):
        if self.parent == None:
            print("Initial state:")
        else:
            self.parent.print_path()
            print("Move", self.operator, "to", self.state)

def generate_puzzle():
    initial = [3, 1, 2, 6, 4, 5, 7, 8, 0]
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    for i in range(100):
        move = random.randint(0, 3)
        if move == 0:
            if initial.index(0) < 3:
                continue
            else:
                index = initial.index(0)
                initial[index], initial[index - 3] = initial[index - 3], initial[index]
        elif move == 1:
            if initial.index(0) > 5:
                continue
            else:
                index = initial.index(0)
                initial[index], initial[index + 3] = initial[index + 3], initial[index]
        elif move == 2:
            if initial.index(0) % 3 == 0:
                continue
            else:
                index = initial.index(0)
                initial[index], initial[index - 1] = initial[index - 1], initial[index]
        else:
            if initial.index(0) % 3 == 2:
                continue
            else:
                index = initial.index(0)
                initial[index], initial[index + 1] = initial[index + 1], initial[index]
    return initial, goal

def main():
    initial, goal = generate_puzzle()
    puzzle = Puzzle(initial, goal)  # Create an instance of the Puzzle class
    print("Initial state:")
    print(initial)
    print("Goal state:")
    print(goal)
    print("BFS:")
    bfs = puzzle.solve("bfs")
    if bfs is not None:
        bfs[0].print_path()
        print("Expanded:", bfs[1])
        print("Time:", bfs[2])
    print("DFS:")
    dfs = puzzle.solve("dfs")
    if dfs is not None:
        dfs[0].print_path()
        print("Expanded:", dfs[1])
        print("Time:", dfs[2])
    print("A*:")
    astar = puzzle.solve("astar")
    if astar is not None:
        astar[0].print_path()
        print("Expanded:", astar[1])
        print("Time:", astar[2])
    print("IDA*:")
    idastar = puzzle.solve("idastar")
    if idastar is not None:
        idastar[0].print_path()
        print("Expanded:", idastar[1])
        print("Time:", idastar[2])

if __name__ == "__main__":
    main()