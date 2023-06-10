/*
 * @lc app=leetcode id=169 lang=rust
 *
 * [169] Majority Element
 */

use std::collections::HashMap;

// @lc code=start
pub struct Solution;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut dict: HashMap<i32, i32> = std::collections::HashMap::new();
        let appearance = nums.len() / 2;
        print!("appearance {}", appearance);
        if nums.len() == 1 {
            return nums[0];
        }
        for num in nums {
            if dict.contains_key(&num) {
                if dict.get(&num).unwrap() + 1 > appearance as i32 {
                    print!("num {}", num);
                    return num;
                } else {
                    dict.insert(num, dict.get(&num).unwrap() + 1);
                }
            } else {
                dict.insert(num, 1);
            }
        }
        return 0;
    }
}

fn main() {
    Solution::majority_element(vec![1]);
    Solution::majority_element(vec![2, 2, 1, 1, 1, 2, 2]);
    Solution::majority_element(vec![3, 2, 3]);
}
// @lc code=end
