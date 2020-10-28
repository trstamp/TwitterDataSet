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
    for item in graph.nodes():
        # Nodes with no cycles go into the if
        if graph.in_degree(item) == 0:
            degratio.append(0.0)
        else:
            degratio.append(graph.out_degree(item) / graph.in_degree(item))

    plt.title("Degree Ratio")
    plt.xlabel(" Degree Ratio Value ")
    plt.ylabel(" Num of nodes ")
    plt.hist(degratio, bins=120)
    plt.xlim(0, 60)
    plt.show()

    # CopelandScore
    copeland = []
    for item in graph.nodes():
        copeland.append(graph.out_degree(item) - graph.in_degree(item))

    plt.title("Copeland Scores")
    plt.xlabel(" Copeland Score Value ")
    plt.ylabel(" Num of nodes ")
    plt.hist(copeland, bins=400)
    plt.xlim(-200, 200)
    plt.show()

    file.close()

def centralities():
    # Read file
    file = gzip.open('twitter_combined.txt.gz')
    Graphtype = networkx.DiGraph()
    graph = networkx.read_edgelist(file, create_using=Graphtype, nodetype=int, data=('weight', float), )

    # Closeness Centrality
    #closeness = sorted(networkx.closeness_centrality(graph).values(), reverse=True)
    closeness = []
    for item in graph.nodes():
        close = networkx.closeness_centrality(graph, item)
        closeness.append(close)
    plt.hist(closeness, bins=50)
    plt.title("Closeness Centrality")
    plt.xlabel(" Closeness Centrality Value ")
    plt.ylabel(" Num of nodes ")
    plt.show()

    # Betweeness Centrality
    betweeness = []
    for item in graph.nodes():
        between = networkx.betweenness_centrality(graph, item)
        betweeness.append(between)
    plt.hist(betweeness, bins=50)
    plt.title("Betweeness Centrality")
    plt.xlabel(" Betweeness Centrality Value ")
    plt.ylabel(" Num of nodes ")
    plt.show()

    # Triadic Census
    triadic = networkx.triadic_census(graph)
    print(triadic)
    
    file.close()

degAndCope()
centralities()
