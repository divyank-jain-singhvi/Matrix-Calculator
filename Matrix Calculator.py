from tkinter import *             # programmed by Divyank Jain Singhvi
def run():                        #matrix multiplication
    a11= sa11.get()               #getting input values  
    a12= sa12.get()
    a13= sa13.get()
    a21= sa21.get()
    a22= sa22.get()
    a23= sa23.get()
    a31= sa31.get()
    a32= sa32.get()
    a33= sa33.get()
    A11= sA11.get()
    A12= sA12.get()
    A13= sA13.get()
    A21= sA21.get()
    A22= sA22.get()
    A23= sA23.get()
    A31= sA31.get()
    A32= sA32.get()
    A33= sA33.get()

    a11=float(a11)                #converting into points
    a12=float(a12)
    a13=float(a13)
    a21=float(a21)
    a22=float(a22)
    a23=float(a23)
    a31=float(a31)
    a32=float(a32)
    a33=float(a33)
    A11=float(A11)
    A12=float(A12)
    A13=float(A13)
    A21=float(A21)
    A22=float(A22)
    A23=float(A23)
    A31=float(A31)
    A32=float(A32)
    A33=float(A33)

    
    list1 = [a11,a12,a13]
    list2 = [a21,a22,a23]
    list3 = [a31,a32,a33]

    
    list4 = [A11,A12,A13]
    list5 = [A21,A22,A23]
    list6 = [A31,A32,A33]

    print("Matrix a =",list1)
    print("          ",list2)
    print("          ",list3)
    print()
    print()
    print("Matrix A =",list4)
    print("          ",list5)
    print("          ",list6)
    print()
    print()
    

    b11= a11*A11+a12*A21+a13*A31              #multipling matrix
    b12= a11*A12+a12*A22+a13*A32
    b13= a11*A13+a12*A23+a13*A33

    b21= a21*A11+a22*A21+a23*A31
    b22= a21*A12+a22*A22+a23*A32
    b23= a21*A13+a22*A23+a23*A33

    b31= a31*A11+a32*A21+a33*A31
    b32= a31*A12+a32*A22+a33*A32
    b33= a31*A13+a32*A23+a33*A33

    b11=float("%.2f" % b11)                   #converting into values
    b12=float("%.2f" % b12)
    b13=float("%.2f" % b13)
    b21=float("%.2f" % b21)
    b22=float("%.2f" % b22)
    b23=float("%.2f" % b23)
    b31=float("%.2f" % b31)
    b32=float("%.2f" % b32)
    b33=float("%.2f" % b33)

    final_list1 = [b11,b12,b13]
    final_list2 = [b21,b22,b23]
    final_list3 = [b31,b32,b33]
                                              #printing labels on screen
    line1 = Label(text = '''[
|
|
|
|
[
''')
    line1.pack()
    line1.place(x = 355 , y = 193)

    line2 = Label(text = ''' ]
|
|
|
|
]''')
    line2.pack()
    line2.place(x = 500 , y = 193)

    mat = Label(text = "Matrix axA =", fg = "dark blue", bg = "light green")
    mat.pack()
    mat.place(x = 270 , y = 230)              #printing values on screen

    B11 = Label(text = b11)
    B11.pack()
    B11.place(x = 375 , y = 200)

    B21 = Label(text = b21)
    B21.pack()
    B21.place(x = 375 , y = 230)

    B31 = Label(text = b31)
    B31.pack()
    B31.place(x = 375 , y = 260)

    B12 = Label(text = b12)
    B12.pack()
    B12.place(x = 415 , y = 200)

    B22 = Label(text = b22)
    B22.pack()
    B22.place(x = 415 , y = 230)

    B32 = Label(text = b32)
    B32.pack()
    B32.place(x = 415 , y = 260)

    B13 = Label(text = b13)
    B13.pack()
    B13.place(x = 455 , y = 200)

    B23 = Label(text = b23)
    B23.pack()
    B23.place(x = 455 , y = 230)

    B33 = Label(text = b33)
    B33.pack()
    B33.place(x = 455 , y = 260)
    
    print("Matrix axA =", final_list1)
    print("            ",final_list2)
    print("            ",final_list3)




