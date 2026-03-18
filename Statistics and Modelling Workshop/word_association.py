# Statistics and Modelling Workshop
# Word Association Visualizer

# This demo shows how you can use NetworkX to generate Markov model chain representation of text.

import networkx as nx
import matplotlib.pyplot as plt

# Basic Markov Chain 

sentence = '''the man and the woman sat at a bench and talked for a very long time the conversation was deep and rich'''

sentence_components = sentence.split(" ")

words = {}

for x in range(len(sentence_components)): 
    if sentence_components[x] not in words:
        words[sentence_components[x]] = []
    if (x < len(sentence_components) - 1):
        words[sentence_components[x]].append(sentence_components[x + 1])
    else:
        words[sentence_components[x]].append('.')

# Make Graph
G = nx.DiGraph() 
G.add_nodes_from(sentence_components)

for word in words:
    for next_word in words[word]:
        G.add_edge(word, next_word)

def main() -> None:
    pos = nx.shell_layout(G)
    nx.draw(
        G, pos, 
        with_labels=True, 
        node_color="lightblue",
        node_size=200,
        font_weight="regular",
        arrowstyle='-|>',
        arrowsize=20
    )
    plt.show()

if __name__ == "__main__":
    main()
