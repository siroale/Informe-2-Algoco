#include <bits/stdc++.h>

using namespace std;

extern map<char, int> abecedaryValues;
extern vector<int> cost_insert;
extern vector<vector<int>> cost_replace;
extern vector<vector<int>> cost_transpose;
extern vector<int> cost_delete;

void getTable(string path, vector<vector<int>> &matrix){ 
    ifstream file(path);
    for (int i = 0; i < 26; i++){
        for (int j = 0; j < 26; j++){
            file >> matrix[i][j];
        }
    }
    file.close();
}

void getArray(string path, vector<int> &array){
    ifstream file(path);
    for (int i = 0; i < 26; i++){
        file >> array[i];
    }
    file.close();
}

int cost_rep(char a, char b){
    int costo = cost_replace[abecedaryValues[a]][abecedaryValues[b]];
    return costo;
}

int cost_trans(char a, char b){
    int costo = cost_transpose[abecedaryValues[a]][abecedaryValues[b]];
    return costo;
}

int cost_ins(char a){
    int costo = cost_insert[abecedaryValues[a]];
    return costo;
}

int cost_del(char a){
    int costo = cost_delete[abecedaryValues[a]];
    return costo;
}