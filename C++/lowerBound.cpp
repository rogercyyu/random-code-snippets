#include <bits/stdc++.h>
using namespace std;


int main() {
    int n, i, q;
    cin >> n;
    int arr[n];
    
    for(i = 0; i < n; i++)
        cin >> arr[i];

    sort(arr, arr + n);
    cin >> q;

    while(q--)
    {
        cin >> i;
        
        int pos = lower_bound(arr, arr + n, i) - arr;
        if (arr[pos] == i)
            cout << "Yes ";
        else
            cout << "No ";

        cout << pos +1 << endl;
    }
    return 0;
}