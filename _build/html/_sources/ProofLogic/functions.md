## Functions

We are probably quite used to thinking about functions when we plot graphs, such as $y = x^2$ or $y = \cos(x)$:
\begin{center}
    \includegraphics[scale=1]{x2cosx.png}
\end{center}
These are examples of a much richer mathematical structure, known as {\bf Functions}, which we can roughly think of as a machine with inputs and outputs:
\begin{center}
    \includegraphics[scale=1]{FunctionMachine2.png}
\end{center}

### Definition of a Function
\noindent To set this up in a firmer mathematical way, we can think about functions as the mapping of elements between different sets.  
Lets denote the set $A$, which contain the elements we wish to map unique to elements in another set $B$, this mapping will be the function $f$ from $A$ to $B$:

\bea
f:\,A \rightarrow B
\eea
 which we read as "$f$ is a function from $A$ to $B$".  The elements of the set $A$, which we think of as the range of values in the inputs, is known as the {\bf Domain} of the function and elements of the set $B$, which we think of as the range of values of the outputs are known as the {\bf Target set} or {\bf Co-Domain} of the function.  
 
 
 \newpage
 
\noindent There are several notations for functions:\\
 
 \begin{center}
    \begin{tabular}{  c | c  } 
    Notation & Meaning \\\hline
    $f(x) = x^2$ & $x$ as a variable for the function $f$\\
    $x \mapsto x^2$ & $x$ goes into $x^2$ \\
    $y = x^2$ & $x$ is the independent variable and\\ & $y$ is the dependent variable 
    \end{tabular} 
    \end{center}
 $\,$\newline
 
 \noindent Given a function $f:\, A \rightarrow B$, then for an element $a \in A$ the function $f(a)$ maps $a$to a unique element in $b \in B$. \\
 
 \noindent We call $f(a)$ the {\bf Image} of $a$ under $f$, or $d(a)$ is the {\bf Value} of $f$ at $a$ or that $f$ {\bf Sends} or {\bf Maps} $a$ into $f(a)$.  \\
 
 \noindent The set of all image values is called the {\bf Range} or {\bf Image} of $f$, which is denoted as 
 \bea
 \text{Im}(f) = \text{Ran}(f) = f(A) = \{b \in B\,:\, \text{there exists }\, a \in A \,\,\text{for which }\, f(a) = b\}
 \eea
 and we should make clear that $\text{Im}(f) \subset B$.\\
 
