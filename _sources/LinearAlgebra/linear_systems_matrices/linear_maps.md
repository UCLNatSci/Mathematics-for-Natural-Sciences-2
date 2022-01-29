# Linear Transformations

In this section we learn to understand matrices geometrically as functions, or transformations. We briefly discuss transformations in general, then specialize to matrix transformations, which are transformations that come from matrices.

## Linear Transformations

A function is a rule that takes inputs and transforms them to outputs. For example, a function $f:\mathbb{R}\rightarrow\mathbb{R}$,

$$f(x)=x^2$$

is a function that takes a real number $x$ as input and outputs another real number, the square of the input. On the other hand, the function $g:\mathbb{R}^2\rightarrow \mathbb{R}$,

$$g(x, y) = x^2 + y^3$$

is a function which maps 2-dimensional vectors $(x, y) \in \mathbb{R}^2$ to real numbers.

```{admonition} Definition

Suppose  $f:\mathbb{R}^n \rightarrow \mathbb{R}^m$ is a function such that

$$f(u + v) =f(u) + f(v)$$

and

$$f(au) = af(u)$$

for all $u, v \in\mathbb{R}^n$ and $a\in\mathbb{R}$.

Then $f$ is a **linear transformation**.
```

```{admonition} Examples
:class: tip
[TODO]

Examples of linear transformations

Examples of non-linear transformations

Geometric examples.
```

## Matrix Transformations

Now let $A$ be an $(m \times n)$ matrix. Then $A$ defines a function

$$T:\mathbb{R}^n\rightarrow\mathbb{R}^m$$

where

$$T(x) = Ax.$$

In other words, $A$ defines a function which takes a vector $x \in \mathbb{R}^n$ and transforms it to a vector $Ax \in \mathbb{R}^m$. In fact, it turns out that the function defined by multiplication by a matrix is a linear transformation.

```{admonition} Theorem
If $A$ is an $(m \times n)$ matrix $A$ then the function

$$T:\mathbb{R}^n\rightarrow\mathbb{R}^m$$

defined by

$$T(x) = Ax$$

is a linear transformation which takes the vector $x \in \mathbb{R}^n$ to the vector $Ax \in \mathbb{R}^m$.
```

The proof of this follows directly from the definitions of matrix arithmetic:

$$
T(u+v) = A(u+v) = Au + Av = T(u) + T(v)\\
T(au) = A(au) = aAu = aT(u).
$$

There is essentially nothing new here, beyond the notation and a slightly different way of thinking about matrix multiplication. In the next section we will see how thinking of a matrix as a transformation allows us to picture its effect geometrically.


## Geometrical Interpretation of Matrices

Consider the matrix

$$A = \begin{pmatrix}-1 & 0\\0 & 1\end{pmatrix}$$

which defines the linear transformation $T:\mathbb{R}^2 \rightarrow \mathbb{R}^2$ defined by $T(x) = Ax$.

Given a vector $x=\begin{pmatrix}x_1\\x_2\end{pmatrix}$ we can consider the effect of the transformation $T$:

$$T(x) = A\begin{pmatrix}x_1\\x_2\end{pmatrix}=\begin{pmatrix}-1 & 0\\0 & 1\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}=\begin{pmatrix}-x_1\\x_2\end{pmatrix}.$$

Multiplication by $A$ negates the $x_1$ co-ordinate and leaves the $x_2$ co-ordinate unchanged i.e. *it reflects over the $x_2$ axis*.

We can illustrate this by picturing the effect of the transformation on the unit co-ordinate vectors $e_1 = \begin{pmatrix}1\\0\end{pmatrix}$ and $e_2=\begin{pmatrix}0\\1\end{pmatrix}$:

$$T(e_1) = Ae_1 =\begin{pmatrix}-1 & 0\\0 & 1\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}-1\\0\end{pmatrix} $$

$$T(e_2) = Ae_2 = \begin{pmatrix}-1 & 0\\0 & 1\end{pmatrix}\begin{pmatrix}0\\1\end{pmatrix}=\begin{pmatrix}0\\1\end{pmatrix}.$$

```{glue:} la_fig_1
```

Furthermore, once we know the transformed unit vectors, we can use the linearity of the transformation to determine how *any* vector is transformed. Given a vector $x = \begin{pmatrix}x_1\\x_2\end{pmatrix}$, we can write $x$ as a sum of unit co-ordinate vectors:

