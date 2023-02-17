import numpy as np
l=12 
w=10
#Question a
#Bending moment(M) and shear force(V) at the first end,  x=0
x=0
M=(w*(-6*x**2+6*l*x-l**2))/12
V=w*(l/2-x)
m='the bending moment at x=0 is'
n='the shear force at x= 0 is'
print()
print('(a.1)'+m+str(M)+'and',n+str(V))

#Bending moment(M) and shear force(V) at the last end, x=l=10
x=l
M=(w*(-6*x**2+6*1*x-1**2))/12
V=w*(l/2-x)
m='the bending moment at x=l is'
n='the shear force at x=l is'
print('(a.2)'+m+str(M)+'and',n+str(V))


#question b 
"""
when the bending moment is zero, we get an expression 6*x**2-6*l*x+l**2=0
"""
# from the expression
a=6
b=-6*l
c=l**2
#using the almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1b=(-b+np.sqrt(discriminant))/2*a
root_2b=(-b-np.sqrt(discriminant))/2*a
print()
print('(b) the points of contra-flexure are {0} and{1}'.format(root_1b,root_2b))


#question c
"""
when the shear force is zero, x=l/2
"""
x=l/2
print()
print('(c)the point at which V=0 is {}'.format(x))
#question d
p=0
s=0.01
q=l+s
x=np.arange(p,q,s)
M=(w*(-6*x**2+6*l*x-l**2))/12
print()
print('(d) usiing the initialized variable, the bending moment of each step in the array is {0}'.format(M))

#question e
V=w*(l/2-x)
print()
print('(e)the shear force for each step along the span is {}'.format(V))

#question f
"""
let the absolute value of the bending moment array be AM
also let the minimum AM be m_AM
"""
AM=abs(M)
m_AM=min(AM)
"""
when the bending moment is m_AM, we get an expression x**2-lx+(l**2/6)+(2*m_AM)/w=0
"""
#from the above the expression
a=1
b=-l
c=(l**2/6)+(2*m_AM)/w
#using the alimighty formula the two roots are;
discriminant=b**2-4*a*c
root_1f=(-b+np.sqrt(discriminant))/2*a
root_2f=(-b-np.sqrt(discriminant))/2*a
print()
print('(f) the points along l at which the absolute values of the bending  array is minimum are {0} and {1}'.format(root_1f, root_2f)) 

#question g
"""
let the relative errors be r_e
"""
r_e1=((root_1b-root_1f)/root_1b*100)
r_e2=((root_2f-root_2b)/root_2f*100)
print()
print('(g)the relative errors between estimated points of the contra-flexure are {0}% and{1}%'.format(r_e1,r_e2))

#question h
"""
let the maximum bemding moment be max_M and the minimum bending moment be min_M
"""
#for the maximum
max_M=max(M)
"""
when the bending moment is max_M, we get an expression x**2-lx+(l**2//6)+(2*min_M)/w=0
"""
a=1
b=-l
c=(l**2/6)+(2*max_M)/w
#using the almighty formula the two root are;
discriminant=b**2-4*a*c
root_1=(-b+np.sqrt(discriminant))/2*a
root_2=(-b-np.sqrt(discriminant))/2*a
print()
print('(h.1)the points at which the maximum bendind moment occur are {0} and{1}'.format(root_1,root_2))

#for the minimum
min_M=min(M)
"""
when the bending moment is min_M, we get an expression x**2-lx+(l**2//6)+(2*min_M)/w=0
"""
a=1
b=-l
c=(l**2//6)+(2*min_M)/w
#using the almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1=(-b-np.sqrt(discriminant))/2*a
root_2=(-b+np.sqrt(discriminant))/2*a
print()
print('(h.2)the points at which the minimum bending moment occur are{0} and{1}'.format(root_1,root_2))


www.github.com/mbrowah





