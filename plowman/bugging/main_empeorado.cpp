#include <iostream>
#include <iterator>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    string from, to;
    cin >> from >> to;

    ifstream is(from);
    if (!is.is_open()) {
        cerr << "Error: No se puede abrir el archivo de entrada " << from << endl;
        return 1;
    }

    istream_iterator<string> ii(is);
    istream_iterator<string> eos;

    ofstream os(to);
    if (!os.is_open()) {
        cerr << "Error: No se puede abrir el archivo de salida " << to << endl;
        return 1;
    }

    ostream_iterator<string> oo(os, "\n");

    vector<string> b(ii, eos);
    sort(b.begin(), b.end());

    unique_copy(b.begin(), b.end(), oo);

    return 0;
}
