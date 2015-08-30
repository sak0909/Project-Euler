/*
https://projecteuler.net/problem=1
https://www.hackerrank.com/contests/projecteuler/challenges/euler001
 
Find all the multiples of 5 and 3 below N.
Can be reframed as a seriers.
Ex. 3+6+9.... -> 3(1+2+3...) -> 3*N*(N-1)/2
Since 15 is a multiple of both 5 and 3 we can minus its multiples.
*/
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <ctype.h>
#include <sstream>
#include <string>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <limits>
#include <cstdlib>
#include <numeric>
#include <functional>
#include <unordered_map>

using namespace std;

typedef unsigned long long int  lli;

lli sumDivisibleBy(lli N, int d)
{
    return d*(((N/d)*((N/d)+1))/2);
}

int main()
{
    int t;
    cin >> t;
    
    while(t--)
    {
        int N;
        cin >> N;
        cout << (sumDivisibleBy(N-1, 3) + sumDivisibleBy(N-1, 5) - sumDivisibleBy(N-1, 15)) << endl;
        
    }
    
    
    return 0;
}





