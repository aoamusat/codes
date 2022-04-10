#include <iostream>
#include <vector>
#include <cstdlib>
#include <algorithm>

using std::vector;

void quick_sort(vector<int> &a)
{
    sort(a.begin(), a.end());
}

int main()
{
    int n;
    std::cin >> n;
    vector<int> a(n);
    for (size_t i = 0; i < a.size(); ++i)
    {
        std::cin >> a[i];
    }
    quick_sort(a);
    for (size_t i = 0; i < a.size(); ++i)
    {
        std::cout << a[i] << ' ';
    }
}

