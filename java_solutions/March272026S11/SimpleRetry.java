package March272026S11;

import javax.xml.crypto.dsig.TransformException;

import March272026S11.BackOffRetry.RetryableTask;
import March272026S11.BackOffRetry.TransientException;

public class SimpleRetry {
    public static<T> T execute(RetryableTask<T> task, int maxAttempts, long intialDelayMs) throws Exception{
        long delay = intialDelayMs;

        for(int attempt= 1; attempt<= maxAttempts; attempt++){
            try{
                return task.run();
            }catch(TransientException e){
                if(attempt ==maxAttempts){
                    throw e;
                }
                Thread.sleep(delay);
                delay *=2; //exponential backoff
            }
        }
        throw new IllegalStateException("unreachable");
    }
}
