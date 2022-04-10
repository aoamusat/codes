#include <bits/stdc++.h>
using namespace std;

int majorityElement(vector<int> v)
{
    sort(v.begin(), v.end());
    int n = v.size(),count = 1, max_ele = -1, temp = v[0], elem;
    for (int i = 1; i < n; i++)
    {
        if (temp == v[i])
        {
            count++;
        }
        else
        {
            count = 1;
            temp = v[i];
        }
        if (max_ele < count)
        {
            max_ele = count;
            elem = v[i];

            if (max_ele > (n / 2))
            {
                return 1;
            }
        }
    }
    return 0;
}

int main()
{
    int n;
    cin >> n;
    vector<int> v;
    for (int i = 0, num; i < n; ++i) {
        cin >> num;
        v.push_back(num);
    }
    
    cout << majorityElement(v) << endl;
}
