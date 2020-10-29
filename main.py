import networkx
import gzip
import matplotlib.pyplot as plt
import statistics
import numpy

def degAndCope():
    # Read file
    file = gzip.open('twitter_combined.txt.gz')

    Graphtype = networkx.DiGraph()
    graph = networkx.read_edgelist(file, create_using=Graphtype, nodetype=int, data=('weight', float),)


    # Degree Ratio
    degratio = []
    for item in graph.nodes():
        # Nodes with no cycles go into the if
        if graph.in_degree(item) == 0:
            degratio.append(0.0)
        else:
            degratio.append(graph.out_degree(item) / graph.in_degree(item))

    degratio.sort()
    print("Mean: ", sum(degratio)/len(degratio))
    print("Median: ", statistics.median(degratio))
    print("Standard Deviation: ", numpy.std(degratio))
    plt.title("Degree Ratio")
    plt.xlabel(" Degree Ratio Value ")
    plt.ylabel(" Num of nodes ")
    plt.hist(degratio, bins=1000)
    plt.xlim(0, 20)
    plt.show()

    # Copeland Score
    copeland = []
    for item in graph.nodes():
        copeland.append(graph.out_degree(item) - graph.in_degree(item))

    print("Mean: ", sum(copeland)/len(copeland))
    print("Median: ", statistics.median(degratio))
    print("Standard Deviation: ", numpy.std(copeland))
    plt.title("Copeland Scores")
    plt.xlabel(" Copeland Score Value ")
    plt.ylabel(" Num of nodes ")
    plt.hist(copeland, bins=400)
    plt.xlim(-200, 200)
    plt.show()

    file.close()

def cCentrality():
    # Read file
    file = gzip.open('twitter_combined.txt.gz')
    Graphtype = networkx.DiGraph()
    graph = networkx.read_edgelist(file, create_using=Graphtype, nodetype=int, data=('weight', float), )

    # Closeness Centrality
    closeness = []
    for item in graph.nodes():
        close = networkx.closeness_centrality(graph, item)
        print(close)
        closeness.append(close)
    plt.hist(closeness, bins=50)
    plt.xlim(0, 1)
    plt.title("Closeness Centrality")
    plt.xlabel(" Closeness Centrality Value ")
    plt.ylabel(" Num of nodes ")
    plt.show()

    file.close()

def bCentrality():
    # Read file
    file = gzip.open('twitter_combined.txt.gz')
    Graphtype = networkx.DiGraph()
    graph = networkx.read_edgelist(file, create_using=Graphtype, nodetype=int, data=('weight', float), )

    # Betweeness Centrality
    betweeness = networkx.betweenness_centrality(graph)
    print("Median: ", statistics.median(betweeness))
    print("Mean: ", statistics.mean(betweeness))
    print("Standard Deviation: ", numpy.std(betweeness))
    plt.hist(betweeness, bins=50)
    plt.title("Betweeness Centrality")
    plt.xlabel(" Betweeness Centrality Value ")
    plt.ylabel(" Num of nodes ")
    plt.show()

    file.close()


def triads():
    # Read file
    file = gzip.open('twitter_combined.txt.gz')
    Graphtype = networkx.DiGraph()
    graph = networkx.read_edgelist(file, create_using=Graphtype, nodetype=int, data=('weight', float), )

    # Triadic Census
    triadic = networkx.triadic_census(graph)
    print(triadic)

    file.close()

degAndCope()
cCentrality()
bCentrality()
triads()