def run1():                                 #getting input values  
    a11= sa11.get()
    a12= sa12.get()
    a13= sa13.get()
    a21= sa21.get()
    a22= sa22.get()
    a23= sa23.get()
    a31= sa31.get()
    a32= sa32.get()
    a33= sa33.get()
    A11= sA11.get()
    A12= sA12.get()
    A13= sA13.get()
    A21= sA21.get()
    A22= sA22.get()
    A23= sA23.get()
    A31= sA31.get()
    A32= sA32.get()
    A33= sA33.get()

    a11=float(a11)                         #converting into points
    a12=float(a12)
    a13=float(a13)
    a21=float(a21)
    a22=float(a22)
    a23=float(a23)
    a31=float(a31)
    a32=float(a32)
    a33=float(a33)
    A11=float(A11)
    A12=float(A12)
    A13=float(A13)
    A21=float(A21)
    A22=float(A22)
    A23=float(A23)
    A31=float(A31)
    A32=float(A32)
    A33=float(A33)

    
    list1 = [a11,a12,a13]            
    list2 = [a21,a22,a23]
    list3 = [a31,a32,a33]

    
    list4 = [A11,A12,A13]
    list5 = [A21,A22,A23]
    list6 = [A31,A32,A33]

    print("Matrix a =",list1)
    print("          ",list2)
    print("          ",list3)
    print()
    print()
    print("Matrix A =",list4)
    print("          ",list5)
    print("          ",list6)
    print()
    print()

    b11= a11+A11                           #adding matrix
    b12= a12+A12
    b13= a13+A13

    b21= a21+A21
    b22= a22+A22
    b23= a23+A23

    b31= a31+A31
    b32= a32+A32
    b33= a33+A33


    b11=float("%.2f" % b11)                #converting into values
    b12=float("%.2f" % b12)
    b13=float("%.2f" % b13)
    b21=float("%.2f" % b21)
    b22=float("%.2f" % b22)
    b23=float("%.2f" % b23)
    b31=float("%.2f" % b31)
    b32=float("%.2f" % b32)
    b33=float("%.2f" % b33)

    final_list1 = [b11,b12,b13]
    final_list2 = [b21,b22,b23]
    final_list3 = [b31,b32,b33]
                                           #printing labels on screen
    line1 = Label(text = '''[
|
|
|
|
[
''')
    line1.pack()
    line1.place(x = 95 , y = 193)

    line2 = Label(text = ''']
|
|
|
|
]''')
    line2.pack()
    line2.place(x = 240 , y = 193)

    mat = Label(text = "Matrix a+A =", fg = "dark blue", bg = "light green")
    mat.pack()
    mat.place(x = 20 , y = 230)

    B11 = Label(text = b11)                 #printing values on screen
    B11.pack()
    B11.place(x = 120 , y = 200)

    B21 = Label(text = b21)
    B21.pack()
    B21.place(x = 120 , y = 230)

    B31 = Label(text = b31)
    B31.pack()
    B31.place(x = 120 , y = 260)

    B12 = Label(text = b12)
    B12.pack()
    B12.place(x = 160 , y = 200)

    B22 = Label(text = b22)
    B22.pack()
    B22.place(x = 160 , y = 230)

    B32 = Label(text = b32)
    B32.pack()
    B32.place(x = 160 , y = 260)

    B13 = Label(text = b13)
    B13.pack()
    B13.place(x = 200 , y = 200)

    B23 = Label(text = b23)
    B23.pack()
    B23.place(x = 200 , y = 230)

    B33 = Label(text = b33)
    B33.pack()
    B33.place(x = 200 , y = 260)
    
    print("Matrix a+A =", final_list1)
    print("            ",final_list2)
    print("            ",final_list3)


