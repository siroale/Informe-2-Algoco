#include <bits/stdc++.h>
#include "getCosts.hpp"
 
using namespace std;
using namespace std::chrono;

map<char, int> abecedaryValues;
vector<int> cost_insert(26);
vector<vector<int>> cost_replace(26, vector<int>(26));
vector<vector<int>> cost_transpose(26, vector<int>(26));
vector<int> cost_delete(26);


int editDistanceDP(const string &cadena1, const string &cadena2) {
    int n = cadena1.size();
    int m = cadena2.size();

    // Crear una matriz DP para almacenar los costos mínimos
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, INT_MAX));

    // Inicializar casos base: transformar cadena vacía en otra solo con inserciones o eliminaciones
    dp[0][0] = 0;
    for (int i = 1; i <= n; ++i) {
        dp[i][0] = dp[i - 1][0] + cost_del(cadena1[i - 1]);
    }
    for (int j = 1; j <= m; ++j) {
        dp[0][j] = dp[0][j - 1] + cost_ins(cadena2[j - 1]);
    }

    // Llenar la matriz DP
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            // Operación de sustitución
            dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + cost_rep(cadena1[i - 1], cadena2[j - 1]));

            // Operación de inserción
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + cost_ins(cadena2[j - 1]));

            // Operación de eliminación
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + cost_del(cadena1[i - 1]));

            // Operación de transposición (solo si hay al menos dos caracteres en ambas cadenas)
            if (i > 1 && j > 1 && cadena1[i - 1] == cadena2[j - 2] && cadena1[i - 2] == cadena2[j - 1]) {
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + cost_trans(cadena1[i - 1], cadena1[i - 2]));
            }
        }
    }

    // El resultado final estará en dp[n][m]
    return dp[n][m];
}

int main(){
    // Asignar valores a cada letra del alfabeto de la 'a' a la 'z'
    for (char ch = 'a'; ch <= 'z'; ++ch) {
        abecedaryValues[ch] = ch - 'a';
    }
    
    getTable("cost_replace.txt", cost_replace);
    getTable("cost_transpose.txt", cost_transpose);
    getArray("cost_delete.txt", cost_delete);
    getArray("cost_insert.txt", cost_insert);


    // Entrada: 2 cadenas
    string cadena1, cadena2;
    string path = "Datasets/similar_dataset.txt";
    ifstream dataset(path);
    for (int k = 0; k < 100; k++){
        dataset >> cadena1 >> cadena2;
        auto start = high_resolution_clock::now();
        int resultado = editDistanceDP(cadena1, cadena2);
        auto stop = high_resolution_clock::now();
        auto duration_us = duration_cast<microseconds>(stop - start);
        double duration_ms = duration_us.count() / 1e3;
        cout << "El costo de la distancia minima de edicion es: " << resultado << endl;
        cout << "Resultado obtenido en: " << duration_ms << " [ms]" << endl;
    }
    return 0;
}