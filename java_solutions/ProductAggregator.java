import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ProductAggregator {
    ExecutorService executor = Executors.newFixedThreadPool(10); 

    public ProductView getProductView(String productId){
        final PriceService priceService = new PriceService();
        final InventoryService inventoryService = new InventoryService();
        final ReviewService reviewService = new ReviewService();

        CompletableFuture<Double> priceFuture = CompletableFuture.supplyAsync(()-> priceService.getPrice(productId), executor)
            .exceptionally( e -> 
                {System.out.print("Price Service failed"); 
                return -1.0;
            });

        CompletableFuture<Boolean> inventoryFuture = CompletableFuture.supplyAsync(()-> inventoryService.inStock(productId), executor)
            .exceptionally(e -> {
                System.out.println("Inventory Service failed");
                    return false;
                
            });

        CompletableFuture<Double> reviewFuture = CompletableFuture.supplyAsync(()-> reviewService.getAverageRating(productId), executor)
            .exceptionally(e-> {
                System.out.println("Review Service Failed");
                return -1.0;
            });

        CompletableFuture<Void> allDone = CompletableFuture.allOf(priceFuture, inventoryFuture, reviewFuture);

        // wait for all and combine
        allDone.join();

        return new ProductView(
            productId,
            priceFuture.join(),
            reviewFuture.join(),
            inventoryFuture.join()
        );
            
    }

    public static void main(String[] args) {
        ProductAggregator aggregator =
                new ProductAggregator();

        ProductView view = aggregator.getProductView("123334");

        System.out.println(view);

        aggregator.shutdown();
    }

    public void shutdown() {
        executor.shutdown();
    }

    class ProductView{
        private final String productId;
        private final Boolean inStock;
        private final Double reviewRating;
        private final Double price;

        public ProductView(String productId, Double reviewRating, Double price,  Boolean inStock){
            this.productId = productId;
            this.inStock = inStock;
            this.reviewRating = reviewRating;
            this.price = price;
        }

        @Override
        public String toString() {
            return "ProductView{" +
                    "productId='" + productId + '\'' +
                    ", price=" + price +
                    ", inStock=" + inStock +
                    ", reviewRating=" + reviewRating +
                    '}';
        }
    }

    class PriceService {
        public double getPrice(String productId) {
            sleep(300);
            return 19.99;
        }

        private void sleep(long ms) {
            try {
                Thread.sleep(ms);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                throw new RuntimeException(e);
            }
        }
    }

    class InventoryService{
        public boolean inStock(String productId){
            sleep(400);
            return true;
        }
        private void sleep(long ms){
            try{
                Thread.sleep(ms);
            }catch(InterruptedException e){
                Thread.currentThread().interrupt();
                throw new RuntimeException(e);
            }
        }
    }

    class ReviewService{
        public double getAverageRating(String productId){
            sleep(400);
            throw new RuntimeException("Reviews unavailable");
        }
        private void sleep(long ms){
            try{
                Thread.sleep(ms);
            }catch(InterruptedException e){
                Thread.currentThread().interrupt();
                throw new RuntimeException(e);
            }
        }
    }
}
