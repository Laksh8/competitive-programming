// // DFS

// #include<iostream> 
// #include <list> 
// #include <limits.h> 
// using namespace std; 

// class Graph 
// { 
// 	int V; // No. of vertices 
// 	list<int> *adj; // Pointer to an array containing adjacency lists 
// 	bool isCyclicUtil(int v, bool visited[], int parent); 
// public:
// 	Graph(int V);
// 	void addEdge(int v, int w); 
// 	bool isCyclic();
// };

// Graph::Graph(int V)
// {
// 	this->V = V;
// 	adj = new list<int>[V];
// }

// void Graph::addEdge(int v, int w)
// {
// 	adj[v].push_back(w);
// 	adj[w].push_back(v);
// }

// bool Graph::isCyclicUtil(int v, bool visited[], int parent)
// {
// 	visited[v] = true;

// 	list<int>::iterator i; 
// 	for (i = adj[v].begin(); i != adj[v].end(); ++i) 
// 	{
// 		if(!visited[*i])
// 		{
// 			if(isCyclicUtil(*i, visited, v))
// 				return true;
// 		}
// 		else if(*i != parent)
// 			return true;
// 	}
// 	return false;
// }

// bool Graph::isCyclic()
// {
// 	bool *visited = new bool[V];
// 	for(int i=0; i<V; i++)
// 		visited[i] = false;

// 	for(int u=0; u<V; u++)
// 		if(!visited[u])
// 			if(isCyclicUtil(u,visited,-1))
// 				return true;

// 	return false;
// }

// int main() 
// { 
//     Graph g1(5); 
//     g1.addEdge(1, 0); 
//     g1.addEdge(0, 2); 
//     g1.addEdge(2, 1); 
//     g1.addEdge(0, 3); 
//     g1.addEdge(3, 4); 
//     g1.isCyclic()? cout << "Graph contains cycle\n": 
//                    cout << "Graph doesn't contain cycle\n"; 
  
//     Graph g2(3); 
//     g2.addEdge(0, 1); 
//     g2.addEdge(1, 2); 
//     g2.isCyclic()? cout << "Graph contains cycle\n": 
//                    cout << "Graph doesn't contain cycle\n"; 
  
//     return 0; 
// } 

// BFS
#include<bits/stdc++.h>
using namespace std;

void addEdge(vector<int>adj[], int u, int v)
{
	adj[u].push_back(v);
	adj[v].push_back(u);
}
bool isCyclicConnented(vector<int>adj[], int s, int V, vector<bool>& visited)
{
	vector<int> parent(V,-1);

	queue<int> q;

	visited[s] = true;
	q.push(s);

	while(!q.empty()){
		int u = q.front();
		q.pop();

		for(auto v : adj[u]){
			if(!visited[v]) {
				visited[v] = true;
				q.push(v);
				parent[v] = u;
			}
			else if (parent[u] != v)
				return true;
		}
	}
	return false;
}

bool isCyclicDisconnected(vector<int> adj[], int V)
{
	vector<bool> visited(V, false);

	for(int i=0; i<V; i++)
		if(!visited[i] && isCyclicConnented(adj,i,V, visited))
			return true;
		return false;
}

int main() 
{ 
    int V = 4; 
    vector<int> adj[V]; 
    addEdge(adj, 0, 1); 
    addEdge(adj, 1, 2); 
    addEdge(adj, 2, 0); 
    addEdge(adj, 2, 3); 
  
    if (isCyclicDisconnected(adj, V)) 
        cout << "Yes"; 
    else
        cout << "No"; 
  
    return 0; 
} 