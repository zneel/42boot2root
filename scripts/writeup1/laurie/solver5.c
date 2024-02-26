// gcc -Ofast solver5.c -o solver5 && ./solver5

#include <stdio.h>

char cmp[6] = "giants";

char get_char(char c) { return "isrveawhobpnutfg"[c & 0xf]; }

int print_all_solution(int index, char soluce[6]) {
  if (index == 6) {
    printf("%s\n", soluce);
    return 0;
  }

  char c = 32;
  c = 32;
  while (c < 127) {
    if (get_char(c) == cmp[index]) {
      if (c >= 97 && c <= 122) {
        soluce[index] = c;
        print_all_solution(index + 1, soluce);
      }
    }
    c++;
  }

  return 1;
}

int main() {
  char soluce[6] = {0};
  print_all_solution(0, soluce);
}