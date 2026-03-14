public class BackoffRetryWithJitter<T> {
    public static <T> T execute(RetryableTask<T> task, int maxAttempts, long intialDelayMs)throws Exception{

        long delay = intialDelayMs;

        for(int attempt =0; attempt< maxAttempts; attempt++){ // loop through attempts until max attempt
            try{
                return task.run();
            }catch (Exception  e){ //transient error
                if(attempt == maxAttempts){
                    throw e;
                }

                //int jitter = Math.random()
                //Thread.sleep(delay + jitter); //sleep the delay
                delay *=2; // exponential backoff current delay * = delay, updated. 
            }
        }
        throw new IllegalStateException("Unreachable");

    }

    @FunctionalInterface
    interface RetryableTask<T> {
        T run() throws Exception;
    }

}
