# Line Integrals

If we apply the total differential expression:
```{math}
:class:  notice
\nabla f \cdot \mathrm{d}{\bf r} = \mathrm{d}f
```
and now try to integrate this:
```{math}
\int \,\mathrm{d}f = \int\,\nabla f \cdot \mathrm{d}{\bf r}
```
we see that this can be thought of doing the scalar product between two vectors ${\bf V}$ and $\mathrm{d}{\bf r}$ 
before finally integrating:

```{math}
\int {\bf V}\cdot \mathrm{d}{\bf r}
```

We call integrals of this kind **line integrals** or otherwise called **contour integrals**.  


````{admonition} Definition
We can define:

```{math}
\int_{\mathcal{C}} {\bf F(r)} \cdot \mathrm{d}{\bf r}
```

which we call a *vector line integral*.  This is an integral through coordinate space along a contour, here denoted $\mathcal{C}$.

For some vector field:
```{math}
{\bf F(r)} = \hat{\bf x}\,P({\bf r}) +\hat{\bf y}\,Q({\bf r}) +\hat{\bf z}\,R({\bf r})
```
this simplifies to:
```{math}
\int_{\mathcal{C}} {\bf F(r)} \cdot \mathrm{d}{\bf r} = \int_{\,\mathcal{C}} \left(F\,\mathrm{d}x + G\,\mathrm{d}y + R\,\mathrm{d}z \right)
```
We notice that that this is a scalar, found from scalar product of $\bf F$ with the differential line element $\mathrm{d}{\bf r}$ along the path $\mathcal{C}$.

We can also think about a *scalar line integral*:

```{math}
\int_{\mathcal{C}} f(r)\, \mathrm{d}s
```

where $\mathrm{d}s$ is the infinitesimal arc length element, which is given by:
```{math}
\mathrm{d} {\bf r} &= \hat{\bf x}\,\mathrm{d}x +\hat{\bf y}\,\mathrm{d}y +\hat{\bf z}\,\mathrm{d}z\\
\mathrm{d} s &= |\mathrm{d} {\bf r}|= \sqrt{\mathrm{d}x^2 + \mathrm{d}y^2 + \mathrm{d}z^2}
``` 

If we pick a closed path through the vector field, we call this a **loop integral**:

```{math}
\oint_{\mathcal{C}} {\bf F(r)} \cdot \mathrm{d}{\bf r}
```
````

What does a line integral actually do? We can think about moving along some line which we denoted $\mathcal{C}$, broken up
into infintesimal sections $\mathrm{d} r$, as depicted in {numref}`lineintegral`.  

```{figure} ../figures/lineintegral.png
---
name: lineintegral
---
Ilustration of a line integral, with $\int_{\mathcal{C}} {\bf F}({\bf r})\cdot \mathrm{d}{\bf r}$
```




## Parameterising and evaluating integrals

Whilst our expressions for line integrals are powerful, they also do not really explain how we can go about *calculating* integrals.  
To see how we can go about this, we need to think about how to parameterise our paths (contours) through coordinate space.  Once 
we have a good way to think about parameterising our contours, we will aim to use a change of variable to evaluate the integrals.


### Parameterising contours

Lets think about different contours between the points $A(-1,\,1)$ and $B(1,\,1)$, as depicted in {numref}`linecontours`.


```{figure} ../figures/linecontours.png
---
name: linecontours
---
Ilustration of a three contours $C_1,\, C_2,\, C_3$ between the points $A(-1,\,1)$ and $B(1,\,1)$.
```

If we travel along contour $C_1$ which follows $y = x^2$ for $-1\leq x \leq 1$, whilst we can also travel along contour $C_2$ which takes 
$y = 1$ for $-\ leq x \leq 1$ and $C_3$ which is a contour with theopposite direction.  These sorts of contours are problematic 
to describe using just $x,\,y$ variables and the orientation of the contours is also not well captured.  

We can use some *standard* parameterisation schemes to capture all the relevant details here:

