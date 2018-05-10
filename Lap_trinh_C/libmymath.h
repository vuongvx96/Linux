#include <stdio.h>

/* Ham tinh giai thua cho mot so nguyen */
unsigned long long int giaithua(int n){
  unsigned long long int gt = 1;
  for (int i = 2; i <= n; i++)
     gt *= i;
  return gt;
}

/* Ham tinh tong chan tu 1 den N */
int tongchan(int N){
  int tong = 0;
  for (int i = 1; i <= N; i++)
     if (i % 2 == 0)
       tong += i;
  return tong;
}

/* Ham tinh tong le tu 1 den N */
int tongle(int N){
  int tong = 0;
  for (int i = 1; i <= N; i++)
     if (i % 2 != 0)
       tong += i;
  return tong;
}

/* Ham tinh luy thua cua x mu n*/
long long luythua(int x, int n){
  long long ketqua = x;
  for (int i = 2; i <= n; i++)
     ketqua *= x;
  return ketqua;
}

