#include <stdio.h>

struct linkedList
{
    int val;
    struct linkedList* next;
};

struct linkedList* primes;

int getSmallestPrime(int n)
{
  while(n != 1)
  {    
    if(!(n%primes->val))
    {
      n = n / primes->val;
      return primes->val;
    }
    else
      primes = primes->next;

  }

  return 1;
}

int countCoprime(n)
{
  int count = n;
  int last = 0;
  int p = 2;

  if(n)
    while(n != 1)
    {
      if(n % p)
        p = getSmallestPrime(n);

      if(last != p)
      {
        count = count * (1-1.0/(double) p);
        last = p;
      }
      n = n / p;
    }

  return count;
}

//Hard coded to 90,000,000
void SOE(long int n, struct linkedList* primeList)
{
  int* numList = (int*) malloc(sizeof(int)*(n+1));
  int i;
  for(i=0;i<=n;i++)
  {
    numList[i] = i;
  }

  primeList->val = 2;
  struct linkedList* lastItem = primeList;

  int pIndex = 1;
  int mult = 3;
  for(i=3;i<=n;i+=2)
  {
    if(numList[i])
    {
      lastItem->next = (struct linkedList*) malloc(sizeof(struct linkedList));
      lastItem = lastItem->next;
      lastItem->val = numList[i];
      lastItem->next = NULL;

      mult = 3;
      for(mult=3;i*mult <= n;mult+=2)
      {
        numList[i*mult] = 0;
      }
    }
  }
}

struct linkedList* getIndex(struct linkedList* tList, int n)
{
  int i;
  struct linkedList* curNode = tList;
  for(i=0;i<n;i++)
  {
    curNode = curNode->next;
  }

  return curNode;
}



int recFunc(int n, struct linkedList* curPrimes)
{
  double ratio = 15499/94744;
  double lowRatio = 0.0;
  int lowN = 0;
  struct linkedList* curNode = curPrimes;

  int totient = countCoprime(n);
  if((double) totient / (double) n < ratio && (double) totient / (double) n > lowRatio && n != 1)
  {
    lowRatio = (double) totient / (double) n;
    lowN = n;
  }

  while(curNode->next)
  {
    int totient = countCoprime(recFunc(n * curNode->val, curNode->next));
    if((double) totient / (double) n < ratio && (double) totient / (double) n > lowRatio)
    {
      lowRatio = (double) totient / (double) n;
      lowN = n;
    }

    curNode = curNode->next;
  }

  return lowN;
}


int main()
{
  primes = (struct linkedList*) malloc(sizeof(struct linkedList));
  primes->val = 2;
  SOE(10000000, primes);

  struct linkedList* newPrimes = (struct linkedList*) malloc(sizeof(struct linkedList));
  SOE(100, newPrimes);
  printf("%i\n", countCoprime(510510));
  printf("%i\n", recFunc(1, newPrimes));
  return 0;

  long int lowIter = 1, lowRes = 0;
  long int iter = 1, res = 0;
  long int n, p, last, totient;
  double toBeat = (15499.0/94744.0);
  //iter = 2*3*5*7*11*13*17*19;
  iter = 1;
  int mult = 1;
  for( ; ;iter++)
  {
    res = 0;
    n = iter;
    last = 0;
    totient = n;
    while(n != 1)
    {
      p = getSmallestPrime(n);
      if(last != p)
      {
        totient = totient * (1-1.0/p);
        last = p;
      }
      else
        break;
      n = n / p;
    }
    res += totient;

    if(n==1 && ((double) res/(double) iter) < ((double) lowRes/(double) lowIter) || !lowRes)
    {
      lowRes = res;
      lowIter = iter;
      printf("Iteration: %lu\n", iter);
      printf("Low Ratio: %f\n", (double) lowRes/(double) lowIter);
      printf("To Beat: %f\n", toBeat);
    }

    if(((double) lowRes/(double) lowIter) < toBeat && res)
      break;
  }

  printf("%lu\n", iter);

  return 0;
}
