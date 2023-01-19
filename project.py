g = {}
vertices = set()
indegree = {}
outdegree = {}
#1. Python uses dictionaries to represent graphs. The dictionary g, above, is a mapping 
# from each vertex to the list of its neighbors.
#2. The set vertices is the set of all vertices in the graph.
#3. The dictionary outdegree is a mapping from each vertex to the number of edges 
# going out of it. The dictionary indegree is a mapping from each vertex to the number of edges coming into it.

def join(l, sep):
  out = ''
  for element in l:
    out += str(element) + sep
  return out[:-len(sep)]
# The function join(l, sep) takes a list l and a separator string sep and returns 
# the concatenation of all the elements of l separated by sep. This is used to print 
# out the edges of a graph in a nice format.

def euler_path(graph, vertices):
  # sum in-degree and out-degree
  indegree = dict.fromkeys(vertices, 0)
  outdegree = dict.fromkeys(vertices, 0)
  for vertex in vertices:
    if vertex in g:
      outdegree[vertex] = len(g[vertex])
      for adj in g[vertex]:
        indegree[adj] += 1
  
#1. First, we create a dictionary with all the vertices as keys and initialize their indegree and outdegree to 0.
#2. Then we traverse all the vertices and for each vertex, we update its outdegree to 
# the length of its adjacency list.
#3. For each vertex in the adjacency list of a vertex, we increment the indegree of that vertex by 1. 

  # determine start and end point
  start = -1
  end = -1
  for vertex in vertices:
    if indegree[vertex] < outdegree[vertex]:
      start = vertex
    elif indegree[vertex] > outdegree[vertex]:
      end = vertex

  print(start, end)

  #1. We first find the start and end vertices for the Eulerian path. 
  #2. We then print them.

  # tour
  current_path, circuit, v = [start], [], start
  while len(current_path) > 0:
    if outdegree[v]:
      current_path.append(v)

      nextv = g[v].pop()
      outdegree[v] -= 1
      v = nextv
    else:
      circuit.append(v)
      v = current_path.pop()
  # print(current_path, circuit)
  circuit.reverse()
  return circuit
  #1. The algorithm starts at a node v and follows a trail of edges until it reaches the end of the trail, 
  # a node w with no outgoing edges.
  #2. The algorithm backtracks from w to the first node that has not been completely explored—call this 
  # node u. (Note that u may be equal to w.)
  #3. The algorithm then chooses a new trail from u and repeats the process until it has returned to the 
  # starting node.
  #4. The algorithm then completes the circuit by traversing the edges that it skipped over in step 2.
  #5. The algorithm outputs the circuit

with open('project_dataset1.txt', 'w') as out:
  with open('project_dataset.txt', 'r') as f:
    for line in f:
      nodes = line[:-1].split(' -> ')
      u = int(nodes[0])
      vs = [int(n) for n in nodes[1].split(',')]

      vertices.add(u)
      vertices = vertices  | set(vs)

      g[u] = vs
    
    path = euler_path(g, list(vertices))

    out.write(join(path, '->'))

    #1. We read the file project_dataset.txt line by line and extract the nodes from the line.
    #2. We add the first node to the set vertices and then we add the second node to the set vertices.
    #3. We create a dictionary g where the key is the first node and the value is the second node.
    #4. We find the path in the Eulerian graph.
    #5. Finally, we write the path in the file project_dataset1.txt.