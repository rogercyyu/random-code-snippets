#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n = 0;
    int a;
    cin >> n;
    vector<int> arr;
    for (int i=0; i<n; i++)
    {
        cin >> a;
        arr.push_back(a);
    }

    sort(arr.begin(), arr.end());

    for (auto x : arr)
    {
        cout << x << " ";
    }

    return 0;
}
