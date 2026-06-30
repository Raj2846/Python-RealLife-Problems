SIZE=5

queue=['_']*SIZE
front=-1
rear=-1

def enqueue(value):
    global front,rear
    
    if (rear+1)%SIZE == front:
        print("Queue is full\n")
        return
    
    if front==-1:
        front=0
    rear=(rear+1)%SIZE
    queue[rear]=value
    print(f"{value} inserted into queue\n")
    
def dequeue():
    global front,rear
    
    if front==-1:
        print("Queue is empty\n")
        return
    
    print("Deleted Element \n",queue[front])
    
    if front==rear:
        front=rear=-1
    else:
        front=(front+1)%SIZE
    
def display():
    if front == -1:
        print("Queue is Empty\n")
        return

    i = front
    print("Queue:", end=" ")

    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % SIZE
        
enqueue("1st vehical")
enqueue("2ns vehical")
enqueue("3rd vehical")
enqueue("4th vehical")
enqueue("5th vehical")
enqueue("6th vehical")

display()

dequeue()
dequeue()
dequeue()

display()