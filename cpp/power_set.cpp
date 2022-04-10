#include <bits/stdc++.h>
using namespace std;

void powerset(string str, vector<string> &res,  string curr="", int index=-1) {
	int n = str.length();

	if(index == n)
		return;
	res.push_back(curr);

	for(int i = index+1; i < n; ++i) {
		curr += str[i];
		powerset(str, res, curr, i);
		curr.erase(curr.size()-1);
	}
	return;
}

int main()
{
	string str = "abc";
	vector<string> res;
	powerset(str, res);
	res.erase(res.begin());
	for(int i=0; i < res.size(); ++i)
		cout << res[i] << endl;

	return 0;
}

