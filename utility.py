'''
# Utility Class: Network Graph Generator

This utility class provides a function to create various types of network graphs using the NetworkX library.

Author: [Your Name]
University of Catanzaro

Function:
  create_graph(model, parameters)

Description:
  Creates a network graph based on the specified model and parameters.

Arguments:
  model (str): The type of network model to create. Supported models:
    - 'erdos-reny': Erdős-Rényi random graph
    - 'GNP': G(n,p) random graph, the same as Erdős-Rényi random graph.
    - 'barabasi-albert': Barabási-Albert preferential attachment model
    - 'sbm': Stochastic Block Model
  parameters (dict): A dictionary containing the parameters for the chosen model. 
    - For 'erdos-reny' and 'GNP':
      - 'n': Number of nodes (int)
      - 'p': Probability of edge creation (float)
    - For 'barabasi-albert':
      - 'n': Number of nodes (int)
      - 'm': Number of edges to attach from a new node to existing nodes (int)
    - For 'sbm':
      - 'n': Number of nodes (int)
      - 'sizes': Block sizes (list of ints)
      - 'probs': Probability matrix (numpy array)

Returns:
  networkx.Graph: The created network graph object.

Example Usage:
  # Create an Erdős-Rényi graph with 10 nodes and edge probability 0.5
  graph = create_graph('erdos-reny', {'n': 10, 'p': 0.5})

  # Create a Barabási-Albert graph with 100 nodes and 2 edges per new node
  graph = create_graph('barabasi-albert', {'n': 100, 'm': 2})

  # Create a Stochastic Block Model
  graph = create_graph('sbm', {'n': 100, 'sizes': [50, 50], 'probs': [[0.8, 0.2], [0.2, 0.8]]})

'''

import networkx as nx

def create_graph(model, parameters):
  if model=='erdos-reny':
      n = parameters['n']  # Number of nodes
      p = parameters['p']  # Probability of edge creation
      G = networkx.erdos_renyi_graph(n, p)
  elif model == 'GNP':  # Added GNP model
      n = parameters['n']  # Number of nodes
      p = parameters['p']  # Probability of edge creation
      G = networkx.gnp_random_graph(n, p)  # Use gnp_random_graph
  elif model == 'GNP':  # Added GNP model
      n = parameters['n']  # Number of nodes
      p = parameters['p']  # Probability of edge creation
      G = networkx.gnp_random_graph(n, p)  # Use gnp_random_graph
  elif model == 'barabasi-albert':
      n = parameters['n']
      m = parameters['m']  # Number of edges to attach from a new node to existing nodes
      G = networkx.barabasi_albert_graph(n, m)  # Use barabasi_albert_graph
  elif model == 'sbm':  # Added SBM model
        n = parameters['n']  # Number of nodes
        sizes = parameters['sizes']  # Block sizes (list)
        probs = parameters['probs']  # Probability matrix (numpy array)
        G = networkx.stochastic_block_model(sizes, probs, seed=0)  # Use stochastic_block_model
  return G


if __name__ == "__main__":
    # Test cases for different network models
    
    # Erdős-Rényi random graph
    er_graph = create_graph('erdos-reny', {'n': 10, 'p': 0.5})
    print("Erdős-Rényi Graph:")
    print(f"Number of nodes: {nx.number_of_nodes(er_graph)}")
    print(f"Number of edges: {nx.number_of_edges(er_graph)}")

    # G(n,p) random graph
    gnp_graph = create_graph('GNP', {'n': 10, 'p': 0.5})
    print("\nG(n,p) Graph:")
    print(f"Number of nodes: {nx.number_of_nodes(gnp_graph)}")
    print(f"Number of edges: {nx.number_of_edges(gnp_graph)}")
    
    # Barabási-Albert preferential attachment model
    ba_graph = create_graph('barabasi-albert', {'n': 100, 'm': 2})
    print("\nBarabási-Albert Graph:")
    print(f"Number of nodes: {nx.number_of_nodes(ba_graph)}")
    print(f"Number of edges: {nx.number_of_edges(ba_graph)}")

    # Stochastic Block Model
    sbm_graph = create_graph('sbm', {'n': 100, 'sizes': [50, 50], 'probs': [[0.8, 0.2], [0.2, 0.8]]})
    print("\nStochastic Block Model Graph:")
    print(f"Number of nodes: {nx.number_of_nodes(sbm_graph)}")
    print(f"Number of edges: {nx.number_of_edges(sbm_graph)}")
