"""
    The interval schedulling problem
    A computation problem that requires optimality and completeness
    
    Approach: A Greedy Algorithm

    Problem statement:
        There is only one Resouerce available of usage by number of request
        Each request utilizes the for a given period of time (r.start and r.end)
        When a request accuqiures the resours of a time t, there shouldnt be any other request that has it

        We are looking to get a solution that selects from a set R of request a subset A 
        such that #requests in A is as close as posible to #requests in original R
        considering R contains requests that dont overlap with in each other
        
    Formalizing the  problem:
        condsire R -> Set implemented as a  HasMap for each entry having a request in the form
        {int Request_id: Request(int start, int end)} 
        Search from R to produce A such that nR ~= nA fulfilling the invariant
        Invariant of the problem : r in A | r(i).end <= r(i+1).start
    
    Solution:
        function Schedule(Request R) returns (Request A):
            L <- sort(r.valuesOfEnd)
            A <- null
            loop:
                for i in L
                    for j=i+1 in L
                    if j.valueOfStart >= i.valueOfEnd then append i in A, i++
                    else 
                        i+j                        
"""

class Request:
    def __init__(self, request_id, start, end):
        self.request_id = request_id
        self.start = start
        self.end = end

def Schedule(R):
    # Sort requests by their end times
    L = sorted(R.values(), key=lambda r: r.end)
    A = []  # List to hold selected requests
    last_end_time = 0  # Track the end time of the last added request

    for request in L:
        if request.start >= last_end_time:  # If the request does not overlap
            A.append(request)  # Add to the selected requests
            last_end_time = request.end  # Update the end time

    return A  # Return the list of selected requests



