# dijkstra-algorithm-project
Shortest route finder using Dijkstra Algorithm with Python Tkinter GUI

This project aims to implement Dijkstra’s algorithm using Python with a Tkinter-based graphical user interface to determine the shortest path between multiple location nodes. The system is designed to represent the shortest path problem using a weighted graph structure, where nodes represent locations and edges represent the distance between them as weights.

In this system, users can select a starting point and a destination through a simple graphical interface. The application then processes the input using Dijkstra’s algorithm to compute the path with the minimum total weight from the source node to the target node. The results are displayed in the form of the optimal route, detailed information about each visited location, and the total travel distance.

The implementation utilizes a priority queue (heapq) to efficiently select the node with the smallest tentative distance during each iteration of the algorithm. Additionally, a dictionary-based weighted graph structure is used to store the relationships between nodes and their corresponding weights.

This program is developed using the Python programming language with the Tkinter library for the user interface. The graph data structure is used to model the map of locations, demonstrating the practical application of Dijkstra’s algorithm in real-world scenarios such as route optimization and navigation systems.
