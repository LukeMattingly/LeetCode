package March272026S11;

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import March272026S11.ProductAggregator.InventoryService;
import March272026S11.ProductAggregator.PriceService;
import March272026S11.ProductAggregator.ReviewService;

public class ProductAggregator {
    

    private final PriceService priceService = new PriceService();
    private final InventoryService inventoryService = new InventoryService();
    private final ReviewService reviewService = new ReviewService();

    private final ExecutorService executor = Executors.newFixedThreadPool(10);

    

    public ProductView getProductView(String productId){
        CompletableFuture<Double> priceFuture = CompletableFuture.supplyAsync(()-> priceService.getPrice(productId))
            .exceptionally(ex -> {return -1.0;});

        CompletableFuture<Boolean> inventoryFuture = CompletableFuture.supplyAsync(()-> inventoryService.isInStock(productId))
            .exceptionally(ex-> {return false;});

        CompletableFuture<Double> reviewFuture = CompletableFuture.supplyAsync(()-> reviewService.getAverageRating(productId))
            .exceptionally(ex-> {return 0.0;});

        CompletableFuture<Void> allDone = CompletableFuture.allOf(priceFuture, inventoryFuture, reviewFuture);

        allDone.join();

        return new ProductView(productId, priceFuture.join(), inventoryFuture.join(), reviewFuture.join());
    }

    class ProductView {
        private final String productId;
        private final double price;
        private final boolean inStock;
        private final double averageRating;

        public ProductView(String productId, double price, boolean inStock, double averageRating) {
            this.productId = productId;
            this.price = price;
            this.inStock = inStock;
            this.averageRating = averageRating;
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

        
    class InventoryService {
        public boolean isInStock(String productId) {
            sleep(200);
            return true;
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

    class ReviewService {
        public double getAverageRating(String productId) {
            sleep(400);
            throw new RuntimeException("Reviews unavailable");
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
    }