def run2():                         #getting input values
    a11= sa11.get()                  
    a12= sa12.get()
    a13= sa13.get()
    a21= sa21.get()
    a22= sa22.get()
    a23= sa23.get()
    a31= sa31.get()
    a32= sa32.get()
    a33= sa33.get()
    A11= sA11.get()
    A12= sA12.get()
    A13= sA13.get()
    A21= sA21.get()
    A22= sA22.get()
    A23= sA23.get()
    A31= sA31.get()
    A32= sA32.get()
    A33= sA33.get()

    a11=float(a11)                 #converting into points
    a12=float(a12)
    a13=float(a13)
    a21=float(a21)
    a22=float(a22)
    a23=float(a23)
    a31=float(a31)
    a32=float(a32)
    a33=float(a33)
    A11=float(A11)
    A12=float(A12)
    A13=float(A13)
    A21=float(A21)
    A22=float(A22)
    A23=float(A23)
    A31=float(A31)
    A32=float(A32)
    A33=float(A33)

    
    list1 = [a11,a12,a13]
    list2 = [a21,a22,a23]
    list3 = [a31,a32,a33]

    
    list4 = [A11,A12,A13]
    list5 = [A21,A22,A23]
    list6 = [A31,A32,A33]

    print("Matrix a =",list1)
    print("          ",list2)
    print("          ",list3)
    print()
    print()
    print("Matrix A =",list4)
    print("          ",list5)
    print("          ",list6)
    print()
    print()

    b11= a11-A11                       #subtracting matrix
    b12= a12-A12
    b13= a13-A13

    b21= a21-A21
    b22= a22-A22
    b23= a23-A23

    b31= a31-A31
    b32= a32-A32
    b33= a33-A33

    b11=float("%.2f" % b11)          #converting into values
    b12=float("%.2f" % b12)
    b13=float("%.2f" % b13)
    b21=float("%.2f" % b21)
    b22=float("%.2f" % b22)
    b23=float("%.2f" % b23)
    b31=float("%.2f" % b31)
    b32=float("%.2f" % b32)
    b33=float("%.2f" % b33)

    final_list1 = [b11,b12,b13]       
    final_list2 = [b21,b22,b23]
    final_list3 = [b31,b32,b33]
                                        #printing labels on screen
    line1 = Label(text = '''   [     
|
|
|
|
[
''')
    line1.pack()
    line1.place(x = 605 , y = 193)

    line2 = Label(text = ''']
|
|
|
|
]''')
    line2.pack()
    line2.place(x = 745 , y = 193)

    mat = Label(text = "Matrix a-A =", fg = "dark blue", bg = "light green")
    mat.pack()
    mat.place(x = 525 , y = 230)

    B11 = Label(text = b11)             #printing values on screen
    B11.pack()
    B11.place(x = 625 , y = 200)

    B21 = Label(text = b21)
    B21.pack()
    B21.place(x = 625 , y = 230)

    B31 = Label(text = b31)
    B31.pack()
    B31.place(x = 625 , y = 260)

    B12 = Label(text = b12)
    B12.pack()
    B12.place(x = 665 , y = 200)

    B22 = Label(text = b22)
    B22.pack()
    B22.place(x = 665 , y = 230)

    B32 = Label(text = b32)
    B32.pack()
    B32.place(x = 665 , y = 260)

    B13 = Label(text = b13)
    B13.pack()
    B13.place(x = 705 , y = 200)

    B23 = Label(text = b23)
    B23.pack()
    B23.place(x = 705 , y = 230)

    B33 = Label(text = b33)
    B33.pack()
    B33.place(x = 705 , y = 260)
    
    print("Matrix a-A =", final_list1)
    print("            ",final_list2)
    print("            ",final_list3)


def run3():                               #getting input values
    a11= sa11.get()
    a12= sa12.get()
    a13= sa13.get()
    a21= sa21.get()
    a22= sa22.get()
    a23= sa23.get()
    a31= sa31.get()
    a32= sa32.get()
    a33= sa33.get()
    A11= sA11.get()
    A12= sA12.get()
    A13= sA13.get()
    A21= sA21.get()
    A22= sA22.get()
    A23= sA23.get()
    A31= sA31.get()
    A32= sA32.get()
    A33= sA33.get()
    n= sn.get()

    a11=float(a11)                       #converting into points
    a12=float(a12)
    a13=float(a13)
    a21=float(a21)
    a22=float(a22)
    a23=float(a23)
    a31=float(a31)
    a32=float(a32)
    a33=float(a33)
    A11=float(A11)
    A12=float(A12)
    A13=float(A13)
    A21=float(A21)
    A22=float(A22)
    A23=float(A23)
    A31=float(A31)
    A32=float(A32)
    A33=float(A33)
    n=float(n)

    
    list1 = [a11,a12,a13]
    list2 = [a21,a22,a23]
    list3 = [a31,a32,a33]

    
    list4 = [A11,A12,A13]
    list5 = [A21,A22,A23]
    list6 = [A31,A32,A33]

    print("Matrix a =",list1)
    print("          ",list2)
    print("          ",list3)
    print()
    print()
    print("Matrix A =",list4)
    print("          ",list5)
    print("          ",list6)
    print()
    print()

    b11= n*a11                          #scalar multiplcation matrix
    b12= n*a12
    b13= n*a13

    b21= n*a21
    b22= n*a22
    b23= n*a23

    b31= n*a31
    b32= n*a32
    b33= n*a33


    b11=float("%.2f" % b11)             #converting into values
    b12=float("%.2f" % b12)
    b13=float("%.2f" % b13)
    b21=float("%.2f" % b21)
    b22=float("%.2f" % b22)
    b23=float("%.2f" % b23)
    b31=float("%.2f" % b31)
    b32=float("%.2f" % b32)
    b33=float("%.2f" % b33)

    final_list1 = [b11,b12,b13]
    final_list2 = [b21,b22,b23]
    final_list3 = [b31,b32,b33]
                                        #printing labels on screen
    line1 = Label(text = '''[
|
|
|
|
[
''')
    line1.pack()
    line1.place(x = 855 , y = 193)

    line2 = Label(text = ''']
|
|
|
|
]''')
    line2.pack()
    line2.place(x = 998 , y = 193)

    mat = Label(text = "Matrix n.a =", fg = "dark blue", bg = "light green")
    mat.pack()
    mat.place(x = 775 , y = 230)

    B11 = Label(text = b11)            #printing values on screen
    B11.pack()
    B11.place(x = 875 , y = 200)

    B21 = Label(text = b21)
    B21.pack()
    B21.place(x = 875 , y = 230)

    B31 = Label(text = b31)
    B31.pack()
    B31.place(x = 875 , y = 260)

    B12 = Label(text = b12)
    B12.pack()
    B12.place(x = 915 , y = 200)

    B22 = Label(text = b22)
    B22.pack()
    B22.place(x = 915 , y = 230)

    B32 = Label(text = b32)
    B32.pack()
    B32.place(x = 915 , y = 260)

    B13 = Label(text = b13)
    B13.pack()
    B13.place(x = 955 , y = 200)

    B23 = Label(text = b23)
    B23.pack()
    B23.place(x = 955 , y = 230)

    B33 = Label(text = b33)
    B33.pack()
    B33.place(x = 955 , y = 260)
    
    print("Matrix n.a =", final_list1)
    print("            ",final_list2)
    print("            ",final_list3)


    
        