- For straight lines over points $(x_0,\, y_0,\, z_0)$ to $(x_1,\, y_1,\, z_1)$, we can parameterise this contour using:
```{math}
x &= x_1 (1-t) + x_1 t\\
y &= y_1 (1-t) + y_1 t\\
z &= z_1 (1-t) + z_1 t
```
where $0 \leq t \leq 1$.  

````{admonition} Worked example
:class: seealso
For the contour $C_2$ between $A(-1,\,1)$ and $B(1,\,1)$, we can see that with $0 \leq t \leq 1$:
```{math}
x &= 2t-1 \\
y &= 1
```

and for the contour $C_3$ between $B(1,\,1)$ and $A(-1,\,1)$, we can see that with $0 \leq t \leq 1$:
```{math}
x &= 1-2t \\
y &= 1
```

````

- For functions $y = f(x)$ over range $a \leq x \leq b$, i.e. over $(a,\, f(a)) \rightarrow b,\, f(b)$, we can parameterise 
using $a \leq t \leq b$:
```{math}
y &= f(t) \\
x &= t
```
We note that here we can also go in the opposite orientation $(b,\, f(b)) \rightarrow (a,\, f(a))$ by switching $x = t \rightarrow x = -t$.
````{admonition} Worked example
:class: seealso
For the contour $C_1$ between $A(-1,\,1)$ and $B(1,\,1)$, we can see that with $-1 \leq t \leq 1$:
```{math}
y &= t^2 \\
x &=t
```
and in order to reverse the contour direction we can just switch $x = t \rightarrow x = -t$.  
````

- For a circular path (or circular arc) between points $(a,\, b)$ and $(c,\, d)$ such that $a^2 + b^2 = c^2 + d^2 = r^2$, 
we can parameterise using $ t_i \leq t \leq t_f$:
```{math}
x &= r\,\cos(t) \\
y &= r\,\sin(t)
``` 


For scalar line integrals, the direction we travel along the contour does not change the result:
```{math}
\int_{-\mathcal{C}}f\,\mathrm{d}s = \int_{\mathcal{C}} f\,\mathrm{d}s
```
this is because the length element $\mathrm{d}s = |\mathrm{d}{\bf r}|$ is taken from the magnitude of a vector, so any 
changes in the orientation are washed out in this.

For vector line integrals, the direction we travel along the contour **does** change the result:
```{math}
\int_{-\mathcal{C}} {\bf F}\cdot \,\mathrm{d}{\bf r} = -\int_{\mathcal{C}} {\bf F}\cdot \,\mathrm{d}{\bf r} 
```
and given that for $Q = R = 0$, we can do a line integral in $x$, or similarly for $y$ $z$:
```{math}
\int_{-\mathcal{C}} P({\bf r})\,\mathrm{d}x &= -\int_{\mathcal{C}} P({\bf r})\,\mathrm{d}x\\
\int_{-\mathcal{C}} Q({\bf r})\,\mathrm{d}y &= -\int_{\mathcal{C}} Q({\bf r})\,\mathrm{d}y\\
\int_{-\mathcal{C}} R({\bf r})\,\mathrm{d}z &= -\int_{\mathcal{C}} R({\bf r})\,\mathrm{d}z
```


### Evaluating line integrals
If we can find one variable $t$ which will effectively parameterise the path through the (scalar or vector) field, then our 
expression simplify:
```{math}
\int_{\mathcal{C}} f({\bf r})\,\mathrm{d}s = \int_{t=a}^{t=b} \left(f({\bf r}(t))\,\frac{\mathrm{d}s}{\mathrm{d}t}\right)\,\mathrm{d}t \\
\int_{\mathcal{C}} {\bf F}({\bf r})\cdot \mathrm{d}{\bf r} = \int_{t=a}^{t=b} \left({\bf F}({\bf r}(t))\cdot\frac{\mathrm{d}{\bf r}}{\mathrm{d}t} \right)\,\mathrm{d}t
```
where the infinitesimal coordinate vector derivatives are given by:
```{math}
\frac{\mathrm{d}{\bf r}}{\mathrm{d}t} &= \hat{\bf x}\,\frac{\mathrm{d}x}{\mathrm{d}t} + \hat{\bf y}\,\frac{\mathrm{d}y}{\mathrm{d}t} + \hat{\bf z}\,\frac{\mathrm{d}z}{\mathrm{d}t}\\
\frac{\mathrm{d}s}{\mathrm{d}t} &= \left|\frac{\mathrm{d}{\bf r}}{\mathrm{d}t}  \right| = \sqrt{\left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^2 + \left(\frac{\mathrm{d}y}{\mathrm{d}t}\right)^2 + \left(\frac{\mathrm{d}z}{\mathrm{d}t}\right)^2}
```

