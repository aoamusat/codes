#include <iostream>
#include <string>
using namespace std;

bool isVogal(char c) {
	if(c == 97 || c == 101 || c == 105 || c == 111 || c == 117)
		return true;
	return false;
}

int main() {
	// your code goes here
	string s, res;
	cin >> s;
	for(int i=0; i < s.size(); ++i) {
		if(isVogal(s[i]))
			res.push_back(toupper(s[i]));
		else
			res.push_back(s[i]);
	}
	cout << res << endl;
	return 0;
}

