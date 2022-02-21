#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#define TOTAL_DIRECTIONS 16

int main(int argc, char *argv[]) {

	if(argc != 2) {
		printf("Usage %s <degrees> \n", argv[0]);
		return 1;
	}

	// char pointer for double conversion
	char *dptr;
	double bearing = strtod(argv[1], &dptr);

	if (bearing == 0) {
        	/* If the value provided was out of range, display a warning message */
	        if (errno == ERANGE) {
			printf("The value provided was out of range\n");
			return 2;
		}
	}
	char *directions[TOTAL_DIRECTIONS] = {"N", "NNW", "NW", "WNW", "W", "WSW", "SW", "SSW",
					      "S", "SSE", "SE", "ESE", "E", "ENE", "NE", "NNE"};

	double degree = bearing / (360 / TOTAL_DIRECTIONS);
	int result = (int) degree;

	printf("%0.2f.º is %s\n", bearing, directions[result % TOTAL_DIRECTIONS]);

	return 0;
}
