# Vector Calculus Theorems

Although the ideas in vector calculus seem quite distinct, area, surface and volume integrals as well as the gradient, divergence and curl, it turns out
that they are connected together thanks to a couple of quite important theorems.  These can in some cases simplify a calculation that we are aiming to 
do and/or give us a better intution about a system.  

## (Gauss-)Divergence Theorem
Lets think about a closed surface $S$ in a space, this surface area therefore encloses a volume $V$, i.e. it forms the boundary $S = \partial V$ (not 
to be confused with taking some partial derivative!), as depicated in {numref}`gaussdivergence`.

```{figure} ../figures/gaussdivergence.png
---
name: gaussdivergence
---
Vectorial surface-area element $\mathrm{d}{\bf S}$ of a closed surface $S = \partial V$, with the convention that 
$\mathrm{d}{\bf S} = \hat{\bf b} \mathrm{D}S$ points outwards.
```
Thinking about a vector field ${\bf G}({\bf r})$ through the closed surface $S$, one thing we can do is count the flux from the surface intregral:
```{math}
\int_S {\bf G}({\bf r})\cdot \mathrm{d}{\bf S}
```
We can see that if the field is uniform, say $\nabla \cdot {\bf G} = 0$, then this net flux will zero (all incoming vectors = all out going vectors), 
however if there is a divergence in the enclosed volume $\nabla \cdot {\bf G} \neq 0$, then there would be a net flux through the surface (with the sign of the flux being related to the sign ofthe divergence).  
This result gives us the <b>Divergence Theorem</b>:
```{math}
\int_S {\bf G}({\bf r})\cdot \mathrm{d}{\bf S} = \int_V \left(\nabla \cdot G\right)\,\mathrm{d}V
```

### Divergence Theorem Example
Lets start with an example, for the vector field:
```{math}
{\bf G}({\bf r}) = \begin{pmatrix} x^2 \\ y \\ z \end{pmatrix}
```
over a cubic volume, centered on the origin, with corners $(\pm 1,\, \pm 1,\, \pm 1)$, as depicted in {numref}`divergencecube`

```{figure} ../figures/divergencecube.png
---
name: divergencecube
---
An example cubic surface around some vector field divergence.
```

If we compute the surface integral:
```{math}
I = \int_{S = \partial V} {\bf G}({\bf r})\cdot \mathrm{d}{\bf S} &=& \,
\int_{-1}^1 \,\mathrm{d}y\,\int_{-1}^1\,\mathrm{d}z \,\begin{pmatrix} 1 \\ y \\ z \end{pmatrix} \cdot \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} 
 + \int_{-1}^1 \,\mathrm{d}y\,\int_{-1}^1\,\mathrm{d}z \,\begin{pmatrix} 1 \\ y \\ z \end{pmatrix} \cdot \begin{pmatrix} - \\ 0\\ 0 \end{pmatrix}  \\ 
&+& \,
\int_{-1}^1 \,\mathrm{d}x\,\int_{-1}^1\,\mathrm{d}z \,\begin{pmatrix} x^2 \\ 1 \\ z \end{pmatrix} \cdot \begin{pmatrix} x^2 \\ 1 \\ 0 \end{pmatrix} 
 + \int_{-1}^1 \,\mathrm{d}y\,\int_{-1}^1\,\mathrm{d}z \,\begin{pmatrix} x^2 \\ -1 \\ z \end{pmatrix} \cdot \begin{pmatrix} x^2 \\ -1 \\ 0 \end{pmatrix}  \\ 
 &+& \,
 \int_{-1}^1 \,\mathrm{d}x\,\int_{-1}^1\,\mathrm{d}y \,\begin{pmatrix} x^2 \\ y \\ 1 \end{pmatrix} \cdot \begin{pmatrix} x^2 \\ y \\ 1 \end{pmatrix} 
 + \int_{-1}^1 \,\mathrm{d}x\,\int_{-1}^1\,\mathrm{d}y \,\begin{pmatrix} x^2 \\ y \\ -1 \end{pmatrix} \cdot \begin{pmatrix} x^2 \\ y \\ -1 \end{pmatrix}  \\ 
 &=& \,
 2 \int_{-1}^1 \,\mathrm{d}x\,\int_{-1}^1\,\mathrm{d}z + \int_{-1}^1 \,\mathrm{d}x\,\int_{-1}^1\,\mathrm{d}y  = 16
```

A little long! However using the Gauss's divergence theorem:
```{math}
\nabla \cdot {\bf G} &=&\, 2x + 2\\ 
I &=&\, \int_{V} (\nabla \cdot {\bf G})\,\mathrm{d}V = \int_{-1}^1\,\mathrm{d}x\, \int_{-1}^1\,\mathrm{d}y\, \int_{-1}^1\,\mathrm{d}z (2x + 2)\\
&=&\, 4\int_{-1}^1\,(2x+2)\,\mathrm{d}x = 4\Bigg[x^2 + 2x\Bigg]_{-1}^1 = 16
```

In agreement with the previous result and whole lot easier to do!


### A Sketch of a Proof

