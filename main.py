import networkx
import gzip
import matplotlib.pyplot as plt

def main():
    # Read file
    file = gzip.open('twitter_combined.txt.gz')
    Graphtype = networkx.DiGraph()
    graph = networkx.read_edgelist(file, create_using=Graphtype, nodetype=int, data=('weight', float), )

    # Degree Ratio
    print("Degree Ratios")
    for item in graph.nodes():
        # Nodes with no cycles go into the if
        if graph.in_degree(item) == 0:
            degratio = 0.0
        else:
            degratio = graph.out_degree(item) / graph.in_degree(item)

    # CopelandScore
    print("Copeland Scores")
    for item in graph.nodes():
        print("Node ", item, ": ", (graph.out_degree(item) - graph.in_degree(item)))

    # Closeness Centrality
    closeness = sorted(networkx.closeness_centrality(graph).values(), reverse=True)
    #for item in graph.nodes():
    #    networkx.closeness_centrality(graph, item)
    plt.loglog(closeness)
    plt.title("Closeness Centrality")
    plt.xlabel(" ")
    plt.ylabel(" ")


    # Betweeness Centrality
    networkx.betweenness_centrality(graph)

    # Triadic Census
    print(networkx.triadic_census(graph))

    file.close()

main()
