#include <iostream>
#include <iterator>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  string from, to;
  cin >> from >> to;

  ifstream is {from};
  istream_iterator<string> ii {is};
  istream_iterator<string> eos {};

  ofstream os{to};
  ostream_iterator<string> oo {os, "\n"};

  vector<string> b { ii, eos };
  sort( b.begin(), b.end() );

  unique_copy( b.begin(), b.end(), oo );

  return !is.eof() || !os;
}
