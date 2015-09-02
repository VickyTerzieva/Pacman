from queue import Queue
from code.walls import taken_by_walls
from code.ghosts import STEP


def neighbours(node):
    neighbours_to_node = []

    if taken_by_walls[node.x() - STEP][node.y()] is False:
        neighbours_to_node.extend([[node.x() - STEP][node.y()]])
    if taken_by_walls[node.x() + STEP][node.y()] is False:
        neighbours_to_node.extend([[node.x() + STEP][node.y()]])
    if taken_by_walls[node.x()][node.y() - STEP] is False:
        neighbours_to_node.extend([[node.x()][node.y() - STEP]])
    if taken_by_walls[node.x()][node.y() + STEP] is False:
        neighbours_to_node.extend([[node.x()][node.y() + STEP]])

    return neighbours_to_node


def breadth_first_search(start, goal):

    visited = [[False for x in range(500)] for y in range(500)]
    queue = Queue()
    queue.put_nowait(start)
    visited[start.x()][start.y()] = True
    current_node = queue.get()
    node_neighbours = neighbours(current_node)

    for i in range(node_neighbours.__len__()):
        if visited[node_neighbours[i].x()][node_neighbours[i].y()] \
                is False:
            
            queue.put_nowait(node_neighbours[i])
            visited[current_node.x()][current_node.y()] = True

    while not current_node.x() == goal.x() \
            and not current_node.y() == goal.y():

        current_node = queue.get()
        node_neighbours = neighbours(current_node)

        for i in range(node_neighbours.__len__()):
            if visited[node_neighbours[i].x()][node_neighbours[i].y()] \
                    is False:
                queue.put_nowait(node_neighbours[i])
                visited[current_node.x()][current_node.y()] = True
