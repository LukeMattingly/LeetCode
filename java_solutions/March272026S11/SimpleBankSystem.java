package March272026S11;

public class SimpleBankSystem {
    long[] balance;

    public SimpleBankSystem(long[] balance) {
        this.balance = balance;
    }
    
    public boolean transfer(int account1, int account2, long money) {
        //withdraw from 1
        //deposit to 2
        if(withdraw(account1, money)){
            if (deposit(account2, money)){
                return true;
            }else{
                deposit(account1, money); // if the withdrawl succeeded but the deposit doesn't, the money needs to go back to original account
            }
        }
        return false;
    }
    
    public boolean deposit(int account, long money) {
        //check if account exists, if so take money and add to account
        if(accountExists(account)){
            balance[account-1] += money; // since accountIds start at 1, but array is 0 indexed
            return true;
        }else{
            return false;
        }
    }
    
    public boolean withdraw(int account, long money) {
        //need to check their balance is enough. 
        if(accountExists(account)){
            long currBalance = balance[account-1];
            if(money <= currBalance){
                balance[account-1] -= money;
                return true;
            }
        }
        return false;
    }

    public boolean accountExists(int accountId){
        return (1<= accountId && accountId <= balance.length) ? true : false;
    }
}
