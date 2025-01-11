#include <vector>
#include <algorithm>  // For lower_bound

using namespace std;

class Solution {
public:
    bool primeSubOperation(vector<int>& nums) {
        static vector<bool> valid(1001, true);
        static vector<int> primes;
        
        // Precompute prime numbers using the Sieve of Eratosthenes
        if (primes.empty()) { // Run the sieve only once
            valid[0] = valid[1] = false;
            for (int i = 2; i < valid.size(); ++i) {
                if (valid[i]) {
                    for (int j = i * i; j < valid.size(); j += i) {
                        valid[j] = false;
                    }
                }
            }
            for (int i = 0; i < valid.size(); ++i) {
                if (valid[i]) primes.push_back(i);
            }
        }
        
        int prev = 0;
        for (int num : nums) {
            if (num <= prev) return false;
            // Find the largest prime less than num - prev using binary search
            auto it = lower_bound(primes.begin(), primes.end(), num - prev);
            if (it != primes.begin()) {
                --it;  // Move to the previous prime
                num -= *it; // Subtract the prime number
            }
            prev = num;
        }
        return true;
    }
};
