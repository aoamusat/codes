#include <bits/stdc++.h>
using namespace std;

int binarySearch(vector<int> v, int key) {
    int lo = 0;
    int hi = v.size()-1;
    int mid;
    while (lo <= hi) {
        mid = (lo + hi) / 2;
        if (v[mid] == key)
            return mid;
        if(v[mid] < key)
            lo = mid + 1;
        else
            hi = mid - 1;
    }
    return -1;
}

int main() {
    int n;
    cin >> n;
    vector<int> v;
    for (int i = 0, num; i < n; ++i) {
        cin >> num;
        v.push_back(num);
    }
    cin >> n;
    for (int i = 0, key; i < n; ++i) {
        cin >> key;
        cout << binarySearch(v, key) << ' ';
    }
    cout << endl;
}