We can sketch out a proof of this result, using the same set up as previously, as seen in {numref}`divergencecubeproof`, 
```{figure} ../figures/divergencecubeproof.png
---
name: divergencecubeproof
---
An infinitesimal cubic surface $\mathrm{d}V = \mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$ around some vector field divergence.
```

Thinking about an infinitesimal flux element $\mathrm{d}F$ for a vector field ${\bf G}({\bf r})$ crossing the sides of the infinitesimal 
volume element $\mathrm{d}V = \mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$:

```{math}
:label: divtheoremproof
\mathrm{d}F &=&\, {\bf G}\left({\bf r} + \frac{1}{2}\mathrm{d}x\,\hat{\bf x} \right)\cdot \hat{\bf x}\,\mathrm{d}y\,\mathrm{d}z 
+ {\bf G}\left({\bf r} - \frac{1}{2}\mathrm{d}x\,\hat{\bf x} \right)\cdot (-\hat{\bf x})\,\mathrm{d}y\,\mathrm{d}z\\
&+&\, {\bf G}\left({\bf r} + \frac{1}{2}\mathrm{d}y\,\hat{\bf y} \right)\cdot \hat{\bf y}\,\mathrm{d}x\,\mathrm{d}z 
+ {\bf G}\left({\bf r} - \frac{1}{2}\mathrm{d}x\,\hat{\bf y} \right)\cdot (-\hat{\bf y})\,\mathrm{d}x\,\mathrm{d}z\\
&+&\, {\bf G}\left({\bf r} + \frac{1}{2}\mathrm{d}z\,\hat{\bf z} \right)\cdot \hat{\bf z}\,\mathrm{d}x\,\mathrm{d}y 
+ {\bf G}\left({\bf r} - \frac{1}{2}\mathrm{d}x\,\hat{\bf z} \right)\cdot (-\hat{\bf z})\,\mathrm{d}x\,\mathrm{d}y
```

The first line of {eq}`divtheoremproof` reduces to:
```{math}
&&\, \left[{\bf G}\left({\bf r} + \frac{1}{2}\mathrm{d}x\,\hat{\bf x} \right)\cdot \hat{\bf x}
+ {\bf G}\left({\bf r} - \frac{1}{2}\mathrm{d}x\,\hat{\bf x} \right)\cdot (-\hat{\bf x})\right]\,\mathrm{d}y\,\mathrm{d}z\\
&=&\, \left[G_x\left({\bf r} + \frac{1}{2}\mathrm{d}x\,\hat{\bf x} \right)
- G_x\left({\bf r} - \frac{1}{2}\mathrm{d}x\,\hat{\bf x} \right)\right]\,\mathrm{d}y\,\mathrm{d}z\\
```
If we do a Taylor expansion of each vector field, around $G_x({\bf r})$:
```{math}
&=&\, \left[G_x({\bf r}) + \frac{1}{2}\partial_x G_x({\bf r})\,\mathrm{d}x 
- \left(G_x({\bf r}) - \frac{1}{2}\partial_x G_x({\bf r})\,\mathrm{d}x \right)\right]\,\mathrm{d}y\,\mathrm{d}z\\
&=&\, \partial_x G_x \,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z
```

We can do similar for the second and third lines of {eq}`divtheoremproof` to find the result:
```{math}
:lanel: 
\mathrm{d}F = \Bigg(\partial G_x + \partial G_y + \partial G_z \Bigg)\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z = 
\Bigg( \nabla \cdot {\bf G}\Bigg)\,\mathrm{d}V
```

And through suitable coordinate transforms we could prove this result for any coordinate system.  Hence the flux across the cubes sides 
is related to the divergence of the vector field over the volume element.

If we then proceed with integrating this flux over the over a given volume, then we can think of this as summing up little cubes with volume 
$\mathrm{d}V$, as depicted in {numref}`infinitesimalcubes`.  

```{figure} ../figures/infinitesimalcubes.png
---
name: infinitesimalcubes
---
Infinitesimal cubic volume $\mathrm{d}V = \mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$ making up some volume $V$.
```

This means we are summing up neighbouring cubes, where the outgoing flux $\int \,\mathrm{d}F > 0$ from one will be an incoming flux 
$\int \,\mathrm{d}F < 0$ for another cube, as depicted in {numref}`inoutgoingflux`.  

```{figure} ../figures/inoutgoingflux.png
---
name: inoutgoingflux
---
A schematic of the infinitesimal flux contributions from neighbouring infintesimal cubic volumes.
```

Therefore we see that the <b>only</b> remaining contributions to the summing of the fluxes over the volume will be from the volumes surface, 
hence:
```{math}
\int_V\,\mathrm{d}F = \int_{S = \partial V}\,\mathrm{d}F = 
\iint_{S = \partial V}\,{\bf G}({\bf r})\cdot \mathrm{d}{\bf S} = \iiint \Bigg( \nabla \cdot {\bf G}({\bf r})\Bigg)\,\mathrm{d}V
```
which is the desired result.

% ## (Kelvin-)Stoke's Theorem