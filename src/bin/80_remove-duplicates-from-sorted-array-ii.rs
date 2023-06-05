/*
 * @lc app=leetcode id=80 lang=rust
 *
 * [80] Remove Duplicates from Sorted Array II
 */

// @lc code=start

pub struct Solution;

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut current_count = 1;
        let mut current_pointer = 0;
        for i in 0..nums.len() {
            if i == 0 || nums[i] != nums[i - 1] {
                nums[current_pointer] = nums[i];
                current_pointer += 1;
                current_count = 1;
                print!("top nums {:?}", nums);
                print!("top currentPointer {:?}", current_pointer);
                println!("top currentCount {:?}", current_count);
            } else {
                if current_count < 2 {
                    nums[current_pointer] = nums[i];
                    current_pointer += 1;
                    current_count += 1;
                } else {
                    current_count += 1;
                }
                print!("nums {:?}", nums);
                print!("currentPointer {:?}", current_pointer);
                println!("currentCount {:?}", current_count);
            }
        }
        print!("final pointer {:?}", current_pointer);
        return current_pointer as i32;
    }
}
// @lc code=end
fn main() {
    //Solution::remove_duplicates(&mut vec![1, 1, 2]);
    //Solution::remove_duplicates(&mut vec![1, 1, 1, 2, 2, 3]);
    Solution::remove_duplicates(&mut vec![0, 0, 1, 1, 1, 1, 2, 3, 3]);
}
