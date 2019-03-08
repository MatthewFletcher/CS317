def dfs(graph, start, visited=None, round=0):

    #If no nodes have been visited, create 
    # an empty set for adding. 
    if visited is None:
        print("No nodes visited. Creating empty list. ")
        visited = set()

    # Add the starting node for this recursion
    # to the visited stack
    visited.add(start)

    #Increment a round counter
    round += 1
    print("\n--->Round {}<---".format(round))

    #Print out the visited nodes.
    print("Nodes visited -->{}<--".format(visited))



    print("Visiting {}.".format(start))
    for next in graph[start] - visited:
        print("Checking node {}".format(next))

        #Recursively continue through graph
        #Code referenced from https://www.programiz.com/dsa/graph-dfs
        dfs(graph, next, visited, round)
    return visited




def getInput():

    graph = {}

    num = int(input("Enter the number of nodes in the graph >> "))

    for i in range(num):

        i = str(i)

        key = []

        line = input("Enter the nodes attached to node {}>> ".format(i))

        for number in line:
            if number.isdigit():
                key.append(number)

        graph[i] = set(key)



    #print(graph)
    # graph = {'0': set(['1', '3', '4']),
    #         '1': set(['0', '2', '4']),
    #         '2': set(['0', '1']),
    #         '3': set(['1','2', '3']),
    #         '4': set(['2', '3'])}

    # print(graph)

    return graph

def main():
    #getInput()
    dfs(getInput(), '0')
if __name__ == '__main__':
    main()