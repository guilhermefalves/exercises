#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int curr, diff;
        unordered_map<int, int> nums_map;

        for (int i = 0; i < nums.size(); i++) {
            curr = nums[i];
            diff = target - curr;

            if (nums_map[diff] > 0) {
                return {nums_map[diff] - 1, i};
            }

            nums_map[curr] = i + 1;
        }

        return {};
    }
};

void printArr(vector<int> arr);

int main() {
    int target;
    vector<int> nums;
    Solution solution;

    nums = {3, 4, 5, 6}, target = 7;
    printArr(solution.twoSum(nums, target));

    nums = {4, 5, 6}, target = 10;
    printArr(solution.twoSum(nums, target));

    nums = {5, 5}, target = 10;
    printArr(solution.twoSum(nums, target));

    nums = {3,2,3}, target = 6;
    printArr(solution.twoSum(nums, target));

    return 0;
}

void printArr(vector<int> arr) {
    cout << "[ ";
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << ", ";
    }
    cout << "]" << endl;
}