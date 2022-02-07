# Multidimensional Integrals

Although we are used to find the area under a curve from the integral of a function $f(x)$ over some limits $x \in [a,\, b]$:

```{math}
A = \int_a^b f(x)\,\mathrm{d}x
```

if we had some area described by a function $f(x,\,y)$ we could try to find the area contained within this 2D shape.  Likewise if we have some 
function $f(x,\,y,\,z)$ describing some shape in 3D space, we could aim to find the total volume contained in this shape.  We think of these 
as multidimensional integals as extending integral calculus to multivariables, akin to partial differentiation extending differential calculus 
to multivaribles.

## Area Integrals
Formally we can think of some scalar field $\phi({\bf r})$ which has as inputs $\bf r$ which is some 2D position vector, which allows us to define:

```{math}
A = \int_A \phi({\bf r})\,\mathrm{d}A 
```
Conceptually we can think of $\mathrm{d}A$ just like we do for the one variable case of integration, breaking up a shape into infintesimal blocks 
which we then sum up over the integral, as depicted in {numref}`infinitesimalarea`:

```{figure} ../figures/infinitesimalarea.png
---
name: infinitesimalarea
---
Division of a 2-dimensional area A into infinitesimal area elements $\mathrm{d}A$.
```

An area integral is a <b>double integral</b>, because we have to perform integrals over both the $x$ and $y$ variables. When integrating over 
one variable, the other is held constant - akin to how we do partial differentiation too.  

```{math}
I = \int_A \phi({\bf r})\,\mathrm{d}A = \iint_A\phi({\bf r})\,\mathrm{d}x\,\mathrm{d}y
```


Note that an important special case is $\phi = 1$, 
where the area integral is equal to the total area, $A = \int_A \,\mathrm{d}A$.  Otherwise what we are finding is an area weighed by the function 
$\phi$ - if $\phi(x,\,y)$ describes a function plotted on the $z$ axis, then the value of $\phi$ in each infinitesimal box will be what is summed
up by this area integral.

The order of the integration can however sometimes matter - this becomes important if the limits of each of the integals depends on one of the other 
variables (this can happen as when the integration is done, all the other variables are considered constant).

### Area Integral Examples 

## Volume Integrals

The concept of an area integral can be extended to volume integrals. The integration region is now a volume having some shape. The integration 
egion is divided up into volume elements $\mathrm{d}V$, and the function to be integrated $\phi({\bf r})$ has a value in each element. Conceptually, 
the integral is the sum of all the contributions $\phi({\bf r])\,\mathrm{d}V$ over all the elements, in the limit where the volume elements become 
infinitesimally small.  In Cartesian coordinates, the volume element is simply $\mathrm{d}V = \mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$, and the volume
integral can be expressed as a <b>triple integral</b> over x, y and z:

```{math}
I = \int_V \phi({\bf r})\,\mathrm{d}V = \iiint_V \phi(x,\,y,\,z)\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z
```

## Volume Integral Examples