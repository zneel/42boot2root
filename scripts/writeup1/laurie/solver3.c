// gcc -Ofast solver3.c -o solver3 && ./solver3

#include <stdio.h>
int solver3(int i, char c, int d) {
  char cVar2;

  switch (i) {
  case 0:
    cVar2 = 'q';
    if (d != 0x309) {
      return 1;
    }
    break;
  case 1:
    cVar2 = 'b';
    if (d != 0xd6) {
      return 1;
    }
    break;
  case 2:
    cVar2 = 'b';
    if (d != 0x2f3) {
      return 1;
    }
    break;
  case 3:
    cVar2 = 'k';
    if (d != 0xfb) {
      return 1;
    }
    break;
  case 4:
    cVar2 = 'o';
    if (d != 0xa0) {
      return 1;
    }
    break;
  case 5:
    cVar2 = 't';
    if (d != 0x1ca) {
      return 1;
    }
    break;
  case 6:
    cVar2 = 'v';
    if (d != 0x30c) {
      return 1;
    }
    break;
  case 7:
    cVar2 = 'b';
    if (d != 0x20c) {
      return 1;
    }
    break;
  default:
    cVar2 = 'x';
    return 1;
  }
  if (cVar2 != c) {
    return 1;
  }
  return 0;
}

int main() {
  char c = 'b';
  int i = 2;
  int d = -2147483647 - 1;

  while (d < 2147483647) {
    if (!solver3(i, c, d)) {
      printf("%d %c %d\n", i, c, d);
    }
    d++;
  }
}