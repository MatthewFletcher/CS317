import collections
from dfs import getInput

#Define the bfs algorithm
def bfs(g, rootnode):

    #Use set() to create an empty set
    #This is the set of visited nodes, which 
    # we will add to as we progress through 
    # the graph
    visited = set()

    #Dequeue the first element in the list
    queue = collections.deque([rootnode])

    #Now that the root node has been dequeued,
    # add it to the visited set. We will not visit
    # this node again. 
    visited.add(rootnode)

    #Use a counter to keep track of rounds
    round = 0

    while queue: 
        print("\nRound {}".format(round))

        #Dequeue the first element in the list. 
        vertex = queue.popleft()
        print("Popped vertex {} from queue".format(vertex))


        #Find each neighbor for the vertex
        for neighbor in g[vertex]: 
            print("Checking neighbor {}".format(neighbor))
            if neighbor not in visited: 
                print("Visiting node {0} on round {1}".format(neighbor, round))

                #Now that it has been visited, add the
                # neighbor to the visisted set. 
                visited.add(neighbor) 

                #Also, queue the neighbor 
                # to be visited in a future round. 
                queue.append(neighbor) 
            else:
                print("Node {0} has already been visited.".format(neighbor))
        #Increment the counter. 
        round += 1

def getInput():

    graph = {}

    num = int(input("Enter the number of nodes in the graph >> "))

    for i in range(num):

        

        key = []

        line = input("Enter the nodes attached to node {}>> ".format(i))

        for number in line:
            if number.isdigit():
                key.append(int(number))

        graph[i] = key


    # print()
    # print(graph)
    # graph = {'0': set(['1', '3', '4']),
    #         '1': set(['0', '2', '4']),
    #         '2': set(['0', '1']),
    #         '3': set(['1','2', '3']),
    #         '4': set(['2', '3'])}

    # print(graph)

    #graph = {0: [1,2], 1: [0,3,4], 2: [0,5,6], 3: [1], 4: [1], 5: [2], 6: [2]} 
    #print(graph)
    return graph

def main():
    #getInput()
    bfs(getInput(), 0)


if __name__ == '__main__':
    main()