public class SimpleRetry<T> {
    public static <T> T execute(RetryableTask<T> task, int maxAttempts, long intialDelayMs)throws Exception{

        long delay = intialDelayMs;

        for(int attempt =0; attempt< maxAttempts; attempt++){
            try{
                return task.run();
            }catch (Exception  e){ //transient error
                if(attempt == maxAttempts){
                    throw e;
                }

                Thread.sleep(delay);
                delay *=2; // exponential backoff
            }
        }
        throw new IllegalStateException("Unreachable");

    }

    @FunctionalInterface
    interface RetryableTask<T> {
        T run() throws Exception;
    }

}
