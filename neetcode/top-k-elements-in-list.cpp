#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequencies;
        for (int n : nums) {
            frequencies[n] += 1;
        }

        vector<pair<int, int>> sorted;
        for (auto f : frequencies) {
            sorted.push_back({f.second, f.first});
        }
        sort(sorted.rbegin(), sorted.rend());

        vector<int> topK;
        for (int i = 0; i < k; i++) {
            topK.push_back(sorted[i].second);
        }

        return topK;
    }
};

void printArr(vector<int> arr);

int main() {
    int k;
    vector<int> nums;
    Solution solution;

    nums = {1, 1, 1, 2, 2, 3}, k = 2;
    printArr(solution.topKFrequent(nums, k));

    nums = {1, 2, 2, 3, 3, 3}, k = 2;
    printArr(solution.topKFrequent(nums, k));

    nums = {7, 4, 4, 4}, k = 1;
    printArr(solution.topKFrequent(nums, k));

    nums = {7, 7}, k = 1;
    printArr(solution.topKFrequent(nums, k));

    return 0;
}

void printArr(vector<int> arr) {
    cout << "[ ";
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << ", ";
    }
    cout << "]" << endl;
}