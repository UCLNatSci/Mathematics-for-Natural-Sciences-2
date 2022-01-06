# Multivariable Calculus
 

The plot shown in {numref}`surf1` is the function $f(x,\, y)= x^3 - y^3 - 2xy + 2$, on which curves marked on the surface for lines of constant $x,\,y$.  We 
can consider the rate of change of the function, both:

- along a curve parallel to the $x$-axis, by holding $y$ constant and differentiating with respect to $x$.

- along a curve parallel to the $y$-axis, by holding $x$ constant and differentiating with respect to $y$.
    
```{figure} ../figures/surf1.png
---
name: surf1
---
A plot of the function $f(x,\, y) = x^3 - y^3 - 2xy + 2$
---
```
    

For instance, along the line $$x=1$$, we have $$f(1,y)=-y^3-2 y+3$$. We can differentiate this function with respect to $$y$$ to obtain the rate of change of $$f(x,y)$$ along the curve. The result is called the "partial" derivative of $$f$$ with respect to $$y$$. It is "partial" because we consider only variations in one of the two variables. We write $$\displaystyle\frac{\partial f(1,y)}{\partial y}=-3y^2-2$$.

More generally, for this function

\begin{align}\frac{\partial f(x,y)}{\partial y}&=-3y^2-2x \quad &\text{(holding $x$ constant and differentiating with respect to $y$)}\\\frac{\partial f(x,y)}{\partial x}&=3x^2-2y \quad &\text{(holding $y$ constant and differentiating with respect to $x$)}\end{align}

Note the different notation $$(x,y)$$. The results show the local rate of change parallel to each axis at a point $$(x,y)$$.

   

Example 1

Calculate all the first partial derivatives $$\frac{\partial}{\partial x},$$ $$\frac{\partial }{\partial y}$$ for the following functions:

(a) $$f(x,y) = 3x^3 y^2 +2 y$$

(b) $$f(x,y) = x^2 \ln(3x+y)$$

(c) $$z(x,y) = \ln(x+y^2\sin(x))$$

     

Solutions

(a) $$\displaystyle\frac{\partial f}{\partial x}=9x^2 y^2, \quad \frac{\partial f}{\partial y}=6x^3 y+2$$.

(b) $$\displaystyle\frac{\partial f}{\partial x}=2x\ln(3x+y) + \frac{3x^2}{3x+y}, \quad \frac{\partial f}{\partial y}=\frac{x^2}{3x+y}$$

(c) $$\displaystyle\frac{\partial z}{\partial x}=\frac{1+y^2\cos(x)}{x+y^2\sin(x)}, \quad \frac{\partial z}{\partial y}=\frac{2y\sin(x)}{x+y^2\sin(x)}$$

    

Second partial derivatives
The second partial derivatives with respect to $$x$$ and $$y$$ are denoted as follows:

\begin{equation}\frac{\partial^2 f}{\partial x^2}=\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right), \quad \frac{\partial^2 f}{\partial y}\left(\frac{\partial f}{\partial y}\right)\end{equation}

The notation is also extended to mixed second partial derivatives:

\begin{equation}\frac{\partial^2 f}{\partial y \partial x}=\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right), \quad \frac{\partial^2 f}{\partial x \partial y}=\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right).\end{equation}

Notice that we work from the inside out, as with function composition and matrix multiplication.

   

Example:

Calculate all second partial derivatives of the function $$f(x,y)=3x^3y^2+2y$$

  

Solution

\begin{equation}\frac{\partial f}{\partial x}=9x^2y^2, \quad \frac{\partial f}{\partial y}=6x^3y+2,\quad \frac{\partial^2 f}{\partial x^2}=18x y^2,\quad \frac{\partial^2 f}{\partial y^2}=6x^3, \quad \frac{\partial^2 f}{\partial y\partial x}=18x^2y, \quad \frac{\partial^2 f}{\partial x\partial y}=18x^2 y\end{equation}

