/*
 * @lc app=leetcode id=27 lang=rust
 *
 * [27] Remove Element
 */
pub struct Solution;

// @lc code=start
impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        nums.retain(|&num| num != val);
        print!("{:?}", nums);
        return nums.len() as i32;
    }
}

fn main() {
    Solution::remove_element(&mut vec![3, 2, 2, 3], 3);
}
// @lc code=end
