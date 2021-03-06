from queue import Queue, LifoQueue
from code.walls import taken_by_walls
from code.pair import Pair

STEP = 12


def breadth_first_search(start, goal):
    visited = [[False for x in range(500)] for y in range(500)]
    dad = [[None for x in range(500)] for y in range(500)]

    queue = Queue()
    visited[start.first()][start.second()] = True
    dad[start.first()][start.second()] = start
    current_node = start
    neighbours_ = neighbours(current_node)

    if not goal.first() - 10 <= current_node.first() <= goal.first() + 10 \
            or not \
            goal.second() - 10 <= current_node.second() <= goal.second() + 10:
        for i in range(neighbours_.__len__()):
            if visited[neighbours_[i].first()][neighbours_[i].second()] \
                    is False:
                queue.put(neighbours_[i])
                visited[neighbours_[i].first()][neighbours_[i].second()] \
                    = True
                dad[neighbours_[i].first()][neighbours_[i].second()] \
                    = current_node

    while (not goal.first() - 10 <= current_node.first() <= goal.first() + 10
            or not goal.second() - 10 <= current_node.second()
            <= goal.second() + 10) and not queue.empty():
        current_node = queue.get_nowait()
        neighbours_ = neighbours(current_node)

        for i in range(neighbours_.__len__()):
            if visited[neighbours_[i].first()][neighbours_[i].second()] \
                    is False:
                queue.put(neighbours_[i])
                visited[neighbours_[i].first()][neighbours_[i].second()] \
                    = True
                dad[neighbours_[i].first()][neighbours_[i].second()] \
                    = current_node

    path = LifoQueue()
    while not current_node.first() == start.first() \
            or not current_node.second() == start.second():
        path.put(current_node)
        current_node = dad[current_node.first()][current_node.second()]

    return path


def neighbours(node):
    neighbours_to_node = []

    if is_in_range(node.first() - STEP, node.second()):
        if taken_by_walls[node.first() - STEP][node.second()] is False:
            new_node = Pair(node.first() - STEP, node.second())
            neighbours_to_node.append(new_node)

    if is_in_range(node.first() + STEP, node.second()):
        if taken_by_walls[node.first() + STEP][node.second()] is False:
            new_node = Pair(node.first() + STEP, node.second())
            neighbours_to_node.append(new_node)

    if is_in_range(node.first(), node.second() - STEP):
        if taken_by_walls[node.first()][node.second() - STEP] is False:
            new_node = Pair(node.first(), node.second() - STEP)
            neighbours_to_node.append(new_node)

    if is_in_range(node.first(), node.second() + STEP):
        if taken_by_walls[node.first()][node.second() + STEP] is False:
            new_node = Pair(node.first(), node.second() + STEP)
            neighbours_to_node.append(new_node)

    return neighbours_to_node


def is_in_range(x, y):
    return 0 <= x <= 470 and 0 <= y <= 500