````{admonition} Worked examples
:class: seealso
1\. Evaluate the scalar line integral $\int_{\mathcal{C}} (x^2 + y^2)\,\mathrm{d}s$ over the contours:

a\. A straight line linking $(1,\,0) \rightarrow (-1,\,0)$.

Here we can use the straight line parametrisation for $0 \leq t \leq 1$:
```{math}
x &= x_0(1-t) + x_1 t = 1-t - t = 1-2t \\
y &= y_0(1-t) + y_1 t = 0
```

Then we can rewrite the integrand in this parameterisation:
```{math}
x^2 + y^2 &= (1-2t)^2 + 0^2 = 1 - 4t + 4t^2 \\
\frac{\mathrm{d}x}{\mathrm{d}t} &= -2\\
\frac{\mathrm{d}y}{\mathrm{d}t} &= 0\\
\frac{\mathrm{d}s}{\mathrm{d}t} = \sqrt{(-2)^2 + 0^2} = 2
```
Finally lets evaluate the integral:
```{math}
\int_0^1 2(1 - 4t + 4t^2)\,\mathrm{d}t = \left[2t - 4t^2 + \frac{8}{3}t^3\right]_0^1 = \frac{2}{3}
```

b\. A semi-circular arc linking $(1,\,0) \rightarrow (-1,\,0)$ in the top half of the plane.

Here we can use polar coordinates, with $r=1$
```{math}
x &= \cos(\theta) \\
y &= \sin(\theta)
```
with $0 \leq \theta \leq \pi$.  

Rewriting the integrand in this parameterisation:
```{math}
x^2 + y^2 &= (\cos(\theta))^2 + (\sin(\theta))^2 = 1 \\
\frac{\mathrm{d}x}{\mathrm{d}t} &= -\sin(\theta)\\
\frac{\mathrm{d}y}{\mathrm{d}t} &= \cos(\theta)\\
\frac{\mathrm{d}s}{\mathrm{d}t} &= \sqrt{(-\sin(\theta))^2 + (\cos(\theta))^2} = 1
```

Finally lets evaluate the integral:
```{math}
\int_0^\pi (1)\,(1)\mathrm{d}\theta = \Big[\theta\Big]_0^\pi = \pi
```

We can picture this system by plotting the surface $z = x^2 + y^2$:

```{figure} ../figures/parabola.png
---
name: parabolasurface
---
Ilustration of a parabolic surface $z = x^2 + y^2$ with the contours in (a) and (b) shown.
```
We can see that the distance for contour (a) is shorter than for contour (b) and since the scalar function is $x^2$ along 
both contours, the integral is the weighted sum of $x^2$ along each of these lengths, hence it makes sense that $I_a < I_b$.



2\. Evaluate the vector line integral $\int_{\mathcal{C}} {\bf F}\cdot \mathrm{d}{\bf r}$ for ${\bf F} = xz\,\hat{\bf x} - yz\,\hat{\bf z}$ 
along the line linking $(-1,\,2,\,0) \rightarrow (3,\,0,\,1)$.

````


````{admonition} Further worked examples
:class: seealso, dropdown
1\. Find the line integral of the vector field:
```{math}
{\bf G(r)} = \begin{pmatrix} xy\\ -y^2 \end{pmatrix}
```
over the following contours:

a\. 
- Straight line path $(0,\,0) \rightarrow (1,\, 2)$

The function following by this path will be $y = 2x,\, x \in [0, 1]$, so:

```{math}
{\bf r}(x) = \begin{pmatrix} x \\ 2x \end{pmatrix}
```

