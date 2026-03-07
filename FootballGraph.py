import networkx as nx
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------------------------------
def main():

    G = nx.DiGraph()

    # Read triples
    with open("Football.txt") as f:
        for line in f:
            if line.strip() == "":
                continue

            s, r, o = line.split()

            if r in ["subclass", "instance"]:
                G.add_edge(o, s, label=r)
            else:
                G.add_edge(s, o, label=r)

    # Set graph spacing
    G.graph["graph"] = {
        "ranksep": "2",   # Vertical spacing
        "nodesep": "1.5"  # Horizontal spacing
    }

    # Hierarchical layout
    pos = nx.nx_pydot.graphviz_layout(G, prog="dot")

    edge_labels = nx.get_edge_attributes(G, "label")

    plt.figure(figsize=(18,14))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightgrey",
        node_size=3000,
        font_size=8,
        arrows=True
    )

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

    plt.savefig("Football.png")
    plt.show()

# --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------------------------