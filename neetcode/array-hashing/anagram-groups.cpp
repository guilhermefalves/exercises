#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        string str, sorted_str;
        unordered_map<string, vector<string>> anagrams_map;

        for (int i = 0; i < strs.size(); i++) {
            str = sorted_str = strs[i];
            sort(sorted_str.begin(), sorted_str.end());

            anagrams_map[sorted_str].push_back(str);
        }

        vector<vector<string>> anagrams;
        for (auto& anagram : anagrams_map) {
            anagrams.push_back(anagram.second);
        }

        return anagrams;
    }
};

void printArr(vector<string> arr);
void printArr(vector<vector<string>> arr);

int main() {
    Solution solution;
    vector<string> strs;

    strs={"act", "pots", "tops", "cat", "stop", "hat"};
    printArr(solution.groupAnagrams(strs));

    strs = {"x"};
    printArr(solution.groupAnagrams(strs));

    strs = {""};
    printArr(solution.groupAnagrams(strs));

    return 0;
}

void printArr(vector<string> arr) {
    cout << "[ ";
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << ", ";
    }
    cout << "]";
}

void printArr(vector<vector<string>> arr) {
    cout << "[ ";
    for (int i = 0; i < arr.size(); i++) {
        printArr(arr[i]);
    }
    cout << " ]" << endl;
}
