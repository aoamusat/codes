#include <stdio.h>
#define MAX 100000
#define MOD 1000000007

long long F[MAX] = {0};

int main(){
	int i, num, T;
	F[0] = F[1] = 1;
	for(i=2; i < 100000; ++i)
		F[i] = i*F[i-1] % MOD;
	scanf("%d", &T);
	for(i=0; i<T; ++i) {
		scanf("%d", &num);
		printf("%lli\n", F[num]);
	}
}

