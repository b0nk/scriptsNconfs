#include <stdio.h>
#include <stdlib.h>

int fsize(FILE *fp) {
    int prev = ftell(fp);
    fseek(fp, 0L, SEEK_END);
    int sz = ftell(fp);
    fseek(fp,prev,SEEK_SET);
    return sz;
}

int main(int argc, char const *argv[]) {
    if (argc != 4) {
        printf("Usage:\n%s infile modifier outfile\nmodifier = decimal notation of 8 bits to xor with (0-255)\n", argv[0]);
        return 0;
    }
    char infile[260];
    char outfile[260];
    int mod;
    sprintf(infile, "%s", argv[1]);
    sscanf(argv[2], "%d", &mod);
    sprintf(outfile, "%s", argv[3]);
    printf("Opening %s\n", infile);
    FILE *file = fopen(infile, "rb");
    int size = fsize(file);
    char *filebuffer = (char *)malloc(size);
    fread(filebuffer, fsize(file), 1, file);
    fclose(file);
    printf("XOR'ing file...\n");
    for (int i = 0; i < size; ++i)
    {
        filebuffer[i] ^= mod;
    }
    printf("Saving %s\n", outfile);
    FILE *fileout = fopen(outfile, "wb");
    fwrite(filebuffer, fsize(file), 1, fileout);
    fclose(fileout);
    free(filebuffer);
    printf("Done ;)\n");
    return 0;
}
