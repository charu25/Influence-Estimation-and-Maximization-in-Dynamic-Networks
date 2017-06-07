#include "dim.hpp"
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <map>
#include <vector>
#include <cstdlib>
#include <locale>
#include <ctime>

using namespace std;

int GetRandomIndex(int n)
{
    return int(rand() % n);
}

void GetPair (const string& line, pair<int, int>& edge)
{
    int i = 0;

    string source = "", dest = "";
    for (; i < line.length() && isdigit(line[i]); i++)
    {
        source += line[i];
    }
    edge.first = stoi(source);
    for (; i < line.length() && !isdigit(line[i]); i++);
    for (; i < line.length() && isdigit(line[i]); i++)
    {
        dest += line[i];
    }
    edge.second = stoi(dest);
}

int main(int argc, char *argv[]) {
    DIM dim;

    //ifstream fi("enron/out.enron");
#if ENRON
    ifstream fi("enron/enron_data_weight.tsv");
#elif DIGG
    ifstream fi("digg/out.munmun_digg_reply_unique");
#endif
    srand ( time(NULL) ); //initialize the random seed

    string line = "";

    map<pair<int, int>, int> edgeMap;
    unordered_map<int, int> vertexDegMap;

#if TR
    cout << "TR" << endl;
    vector<double> probs = {0.1, 0.01, 0.001};

#elif WC
    cout << "WC" << endl;

#endif

    long long numVertices = 1000;

    /*
    cout << "Argc = " << argc << endl;
    for (int i = 0; i < argc; i++)
    {
        cout << argv[i] << endl;
    }
    */
    if (argc > 1)
    {
        if (stoi(argv[1]) == -1)
        {
            numVertices = LLONG_MAX;
        }
        else
        {
            numVertices = stoi(argv[1]);
        }
    }
    cout << ((numVertices == LLONG_MAX)? -1: numVertices) << endl;

    while (getline(fi, line) && numVertices > vertexDegMap.size())
    {
        if (line.find("%") == string::npos)
        {
            pair<int, int> edge(0,0);
            GetPair(line, edge);

            if (edge.first == edge.second)
                continue;

            vertexDegMap[edge.first]++;
            vertexDegMap[edge.second]++;
            edgeMap[edge]++;
        }
    }

	bool foundEdge = false, foundVertex = false;

	pair<int, int> nextEdge(0,0);
	int nextVertex = -1;
	while (getline(fi, line) && (foundVertex == false || foundEdge == false))
    {
        if (line.find("%") == string::npos)
        {
            pair<int, int> edge(0,0);
            GetPair(line, edge);

            if (edge.first == edge.second)
                continue;

			if (foundEdge == false && edgeMap.find(edge) == edgeMap.end())
			{
				foundEdge = true;
				nextEdge.first = edge.first;
				nextEdge.second = edge.second;
				vertexDegMap[edge.first]++;
				vertexDegMap[edge.second]++;
			}

			if (foundVertex == false && vertexDegMap.find(edge.first) == vertexDegMap.end())
			{
				foundVertex = true;
				nextVertex = edge.first;
			}
			else if (foundVertex == false && vertexDegMap.find(edge.second) == vertexDegMap.end())
			{
				foundVertex = true;
				nextVertex = edge.second;
			}
        }
    }

    fi.close();

    dim.init();
    dim.naive_operation = false;
    dim.set_beta(32); // Set beta=32

    for (unordered_map<int, int>::iterator it = vertexDegMap.begin(); it != vertexDegMap.end(); it++)
    {
        dim.insert(it->first);
    }

    for (map<pair<int, int>, int>::iterator it = edgeMap.begin(); it != edgeMap.end(); it++)
    {
#if TR
        dim.insert(it->first.first, it->first.second, probs[GetRandomIndex(probs.size())]);
#elif WC
        dim.insert(it->first.first, it->first.second, (1.0/vertexDegMap[it->second]));
#endif
    }
	/*
    cout << "Number of subgraphs generated: " << dim.hs.size() << endl;

    cout << "[";
    for (unordered_map<int, int>::iterator it = vertexDegMap.begin(); it != vertexDegMap.end(); it++)
        cout << dim.infest(it->first) << ", ";
    cout << "\b\b]" << endl;
    //printf("Most influential vertex is %d\n", dim.infmax(1)[0]);
	*/

    dim.naive_operation = false;
    int start_s=clock();

	//edge deletion
	//dim.erase(edgeMap.begin()->first.first, edgeMap.begin()->first.second);

	/*
	//edge addition
#if TR
	dim.insert(nextEdge.first, nextEdge.second, probs[GetRandomIndex(probs.size())]);
#elif WC
	dim.insert(nextEdge.first, nextEdge.second, (1.0/vertexDegMap[nextEdge.second]));
#endif
	*/
	//vertex addition
	//dim.insert(nextVertex);

	//vertex deletion
	//dim.erase(edgeMap.begin()->first.first);

    //change edge pririority
	dim.change(edgeMap.begin()->first.first, edgeMap.begin()->first.second, 0.3);

    int stop_s=clock();
    cout << (stop_s - start_s)/double(CLOCKS_PER_SEC) << endl;

    return 0;
}
