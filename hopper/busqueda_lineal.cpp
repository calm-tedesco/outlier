#include <algorithm>
#include <cstdlib> // Para generación de números pseudoaleatorios
#include <ctime>   // Recursos para medir tiempos
#include <iostream>

using namespace std;

int buscar(const int *v, int n, int x) {
  int i = 0;
  while (i < n && v[i] != x)
    i = i + 1;
  if (i < n)
    return i;
  else
    return -1;
}

void sintaxis() {
  cerr << "Sintaxis:" << endl;
  cerr << "  TAM: Tamaño del vector (>0)" << endl;
  cerr << "  VMAX: Valor máximo (>0)" << endl;
  cerr << "Se genera un vector de tamaño TAM con elementos aleatorios en "
          "[0,VMAX["
       << endl;
  exit(EXIT_FAILURE);
}

int main(int argc, char *argv[]) {

  if (argc != 3)
    sintaxis();
  int tam = atoi(argv[1]);
  int vmax = atoi(argv[2]);
  if (tam <= 0 || vmax <= 0)
    sintaxis();

  int *v = new int[tam];
  srand(time(0));
  for (int i = 0; i < tam; i++)
    v[i] = rand() % vmax;

  clock_t tini;
  tini = clock();

  int x = vmax + 1;
  int indice = buscar(v, tam, x);

  clock_t tfin;
  tfin = clock();

  cout << indice << "\t" << (tfin - tini) / (double)CLOCKS_PER_SEC << endl;

  tini = clock();

  x = 34;
  v[76] = 34;
  indice = buscar(v, tam, x);

  tfin = clock();

  cout << indice << "\t" << (tfin - tini) / (double)CLOCKS_PER_SEC << endl;

  delete[] v; // Liberamos memoria dinámica
}
