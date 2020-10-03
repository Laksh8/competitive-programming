#include<iostream>
#include<list>
#define NIL -1
using namespace std;

class Graph
{
	int V;
	list<int> *adj;
	void bridgeUtil(int v, bool visited[], int disc[], int low[], int parent[]);

public:
	Graph(int V);
	void addEdge(int v,int w);
	void bridge();
};

Graph::Graph(int V)
{
	this->V = V;
	adj = new list<int>[V];
}

void Graph::addEdge(int v, int w)
{
	adj[v].push_back(w);
	adj[w].push_back(v);
}

void Graph::bridgeUtil(int u, bool visited[], int disc[], int low[], int parent[])
{
	static int time = 0;

	visited[u] = true;
	disc[u] = low[u] = ++time;

	list<int>::iterator i;
	for(i = adj[u].begin(); i!=adj[u].end(); i++)
	{
		int v = *i;

		if(!visited[v])
		{
			parent[v] = u;
			bridgeUtil(v,visited,disc, low,parent);

			low[u] = min(low[u], low[v]);
			if(low[v]>low[u])
				cout<<u<<" "<<v<<endl;
		}
		else if(v != parent[u])
			low[u] = min(low[u], disc[v]);
	}
}

void Graph::bridge() 
{ 
    // Mark all the vertices as not visited 
    bool *visited = new bool[V]; 
    int *disc = new int[V]; 
    int *low = new int[V]; 
    int *parent = new int[V]; 
  
    // Initialize parent and visited arrays 
    for (int i = 0; i < V; i++) 
    { 
        parent[i] = NIL; 
        visited[i] = false; 
    } 
  
    // Call the recursive helper function to find Bridges 
    // in DFS tree rooted with vertex 'i' 
    for (int i = 0; i < V; i++) 
        if (visited[i] == false) 
            bridgeUtil(i, visited, disc, low, parent); 
} 

int main() 
{ 
    // Create graphs given in above diagrams 
    cout << "\nBridges in first graph \n"; 
    Graph g1(5); 
    g1.addEdge(1, 0); 
    g1.addEdge(0, 2); 
    g1.addEdge(2, 1); 
    g1.addEdge(0, 3); 
    g1.addEdge(3, 4); 
    g1.bridge(); 

    return 0;
}