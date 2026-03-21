package March202026S6;

public class SimpleBankSystem {
    private long[] balance;

    public SimpleBankSystem(long[] balance) {
        this.balance = balance;
    }
    
    public boolean transfer(int account1, int account2, long money) {
        if(isValidAccount(account1) && isValidAccount(account2)){
            if(withdraw(account1, money)){
                deposit(account2, money);
                return true;
                }
            }
        return false; 

    }
    
    public boolean deposit(int account, long money) {
         if(isValidAccount(account)){
            balance[account-1] +=money;
            return true;
         }
         return false;
    }
    
    public boolean withdraw(int account, long money) {
        if(isValidAccount(account) && money <=balance[account-1]){
            balance[account-1] -= money;
            return true;
        }
        return false;
    }

    public boolean isValidAccount(int accountId){
         return accountId >=1 && accountId <= balance.length;
    }
     
}
