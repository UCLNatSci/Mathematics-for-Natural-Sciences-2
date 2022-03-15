# Bifurcation analysis

In this section we will start to examine systems with more than one equilibrium point. We will also allow that the systems may contain parameters and we will consider how the number of equilibrium points and their stability changes as parameter values are varied.

To assist our analysis we will introduce an analytic method for classifying equilibrium points of nonlinear systems (linearisation). We will also introduce the idea of a *bifurcation diagram* as a way of representing our findings.

## Linearisation

We now consider a general first order coupled autonomous system involving two dependent variables. The problem may be written in the following form, in which the arbitrary functions $f$ and $g$ may be nonlinear:

\begin{align}
\dot{x} & = f(x,y)\\
\dot{y} & = g(x,y)
\end{align}

We will assume that the system has an equilibrium point $(x_0,y_0)$ satisfying

\begin{equation}
f(x_0,y_0)=g(x_0,y_0)=0.
\end{equation}

```{admonition} Finding equilibria
:class: theorem
It is not always possible to find all equilibrium points by hand if $f,g$ are not both simple algebraic functions. In such cases a numerical root-finding algorithm such as Newton-Raphson or bisection algorithm could be employed.
```

To examine the nature of the equilibrium point, we will expand the functions $f$ and $g$ using Taylor series centred at $(x_0,y_0)$. Since we are interested in the behaviour of solution trajectories in the neighbourhood of the point, we can linearise the expansion:

\begin{align}
f(x,y) & = f(x_0,y_0) +(x-x_0)\frac{\partial f}{\partial x}\biggr|_{(x_0,y_0)}+(y-y_0)\frac{\partial f}{\partial y}\biggr|_{(x_0,y_0)}+\dots\\
g(x,y) & = g(x_0,y_0) +(x-x_0)\frac{\partial g}{\partial x}\biggr|_{(x_0,y_0)}+(y-y_0)\frac{\partial g}{\partial y}\biggr|_{(x_0,y_0)}+\dots\\
\end{align}

We can further simplify by making the variable substitution $X=(x-x_0)$, $Y=(y-y_0)$ to obtain

\begin{align}
\dot{X} &= X\frac{\partial f}{\partial x}\biggr|_{(x_0,y_0)}+Y\frac{\partial f}{\partial y}\biggr|_{(x_0,y_0)}\\
\dot{Y} &= X\frac{\partial g}{\partial x}\biggr|_{(x_0,y_0)}+Y\frac{\partial g}{\partial y}\biggr|_{(x_0,y_0)}
\end{align}

 This is a first order linear system in two unknowns, with equilibrium point at $(X,Y)=(0,0)$. We can write it in matrix form, just as we did in the previous chapters:

\begin{equation}
\frac{\mathrm{d}}{\mathrm{d}t}\begin{bmatrix}X\\Y\end{bmatrix} = J(x_0,y_0)\begin{bmatrix}X\\Y\end{bmatrix}, \qquad J(x_0,y_0)= \begin{bmatrix}\frac{\partial f}{\partial x} & \frac{\partial f}{\partial y}\\ \frac{\partial g}{\partial x} & \frac{\partial g}{\partial y}\end{bmatrix}_{(x_0,y_0)}
\end{equation}

The coefficient matrix $J(x,y)$ is called the Jacobian. Finding the eigenvalues and eigenvectors of the Jacobian at the stationary point tells us its stability and allows us to plot the shape of the solution trajectories.

### Example: Nonlinear pendulum

Recall the equation for the undamped pendulum that was given in the {numref}`undamp-pend` :

\begin{align}
\dot{x} & = y && =f(x,y)\\
\dot{y} & = -\omega^2 \sin(x) && =g(x,y)
\end{align}

Equilibrium points:
\begin{equation}
f=g=0 \qquad \Rightarrow \quad x=n\pi, \ n\in\mathbb{Z}
\end{equation}

Evaluate the Jacobian:

\begin{equation}
J(x,y) = \begin{bmatrix}\frac{\partial f}{\partial x} & \frac{\partial f}{\partial y}\\ \frac{\partial g}{\partial x} & \frac{\partial g}{\partial y}\end{bmatrix} = \begin{bmatrix}0 & 1\\ -\omega^2\cos(x) & 0\end{bmatrix}
\end{equation}