screen = Tk()                                     #screen setting
screen.title("Matrix Multiplication" ,)
screen.geometry("1050x400")

welcome = Label(text = "Welcome please enter matrix a,A to solve your question ", fg = "red", bg = "yellow")
welcome.pack()
welcome.place(x = 375, y =10)

matrix_a = Label(text = "Matrix a = ", fg = "black")
matrix_a.pack()
matrix_a.place(x = 15, y = 87)

matrix_A = Label(text = "Matrix A = ", fg = "black")
matrix_A.pack()
matrix_A.place(x = 515, y =87)

scalar = Label(text = "n.a =", fg = "black")
scalar.pack()
scalar.place(x = 852.5, y =325.5)



sa11 = StringVar()                                #1st matrix location boxes
a11 = Entry(text = sa11)
a11.pack()
a11.place( x=80 ,y =60)

sa12 = StringVar()
a12 = Entry(text = sa12)
a12.pack()
a12.place( x=210 ,y =60)


sa13 = StringVar()
a13 = Entry(text = sa13)
a13.pack()
a13.place( x=340 ,y =60)

sa21 = StringVar()
a21 = Entry(text = sa21)
a21.pack()
a21.place( x=80 ,y =90)

sa22 = StringVar()
a22 = Entry(text = sa22)
a22.pack()
a22.place( x=210 ,y =90)

sa23 = StringVar()
a23 = Entry(text = sa23)
a23.pack()
a23.place( x=340 ,y =90)

sa31 = StringVar()
a31 = Entry(text = sa31)
a31.pack()
a31.place( x=80 ,y = 120)

sa32 = StringVar()
a32 = Entry(text = sa32)
a32.pack()
a32.place( x=210 ,y =120)

sa33 = StringVar()
a33 = Entry(text = sa33)
a33.pack()
a33.place( x=340 ,y =120)








sA11 = StringVar()                         #2st matrix location boxes
A11 = Entry(text = sA11)
A11.pack()
A11.place( x=580 ,y =60)

sA12 = StringVar()
A12 = Entry(text = sA12)
A12.pack()
A12.place( x=710 ,y =60)


sA13 = StringVar()
A13 = Entry(text = sA13)
A13.pack()
A13.place( x=840 ,y =60)

sA21 = StringVar()
A21 = Entry(text = sA21)
A21.pack()
A21.place( x=580 ,y =90)

sA22 = StringVar()
A22 = Entry(text = sA22)
A22.pack()
A22.place( x=710 ,y =90)

sA23 = StringVar()
A23 = Entry(text = sA23)
A23.pack()
A23.place( x=840 ,y =90)

sA31 = StringVar()
A31 = Entry(text = sA31)
A31.pack()
A31.place( x=580 ,y = 120)

sA32 = StringVar()
A32 = Entry(text = sA32)
A32.pack()
A32.place( x=710 ,y =120)

sA33 = StringVar()
A33 = Entry(text = sA33)
A33.pack()
A33.place( x=840 ,y =120)



sn = StringVar()
n = Entry(text = sn)
n.pack()
n.place( x=884 ,y =327)

             #buttons command

click = Button(text = "multiplication of a x A", fg = "red", bg = "yellow" , command = run) 
click.place(x = 366, y = 350)

click = Button(text = "Addition of a + A", fg = "red", bg = "yellow" , command = run1)
click.place(x = 123, y = 350)

click = Button(text = "minus of a - A", fg = "red", bg = "yellow" , command = run2)
click.place(x = 638, y = 350)

click = Button(text = " scalar multiplication of n.a", fg = "red", bg = "yellow" , command = run3)
click.place(x = 854, y = 350)

screen.mainloop()



