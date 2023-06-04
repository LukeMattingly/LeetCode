/*
 * @lc app=leetcode id=26 lang=rust
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
use std::collections::HashSet;

pub struct Solution;

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut uniques: HashSet<i32> = HashSet::new();
        let mut k = 0; //index of the last unique element
        for i in 0..nums.len() {
            if !uniques.contains(&nums[i]) {
                uniques.insert(nums[i]);
                nums[k] = nums[i];
                k += 1;
                print!("nums {:?}", nums);
                println!("uniques {:?}", uniques);
                print!("k {:?}", k);
            }
        }
        let result: i32 = k as i32;

        print!("final nums {:?}", nums);
        print!("final result {:?}", result);
        return result;
    }
}
// @lc code=end
fn main() {
    //Solution::remove_duplicates(&mut vec![1, 1, 2]);
    Solution::remove_duplicates(&mut vec![0, 0, 1, 1, 1, 2, 2, 3, 3, 4]);
}