$$x = \begin{pmatrix}x_1\\x_2\end{pmatrix} = x_1e_1 + x_2e_2$$

and use the linearity property to calculate the result

$$T(x) = Ax = A(x_1e_1 + x_2e_2) = x_1Ae_1 + x_2Ae_2 = x_1T(e_1) + x_2T(e_2).$$

For example, the vector $e_1 + e_2$ is transformed to $T(e_1) + T(e_2)$ so we can use this to draw the image of the unit square which has vertices $0$, $e_1$, $e_2$ and $e_1 + e_2$:

```{glue:} la_fig_2
```

```{admonition} Example
:class: tip
Determine the geometrical effect of the transformation given by the matrix

$$A = \begin{pmatrix} \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}\\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}\end{pmatrix}.$$

**Solution**

TODO

```

## The Matrix of a Linear Transformations

In this section will learn that *all* linear transformations are matrix transformations - in other words, any function $T$ which satisfies the linearity properties can be written as a matrix $T(x) = Ax$. Before doing so, we need the following important notation.

```{admonition} Definition
The **standard coordinate vectors** in $\mathbb{R}^n$ are the $n$ vectors

$$e_1 = \begin{pmatrix}1\\0\\\vdots\\0\end{pmatrix},~e_2 = \begin{pmatrix}0\\1\\\vdots\\0\end{pmatrix},\ldots,~e_n = \begin{pmatrix}0\\0\\\vdots\\1\end{pmatrix}.$$
```

The standard coordinate vectors are useful because of the following property:

**Multiplying a matrix by the standard co-ordinate vector $e_i$ selects the $i$th column of the matrix**.

Suppose that an $(m \times n)$ matrix $A$ is composed of the $n$ column vectors $v_1, v_2, \ldots, v_n$. Then,

$$\begin{pmatrix}| & | & & | \\v_1 & v_2 & \cdots & v_n\\| & | & & |\end{pmatrix}e_i = v_i.$$

For exampl

$$\begin{pmatrix}1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9\end{pmatrix}\begin{pmatrix}1 \\ 0 \\ 0\end{pmatrix} =\begin{pmatrix}1 \\ 4 \\ 7\end{pmatrix}.$$

```{admonition} Theorem

Let $T:\mathbb{R}^n \rightarrow \mathbb{R}^m$ be a linear transformation. Then the $(m \times n)$ matrix

$$A = \begin{pmatrix}| & | & & | \\T(e_1) & T(e_2) & \cdots & T(e_n)\\| & | & & |\end{pmatrix}$$

is the matrix corresponding to the transformation $T$ and $T(x)=Ax$.
```

Using this theorem, we can write down the matrix of *any* linear transformation.

:::{admonition} Example
:class: tip

Determine the matrix of the linear transformation $T:\mathbb{R}^2 \rightarrow \mathbb{R}^2$ corresponding to reflection across the line $x_2 = -x_1$.

**Solution**

First, determine the transformation of the unit coordinate vectors.

```{glue:} la_fig_3
```

$$T(e_1) = \begin{pmatrix}0\\-1\end{pmatrix}\\
T(e_2) = \begin{pmatrix}-1\\0\end{pmatrix}$$

Therefore the matrix,

$$A = \begin{pmatrix}| & |\\T(e_1) & T(e_2) \\| & | \end{pmatrix} = \begin{pmatrix}0 & -1 \\-1 &0\end{pmatrix}$$

is the matrix of the transformation $T$.

:::

## Rotation matrices in 2D

Suppose the linear transformation $T:\mathbb{R}^2 \rightarrow \mathbb{R}^2$ corresponds to an anticlockwise rotation by an angle $\theta$ around the origin. Then we can use trigonometry to determine the destination of the coordinate vectors under $T$:

```{glue:} la_fig_4
```

$$T(e_1) = \begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix}\\
T(e_2) = \begin{pmatrix}-\sin\theta\\\cos\theta\end{pmatrix}$$

```{admonition} Rotation Matrix
The matrix corresponding to an anticlockwise rotation by $\theta$ degrees around the origin is given by:

$$A = \begin{pmatrix}\cos\theta & -\sin\theta\\\sin\theta & \cos\theta\end{pmatrix}.$$

```

## Projection Matrix

[TODO]

## Sequence of transformations

[TODO]