Notice that $$\frac{\partial^2 f}{\partial x\partial y}=\frac{\partial^2 f}{\partial y \partial}$$. This result is general, provided that $$f$$ is continuous and differentiable. The proof of this result (called Schwarz's theorem) is quite involved and is beyond the scope of this course. It relies on showing that the following results are equivalent (provided the partial limits exist and are finite):

\begin{align} \frac{\partial^2 f}{\partial x\partial y}=\lim_{\Delta x\rightarrow 0}\biggr[\frac{\frac{\partial f(x+\Delta x,y)}{\partial y}-\frac{\partial f(x,y)}{\partial y}}{\Delta x}\biggr] &=\lim_{\Delta x \rightarrow 0}\biggr[\frac{\displaystyle\lim_{\Delta y\rightarrow 0}\left[\frac{f(x+\Delta x,y+\Delta y)-f(x+\Delta x,y)}{\Delta y}\right]-\lim_{\Delta y\rightarrow 0}\left[\frac{f(x,y+\Delta y)-f(x,y)}{\Delta y}\right]}{\Delta x}\biggr]\\&=\lim_{\Delta x\rightarrow 0}\lim_{\Delta y\rightarrow 0}\left[\frac{f(x+\Delta x,y+\Delta y)-f(c+\Delta x,y)-f(x,y+\Delta y)+f(x,y)}{\Delta x\Delta y}\right]\end{align}

\begin{align} \frac{\partial^2 f}{\partial y\partial x}=\lim_{\Delta y\rightarrow 0}\biggr[\frac{\frac{\partial f(x,y+\Delta y)}{\partial y}-\frac{\partial f(x,y)}{\partial y}}{\Delta y}\biggr] &=\lim_{\Delta y \rightarrow 0}\biggr[\frac{\displaystyle\lim_{\Delta x\rightarrow 0}\left[\frac{f(x+\Delta x,y+\Delta y)-f(x,y+\Delta y)}{\Delta x}\right]-\lim_{\Delta y\rightarrow 0}\left[\frac{f(x+\Delta x,y)-f(x,y)}{\Delta x}\right]}{\Delta x}\biggr]\\&=\lim_{\Delta y\rightarrow 0}\lim_{\Delta x\rightarrow 0}\left[\frac{f(x+\Delta x,y+\Delta y)-f(c+\Delta x,y)-f(x,y+\Delta y)+f(x,y)}{\Delta x\Delta y}\right]\end{align}

Interchanging the order of limits is not always possible, although it is valid for "well-behaved" functions. It is possible to show that the assumptions of continuity and differentiability guarantee that the order of the limits can be interchanged.

    

A common mistake
To calculate $$\frac{\partial^2}{\partial y\partial x}(x^2 y^3+x+y)$$ at the point $$(1,1)$$...

 

Put $$y=1$$ and differentiate with respect to $$x$$ to obtain $$\frac{\partial}{\partial x}(x^2+x+1)=2x$$       $$\leftarrow$$ This step is incorrect!

Put $$x=1$$ and differentiate with respect to $$y$$ to obtain $$\frac{\partial}{\partial y}(2)=0$$.

The result is wrong, because we took $$y=1$$ before differentiating with respect to $$y$$. To avoid mistakes of this nature, we should always perform differentiation first and only substitute in the values in the very last step. The correct result is

$$\biggr[\frac{\partial^2}{\partial y\partial x}\left(x^2 y^3 +x+y\right)\biggr]_{(1,1)} = \biggr[\frac{\partial }{\partial y}(2xy^3+1)\biggr]_{(1,1)} = \biggr[6xy^2\biggr]_{(1,1)} = 6$$ 

   

Notation:
Partial derivatives are commonly denoted using subscript notation:

$$f_x=\frac{\partial f}{\partial x}, \quad f_y=\frac{\partial f}{\partial y}, \quad f_{xx}=\frac{\partial^2 f}{\partial x^2}\quad f_{yy}=\frac{\partial^2 f}{\partial y^2}$$

For mixed derivatives the order or subscripts is from left to right:

$$f_{xy} = (f_x)_y = \frac{\partial^2 f}{\partial y \partial x}, \quad f_{yx}=(f_y)_x = \frac{\partial^2 f}{\partial x \partial y}$$.

You will likely come across yet more alternative notations in the literature. For instance, the notation $$D_x=\frac{\partial}{\partial x}$$ is also common.

   

Example 2

The Hessian matrix for a function $$f(x,y)$$ is the (2x2) matrix $$H =\left(\begin{matrix}f_{xx}& f_{x y}\\f_{y x}&f_{yy}\end{matrix}\right)$$.

Calculate the determinant of the Hessian matrix for the function $$f(x,y) = x^3 - y^3 -2xy+2$$.

   

Solution

We have $$f_x = 3x^2-2y, \quad f_y = -3y^2 - 2x$$

$$f_{xx}=6x, \quad f_{yy}=-6y, \quad f_{xy}=f_{yx}=-2$$

$$H=f_{xx}f_{yy} - f_{xy}f_{yx} = -36xy-4$$.

The Hessian matrix is useful for classifying stationary points.

    

Multi-variate chain rule
We now consider a function $$f(x,y)$$ subjected to small variations in both $$x$$ and $$y$$ as shown in the figure below

multivariate chain rule illustration
Figure 2

$$f(x+\Delta x, y+\Delta y)$$ in two steps.

   

Loosely speaking, the total change in the function $$f$$ is the sum of changes due to each variable:

\begin{equation}\Delta f = \frac{\partial f}{\partial x}\Delta x + \frac{\partial f}{\partial y}\Delta y\end{equation}

If we now suppose that $$x=x(u,v)$$ and $$y=y(u,v)$$ then we may similarly write $$\Delta x$$ and $$\Delta y$$ as the sum of changes due to variables $$u$$ and $$v$$:

\begin{equation}\Delta f = \frac{\partial f}{\partial x}\left[\frac{\partial x}{\partial u}\Delta u +\frac{\partial x}{\partial v}\Delta v\right] + \frac{\partial f}{\partial y}\left[\frac{\partial y}{\partial u}\Delta u +\frac{\partial y}{\partial v}\Delta v\right]\end{equation}

Holding $$v$$ constant in this expression ($$\Delta v=0$$) gives 

\begin{equation}\frac{\Delta f}{\Delta u}=\frac{\partial f}{\partial x}\frac{\partial x}{\partial u}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial u}\end{equation}