Thus ${\bf G}({\bf r}(x))$ will be:

```{math}
{\bf G}({\bf r}(x)) = \begin{pmatrix} 2x^2 \\ -4x^2 \end{pmatrix}
```

and ${\bf r'}(x)$ is given by:

```{math}
{\bf r}'(x) = \begin{pmatrix} 1 \\ 2 \end{pmatrix}
```

so the line integral is found by:

```{math}
I &=  \int_{\mathcal{C}} {\bf G}(r) \cdot \mathrm{d}{\bf r} = \int_0^1 {\bf G}({\bf r}(t)) \cdot {\bf r}'(t)\,\mathrm{d}t = 
\int_0^1 \begin{pmatrix} 2x^2 \\ -4x^2 \end{pmatrix} \cdot \begin{pmatrix} 1 \\ 2 \end{pmatrix} \mathrm{d}x \\
&=  \int_0^1 \left( 2x^2 - 8x^2 \right)\,\textrm{d}x = -\int_0^1 6x^2 \,\textrm{d}x = \Big[ -\frac{6}{3}x^3\Big ]_0^1 = -2
```

- Curved path following $y = x^2$ for $0 \leq x \leq 1$


```{math}
{\bf r}(x) = \begin{pmatrix} x \\ x^2 \end{pmatrix}
```

Thus ${\bf G}({\bf r}(x))$ will be:

```{math}
{\bf G}({\bf r}(x)) = \begin{pmatrix} x^3 \\ -x^4 \end{pmatrix}
```

and ${\bf r'}(x)$ is given by:

```{math}
{\bf r}'(x) = \begin{pmatrix} 1 \\ 2x \end{pmatrix}
```

so the line integral is found by:

```{math}
I &=  \int_{\mathcal{C}} {\bf G}(r) \cdot \mathrm{d}{\bf r} = \int_0^1 {\bf G}({\bf r}(t)) \cdot {\bf r}'(t)\,\mathrm{d}t = 
\int_0^1 \begin{pmatrix} x^3 \\ -x^4 \end{pmatrix} \cdot \begin{pmatrix} 1 \\ 2x \end{pmatrix} \mathrm{d}x \\
&=  \int_0^1 \left( x^3 - 2x^5 \right)\,\textrm{d}x = \Big[\frac{1}{4}x^4 - \frac{1}{3}x^6 \Big ]_0^1 = -\frac{1}{12}
```

- Curved path following $y = x^{1/2}$ over $0 \leq x \leq 1$


```{math}
{\bf r}(x) = \begin{pmatrix} x \\ x^{1/2} \end{pmatrix}
```

Thus ${\bf G}({\bf r}(x))$ will be:

```{math}
{\bf G}({\bf r}(x)) = \begin{pmatrix} x^{3/2} \\ -x \end{pmatrix}
```

and ${\bf r'}(x)$ is given by:

```{math}
{\bf r}'(x) = \begin{pmatrix} 1 \\ \frac{1}{2} x^{-1/2} \end{pmatrix}
```

so the line integral is found by:

```{math}
I &=  \int_{\mathcal{C}} {\bf G}(r) \cdot \mathrm{d}{\bf r} = \int_0^1 {\bf G}({\bf r}(t)) \cdot {\bf r}'(t)\,\mathrm{d}t = 
\int_0^1 \begin{pmatrix} x^{3/2} \\ -x \end{pmatrix} \cdot \begin{pmatrix} 1 \\ \frac{1}{2} x^{-1/2} \end{pmatrix} \mathrm{d}x \\
&=  \int_0^1 \left( x^{3/2} - \frac{1}{2}x^{1/2} \right)\,\textrm{d}x = \Big[\frac{2}{5}x^{5/2} - \frac{1}{3}x^{3/2} \Big ]_0^1 = \frac{1}{15}
```
````

## Conservative Vector Fields

There is an important class of vector fields, known as **conservative** vector fields, for which line integrals do not depend on 
which path is taken from rA to rB, and for which all loop integrals are zero.  We see that our example 
```{math}
{\bf G(r)} = xy\hat{\bf x} - y^2 \hat{\bf y}
```
is not conservative since the line integrals along different paths from $(0,\, 0)$ to $(1,\,2)$ gave different values.  

Whist it is not possible show that for all paths ${\bf r}_A \rightarrow {\bf r}_B$. the line integral gives the same value, simply because there exist
infinitely many possible paths. Instead we can use an equivalent definition of conservative fields:

```{math}
\text{Vector Field}\,{\bf G(r)}\,\text{is conservative} \Longleftrightarrow \exists\,\phi({\bf r}),\, 
\text{s.t.}\,{\bf G} = \nabla \phi
```

where $\phi{(\bf{r})$ is a scalar field.  

To show that a vector field which satisfies this condition is conservative, lets think about a line integral taken along a path 
${\bf r}_A \rightarrow {\bf r}_B$, which we have parameterised by the $t \in [a,\, b]$, where ${\bf}(t=a) = {\bf r}_A$ and ${\bf}(t=b) = {\bf r}_B$
```{math}
I &=  \int_{\mathcal{C}} {\bf G(r)}\cdot \mathrm{d}{\bf r} = \int_{t=a}^{t=b} {\bf G(r)}\cdot {\bf r}'(t) \mathrm{d}t\\
&=  \int_{t=a}^{t=b} (\nabla \phi({\bf r}(t)))\cdot {\bf r}'(t) \mathrm{d}t
```
However using the fact that the total differential $\mathrm{d}\phi = \nabla \phi \cdot \mathrm{d}{\bf r}$, 
then $\mathrm{d}\phi/\mathrm{d}t = \nabla \phi \cdot \mathrm{d}{\bf r}'$ and thus:
```{math}
I &=  \int_{t=a}^{t=b} \frac{\mathrm{d}}{\mathrm{d}t}\phi({\bf r}(t)) \mathrm{d}t  \\
&=  \Bigg[ \phi({\bf r}(t)) \Bigg]_{t=a}^{t=b} = \phi({\bf r_B}) - \phi({\bf r_A})
```
which means that the details of the line integral only depend on the start and finish of the contour, not the path taken.  Likewise if we have a 
conservative vector field and a closed loop integral, then ${\bf r_A} = \bf{r_B}$ and so the integral becomes zero.

For a three dimensional vector field defined on a domain that is <em>simply connected</em> (that is contains no holes) there exists another 
equivalent definition of conservativeness:
```{math}
\text{Vector Field}\,{\bf G(r)}\,\text{is conservative} \Longleftrightarrow \nabla \times {\bf G} = 0
```

````{admonition} Worked example
Is the vector ${\bf G(r)} = 2xy \hat{\bf x} + (x^2 - 2y)\hat{\bf y} + \hat{\bf z}$ is conservative?

Since G is defined on the entire three-dimensional space $\mathbb{R}^3$, we can make use the curl criterion, hence
```{math}
\nabla \times {\bf G} &= 
\begin{pmatrix} \partial_y G_z - \partial_z G_y \\ \partial_z G_x - \partial_x G_y \\ \partial_y G_x - \partial_x G_y\end{pmatrix}\\
&=  \begin{pmatrix} 0 - 0 \\ 0 - 0 \\ 2x - 2x\end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
```
Hence since the curl of $\bf G$ is zero, $\bf G$ is a conservative vector field, so it must be possible to find a potential $\phi({\bf r})$ such 
that ${\bf G} = \nabla \phi$.  This means that:

- $\partial_x \phi = 2xy$
- $\partial_x \phi = x^2-2y$
- $\partial_x \phi = 1$

Integrating each of these in turn we find that:

- $\phi = x^2y + f(y,\,z)$
- $\phi = x^2y - y^2 + g(x,\,z)$
- $\phi = z + h(z,\,y)$

Since these all need to be consistent, we find that 
```{math}
\phi(x,\,y,\,z) = x^2y - y^2 + z + C
```
up to an additive constant $C \in \mathbb{C}$.  We notice that for the line integral this constant drops out of the calculation anyway.

````