We can separate treatment of the equilibrium points according to even and odd $n$.

````{panels}
:column: col-6
:card: border-2
At $x=n\pi$ ($n$ even)
^^^
$J(2m\pi,0) = \begin{bmatrix}0 & 1\\-\omega^2 & 0 \end{bmatrix}$

Eigenvalues: $\lambda=\pm i\omega$ (centres)
---
At $x=n\pi$ ($n$ odd)
^^^
$J((2m+1)\pi,0) = \begin{bmatrix}0 & 1\\\omega^2 & 0 \end{bmatrix}$

Eigenvalues: $\lambda=\pm \omega$ (saddles)
````

This agrees with the results we found earlier by plotting the vector field and solution trajectories.

```{exercise}
The equation of motion for the damped pendulum is given by
\begin{align*}
\dot{x}& = y\\
\dot{y} & = -\omega^2 \sin(x)-ky \\
\end{align*}

Find and classify the equilibrium points, using the linearisation technique.
```

```{toggle}
**Solution**

The equilibrium points are at $x=n\pi$, as for the stable case.

For $n$ even the eigenvalues are $\lambda=-k\pm  i\sqrt{\omega^2-k^2}$ (stable spirals)

For $n$ odd the eigenvalues are $\lambda=-k\pm \sqrt{k^2+\omega^2}$ (saddles)
```

## Differential equations with a parameter

We now consider an example of a system featuring a parameter. We looked at some examples of this sort in previous exercises by trying a few different parameter values. For example,
* {numref}`ex-222` featured parameters $c,k$
* {numref}`ex-235` featured parameter $c$

We will now attempt to sytematically study the location and nature of any equilibria for different parameter values.

### Example: A pitchfork bifurcation

To illustrate the approach, let us consider the following system that features parameter $\mu$ :

\begin{align}
\dot{x} &=y &&=f(x,y)\\
\dot{y}&=\mu x - y - x^3-x^2 y &&=g(x,y)
\end{align}

Equilibrium points are found at $(0,0)$, $(\pm\sqrt{\mu},0)$, with the latter points existing only for $\mu\geq 0$. To classify the equilibrium points we use the Jacobian, which is given by

\begin{equation}
J(x,y)=\begin{bmatrix}0 & 1\\ \mu-3x^2-2xy & -1-x^2\end{bmatrix}
\end{equation}

````{panels}
:column: col-6
:card: border-2
At $(0,0)$ the eigenvalues are
^^^
\begin{equation*}
\lambda = \frac{1\pm \sqrt{1+4\mu}}{2}
\end{equation*}

This equilibrium point is:
* stable spiral for $\mu<-1/4$
* stable inflected node at $\mu=-1/4$
* stable node for $-1/4<\mu<0$
---
At $(\pm\sqrt{\mu},0)$ the eigenvalues are
^^^
\begin{equation*}
\lambda =\frac{-(1+\mu)\pm \sqrt{\mu^2-6\mu+1}}{2}
\end{equation*}

This equilibrium point is:
* stable node for $0<\mu<3-2\sqrt{2}$
* stable inflected node for $\mu=3\pm2\sqrt{2}$
* stable spiral for $3-2\sqrt{2}<\mu<3+2\sqrt{2}$
* stable node for $\mu>2+2\sqrt{2}$
````

This information can be represented on a bifurcation diagram, in which we represent the parameter $\mu$ on the horizontal axis and the $x$-location of the equilibrium point(s) on the vertical axis. A solid line is used to represent a stable equilibrium and a dashed line is used to represent an unstable equilibrium.

```{figure} ../figures/pitchfork1.png
---
name: pitchfork
---
```

At $\mu=0$ the stable equilibrium at $x=0$ becomes unstable and from it emerges two stable equilibria. This type of bifurcation is called a "pitchfork bifurcation".


```{admonition} Bifurcation
:class: theorem
A *bifurcation* of an equilibrium point is a change in the number or stability of equilibrium points in a differential equation as a parameter changes its value.
```

## Classifying bifurcations

In this subsection we will look at some of the most commonly encountered types of bifurcation. The example systems used to illustrate feature only a single dependent variable, so we do not need to use the Jacobian to classify. We can simply consider the direction of the change vectors either side of any equilibrium points, as we did in {numref}`motv-exam`.

