#include <bits/stdc++.h>
#include "getCosts.hpp"
 
using namespace std;
using namespace std::chrono;

map<char, int> abecedaryValues;
vector<int> cost_insert(26);
vector<vector<int>> cost_replace(26, vector<int>(26));
vector<vector<int>> cost_transpose(26, vector<int>(26));
vector<int> cost_delete(26);


int editDistanceBruteForce(const string &cadena1, const string &cadena2, int i, int j) {
    // Caso base: si llegamos al final de una de las cadenas
    if (i == cadena1.size()) {
        int cost = 0;
        for (int k = j; k < cadena2.size(); ++k) {
            cost += cost_ins(cadena2[k]);
        }
        return cost;
    }
    if (j == cadena2.size()) {
        int cost = 0;
        for (int k = i; k < cadena1.size(); ++k) {
            cost += cost_del(cadena1[k]);
        }
        return cost;
    }

    // Probar todas las operaciones posibles y tomar el mínimo
    // Sustitución
    int replaceCost = editDistanceBruteForce(cadena1, cadena2, i + 1, j + 1) 
                    + cost_rep(cadena1[i], cadena2[j]);
    // Inserción
    int insertCost = editDistanceBruteForce(cadena1, cadena2, i, j + 1) 
                   + cost_ins(cadena2[j]);
    // Eliminación
    int deleteCost = editDistanceBruteForce(cadena1, cadena2, i + 1, j) 
                   + cost_del(cadena1[i]);
    // Transposición
    int transposeCost = INT_MAX;
    if (i + 1 < cadena1.size() && j + 1 < cadena2.size() &&
        cadena1[i] == cadena2[j + 1] && cadena1[i + 1] == cadena2[j]) {
        transposeCost = editDistanceBruteForce(cadena1, cadena2, i + 2, j + 2) 
                      + cost_trans(cadena1[i], cadena1[i + 1]);
    }

    return min({replaceCost, insertCost, deleteCost, transposeCost});
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


    // Entrada:
double promedio = 0.0;
    double megaPromedio = 0.0;
    string cadena1, cadena2;
    string path = "Datasets/small_empty_dataset.txt";

    // Archivo de entrada
    ifstream dataset(path);
    if (!dataset) {
        cerr << "Error al abrir el dataset: " << path << endl;
        return 1;
    }

    // Archivo de salida
    ofstream outputFile("promedios_tabla.txt");
    if (!outputFile) {
        cerr << "Error al abrir el archivo para guardar los promedios" << endl;
        return 1;
    }

    for (int m = 0; m < 5; m++) {
        promedio = 0.0;
        cout << "Iteración " << m + 1 << ":" << endl;

        for (int k = 0; k < 10; k++) {
            dataset >> cadena1 >> cadena2; // Leer par de cadenas

            // Medir tiempo de ejecución
            auto start = high_resolution_clock::now();
            int resultado = editDistanceBruteForce(cadena1, cadena2,0 ,0);
            auto stop = high_resolution_clock::now();
            auto duration_us = duration_cast<microseconds>(stop - start);
            double duration_ms = duration_us.count() / 1e3;

            promedio += duration_ms;

            // Mostrar resultados en consola
            cout << k + 1 << ". El costo de la distancia mínima de edición es: " << resultado << endl;
            cout << "Resultado obtenido en: " << fixed << setprecision(3) << duration_ms << " ms" << endl;
        }

        promedio /= 10.0; // Promedio de la iteración
        megaPromedio += promedio;

        // Guardar promedio en archivo con formato de tabla
        outputFile << (m + 1) << "\t" 
                   << fixed << setprecision(4) << promedio << "\t" 
                   << cadena1.length() << endl;

        cout << "Promedio de tiempo de ejecución (Iteración " << m + 1 << "): "
             << promedio << " ms" << endl;
    }

    megaPromedio /= 5.0; // Mega promedio general
    cout << "Promedio de tiempo de ejecución total: " << megaPromedio << " ms" << endl;

    // Cerrar archivos
    dataset.close();
    outputFile.close();
    return 0;
}