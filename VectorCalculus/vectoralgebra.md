# Vectors and Vector Algebra

We can think of vectors at their heart as directions being given to get between two points in space.  If we have to move in one, two or three dimensions, along spatially flat or curved surfaces, 
we can attempt to give directions.  At the heart of a any vector system are the <b>basis vectors</b>, these give us the funadmental possible directions within a vector space, which any vector can be
decompsoed into a weighted sum of.

In the Cartesian coordinate system, in three dimensions the basis vectors are given as:

```{math}
\hat{\bf x} = \,\begin{pmatrix}
 1 \\
 0 \\
 0 
\end{pmatrix}, \quad 
\hat{\bf y} = \,\begin{pmatrix}
 0 \\
 1 \\
 0 
\end{pmatrix}, \quad 
\hat{\bf z} \,\begin{pmatrix}
 0 \\
 0 \\
 1 
\end{pmatrix}
```
and when we switch to different coordinate systems, we will consider how these change.  Note that a variety of different letters are employed for the Cartessian system:
```{math}

\hat{\bf x} &=&\, {\bf e_x} = \vec{x} = \hat{\bf i}\\
\hat{\bf y} &=&\, {\bf e_y} = \vec{y} = \hat{\bf j}\\
\hat{\bf z} &=&\, {\bf e_z} = \vec{z} = \hat{\bf k}
```
To see how these visually fit together, see {numref}`CartCoords`.  We note that all the coordinates meet at right angles and that we have defined <em>right handed axes</em>.

```{figure} ../figures/CartesianCoordinateSystem.png
---
name: CartCoords
---

<b>Left Pane</b>: Graphical breakdown of the Cartesian coordinate system with vector path in red,
<b>Right Pane</b>: The differences between left handed (top) and right handed (bottom) axes.
```

We can also write coordinates in so-called <b>index notation</b>:
```{math}
x_i = \left(\hat{\bf x},\, \hat{\bf y},\, \hat{\bf z}\right)
```
where the value of $i = \in \{1,\,2,\,3\}$ denotes the specific basis vector.

## Addition and Scaling of Vectors

If we start with the basis vectors as building blocks of our coordinate system, then we can write any three dimensional Cartesian coordinate in terms of 
weighted basis vectors, we can see this in {numref}`basisvectors`.

```{figure} ../figures/basisvectors.png
---
name: basisvectors
---
Breakdown of vector $\bf a = a_x \,\hat{\bf x} + a_y \,\hat{\bf y} + a_z \,\hat{\bf z}$.
```

As an example we can define two vectors $\bf v_1,\, v_2$
```{math}
{\bf v}_1 &=&\, \begin{pmatrix}
 3 \\
 4 \\
 12 
\end{pmatrix} = 3\hat{\bf x} + 4\hat{\bf y} + 12\hat{\bf z}\\
{\bf v}_2 &=&\, \begin{pmatrix}
 5 \\
 12 \\
 13 
\end{pmatrix} = 5\hat{\bf x} + 12\hat{\bf y} + 13\hat{\bf z}
```
Then we can add or sutract these vectors:

```{math}
{\bf v}_1 + {\bf v}_2  &=&\, \begin{pmatrix}
 3 \\
 4 \\
 12 
\end{pmatrix} + \begin{pmatrix}
 5 \\
 12 \\
 13 
\end{pmatrix} = \begin{pmatrix}
 8 \\
 16 \\
 25 
\end{pmatrix} = 8\hat{\bf x} + 16\hat{\bf y} + 25\hat{\bf z}\\
{\bf v}_2 - {\bf v}_1  &=&\, \begin{pmatrix}
 5 \\
 12 \\
 13 
\end{pmatrix} - 
\begin{pmatrix}
 3 \\
 4 \\
 12 
\end{pmatrix} = \begin{pmatrix}
 2 \\
 8 \\
 1 
\end{pmatrix} = 2\hat{\bf x} + 8\hat{\bf y} + \hat{\bf z}

```
Likewise we can scale each of the vectors and then proceed to add them:
```{math}
2{\bf v}_1 + 3{\bf v}_2  &=&\,  2\begin{pmatrix}
 3 \\
 4 \\
 12 
\end{pmatrix} + 3\begin{pmatrix}
 5 \\
 12 \\
 13 
\end{pmatrix} = \begin{pmatrix}
 21 \\
 44 \\
 63 
\end{pmatrix} = 21\hat{\bf x} + 44\hat{\bf y} + 49\hat{\bf z}
```

