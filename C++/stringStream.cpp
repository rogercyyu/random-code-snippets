#include <sstream>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

vector<int> parseInts(string str) {
	stringstream ss;
    vector<int> result;

    ss << str;
    
    while(ss.good())
    {
        string substr;
        getline(ss, substr, ',');
        result.push_back(stoi(substr));
    }

    return result;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}

