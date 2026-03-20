package March192026S3;


public class ValidPalindrome {
    //we need to do some regex to string replace all non alpha numeric characetrs
    //to lower everything
    // 1. reverse it and compare
    // 2. two pointers one starting at end and other at beginning
    public boolean isPalindrome(String s) {
        
        String replaced = s.replaceAll("[^A-Za-z0-9]", "");
        replaced = replaced.toLowerCase();
        System.out.print(replaced);
        String reverse = new StringBuilder(new String(replaced)).reverse().toString();

        if(replaced.equals(reverse)) return true;
        else return false;
    }
}
