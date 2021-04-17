def swapFileDate():
    with open(r"C:\Users\lokesh kumar sharma\Downloads\Project-98\sample1.txt",'r')as a:
        data_a = a.read()

    with open(r"C:\Users\lokesh kumar sharma\Downloads\Project-98\sample2.txt",'r')as b:
        data_b = b.read()

    with open(r"C:\Users\lokesh kumar sharma\Downloads\Project-98\sample1.txt",'r')as a:
         a.write(data_b)

    with open(r"C:\Users\lokesh kumar sharma\Downloads\Project-98\sample2.txt",'r')as b:
         b.write(data_a)            
         