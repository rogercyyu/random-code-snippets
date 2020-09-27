#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n = 0;

    cin >> n;
    vector<int> arr(n);

    for(int i=0; i<n; i++)
    {
        cin >> arr[i];
    }

    int remove;

    cin >> remove;

    arr.erase(arr.begin()+remove-1);

    int min = 0;
    int max = 0;

    cin >> min >> max;


    arr.erase(arr.begin() + min - 1, arr.begin() + max - 1);

    cout << arr.size() << endl;


    for (auto x: arr)
    {
        cout << x << " ";
    }

    return 0;
}
