package concurrent;
/*
You have a class designed to handle unique user sessions. Something is wrong with how it stores the token and tracks the count.
 */

public class UserSessionOriginal {
    private static String sessionToken;
    private int sessionCount = 0;

    public void initSession(String token) {
        sessionToken = token;
        sessionCount++;
    }

    public String getDetails() {
        return "Session: " + sessionToken + " | Total: " + sessionCount;
    }
}