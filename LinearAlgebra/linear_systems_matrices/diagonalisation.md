# Matrix Diagonalisation

## Diagonalisation

Recall that a diagonal matrix is a square matrix with zeros everywhere except the main diagonal. Multiplying a vector by a diagonal matrix $D$ is easy. Just multiply each entry of the vector by the the element in the corresponding position of the diagonal matrix:

$$\begin{pmatrix}d_{1}&0&\cdots&0\\0&d_{2}&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&d_{n}\end{pmatrix}\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix} = \begin{pmatrix}d_{1}x_1\\d_{2}x_2\\\vdots\\d_{n}x_n\end{pmatrix}.$$

The diagonal entries of $D$ act separately on each of the components of the vector $x$.

In fact, for diagonal matrices we immediately have the eigenvalues and eigenvectors! The eigenvalues are the diagonal entries $d_i$ and the eigenvectors are the standard coordinate vectors $e_i$:

$$De_i = d_ie_i.$$

Multiplying by a diagonal matrix is easy because any vector is a linear sum of coordinate vectors.

What about general (non-diagonal) square matrices? If $x$ is an eigenvector of a square matrix $A$ and $\lambda$ its eigenvalue, then we have

$$Ax = \lambda x.$$

If $x$ is an eigenvector, $A$ behaves like a diagonal matrix where the diagonal entries are the eigenvalues! In fact, in may cases it turns out that we can use the eigenvectors to express $A$ as a diagonal matrix.

```{admonition} Matrix Diagonalisation

Let $A$ be an $(n \times n)$ matrix with $n$ eigenvectors $x_i$ and corresponding eigenvalues $\lambda_i$. Let

$$X = \begin{pmatrix}|&&|\\x_1&\cdots&x_n\\|&&|\end{pmatrix}$$

be the matrix of eigenvectors and

$$\Lambda = \begin{pmatrix}\lambda_1 &&\\&\ddots&\\&&\lambda_n\end{pmatrix} $$

the matrix of eigenvalues. If $X$ is invertible, then

$$X^{-1}AX = \Lambda.$$
```

Note that we use capital lambda $\Lambda$ to represent the matrix of eigenvalues.

To see why the above result is true, let us write the equation $X^{-1}AX=\Lambda$ slightly differently:

$$AX = X\Lambda.$$

Then the left hand side $AX$ is $A$ times the eigenvectors:

$$AX = A\begin{pmatrix}|&&|\\x_1&\cdots&x_n\\|&&|\end{pmatrix} = \begin{pmatrix}|&&|\\\lambda_1x_1&\cdots&\lambda_nx_n\\|&&|\end{pmatrix}$$

because $Ax_i= \lambda_ix_i$.

Whereas right hand side $X\Lambda$ is the eigenvectors times the eigenvalues:

$$X\Lambda = \begin{pmatrix}|&&|\\x_1&\cdots&x_n\\|&&|\end{pmatrix}\begin{pmatrix}\lambda_1 &&\\&\ddots&\\&&\lambda_n\end{pmatrix} = \begin{pmatrix}|&&|\\\lambda_1x_1&\cdots&\lambda_nx_n\\|&&|\end{pmatrix}.$$

Thus we see that $AX=X\Lambda$.

```{attention}
1. Diagonalisation only works if we have $n$ different (linearly independent) eigenvectors so that $X$ is invertible. Not every $(n \times n)$ matrix has $n$ linearly independent eigenvectors, so not all matrices are diagonalisable.
4. The eigenvectors in $X$ must be written in the same order as the eigenvalues in $\Lambda$.
2. Diagonalisation is not unique, because eigenvectors are not unique. If we multiply an eigenvector by a constant, we get another eigenvector and therefore another eigenvector matrix $X$.
3. The eigenvalue matrix $\Lambda$ *is* unique (up to order).
```


## Complex Eigenvalues

[TODO]

## Application E.g. Stochastic Matrices

[TODO]
