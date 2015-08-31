/*
https://projecteuler.net/problem=3
https://www.hackerrank.com/contests/projecteuler/challenges/euler003
*/


#include <iostream>     // std::cout
#include <algorithm>    // std::set_intersection, std::sort
#include <vector>       // std::vector
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <limits>
#include <queue>
#include <functional>
#include <iterator>
#include <numeric>


using namespace std;
typedef vector<long long int > VI;
typedef vector< vector<long long int> > VVI;
typedef unordered_map<int, long long int> HT;
typedef unsigned long long int lli;
ostream_iterator<int> out_it (cout, " ");

HT freq;
set<int> S;
unordered_set<unsigned int> P;
unordered_map<int, unordered_set<unsigned int> > cache;


lli largest_prime_factor(lli n)
{

    lli   largest_factor = 1;
    lli   p = 3;
    lli   div = n;
    int   sqrtN = sqrt(n);
    sqrtN++;

    /* remove any factors of 2 first */
    while ((div & 1) == 0)
    {
        largest_factor = 2;
        div >>= 1;
    }

    /* now look at other odd factors till sqrt(n) and remove the composites.
        if the remainder is greater than 2 then its a prime, else return the largest_factor */
    while (div != 1)
    {
        while (div % p == 0 )
        {
            largest_factor = p;
            div = div/p;
        }
        p += 2;
        if(p > sqrtN)
        {
            if(div > 2)
                return div;
            else
                return largest_factor;
        }
    }

    return largest_factor;
}

int main()
{
    int T;
    cin >> T;

    while(T--)
    {
        unsigned long long int N;
        cin >> N;
        cout << largest_prime_factor(N) << endl;

    }
    return 0;
}
