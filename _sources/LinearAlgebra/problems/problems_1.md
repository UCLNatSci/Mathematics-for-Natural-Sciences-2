# Linear Algebra - Problem Sheet 1

## Question 1

<!---
Strang 3.2 Q1
-->

1\. Reduce $A$ and $B$ to row echelon form. Which variables are free?

a) $A = \begin{pmatrix}
1 & 2 & 2 & 4 & 6\\
1 & 2 & 3 & 6 & 9\\
0 & 0 & 1 & 2 & 3
\end{pmatrix}$
b) $B = \begin{pmatrix}
2 & 4 & 2\\
0 & 4 & 4\\
0 & 8 & 8\\
\end{pmatrix}$

2\. For the matrices $A$ and $B$, find a special solution for each free variable. (Set the free variable to 1 and set the other free variables to 0.)

3\. By further row operations, find the *reduced* echelon form of $A$ and $B$ and calculate the nullspace of each.

4\. *True or False, with explanation*: The nullspace of a matrix is the same as the nullspace of its reduced echelon form.

## Question 2

Solve Ax=B.

# Question 3

Kirchoff's law.

<!---
Strang 3.2 Q32
-->

## Question 4

Permutation matrices.

## Application: Kirchoff's Law
In general, Gaussian elimination can be used to solve the problems obtained by applying Kirchoff's laws. For example, see the problems given here:

https://www.intmath.com/matrices-determinants/6-matrices-linear-equations.php

In the example below, the technique is applied to a case where the system of equations is under-determined, so a unique solution cannot be obtained.

![](kirchoff.png)

```{admonition} Kirchoff's Law

Kirchoff's law states that

$$\mathrm{current~in} = \mathrm{current~out}$$

```

For the system of 4 nodes shown above, this gives us four equations:

\begin{align}y_3&=y_1+y_4\\y_1&=y_2+y_5\\y_2&=y_3+y_6\\y_4+y_5+y_6&=0\end{align}

The equations at each node are of the form $c_1 y_1 +c_2 y_2+\dots +c_6 y_6=d$. Written in augmented matrix form, the system is:

$$\left(\begin{array}{cccccc:c}1 & 0 & -1 & 1 & 0 & 0 &0\\-1 & 1 & 0 & 0 & 1 & 0&0 \\0 & -1 & 1 & 0 & 0 & 1&0 \\0 & 0 & 0 & -1 & -1 & -1 &0\\\end{array}\right)$$

The first 6 columns are for the coefficients of $y_1,\dots y_6$ and the last column is the constant term that appears on the right hand side of the equation.

Here, Gaussian elimination is applied as usual, but the complicating factor is that there are more unknowns than equations and so the system is under-determined. It has "free variables", that can be made to take any value!

After applying Gaussian elimination to the pivot elements in the first and second column, we can't do anything with the third column without spoiling the progress we've made in the first two columns, so we leave that one and move on to use the fourth column as a pivot. After that, we can't make any more progress so we stop. We obtain:

$$\left(\begin{array}{cccccc:c}1 & 0 & -1 & 0 & -1 & -1 & 0 \\0 & 1 & -1 & 0 & 0 & -1 & 0 \\0 & 0 & 0 & 1 & 1 & 1 & 0 \\0 & 0 & 0 & 0 & 0 & 0 & 0 \\\end{array}\right)$$

The first, second, and fourth columns are the pivot columns, and the other columns are all "free" since they can be obtained from a combination of the other columns.

Choosing $(y_3,y_5,y_6)=(1,0,0)$ gives the special solution $s_1:(1,1,1,0,0,0)$  
Choosing $(y_3,y_5,y_6)=(0,1,0)$ gives the special solution $s_2:(1,0,0,-1,1,0)$  
Choosing $(y_3,y_5,y_6)=(0,0,1)$ gives the special solution $s_3:(1,1,0,-1,0,1)$

The full solution space consists of all possible linear combinations $a s_1 + b s_2 +c s_3$.
