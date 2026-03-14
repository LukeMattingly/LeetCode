package concurrent;
/*
You are fetching two pieces of data from different services. 
Currently, fetchOrder waits for fetchUser to finish. R
efactor this to run in parallel using a FixedThreadPool of 2 threads and combine the results once both are done.
*/

public class OrderServiceOriginal {
    public String getFullOrderDetails() {
        // These are slow, blocking network calls
        String user = fetchUser(); 
        String order = fetchOrder();
        
        return user + " details for " + order;
    }

    private String fetchUser() { return "User_123"; }
    private String fetchOrder() { return "Order_999"; }
}