\noindent Given $f: A \rightarrow B$, then for some subset $A' \subset A$. $f(A')$ denotes the set of images of elements in $A'$ and if $B' \subset B$ and $f^{-1}(B')$ denotes the set of elements of A each whose image belongs to $B'$:
  \bea
 f(A') = \{f(a)\,:\,a \in A\} && f^{-1}(B') = \{a\in A\,:\,f(a)\in B\}
 \eea
given we call $f(A')$ the imagine of $A'$, we call $f^{-1}(B')$ the {\bf inverse image} or {\bf preimage} of $B'$.\\

\noindent We also define an {\bf Identity} function $I_A$, which simply send an element back to itself, $I_A:\,A \rightarrow A$
\bea
I_A(a) = a
\eea
for every element $a \in A$.\\

\noindent Finally we can define the {\bf graph} of a function $f:\,A \rightarrow B$ as the series of order pairs of elements $a \in A$ mapped to elements $b = f(a) \in B$
\bea
\text{Graph of }\,f = \{(a,\,b)\,:\, a \in A,\,b = f(a)\}
\eea


\newpage 


\noindent A function $f$ is defined from a set $A = \{a,\,b,\,c,\,d\}$ into a set $B = \{r,\,s,\,t,\,u\}$. with a mapping 
\bea
f(a) &=& s \\
f(b) &=& u \\
f(c) &=& r \\
f(d) &=& s
\eea
which we can represent graphically as:
\begin{figure}[h!]
    \centering
    \includegraphics[scale=1]{FunctionImage.png}
\end{figure}
The image $f$ is the set $\text{Im}(f) = \{r,\,s,\,u\}$ and the element is $t \notin \text{Im}(f)$ because $t$ is not the image of any element of $A$ under $f$ - therefore any elements not mapped {\it to} under a function are excluded from the image of the function.\\

\noindent The graph of $f$ is the following set of ordered pairs:
\bea
\{ (a,\,s),\,(b,\,u),\,(c,\,r),\,(d,s) \}
\eea

## Composite Functions
Using the idea of mapping from one set to another, it is possible to introduce functions of functions or {\bf composite functions}, mapping from one set to another, through some intermediate set.  Consider functions $f:\,A \rightarrow B$ and $g:\,B \rightarrow C$, where the target set $B$ of $f$ is the domain of $g$.  We can call this new function the {\bf composition} of $f$ and $g$, denoted by:
\bea
g \circ f \equiv g(f(a)
\eea
where we emphasise that the composition of functions is read from right to left (and not left to right as we usually do).  We can picture this as follows:
\begin{figure}[h!]
    \centering
    \includegraphics[scale=0.8]{compositefunction.png}
\end{figure}
We can introduce more and more functions and same rules apply, however we can also consider the associativity of the composition of functions, given $f:\,A \rightarrow B,\,g:\, b \rightarrow C,\,h:\,c \rightarrow D$
\bea
h \circ(g \circ f) = (h \circ g) \circ f
\eea
which we can prove diagrammatically:
\begin{figure}[h!]
    \centering
    \includegraphics[scale=1]{associativitycompositefunctions.png}
\end{figure}


Lets think about two simple functions:
\bea
f(x) &=& x^2\\
g(x) &=& \cos(x)
\eea
We can composite these functions by writing:
\bea
f(g(x)) = (f \circ g)(x) &=& (\cos(x))^2 \\
g(f(x)) = (g \circ f)(x) &=& \cos(x^2)
\eea
where we notice that in general $f(g(x)) \neq g(f(x))$.  These composite functions can be built up by looking at the function on the {\it furthest right} and then adding more functions on to the {\it left hand side}.  Suppose we introduce a third function:
\bea
h(x) = \frac{2}{x}
\eea
then the six different functional compositions would be:
\bea
\begin{array}{ll}
f \circ (g \circ h) = \left( \cos \left( \frac{2}{x} \right) \right)^2 & f \circ (h \circ g) = \left( \frac{2}{\cos(x)} \right)^2 \medskip\\ 
g \circ (h \circ f) = \cos \left( \frac{2}{x^2} \right) & g \circ (f \circ h) = \cos \left( \left( \frac{2}{x}\right)^2  \right) \medskip\\ 
h \circ (f \circ g) = \frac{2}{\left( \cos (x) \right)^2 } & h \circ (g \circ f) = \frac{2}{\cos(x^2)}
\end{array}
\eea
and we see that the associativity of these composites can be shown to be true:
\bea
&& f\circ g = (\cos(x))^2\\
&& g \circ h = \cos\left(\frac{2}{x}\right) \\ 
&& f \circ (g \circ h) = (f \circ g) \circ h = \left( \cos \left( \frac{2}{x} \right) \right)^2
\eea

\newpage

## Invertibility of Functions
A function $f:\,A \rightarrow B$ is said to be {\bf one-to-one} or {\bf injective} if different elements in the domain $A$ have distinct images, i.e.
\bea
f\,\text{ is one-to-one if }\,f(a) = f(a') \Rightarrow a = a'
\eea
Likewise we can set up a function $f:\,A \rightarrow B$ is said to be an {\bf onto} function or {\bf surjective} if every element $b \in B$ is the image of some element $a \in A$, i.e. the image of $f$ is the {\it entire} target set $B$:
\bea
f\,\text{ maps }\,A \text{ onto }\,B\,\text{ if }\,\forall\, b \in B,\, \exists \,a \in A, \,\text{ s.t.}\, f(a) = b
\eea
A function $f:\,A \rightarrow B$ is said to be {\bf invertible} if there exists a function $f^{-1}:\, B\rightarrow A$ such that:
\bea
f^{-1} \circ f = I_A \Longleftrightarrow f \circ f^{-1} = I_B
\eea
A function $f:\,A \rightarrow B$ is invertible iff $f$ is both one-to-one and onto.  We say such functions are a {\bf one-to-one correspondence} between $A$ and $B$.  This is also known as a {\bf bijection}.


Lets consider functions $f_1:\,A \rightarrow B$, $f_2:\,B \rightarrow C$, $f_3:\,C \rightarrow D$, $f_4:\,D \rightarrow E$ depicted below:

\begin{figure}[h!]
    \centering
    \includegraphics[scale = 0.75]{InvertibilityOfFunctions.png}
\end{figure}

\begin{itemize}
    \item $f_1:\,A \rightarrow B$ is one-to-one but not onto, since every element in $A$ has a unique image, but element $3 \in B$ does not have any image under $f_1$.
    \item $f_2:\,B \rightarrow C$ is both one-to-one and onto, i.e. it is a onto-to-one correspondence for all elements in $B$ and $C$ and thus $f^{-1}:\, C \rightarrow B$ exists.
    \item $f_3:\,C \rightarrow D$ is not one-to-one but is onto since $f_3(r) = f_3(u) = v$, but every element in $D$ has an image under $f_3$. 
    \item $f_4:\, D \rightarrow E$ is neither one-to-one nor onto, since $f_4(v) = f_4(w) = z$ and there are elements in $E$ which are not images under $f_4$.
\end{itemize}
    