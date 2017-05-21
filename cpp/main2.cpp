#include "dim.hpp"
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <map>
#include <unordered_set>
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

    ifstream fi("enron/out.enron");
    srand ( time(NULL) ); //initialize the random seed

    string line = "";

    map<pair<int, int>, int> edgeSet;
    unordered_set<int> vertexSet;
    vector<double> probs = {0.1, 0.01, 0.001};

    int i = 100;
    while (getline(fi, line) && i--)
    {
        if (line.find("%") == string::npos)
        {
            pair<int, int> edge(0,0);
            GetPair(line, edge);

            if (edge.first == edge.second)
                continue;

            vertexSet.insert(edge.first);
            vertexSet.insert(edge.second);
            edgeSet[edge]++;
        }
    }

    fi.close();

    dim.init();
    dim.set_beta(128); // Set beta=32

    for (unordered_set<int>::iterator it = vertexSet.begin(); it != vertexSet.end(); it++)
    {
        dim.insert(*it);
    }

    for (map<pair<int, int>, int>::iterator it = edgeSet.begin(); it != edgeSet.end(); it++)
    {
        dim.insert(it->first.first, it->first.second, probs[GetRandomIndex(probs.size())]);
    }

    for (unordered_set<int>::iterator it = vertexSet.begin(); it != vertexSet.end(); it++)
        printf("Influence of %d is %1.6f\n", *it, dim.infest(*it));
    printf("Most influential vertex is %d\n", dim.infmax(1)[0]);



    return 0;
}