Holding $$u$$ constant in this expression ($$\Delta u=0$$) gives 

\begin{equation}\frac{\Delta f}{\Delta v}=\frac{\partial f}{\partial x}\frac{\partial x}{\partial v}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial v}\end{equation} 

  

This was a somewhat "hand-waving" argument, but the results are valid in the limit $$\Delta u\rightarrow 0$$, $$\Delta v\rightarrow 0$$ and can be proved using the limit definition of the derivative. We obtain the multi-variate chain rule, written in the box below:

 

The multivariate chain rule

If $$f=f(x,y)$$ where $$x=x(u,v)$$ and $$y=y(u,v)$$ then

\begin{align}\frac{\partial f}{\partial u}&=\frac{\partial f}{\partial x}\frac{\partial x}{\partial u}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial u}\\\frac{\partial f}{\partial v}&=\frac{\partial f}{\partial x}\frac{\partial x}{\partial v}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial v}\end{align}

   

Student's first encountering this rule often think that it "can't be right", because replacing the partial derivatives with differences gives

$$\Delta f = \frac{\Delta f}{\Delta x}\Delta x + \frac{\Delta f}{\Delta y}\Delta y,$$

which suggests the result $$\Delta f = 2\Delta f$$. However, this misunderstanding comes from ambiguity in writing $$\Delta f$$. On the left-hand side it means changes in $$f$$ dues to variations in both $$x$$ and $$y$$, whilst in $$f_x$$ and $$f_y$$ the changes are due to only one of these variables whilst the other is held constant. Written formally,

$$\displaystyle \frac{\partial f}{\partial u} = \lim_{\Delta u\rightarrow 0}\frac{f(x(u+\Delta u,v),y(u+\Delta u,v))-f(x(u,v),y(u,v))}{\Delta u}$$,

$$\displaystyle\frac{\partial f}{\partial x} = \lim_{\Delta x\rightarrow 0}\frac{f(x+\Delta x,y)-f(x,v)}{\Delta x}=\lim_{\Delta u\rightarrow 0}\frac{f(x(u+\Delta u,v),y(u,v))-f(x(u,v),y(u,v))}{\Delta u}$$

   

