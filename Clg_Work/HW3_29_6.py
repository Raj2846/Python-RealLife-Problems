"""GPS Navigation """

forward=[]
backward=[]

def visit(place):
    backward.append(place)
    print(backward)
    
def go_back():
    forward.append(backward.pop())
    
    print(backward)
    print(forward)
    
def go_front():
    backward.append(forward.pop(-1))
    
    print("forward one")
    print(backward)
    print(forward)

visit("hindi")
visit("marathi")
visit("telegu")
visit("tamil")
visit("rajasthani")
visit("up")

go_back()    
go_back()    
go_back()    


go_front()


