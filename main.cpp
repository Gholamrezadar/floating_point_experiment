#include <climits>
#include <iostream>

int main() {
  std::cout << "int,float\n";
  int delta = 1000;
  for (int i = 0; i < INT_MAX - delta; i += delta) {
    std::cout << i << "," << *((float *)&i) << "\n";
  }
  return 0;
}