It is dangerous to treat partial derivatives as fractions!

   

Dependency trees
The multivariate chain rule can be illustrated as a dependency tree. For the first and second derivatives of $$f(x,y)$$ where $$x=x(u,v)$$ and $$y=y(u,v)$$:

dependency tree for first derivatives

 

For instance, if we follow the dependency routes involving $$u$$, we get $$f_u = f_x x_u + f_y y_u$$.

We can do the same thing for the second derivatives (a repeat application of the chain rule):

dependency tree for second derivatives

   

Example 3:

(a) For the function $$f(x,y)=x^2 y+y^2$$, calculate $$\frac{\partial f}{\partial u}$$ and $$\frac{\partial f}{\partial v}$$, where $$x=u+v$$ and $$y=u-v$$.

(b) Calculate $$\frac{\partial f}{\partial x}$$ for the function $$f(x,y)=\sin(x^2+2xy)+(x-y)^2$$

   

Solution

(a)

$$f_x = 2xy, \quad f_y = x^2+2y$$

$$x_u=1, \quad x_v=1, \quad y_u=1, \quad y_v=-1$$

$$f_u = f_x x_u + y_y y_u = 2xy+(x^2+2y) = 2(u+v)(u-v)+(u+v)^2+2(u-v)$$

$$f_v = f_x x_v + f_y y_v = 2xy-(x^2+2y) = 2(u+v)(u-v)-(u+v)^2-2(u-v)$$

   

(b)

We can let $$u=x^2+2xy$$, $$v=x-y$$, then,

$$f_x = f_u u_x +f_v v_x =\cos(u)(2x+2y)+2v = 2(x+u)\cos(x^2+2xy)+2(x-y)$$

   

Exact derivatives/exact differentials
The multivariate chain rule is sometimes written in "differential form"

\begin{equation}\mathrm{d}F=\frac{\partial F}{\partial x}\mathrm{d}x+\frac{\partial F}{\partial y}\mathrm{d}y.\end{equation}

Comparing this result to a general expression of the form

\begin{equation}\mathrm{d}F=A(x,y)\mathrm{d}x+B(x,y)\mathrm{d}y\end{equation}

tells us that $$A = \frac{\partial F}{\partial x}$$ and $$B=\frac{\partial F}{\partial y}$$.

For these two results to be consistent, we require that the mixed second derivatives of $$F$$ are equal, in accordance with Schwarz' theorem. Therefore, we require that

\begin{equation}\frac{\partial A}{\partial y}\equiv\frac{\partial B}{\partial x}.\end{equation}

If the differential is exact, then it can be exactly integrated to obtain a solution $$F$$. You will not be asked to obtain solutions for $$F$$, but you will be asked to verify if a differential expression is exact by testing the condition given above.

   

Example 4:

Show that \((y\cos{x}+\sin{y}+y)\mathrm{d}x + (\sin{x}+x\cos{y}+x)\mathrm{d}y\) is an exact differential.

      

Solution:

The expression is of the form \(A(x,y)\mathrm{d}x+B(x,y)\mathrm{d}y=0\) where

\(A=y\cos{x}+\sin{y}+y\)

\(B=\sin{x}+x\cos{y}+x\)

Then, \(\frac{\partial A}{\partial y} = \cos{x}+\cos{y}+1 = \frac{\partial B}{\partial x}\) and so the expression is exact.

Optional: The result could be used to solve the nonlinear 1st order ODE

\(\frac{\mathrm{d}y}{\mathrm{d}x} + \frac{y\cos{x}+\sin{y}+y}{\sin{x}+x\cos{y}+x}=0\)

Let \(A=\frac{\partial F}{\partial x},\ B=\frac{\partial F}{\partial y}\) where \(F(x,y)\) is to be determined.

By integrating \(A\) w.r.t. \(x\) and \(B\) w.r.t \(y\) we obtain

\(F=y\sin{x}+x\sin{y}+xy+F_1(y)\)

\(F=y\sin{x}+x\sin{y}+xy+F_2(x)\)

where we introduced the arbitrary functions \(F_1,\ F_2\)

