#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    string num[10] = {"odd","one","two","three","four","five","six","seven","eight","nine"};

    int first;
    int last;

    cin >> first;
    cin >> last;

    for (int i = 0; i + first <= last; i++)
    {
        if (first + i > 9 && (first + i) % 2 == 0 )
        {
            cout << "even" << endl;
        } 
        else if (first + i > 9 && (first + i) % 2 != 0)
        {
            cout << "odd" << endl;
        }
        else
        {
            cout << num[first + i] << endl;
        }
    }


    return 0;
}

