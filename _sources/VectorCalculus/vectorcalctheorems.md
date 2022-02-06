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
I = \int_{S = \partial V} {\bf G}({\bf r})\cdot \mathrm{d}{\bf S} &=& 
\int_{-1}^1 \,\mathrm{d}y\,\int_{-1}^1\,\mathrm{d}z \,\begin{pmatrix} 1 \\ y \\ z \end{pmatrix} \cdot \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} 
 + \int_{-1}^1 \,\mathrm{d}y\,\int_{-1}^1\,\mathrm{d}z \,\begin{pmatrix} 1 \\ y \\ z \end{pmatrix} \cdot \begin{pmatrix} - \\ 0\\ 0 \end{pmatrix}  \\ 
&+& 
\int_{-1}^1 \,\mathrm{d}x\,\int_{-1}^1\,\mathrm{d}z \,\begin{pmatrix} x^2 \\ 1 \\ z \end{pmatrix} \cdot \begin{pmatrix} x^2 \\ 1 \\ 0 \end{pmatrix} 
 + \int_{-1}^1 \,\mathrm{d}y\,\int_{-1}^1\,\mathrm{d}z \,\begin{pmatrix} x^2 \\ -1 \\ z \end{pmatrix} \cdot \begin{pmatrix} x^2 \\ -1 \\ 0 \end{pmatrix}  \\ 
 &+& 
 \int_{-1}^1 \,\mathrm{d}x\,\int_{-1}^1\,\mathrm{d}y \,\begin{pmatrix} x^2 \\ y \\ 1 \end{pmatrix} \cdot \begin{pmatrix} x^2 \\ y \\ 1 \end{pmatrix} 
 + \int_{-1}^1 \,\mathrm{d}x\,\int_{-1}^1\,\mathrm{d}y \,\begin{pmatrix} x^2 \\ y \\ -1 \end{pmatrix} \cdot \begin{pmatrix} x^2 \\ y \\ -1 \end{pmatrix}  \\ 
 &=& 
 2 \int_{-1}^1 \,\mathrm{d}x\,\int_{-1}^1\,\mathrm{d}z + \int_{-1}^1 \,\mathrm{d}x\,\int_{-1}^1\,\mathrm{d}y  = 16
```

A little long! However using the Gauss's ivergnece theorem:
```{math}
\nabla \cdot {\bf G} &=& 2x + 2\\ 
I & &\int_{V} (\nabla \cdot {\bf G})\,\mathrm{d}V = \int_{-1}^1\,\mathrm{d}x\, \int_{-1}^1\,\mathrm{d}y\, \int_{-1}^1\,\mathrm{d}z (2x + 2)\\
&=& 4\int_{-1}^1\,(2x+2)\,\mathrm{d}x = 4\Bigg[x^2 + 2x\Bigg]_{-1}^1 = 16
```

In agreement with the previous result and whole lot easier to do!


% ## (Kelvin-)Stoke's Theorem