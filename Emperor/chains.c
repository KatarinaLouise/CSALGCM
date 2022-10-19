#include <stdio.h>

#define NUM_CARDS 10

int ans, cur_val, cards[NUM_CARDS];

int solve(int cards[]) {
    int solved = 0;
    int i = 1;
    int count = 0;
    
    while (!solved){
        if (cards[i] > 0){
            cards[i] -= 1;
            count++;
        }
        i++;
        if (i > 9){
            i = 0;
            if(cards[i] == 0){
                solved = 1;
            }
        }
    }
  	return count;
}

int main() {
	for(int i = 0; i < NUM_CARDS; i++) {
		scanf("%d",&cards[i]);
	}
	printf("%d\n",solve(cards));
}