import java.util.concurrent.atomic.AtomicInteger;

/*
In the original code, sessionToken was static. This means every single UserSession object shared the exact same token.
 If User A logged in, and then User B logged in, User A’s token would be overwritten by User B’s. 
Conversely, sessionCount was an instance variable, meaning it only tracked the count for that specific object
 (likely staying at 1) rather than the total sessions across the application. 
 */

public class UserSessionFixed {
    // Instance variable: Each session object gets its own unique token
    private final String sessionToken; 

    // Static variable: Shared across all instances to track the global count
    // AtomicInteger ensures thread-safe increments
    private static final AtomicInteger sessionCount = new AtomicInteger(0);
    

    public UserSessionFixed(String token) {
        this.sessionToken = token;
        sessionCount.incrementAndGet(); //each new session created it increments it
    }

    public String getDetails() {
        return "Session: " + this.sessionToken + " | Global Total: " + sessionCount.get();
    }

}