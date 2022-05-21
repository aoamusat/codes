#include <iostream>
#include <string>
#include <math.h>
using namespace std;

int fromHex(char c) {
	if(c == 'A') return 10;
	if(c == 'B') return 11;
	if(c == 'C') return 12;
	if(c == 'D') return 13;
	if(c == 'E') return 14;
	if(c == 'F') return 15;
	return -1;
}

int convert(string hex){
	int power = 0;
	int ans = 0, aux;
	for(int i=hex.size()-1; i >= 0; --i) {
		aux = hex[i] - '0';
		if(aux > 9)
			aux = fromHex(hex[i]);
		ans += (int)(aux * pow(16, power));
		power++;
	}
	return ans;
}

int main() {
	int T;
	cin >> T;
	string s;
	for(int i=0; i<T; ++i) {
		cin >> s;
		cout << convert(s) << endl;
	}
	// your code goes here
	return 0;
}

