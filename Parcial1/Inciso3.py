from stack import Stack

def respuesta3():
    n = 11050000
    n2 = 11050000 * 2
    n3 = 11050000 * 3
    n4 = 11050000 * 4
    n5 = 11050000 * 5
    
    s1 = Stack(n)
    for i in range(n):
        s1.push('f')

    s2 = Stack(n2)
    for i in range(n2):
        s2.push('f')

    s3 = Stack(n3)
    for i in range(n3):
        s3.push('f')
    
    s4 = Stack(n4)
    for i in range(n4):
        s4.push('f')
    
    s5 = Stack(n5)
    for i in range(n5):
        s5.push('f')
    
    s1.search('g')
    s2.search('g')
    s3.search('g')
    s4.search('g')
    s5.search('g')


