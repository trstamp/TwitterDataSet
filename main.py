import networkx
import gzip
import matplotlib.pyplot as plt

def degAndCope():
    # Read file
    file = gzip.open('twitter_combined.txt.gz')

    Graphtype = networkx.DiGraph()
    graph = networkx.read_edgelist(file, create_using=Graphtype, nodetype=int, data=('weight', float),)

    
    # Degree Ratio
    degratio = []
    print("Degree Ratios")
    for item in graph.nodes():
        # Nodes with no cycles go into the if
        if graph.in_degree(item) == 0:
            degratio.append(0.0)
        else:
            degratio.append(graph.out_degree(item) / graph.in_degree(item))

    plt.title("Degree Ratio")
    plt.hist(degratio, bins=6)
    plt.xlim(0, 60)
    plt.show()

    # CopelandScore
    copeland = []
    print("Copeland Scores")
    for item in graph.nodes():
        copeland.append(graph.out_degree(item) - graph.in_degree(item))

    plt.title("Copeland Scores")
    plt.hist(copeland, bins=15)
    plt.xlim(-200, 200)
    plt.show()

    file.close()

def centralities():
    # Read file
    file = gzip.open('twitter_combined.txt.gz')
    Graphtype = networkx.DiGraph()
    graph = networkx.read_edgelist(file, create_using=Graphtype, nodetype=int, data=('weight', float), )

    # Closeness Centrality
    closeness = sorted(networkx.closeness_centrality(graph).values(), reverse=True)
    # for item in graph.nodes():
    #    networkx.closeness_centrality(graph, item)
    plt.hist(x=closeness)
    plt.title("Closeness Centrality")
    plt.xlabel(" ")
    plt.ylabel(" ")

    # Betweeness Centrality
    networkx.betweenness_centrality(graph)

    # Triadic Census
    print(networkx.triadic_census(graph))

degAndCope()
