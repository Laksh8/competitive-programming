#include<iostream>
#include<list>
#include<queue>
using namespace std;

class Graph{
	int V;

	// Array of linked lists of size V, V linkedlist are there
	list<int> *adjList;
public:

	Graph(int v){
		V = v;
		adjList = new list<int>[V];
	}
	void addEdge(int u, int v, bool bidir=true)
	{
		adjList[u].push_back(v);
		if(bidir){
			adjList[v].push_back(u);
		}
	}
	// void printAdjList(){
	// 	for(int i=0; i<V; i++){
	// 		cout<<i<<"->";
	// 		for(int node:adjList[i]){
	// 			cout<<node<<",";
	// 		}
	// 		cout<<endl;
	// 	}
		
	// }
	void bfs(int src, int dest){
		//traverse all the nodes of the graph
		queue<int>q;
		bool *visited = new bool[V]{0};
		int *dist = new int[V+1]{0};
		int *parent = new int[V+1];

		for(int i=0; i<V; i++){
			parent[i] = -1;
		}

		q.push(src);
		visited[src] = true;

		while(!q.empty()){
			int node = q.front();
			cout<<node<<" ";
			q.pop();

			for(int neighbour:adjList[node]){
				if(!visited[neighbour]){
					q.push(neighbour);
					visited[neighbour] = true;
					dist[neighbour] = dist[node] + 1;
					parent[neighbour] = node;
				}
			}
		}
		cout<<endl;
		//print the distance of every node from source
		for(int i=0;i<V;i++){
			//cout<<i<<"node having dist "<<dist[i]<<endl;
		}
		cout<<"shortest dist is "<<dist[dest]<<endl;
		cout<<"shortest path is";

		int temp = dest;
		while(temp!=-1){
			cout<<temp<<"<--";
			temp = parent[temp];
		}
	}
};

int main(){
	Graph g(6);
	g.addEdge(0,1);
	g.addEdge(1,2);
	g.addEdge(0,4);
	g.addEdge(2,4);
	g.addEdge(3,2);
	g.addEdge(2,3);
	g.addEdge(3,5);
	g.addEdge(3,4);

	//g.printAdjList();
	g.bfs(0,5);

	return 0;
}