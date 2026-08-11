#used to create an fibonacci series which is used to multiply by the transaction 
def weighted_transaction_stream(transactions):
    a, b = 1, 1

    for amount in transactions:
        yield amount * a

        # Calculate the next Fibonacci number lazily
        a, b = b, a + b
        
def weighted_values(trans,thresh):
    weighted=weighted_transaction_stream(trans)
    
    fil= (value for value in weighted if value > thresh)
    
    result=[]
    
    for i in range(3):
        result.append(next(fil))
        
    return result



transactions = [100, 200, 150, 50, 400, 90, 60]
threshold = 500

result = weighted_values(transactions, threshold)

print("First 3 exceeding 500:", result)