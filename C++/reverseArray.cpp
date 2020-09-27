#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int amount;
    
    cin >> amount; // bad practice...

    int arr[amount]; 

    for (int i = 0; i < amount; i++)
    {
        cin >> arr[i];
    }

    for (int i = amount - 1; i >= 0; i--)
    {
        cout << arr[i] << " ";
    }

    return 0;
}
