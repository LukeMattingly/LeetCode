package March272026S11;

public class BackOffRetry {

    private final double backoffMultiplier;
    private final long maxDelayMs;
    public BackOffRetry( double backoffMultiplier, long maxDelayMs){
        this.backoffMultiplier = backoffMultiplier;
        this.maxDelayMs = maxDelayMs;
    }
    
    public <T> T execute(RetryableTask<T> task, int maxAttempts, long intialDelayMs) throws Exception{
        long delay = intialDelayMs;
        Exception lastException = null;
        for(int attempt =1; attempt<= maxAttempts; attempt++){
            try{
                return task.run();
            }catch(TransientException e){
                lastException = e;
                if(!isRetryable(e) || attempt == maxAttempts){
                    throw e;
                }

                System.out.print("Attempt "+ attempt + " delay "+ delay);

                Thread.sleep(delay);
                delay = nextDelay(delay);
            }
        }
        throw lastException;
    }

    @FunctionalInterface
    interface RetryableTask<t>{
        t run() throws Exception;
    }

    class TransientException extends Exception{
        public TransientException(String message){
            super(message);
        }
    }

    private boolean isRetryable(Exception e){
        return (e instanceof TransientException) ? true : false;
    }

    private long nextDelay(long currentDelay){
        long next = (long)(currentDelay * backoffMultiplier);
        return Math.min(next, maxDelayMs);
    }
}
