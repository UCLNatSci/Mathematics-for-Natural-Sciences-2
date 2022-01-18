# Divergence and Curl

## Divergence

If we start with a vector field ${\bf A(r)} = A_x({\bf r})\,\hat{\bf x} + A_y({\bf r})\,\hat{\bf y} + A_z({\bf r})\,\hat{\bf z} $, then we can define the quantity 
$\nabla\cdot {\bf A(r)}$, i.e. taking the scalar product of the gradient operator with vector field ${\bf A(r)} $ which since the gradient vector is a differential 
operator, means the expression has the form:

```{math}
\nabla\cdot {\bf A(r)} = \partial_x\, A_x + \partial_y\, A_y + \partial_z\, A_z
```

This is often known as the <b>Divergence</b> of ${\bf A(r)}$ or $\text{div}\,{\bf A(r)}$.  Note that in the case of operators we need to be a little careful of the 
ordering of the terms, since ${\bf A(r)}\cdot \nabla$ would give:

```{math}
{\bf A(r)} \cdot \nabla= A_x\,\partial_x  + A_y\,\partial_y  + A_z\,\partial_z  
```

which is also a differential operator, waiting to act on another term, which we apply on the right. 

Lets see the effect of this on two vector fields ${\bf A_1(r)} = \begin{pmatrix} x \\ y \\ 0\end{pmatrix}, \,{\bf A_2(r)} = \begin{pmatrix} y \\ -x \\ 0\end{pmatrix}$:

```{math}
\nabla \cdot {\bf A_1} &=&\, \partial_x\, x + \partial_y\, y + \partial_z\, 0 = 2 \\
\nabla \cdot {\bf A_2} &=&\, \partial_x\, y - \partial_y\, x + \partial_z\, 0 = 0 
```

## Curl

We can likewise take a vector field $${\bf A(r)} $ and here take the vector product with the gradient operator $\nabla\times {\bf A(r)}$, which has components:

```{math}
\nabla\times {\bf A(r)} = \begin{pmatrix} \partial_y\, A_z - \partial_z\, A_y \\ \partial_z\, A_x - \partial_x\, A_z \\ \partial_x\, A_y - \partial_y\, A_x  \end{pmatrix}
```

which is know as the <b>Curl</b> or <b>Rotation</b> of the vector field $\bf A(r)$ or $\text{curl}\,{\bf A(r)}$.

To see the effects of these, lets consider again ${\bf A_1(r)} = \begin{pmatrix} x \\ y \\ 0\end{pmatrix}, \,{\bf A_2(r)} = \begin{pmatrix} y \\ -x \\ 0\end{pmatrix}$:

```{math}
\nabla \times {\bf A_1} &=&\, \begin{pmatrix} \partial_y\, 0 + \partial_z\, x \\ \partial_z\, y - \partial_x\, 0 \\ \partial_x\, y - \partial_y\, x  \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \\
\nabla \times {\bf A_2} &=&\, \begin{pmatrix} \partial_y\, 0 + \partial_z\, x \\ \partial_z\, y - \partial_x\, 0 \\ \partial_x\, x + \partial_y\, y  \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 2 \end{pmatrix}
```
