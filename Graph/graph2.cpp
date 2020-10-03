#include<iostream>
#include<map>
#include<cstring>
#include<list>
using namespace std;

// Template for a Generic Graph - any kind of data like int, strings, bool etc
template<typename T>
class Graph{
	map<T,list<T> >adjList;

public:
	Graph(){

	}
	void addEdge(T u, T v, bool bidir=true){
		adjList[u].push_back(v);
		if(bidir){
			adjList[v].push_back(u);
		}
	}
	void printAdjlist(){
		// iterate over maps by use of for eac loop
		for(auto row: adjList){
			T key = row.first;
			cout<<key<<"->";

			for(T element:row.second){
				cout<<element<<",";
			}
			cout<<endl;
		}
	}
};

int main(){
        Graph<string> g ;
        g.addEdge("Amritsar","Delhi");
        g.addEdge("Amritsar","Jaipur");
        g.addEdge("Delhi","Siachin");
        g.addEdge("Delhi","Banglore");
        g.addEdge("Delhi", "Agra");
        g.addEdge("Amritsar","Siachin");

        g.printAdjlist();

        return 0;
}