## Magnitude of a Vector

Given some vector, which will take us some distance from two points in space, we can find the shortest path length between the points.  

In two dimensions this would just follow Pythagoras's theorem:
```{math}
{\bf v} = a_x\hat{\bf x} + a_y\hat{\bf y}
v_3 = |{\bf v}| = \sqrt{{a_x}^2 + {a_y}^2}
```

and in three dimensions a similar relation holds (which we can prove geometrically:
```{math}
{\bf v} = a_x\hat{\bf x} + a_y\hat{\bf y} + a_z\hat{\bf z}
v_3 = |{\bf v}| = \sqrt{{a_x}^2 + {a_y}^2 + {a_z}^2} 
```
As an example lets consider $\bf v_1$:

```{math}
|3\hat{\bf x} + 4\hat{\bf y} + 12\hat{\bf z}| = \sqrt{3^2 + 4^2 + 12^2} = 13
```


## Normalised Vectors
Each of the basis vectors is a normalised vector $|\hat{\bf x}| = |\hat{\bf y}| = |\hat{\bf z}| = 1$, however if we have a more general vector 
${\bf v} = a_x\hat{\bf x} + a_y\hat{\bf y} + a_z\hat{\bf z}$ moving in some direction, we can also construct a normalised vector:
```{math}
\hat{\bf v} = \frac{\bf v}{|\bf v|} = \frac{a_x\hat{\bf x} + a_y\hat{\bf y} + a_z\hat{\bf z}}{\sqrt{{a_x}^2 + {a_y}^2 + {a_z}^2}}
```

As an example lets consider $\bf v_1$:

```{math}
\hat{\bf v_1} = \frac{\bf v_1}{|\bf v_1|} = \frac{3\hat{\bf x} + 4\hat{\bf y} + 12\hat{\bf z}}{\sqrt{3^2 + 4^2 + 12^2}} = \frac{1}{13}\left(3\hat{\bf x} + 4\hat{\bf y} + 12\hat{\bf z}\right)
```

## Scalar Product / Dot Product
### Geometric Definiton
Lets consider two vectors $\bf A,\, B$, as shown in {numref}`scalarprojection`.  We can consider the scalar projection of the vector $\bf B$ on to the vector $\bf A$, where we resolve the 
parallel components of $\bf B$ in the direction of vector $\bf A$.

```{figure} ../figures/scalarprojection.png
---
name: scalarprojection
---
<b>Left Pane</b>: Vectors $\bf A,\, B$ which share a common coordinate and span an angle $\theta$ between them,
<b>Right Pane</b> The scalar projection of the vector $\bf B$ on to the vector $\bf A$, which by trigonometry gives the length $|{\bf B}| \cos\theta$.
```

If we multiply these two distances, this is <b>Scalar Product</b> of the vectors:

```{math}
{\bf A \cdot B} = |{\bf A}||{\bf B}|\cos(\theta)
```
also known as the <b>Dot Product</b>.

So we can calculate the scalar projection of $\bf B$ onto vector $\bf A$ using ${\bf A \cdot B} / |{\bf A}|$.  Likewise we can think about the scalar projection of $\bf A$ onto the vector 
$\bf B$, using ${\bf A \cdot B} / |{\bf B}|$.

We can also find the magntiude of a vector from $\bf A \cdot A = |A|^2 $.

### Algebraic Definition
There is another perspective on the scalar product, which is for two vectors with components:
```{math}
{\bf A} &=&\, a_x\,\hat{\bf x} + a_y\,\hat{\bf y} + a_z\,\hat{\bf z} = \begin{pmatrix}
 a_x \\
 a_y \\
 a_z 
\end{pmatrix} \\
{\bf B} &=&\, b_x\,\hat{\bf x} + b_y\,\hat{\bf y} + b_z\,\hat{\bf z} = \begin{pmatrix}
 b_x \\
 b_y \\
 b_z 
\end{pmatrix}
```
then the dot product can be found by:
```{math}
{\bf A \cdot B} = a_x\,b_x + a_y\,b_y + a_z\,b_z= \sum_{i=1}^3 a_i\,b_i
```
where the last expression uses the index notation.

### Properties of the Dot Product

The dot product of two vectors $\bf a,\, b$ have the following mathematical properties:

- <b>Commutative:
$\mathbf {a} \cdot \mathbf {b} = \mathbf {b} \cdot \mathbf {a}$

- Distributive over Vector Addition:
$  \mathbf {a} \cdot (\mathbf {b} +\mathbf {c} )=\mathbf {a} \cdot \mathbf {b} +\mathbf {a} \cdot \mathbf {c}$

- Bilinear:
$ \mathbf {a} \cdot (r\mathbf {b} +\mathbf {c} )=r(\mathbf {a} \cdot \mathbf {b} )+(\mathbf {a} \cdot \mathbf {c} )$

- Scalar Multiplication:
$ (c_{1}\mathbf {a} )\cdot (c_{2}\mathbf {b} )=c_{1}c_{2}(\mathbf {a} \cdot \mathbf {b} )$

- Orthogonal:</b>
Two non-zero vectors $\bf a,\, b$ are orthogonal if and only if $\bf a \cdot b = 0$.

## Vector Product / Cross Product
### Geometric Definition
Unsurprisingly we can also make a vector product that results in a vector, rather than a scalar.  This <b>Vector Product</b>, also known as the <b>Cross Product</b>,
can be constructed from the basis vectors:
```{math}
\hat{\bf x} \times \hat{\bf y} &=&\, \hat{\bf z} \\
\hat{\bf y} \times \hat{\bf z} &=&\, \hat{\bf x} \\
\hat{\bf z} \times \hat{\bf x} &=&\, \hat{\bf y} 
```
In general however we write the cross product between two vectors as a new vector, normal to the other two (following the right hand rule), as depicted in 
{numref}`VectorProduct`.

```{figure} ../figures/VectorProduct.png
---
name: VectorProduct
---

<b>Left Pane</b>: Graphical depiction of the cross product, producing a vector $\bf a \times b$ which is normal to both $\bf a,\, b$,
<b>Right Pane</b>: The area of the parallogram produced by vectors $\bf a,\, b$ is found from $|\bf a \times b|$
```
This means that if vectors span an angle $\theta$, then we need to resolve the perpendicular component:
```{math}
{\bf a \times b} = {\bf |a||b|}\sin(\theta)\,\hat{\bf n}
```
where $\hat{\bf n}$ is vector which is normal to both $\bf a,\, b$.

Because the cross product follows the right hand rule for axes, it is anti-commutative:
```{math}
\bf a \times b = -\,b \times a
```
We also find the at the cross product is distributive over addition,

```{math}
\mathbf {a} \times (\mathbf {b} +\mathbf {c} )=(\mathbf {a} \times \mathbf {b} )+(\mathbf {a} \times \mathbf {c} )
```

and compatible with scalar multiplication:

```{math}
(r\,\mathbf {a} )\times \mathbf {b} =\mathbf {a} \times (r\,\mathbf {b} )=r\,(\mathbf {a} \times \mathbf {b} )
```

Likewise since the vector magnitude depends on the angle between the two vectors, if we cross a vector with itself (or another vector that is parallel / anti-parallel), 
the answer is zero:

```{math}
\bf a \times a = 0
```
where $\bf 0$ is a zero vector.

### Algebraic Definition
Once again there is also an algebraic route to the cross product, this is based on the vector components.  

Since the cross product is distributive over addition we find that:

```{math}
 \mathbf{a}\times\mathbf{b} = {} &(a_x\,\hat{\bf x} + a_y\,\hat{\bf y} + a_z\,\hat{\bf z}) \times (b_x\,\hat{\bf x} + b_y\,\hat{\bf y} + b_z\,\hat{\bf z})\\
                            = {} &a_x\,b_x(\hat{\bf x} \times \hat{\bf x}) + a_x\,b_y(\hat{\bf x} \times \hat{\bf y}) + a_x\,b_z(\hat{\bf x} \times \hat{\bf z}) + {}\\
                                 &a_y\,b_x(\hat{\bf y} \times \hat{\bf x}) + a_y\,b_y(\hat{\bf y} \times \hat{\bf y}) + a_y\,b_z(\hat{\bf y} \times \hat{\bf z}) + {}\\
                                 &a_z\,b_x(\hat{\bf z} \times \hat{\bf x}) + a_z\,b_y(\hat{\bf z} \times \hat{\bf y}) + a_z\,b_z(\hat{\bf z} \times \hat{\bf z})\\
```
If we follow through our rules for computing the cross products of basis vectors, we find this simplifies to:
```{math}
 \mathbf{a}\times\mathbf{b} = {} &a_x\,b_x(0) + a_x\,b_y(\hat{\bf z}) + a_x\,b_z(-\hat{\bf y}) + {}\\
                                 &a_y\,b_x(-\hat{\bf z}) + a_y\,b_y(0) + a_y\,b_z(\hat{\bf x}) + {}\\
                                 &a_z\,b_x(\hat{\bf y}) + a_z\,b_y(-\hat{\bf x}) + a_z\,b_z(0)\\
							= {} &(a_y\,b_z - a_z\,b_y)\hat{\bf x} + (a_z\,b_x - a_x\,b_z)\hat{\bf y} + (a_x\,b_y - a_y\,b_x)\hat{\bf z} 
```

Finding the cross product can also be found using a matrix determinant:

```{math}
 \mathbf{a}\times\mathbf{b} = \begin{vmatrix}
 \hat{\bf x} & \hat{\bf y} & \hat{\bf z} \\
 a_x & a_y & a_z \\
 b_x & b_y & b_z
\end{vmatrix}
```
which by the cofactor method along the first row produces:

```{math}
 \mathbf{a}\times\mathbf{b} &=&\, \begin{vmatrix}
 a_y & a_z \\
 b_y & b_z
\end{vmatrix}\hat{\bf x} - \begin{vmatrix}
 a_x & a_z \\
 b_x & b_z
\end{vmatrix}\hat{\bf y} + \begin{vmatrix}
 a_x & a_y 
 b_x & b_y 
\end{vmatrix}\hat{\bf z} \\
&=&\, (a_y\,b_z - a_z\,b_y)\hat{\bf x} - (a_x\,b_z - a_x\,b_z)\hat{\bf y} + (a_x\,b_y - a_y\,b_x)\hat{\bf z} 
```
which we find are equivalent definitions.

## Triple Vector Products
Now that we have multiplcation of two vectors formalised, we find that multiplying three vectors also leads to some further geometric and algebraic ideas.

### Triple Scalar Product
Here we have three vectors $\bf a, \,b,\,c$ composed so that
```{math}
\bf a \cdot (b \times c)
```
since the combination of $\bf b \times c$ produces a vector, which we can then do a scalar multiplcation with $\bf a$.  Therefore this produces a scalar result.

Geometrically this is related to the parallepiped, as depicted in {numref}`parallepiped`, where the magnitude of this result is the shapes volume:
```{math}
V = |{\bf a \cdot (b \times c)}|
```

```{figure} ../figures/parallepiped.png
---
name: parallepiped
---
A parallepiped, composed from three vectors $\bf a, \,b,\,c$.
```

We can also evaluate the triple scalar product from a matrix determinant:
```{math}
 {\bf a \cdot (b \times c)} = \mathbf{a}\times\mathbf{b} = \begin{vmatrix}
 a_x & a_y & a_z \\
 b_x & b_y & b_z \\
 c_x & c_y & c_z \\
\end{vmatrix}
```

### Triple Vector Product
Unsurprisingly we can also find an expression for the vector product between three vectors $\bf a, \,b,\,c$:
```{math}
\bf a \times (b \times c) = (a\cdot c)b - (a \cdot b)c
```
which is useful particularly when we want to work out results like:
```{math}
\bf \nabla \times \nabla \times A = \nabla(\nabla \cdot A) - (\nabla\cdot \nabla)A = \nabla(\nabla \cdot A) - \nabla^2 A
```
which will be useful later!