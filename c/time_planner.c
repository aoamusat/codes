#include <stdio.h>
#include <stdlib.h>

void meetingPlanner(int slotsA[][2], size_t slotsALength, int slotsB[][2], size_t slotsBLength, int dur, int *out) 
{
  // your code goes here
  int nA = slotsALength, nB = slotsBLength;
  int i=0, j=0;
  while(1) {
    if(i < nA && j < nB) {
     if((slotsA[i][0] > slotsB[j][0] && slotsB[j][1] < slotsA[i][0]+dur) || (slotsB[j][0]+dur > slotsB[j][1])) {
        ++j;
      }else if((slotsA[i][0] < slotsB[j][0] && slotsA[i][1] < slotsB[j][0]+dur) || (slotsA[i][0]+dur > slotsA[i][1])) {
        ++i;
      }else if(slotsA[i][0] > slotsB[j][0]){
        out[0] = slotsA[i][0];
        out[1] = slotsA[i][0]+dur;
        break;
      }else {
        out[0] = slotsB[j][0];
        out[1] = slotsB[j][0]+dur;
        break;	
      }
    }else {
      break;
    }
  }
}

int main() {
	/*
[[10,50],[60,120],[140,210]], [[0,15],[60,72]], 12*/
	int slotsA[3][2] = {{10, 50}, {60, 120}, {140, 210}};
	int slotsB[2][2] = {{0, 15}, {60, 72}};
	int dur = 12;
	int *out = malloc(sizeof(int) * 2);;
	int a = 3, b = 2;
	meetingPlanner(slotsA, a, slotsB, b, dur, out);
	printf("[%d, %d]\n", out[0], out[1]);
	return 0;
}
