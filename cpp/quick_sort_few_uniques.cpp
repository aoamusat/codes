#include <iostream>
#include <vector>
#include <cstdlib>

using std::vector;
using std::swap;
using std::pair;

int partition2(vector<int> &a, int l, int r) {
  int x = a[l];
  int j = l;
  for (int i = l + 1; i <= r; i++) {
    if (a[i] <= x) {
      j++;
      swap(a[i], a[j]);
    }
  }
  swap(a[l], a[j]);
  return j;
}

pair<int, int> partition3(vector<int> &a, int l, int r)
{
    int pivot = a[l];
    int j = l, k = l;
    for (int i = l + 1; i <= r; ++i)
    {
        if (a[i] < pivot) {
            j++;
            swap(a[j], a[i]);
        }
        else if (a[i] == pivot) {
            k++;
            swap(a[k], a[i]);
        }
    }
    swap(a[l], a[j]);
    pair<int, int> p;
    p.first = j;
    p.second = k + 1;
    return p;
}

void randomized_quick_sort(vector<int> &a, int l, int r) {
  if (l >= r) {
    return;
  }

  int k = l + rand() % (r - l + 1);
  swap(a[l], a[k]);
  pair<int, int> m = partition3(a, l, r);

  randomized_quick_sort(a, l, m.first);
  randomized_quick_sort(a, m.second, r);
}

int main() {
    int n;
    std::cin >> n;
    vector<int> a(n);
    for (size_t i = 0; i < a.size(); ++i) {
        std::cin >> a[i];
    }
    randomized_quick_sort(a, 0, a.size() - 1);
    for (size_t i = 0; i < a.size(); ++i) {
        std::cout << a[i] << ' ';
    }
}

