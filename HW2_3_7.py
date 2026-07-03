""" The E-commerce Price Filter (firest occurance >= Target)
You're on Flipkart. You filter products: "Show me laptops priced ₹50,000 or above." Products are sorted by price. Flipkart must find the first product ≥ ₹50,000 — classic binary search variant called lower bound.
"""

prices = [32000, 38000, 42000, 50000, 50000, 55000, 62000, 70000]

target=int(input("Enter the product price : "))

low=0
high=len(prices)-1
ans=-1

#search Algo
while low <= high:
    mid=(low+high)//2
    
    if prices[mid] >= target:
        ans=mid
        high=mid-1
    else:
        low=mid+1
        
if ans != -1:
    print(f"Price is {prices[ans]} at index {ans}")
else:
    print("no laptop in that range")