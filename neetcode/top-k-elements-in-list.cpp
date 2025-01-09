#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <utility>

using namespace std;

void printArr(vector<int> arr);

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequency;
        for (int i = 0; i < nums.size(); i++) {
            frequency[nums[i]] += 1;
        }

        vector<pair<int, int>> sorted_frequency = sortFrequency(frequency);

        vector<int> top_k;
        for (auto f : sorted_frequency) {
            if (top_k.size() == k) {
                break;
            }

            top_k.push_back(f.second);
        }

        return top_k;
    }

    vector<pair<int, int>> sortFrequency(unordered_map<int, int> frequency) {
        vector<pair<int, int>> frequency_arr;
        for (auto f : frequency) {
            frequency_arr.push_back({f.second, f.first});
        }
        sort(frequency_arr.rbegin(), frequency_arr.rend());
        return frequency_arr;
    }
};



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

    // nums = {7, 7}, k = 1;
    // printArr(solution.topKFrequent(nums, k));

    return 0;
}

void printArr(vector<int> arr) {
    cout << "[ ";
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << ", ";
    }
    cout << "]" << endl;
}