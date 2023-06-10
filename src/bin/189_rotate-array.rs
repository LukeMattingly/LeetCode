/*
 * @lc app=leetcode id=189 lang=rust
 *
 * [189] Rotate Array
 */

// @lc code=start
struct Solution;

impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        for _i in 0..k as usize {
            nums.insert(0, nums.last().unwrap().clone());
            nums.pop();
        }
    }
}

fn main() {
    Solution::rotate(&mut vec![1, 2, 3, 4, 5, 6, 7], 3);
    Solution::rotate(&mut vec![-1, -100, 3, 99], 2);
    //Solution::rotate(&mut vec![1, 2, 3, 4, 5, 6, 7], 9);
}
// @lc code=end
