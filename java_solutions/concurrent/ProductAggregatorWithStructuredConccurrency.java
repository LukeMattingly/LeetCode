package concurrent;

import java.util.concurrent.StructuredTaskScope;

public class ProductAggregatorWithStructuredConccurrency {
    private final PriceService priceService = new PriceService();
    private final InventoryService inventoryService = new InventoryService();
    private final ReviewService reviewService = new ReviewService();

    public ProductView getProductView(String productId) throws InterruptedException{
        try(var scope = new StructuredTaskScope.ShutdownOnFailure()){

            StructuredTaskScope.Subtask<Double> priceTask = scope.fork(()-> priceService.getPrice(productId));

            StructuredTaskScope.Subtask<Boolean> inventoryTask = scope.fork(()-> inventoryService.inStock(productId));

            StructuredTaskScope.Subtask<Double> reviewTask = scope.fork(()-> reviewService.getAverageRating(productId));

            scope.join();

            double price = getOrDefault(priceTask, -1.0);
            boolean inventory = getOrDefault(inventoryTask, false);
            double rating = getOrDefault(reviewTask, 0.0);

            return new ProductView(productId, rating, price, inventory);
        }
    }

    private <T> T getOrDefault(StructuredTaskScope.Subtask<T> task, T defaultValue) {
        return switch (task.state()) {
            case SUCCESS -> task.get();
            case FAILED, UNAVAILABLE -> defaultValue;
        };
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
