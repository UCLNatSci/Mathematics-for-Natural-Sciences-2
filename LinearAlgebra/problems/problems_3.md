# Linear Algebra Problems 3

## Determinant Question

Define $K_n$ to be the matrix with $2$s on the main diagonal and $-1$s on the subdiagonal and superdiagonal. $K_4$ is shown below:

$$K_4 = \begin{pmatrix}2&-1&0&0\\-1&2&-1&0\\0&-1&2&-1\\ 0&0&-1&2\end{pmatrix}.$$

Show that $\det(K_n) = n + 1$:

1. Using row operations to reduce the matrix to a triangular matrix.
2. Using the cofactor formula.

## 3 x 3 Inverse Question

[TODO]

## Invertible Matrix Theorem Question

[TODO]

## Question 1

<!-- https://www.sheffield.ac.uk/polopoly_fs/1.892866!/file/eignval_eignvec_basics_HELM.pdf -->

If $\lambda_1, \ldots, \lambda_n$ are the eigenvalues of a matrix $A$, prove the following:

1. $A^T$ has eigenvalues $\lambda_1, \ldots, \lambda_n$.
2. If $A$ is upper triangular, then its eigenvalues are exactly the main diagonal entries.
3. The inverse matrix $A^{-1}$ has eigenvalues $\frac{1}{\lambda_1}, \ldots, \frac{1}{\lambda_n}$.
4. The matrix $A-kI$ has eigenvalues $\lambda_1-k, \ldots, \lambda_n-k$.
5. The matrix $A^2$ has eigenvalues $\lambda_1^2, \ldots, \lambda_n^2$.
6. The matrix $A^k$ where $k \in \mathbb{N}$ has eigenvalues has eigenvalues $\lambda_1^k, \ldots, \lambda_n^k$.

## Question 2

<!-- Yutsumura 719 -->

Let $A$ be the matrix given by

$$A = \begin{pmatrix}-2 & 0 & 1\\-5 & 3 & a\\4 & -2 & -1\end{pmatrix}$$

for some $a \in \mathbb{R}$. Find all values of $a$ which guarantee that $A$ has eigenvalues $0, 3$ and $-3$.

## Question 3

<!-- yutsumura 630 -->

Let

$$A = \begin{pmatrix}a&-b\\b&a\end{pmatrix}$$

where $a, b \in \mathbb{R}$ and $b \neq 0$.

1. Find all eigenvalues of $A$.
2. Find the eigenspace corresponding to each eigenvalue.
3. Diagonalise the matrix $A$ by finding an invertible matrix $S$ and diagonal matrix $D$ such that $S^{-1}AS=D$.

## Question 4

<!-- yutsumura 593 -->

Given a nonzero vector $v_0 \in \mathbb{R}$ we define a function $T:\mathbb{R}^3 \rightarrow \mathbb{R}^3$ by

$$T(x) = v_0 \times x$$

where $\times$ represents the vector (cross) product.

1. Show that $T:\mathbb{R}^3\rightarrow \mathbb{R}^3$ is a linear transformation.
2. Determine the eigenvalues and eigenvectors of $T$.

## Question 5

<!-- yutsumura 583 -->

Consider the matrix

$$A = \begin{pmatrix}a&b-a\\0&b\end{pmatrix}$$

where $a, b \in \mathbb{C}$.

1. Find the eigenvalues and eigenvectors of $A$.
2. Diagonalise $A$.
3. Compute and simplify $A^k$ where $k\in\mathbb{N}$.

## Question 6

<!-- yutsumura 550 -->

Let

$$A = \begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$$

for some $\theta \in \mathbb{R}$.

1. Find the characteristic polynomial of $A$.
2. Find the eigenvalues of $A$.
3. Determine the corresponding eigenvectors.

## Question 7

<!-- yutsumura 485 -->

Let

$A=\begin{pmatrix}1&-14&4\\-1&6&-2\\-2&24&-7\end{pmatrix}$ and $v = \begin{pmatrix}4\\-1\\-7\end{pmatrix}$.

1. Show that $-1, 0$ and $1$ are eigenvalues of $A$.
2. Determine the corresponding eigenspaces.
3. Calculate $A^{10}$.