### Pitchfork bifurcation

A pitchfork bifurcation occurs when a system transitions from one equilibrium point to three.

* In a supercritical pitchfork bifurcation the transition to three points occurs as the parameter value is increased.
* In a subcritical pitchfork bifurcation the transition to three points occurs as the parameter value is decreased.

Illustrations of both types are shown below. In these examples the parameter $\mu$ is shown on the horizontal axis and the equilibrium point is shown on the vertical axis.  


````{panels}
:column: col-6
:card: border-2
**Supercritical case**
^^^
\begin{equation*}
\dot{x}=\mu x -x^3
\end{equation*}

```{figure} ../figures/pitchfork2.png
:scale: 60%
```
---
**Subcritical case**
^^^
\begin{equation*}
\dot{x}=\mu x +x^3
\end{equation*}

```{figure} ../figures/pitchfork3.png
:scale: 60%
```
````

```{exercise}
Pick one of the two examples above and sketch change vectors on the diagram.
```

````{toggle}
**Solution:**

The plot below is for the case $\dot{x}=\mu x +x^3$

```{figure} ../figures/pitchfork4.png
:scale: 60%
```
For example, consider that for $\mu<0$ the shape of the change function is as shown below. The change function is positive for $-\sqrt{\mu}<x<0$, negative $x<-\sqrt{\mu}$, etc.

```{figure} ../figures/schematic.png
```

````

### Saddle node bifurcation

A saddle node bifurcation or fold bifurcation occurs when two equilibrium points coalesce and annihilate each other. The supercritical and subcritical cases are shown below.

````{panels}
:column: col-6
:card: border-2
**Supercritical case**
^^^
\begin{equation*}
\dot{x} = \mu -x^2
\end{equation*}

```{figure} ../figures/saddlenode2.png
:scale: 60%
```
---
**Subcritical case**
^^^
\begin{equation*}
\dot{x} = \mu +x^2
\end{equation*}

```{figure} ../figures/saddlenode3.png
:scale: 60%
```
````

```{exercise}
Show that the following two-dimensional problem has a saddle-node bifurcation at $\mu=0$:

\begin{align*}
\dot{x}&=\mu-x^2\\
\dot{y}&=-y
\end{align*}

```

````{toggle}
**Solution**

Equilibrium points $(\pm\sqrt{\mu},0)$, for $\mu\geq 0$

Jacobian: $\begin{bmatrix}-2x & 0\\0&-1\end{bmatrix}$

Eigenvalues: $\lambda=-1,\mp\sqrt{\mu}$

The point $(0,-\sqrt{\mu})$ is a saddle node

The point $(0,\sqrt{\mu})$ is a stable node
````

### Transcritical bifurcation

A transcritical bifurcation is characterised by a system with one stable equilibrium point and one unstable equilibrium point, which exchange stability when they collide.

\begin{equation}
\dot{x}=\mu x - x^2
\end{equation}

```{figure} ../figures/transcritical2.png
:scale: 60%
```

### Hopf bifurcation

A Hopf bifurcation occurs when a parameter in the system creates a change from a stable equilibrium point to an unstable equilibrium point together with a periodic solution that takes the form of a *limit cycle*. We have already seen illustrated examples of limit cycles in in {numref}`ex-222` and {numref}`ex-235`.

```{admonition} Limit cycle
:class:theorem
A limit cycle is an isolated periodic solution, unlike a centre which has a family of periodic solutions.

* For a stable limit cycle all trajectories approach the limit cycle as $t\rightarrow\infty$
* For an unstable limit cycle all trajectories approach the limit cycle as $t\rightarrow -\infty$

Limit cycles can be extremely difficult to find.
```

Again, we can distinguish between a supercritical and subritical Hopf bifurcation.


```{exercise}
For the glycolysis problem introduced in {numref}`ex-222`, with $k=v_0=1$, show that there is an equilibrium point at
$(s,p)=(1/c,1)$. Find the eigenvalues and show that decreasing the parameter past $c=1$ creates a subcrtical Hopf bifurcation.
```

```{exercise}
Find the eigenvalues of the Rayleigh problem introduced in {numref}`ex-235`. Show that a Hopf bifurcation occurs at $c=0$. Is this a supercritical or a subcritical bifurcation?
```
