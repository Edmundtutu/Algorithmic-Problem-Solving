import java.util.*;

public class SchedulingProblem {
    // Request class to hold start and end times
    static class Request {
        int id;
        int start;
        int end;

        Request(int id, int start, int end) {
            this.id = id;
            this.start = start;
            this.end = end;
        }
    }

    // Method to schedule requests
    public static List<Request> schedule(List<Request> requests) {
        // Sort requests by their end times
        requests.sort(Comparator.comparingInt(r -> r.end));
        
        List<Request> selectedRequests = new ArrayList<>();
        Request lastSelected = null;

        for (Request request : requests) {
            // If this request starts after or when the last selected request ends
            if (lastSelected == null || request.start >= lastSelected.end) {
                selectedRequests.add(request);
                lastSelected = request; // Update the last selected request
            }
        }
        
        return selectedRequests;
    }

    // Main method for testing
    public static void main(String[] args) {
        List<Request> requests = Arrays.asList(
            new Request(1, 0, 3),
            new Request(2, 1, 4),
            new Request(3, 3, 5),
            new Request(4, 5, 6),
            new Request(5, 2, 7),
            new Request(6, 6, 8),
            new Request(7, 7, 9),
            new Request(8, 8, 10),
            new Request(9, 9, 11),
            new Request(10, 10, 12)
        );

        List<Request> scheduledRequests = schedule(requests);
        for (Request req : scheduledRequests) {
            System.out.println("Request ID: " + req.id + " Start: " + req.start + " End: " + req.end);
        }
    }
}
