# Linear Algebra Problems 2

## Question 1

Identify the set of points in the plane that are invariant (do not change) under the transformation matrix

$$A=\begin{pmatrix}-\frac{1}{2}&\frac{\sqrt{3}}{2}\\\frac{\sqrt{3}}{2}&\frac{1}{2}\end{pmatrix}.$$

What transformation is represented by this matrix?

## Yutsumura 610

Define two functions T:R2→R2 and S:R2→R2 by
T([xy])=[2x+y0],S([xy])=[x+yxy].
Determine whether T, S, and the composite S∘T are linear transformations.

## Yutsumura 171

Define two functions T:R2→R2 and S:R2→R2 by
T([xy])=[2x+y0],S([xy])=[x+yxy].
Determine whether T, S, and the composite S∘T are linear transformations.

## Yutsumura 368 or Problem 324

Let T be a linear transformation from R3 to R2 such that
T⎛⎝⎜⎡⎣⎢010⎤⎦⎥⎞⎠⎟=[12] and T⎛⎝⎜⎡⎣⎢011⎤⎦⎥⎞⎠⎟=[01].
Then find T⎛⎝⎜⎡⎣⎢012⎤⎦⎥⎞⎠⎟.

## Yutsumura Problem 44


## Projection matrix



### answer

Points which are invariant under transform $x \mapsto Ax$ satisfy $Ax=x$ (they are mapped to themselves). We can rearrange this as $(A−I)x=0$.

Written in equation form for $x=\begin{pmatrix}x_1\\x_2\end{pmatrix}$ we have

$$\begin{pmatrix}-\frac{3}{2}&\frac{\sqrt{3}}{2}\\\frac{\sqrt{3}}{2}&-\frac{1}{2}\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix} = \begin{pmatrix}0\\0\end{pmatrix}.$$

Since $\det(A−I)=0$ these two equations are equivalent. In this case the first equation is $−\sqrt{3}$ times the second. So there is not a unique solution. We will find an infinite number of invariant points, which lie on the line $x_2=–\sqrt{3}x_1$, by solving either of the two equations.

The transform represented here is a reflection in the line $x_2=\sqrt{3}x_1$, as can be verified by substituting $\theta=\arctan(\sqrt{3})=\pi/3$ into the reflection matrix.

## Question 2

1. State equivalent conditions for a square matrix $M$ to be invertible, and give an example of a $(2\times2)$ matrix that is not invertible.

2. Provide a definition of the inverse matrix $M^{−1}$ , where $M$ is an invertible square matrix.

3. Given that $M=\begin{pmatrix}1&2\\3&5\end{pmatrix}$, find the inverse matrix $M^{−1}$.

4. Use your result from part 3 to find the unique matrix $X$ that satisfies the equation

$$X\begin{pmatrix}1&2\\3&5\end{pmatrix}=\begin{pmatrix}7&0\\2&9\end{pmatrix}.$$



## More Questions

### Question

https://moodle.ucl.ac.uk/question/question.php?returnurl=%2Fquestion%2Fedit.php%3Fcmid%3D3169235%26cat%3D106206%252C678882%26qpage%3D0%26recurse%3D0%26showhidden%3D0%26qbshowtext%3D0&cmid=3169235&id=335131

In this question, we will construct the 3-dimensional transformation matrix for a rotation about the line $x=y=z$ by an angle $\frac{\pi}{3}$.

The vector $\underline{v}=\underline{i}+\underline{j}+\underline{k}$ is parallel to the line.

The direction of rotation will be chosen as follows:

Point your thumb of your right hand in the direction of $\underline{v}$ and curl your fingers towards your palm. The direction that your fingers are curled is the rotation direction.

Under this transformation, the unit vectors $\underline{i}$ and $\underline{j}$ are mapped to

$$\frac{1}{3}(2\underline{i}+2\underline{j}-1\underline{k})$$

$$\frac{1}{3}(-1\underline{i}+2\underline{j}+2\underline{k})$$

respectively.

Use the fact that orthogonal vectors remain orthogonal under rotation to find out what happens to the unit vector $\underline{k}$ under the transform

Hence, construct the transformation matrix $T$.

Use your transformation matrix to calculate what happens to the point $(3,0,3)$ under the rotation.

Enter the $x$ coordinate of the point after transformation in the space provided.

### answer

Calculate the vector product of the transformed $\underline{i}$ and $\underline{j}$ vectors:

$$\frac{1}{9}\left|\begin{array}{ccc}\underline{i} & \underline{j} &\underline{k}\\2 & 2 & -1\\-1 & 2 & 2\end{array}\right|$$

$$=\frac{1}{3}(2\underline{i}-\underline{j}+2\underline{k})$$

Thus, the transformation matrix is

$$T=\frac{1}{3}\left(\begin{array}{ccc}2 & -1 & 2\\2 & 2 & -1\\-1 & 2 & 2\end{array}\right)$$

To transform the given point:

$$\frac{1}{3}\left(\begin{array}{ccc}2 & -1 & 2\\2 & 2 & -1\\-1 & 2 & 2\end{array}\right)\left(\begin{array}{c}3\\0\\3\end{array}\right)$$

$$=\left(\begin{array}{c}2+2\\2-1\\-1+2\end{array}\right)$$

### Question

Write down the 2D transformation matrix $M$ for a reflection in the line $y=\sqrt{3}x$

This transform is followed by another linear transform represented by matrix $N$.

The composite transform $M$ followed by $N$ is given by

$$T=\frac{1}{2}\left(\begin{array}{cc}-1+2\sqrt{3} & 2+\sqrt{3}\\ \sqrt{3} & 1\end{array}\right).$$

Use this information to calculate the transformation matrix $N$

Enter the value $N_{1,2}$ in the space provided.

### answer

$M=\left(\begin{array}{cc}\cos{2\theta}&\sin{2\theta}\\ \sin{2\theta}&-\cos{2\theta}\end{array}\right)$ with $\theta=\tan^{-1}{\sqrt{3}}=\frac{\pi}{3}$

gives

$$M=\frac{1}{2}\left(\begin{array}{cc}-1&\sqrt{3}\\ \sqrt{3}&1\end{array}\right)$$

$$\det{M}=\left(\frac{1}{2}\right)^2(-1-3)=-1$$

so

$$M^{-1}=-\frac{1}{2}\left(\begin{array}{cc}1&-\sqrt{3}\\ -\sqrt{3}&-1\end{array}\right)$$

$$T=NM$$

(transform $M$ is applied first)