For consistency we require that \(F_1(y) = F_2(x) = \mathrm{const.}\) This allows us to write the given ODE as

\(\frac{\mathrm{d}}{\mathrm{d}x}\left(y\sin{x}+x\sin{y}+xy\right)=0\)

The solution is

\(y\sin{x}+x\sin{y}+xy=\mathrm{const.}\)

That is, \(F(x,y)=0\) where \(F(x,y)=y\sin{x}+x\sin{y}+xy+k\) and \(k\) is an arbitrary constant.

       

Questions for you to try

1. Show that $$\frac{\partial^2 f}{\partial y \partial x} = \frac{\partial^2 f}{\partial x \partial y}$$ for the following functions:

(a) $$f(x,y) = x^2-xy+y^2$$

(b) $$f(x,y)=x(y-x)\sin(x)$$

   

2. Given that $$f(x,y)=\sin(x^2+2xy)+(x-y)^2$$, calculate $$\frac{\partial f}{\partial x}$$ and $$\frac{\mathrm{d} f}{\mathrm{d}x}$$

   

3. Given that $$F=x^2\sin(y)$$, calculate $$\frac{\mathrm{d}F}{\mathrm{d}x}$$, giving your answer in the form \begin{equation}\frac{\mathrm{d}F}{\mathrm{d}x} = A(x,y)+B(x,y)\frac{\mathrm{d}y}{\mathrm{d}x}\end{equation}

and verify that $$\frac{\partial A}{\partial y}=\frac{\partial B}{\partial x}$$.

   

4. Given a general differential $$\mathrm{d}f=A(x,y)\mathrm{d}x+B(x,y)\mathrm{d}y,$$ state the condition for $$\mathrm{d}f$$ to be exact. Hence, determine whether the following are exact differentials:

(a) $$\mathrm{d}f=\frac{x}{x^2+y^2}\mathrm{d}y-\frac{y}{x^2+y^2}\mathrm{d}x$$

(b) $$\mathrm{d}f = y(1+x-x^2)\mathrm{d}x+x(x+1)\mathrm{d}y$$

(c) $$2x\sin(y)\mathrm{d}x+x^3\cos(y)\mathrm{d}y$$

   

Harder questions:

1. Show that the product and quotient rules can be deduced from the multivariate chain rule.

   

2. If $$V= x f\left(\frac{y}{x}\right)$$, show that

\begin{equation}x^2\frac{\partial^2 V}{\partial x^2}+2xy\frac{\partial^2 V}{\partial x \partial y}+y^2\frac{\partial^2 V}{\partial y^2}=0\end{equation}

   

3. Assume that $$\xi=\xi(x,y)$$ where $$x$$ and $$y$$ are given in plane polar coordinates $$(r,\theta)$$ so that

$$x=r\cos(\theta),\quad y=r\sin(\theta).$$

(a) Calculate $$\xi_r$$ and $$xi_{\theta}$$ in terms of $$\xi_x$$ and $$\xi_y$$, where a subscript denotes partial differentiatio with respect to the subscripted variable. Hence, show that

$$\left(\begin{array}{c}\xi_r\\\xi_{\theta}\end{array}\right)=J(r,\theta)\left(\begin{array}{c}\xi_x\\\xi_y\end{array}\right), \quad \text{where}\quad J(r,\theta)=\left(\begin{array}{cc}\cos(\theta)&\sin(\theta)\\-r\sin(\theta)&r\cos(\theta)\end{array}\right)$$

   

(b) Calculate the inverse of the matrix $$J(r\theta)$$ given in part (a) and deduce the results below:

\begin{align}\xi_x&=\cos(\theta)\xi_r - \frac{\sin(\theta)}{r}\xi_{\theta}\\\xi_y&=\sin(\theta)\xi_r+\frac{\cos(\theta)}{r}\xi_{\theta}\end{align}

  

(c) Use the relationships given below to calculate the first partial derivatives of $$r$$ and $$\theta$$ with respect to $$x$$ and $$y$$ and hence calculate $$\xi_x$$ and $$\xi_y$$ in terms of $$\xi_r$$ and $$\xi_{\theta}$$

\begin{align}r^2&=x^2+y^2\\\tan(\theta)&=\frac{y}{x}\end{align}