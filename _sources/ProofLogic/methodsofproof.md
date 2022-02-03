# Techniques of Proof

## Proof by Contradiction
This is a form of proof that seeks to establish if the validity of a proposition by showing that by assuming the proposition is false leads to a direct contradiction. 
We can summarise the technique as:

1. The statement to proven $P$ is assumed false, i.e. assume $\lnot{P}$ is true.
2. $\lnot P$ leads directly to assertions $Q$ and $R$, such that $R = \lnot Q$.
3. Since $Q$ and $\lnot Q$ cannot both be simultaneously true, $\lnot P$ is also untrue and hence $P$ is true.

By way of an example, consider this classic proof from Euclid:

<b>Statement:</b> There are infinitely many prime numbers

<b>Proof:</b> 
The <b>fundamental theorem of arithmetic</b> states that every positive integer (other than 1) can be represented in exactly one way (apart from rearrangement) 
as a product of one or more primes.  Assume there are $n$ finitely many prime numbers $p$, then consider the number $N$ composed of the product of all of the 
prime numbers from the first $p_1 = 2$ up to the largest $p_n$:
```{math}
N = p_1.p_2...p_{n-1}.p_n
```
Now consider the number $N+1$
```{math}
N+1 = p_1.p_2...p_{n-1}.p_n+1
```
Since $N+1$ is another whole number, it should be divisible by one of the prime numbers $p={p_1,p_2,\dots,p_n}$, but clearly it cannot be - hence contradiction.  Therefore 
there cannot be a finite number of primes and so there are an infinite number of primes. <b>QED</b>

## Proof by Counterexample
This is form of proof that disproves a proposition by giving an example which is a direct contradiction to the proposition.  This technique is often used to disprove a 
universal (or $\forall$ type) statement.  We can summarise the technique as:

1. The statement $P$ is shown to be satisfied by an example $E_1$ and it is assumed 
2. A further example $E_2$ is shown not to satisfy $P$ or leads directly to assertion $\lnot P$ being true.
3. Since $P$ and $\lnot P$ cannot both be simultaneously true, $P$ cannot be held to be always true (although can be shown to sometimes hold).

By way of an example, consider this classic proof:

<b>Statement:</b> $\forall n \in \mathbb{R}$, if $n^2$ is divisible by 4, then $n$ is divisible by 4.

<b>Proof:</b> 
We can find examples where this proof holds for both divisibility, e.g. $n=4$, $n^2 = 16$ and non-divisibility e.g. $n=5$, $n^2=25$.  

However a counter example to this statement would be given by $n = 6$, $n^2=36$, here the $n^2$ statement passes the test but $n$ statement in the 
proposition does not - hence the statement can be shown not be always true.  <b>QED</b> 

## Proof by Induction
This is a form of proof where a proposition, which is shown to be true for an initial case and a more general case $n$, which then allows a higher general 
case $n+1$ to be shown to be true.  This idea of a higher and higher steps on a proof ladder can be quite a powerful technique.  We can summarise the technique as:

1. A proposition $P_n$ is shown to be true for an initial or base case, i.e. we can prove that the statement holds for $0, 1$.
2. Assuming that the proposition is true for $P_n$, we can show that it is true for $P_{n+1}$.

By way of an example, consider this classic proof:

<b>Statement:</b> Prove that 

```{math} 
S_n = 1 + 2 + \dots + n = \frac{n(n+1)}{2}
```

<b>Proof:</b> 
$S_1 = \frac{1(2)}{2} = 1$ which is true, $S_2 = \frac{2(3)}{2} = 3$ which is also true. Assuming that $S_n$ is true, we need to see if we can prove $S_{n+1} = \frac{(n+1)(n+2)}{2}$:

```{math}
S_{n+1} &=&\, 1 + 2 + \dots + n + n+1 = S_{n} + n+1 \\ 
&=&\, \frac{n(n+1)}{2} + n+1 \\ 
&=&\, \frac{n(n+1) + 2(n+1)}{2} \\ 
&=&\, \frac{(n+1)(n+2)}{2}
``` 
<b>QED</b> 


## Proof by Contraposition
We can summarise this technique as:
1. Given a statement $P$ which leads directly to assertion $Q$, i.e. 
```{math} 
P \rightarrow Q 
```
2. First order tells us that the negation of statement $Q$, i.e. $\neg Q$ leads directly to the negation of assertion $P$, i.e. $\neg P$, 
```{math}
\neg Q \rightarrow \neg P
```

By way of an example, consider this classic proof:

<b>Statement:</b> Prove that for $x \in \mathbb{R}$, if the function $x^2 - 6x + 5$ is even, then $x$ is odd.

<b>Proof:</b> Suppose $x \in \mathbb{R}$ is even, when we need to show $x^2 - 6x + 5$ is odd.  
Lets write $x = 2a$ with some $a \in \mathbb{Z}$, then we find that:
```{math}
x^2 - 6x + 5 &=& (2a)^2 - 6(2a) + 5 \\
&=& 4a^2 - 12a + 5 \\
&=& 2(2a^2 - 6a + 2) + 1
```
which we can see clearly is odd.  Thus when $x^2 - 6x + 5$ is odd, $x$ is even and therefore when $x^2 - 6x + 5$ is even, $x$ is odd. <b>QED</b> 

## Proof By Construction
We can summarise this technique as:
1. Given a statement $P_1$, we construct  $P_2,\,P_3,\,\dots,\,P_n$ which leads to assertion $Q$,
```{math}
    \{P_1,\,P_2,\,P_3,\,\dots,\,P_n\} \vdash Q
```

<b>Statement:</b> Prove that for $x \in \mathbb{R}$, if the function $x^2 - 6x + 5$ is even, then $x$ is odd.

<b>Proof:</b> For $x \in \mathbb{R}$, lets write $x^2 - 6x + 5 = 2a$ with some $a \in \mathbb{N}$, so that $x^2 - 6x + 5$ is even, then we find that:
```{math}
x^2 - 6x + 5 &=& 2a  \\
x^2 - 6x &=& 2a - 5 \\
x(x-6) &=& 2a - 5
```
Since the RHS is clearly odd by construction, this means the LHS is odd.  Given that ODD $\times$ ODD = ODD, then given $x$ and $x-6$ differ by an even numbers, $x$ must be an odd number. <b>QED</b> 


### Number Theory Types of Construction
Sometimes instead of directly proving a proposition, we can construct facts about the proposition which the lead to the answer.  This is often employed 
when we have to prove some facts about numbers, for example lets try to prove that:
```{math}
a^5 = 10m + a,\quad {a,\,m,} \in \mathbb{Z}
```
We could argue that this can be proved by induction, with proposition 
```{math}
P_a: a^5 = 10m + a,\, a,\,m \in \mathbb{Z}
```
and given the starting cases: 
```{math}
1^5 &=&\, 1 = 10(0) + 1 \\
2^5 &=&\, 32 = 10(3) + 2 \\
3^5 &=&\, 243 = 10(24) + 3
```
which works and therefore to shown the proposition true, we need to work out $(a+1)^5$:
```{math}
(a+1)^5 &=&\, a^5 + 5a^4 + 10a^3 + 10a^2 + 5a + 1 \\
&=&\, 10m + a + 10a^3 + 10a^2 + 5a^4 + 5a + 1 \\
&=&\, 10(m + a^2 + a^4) + 5a(1 + a^3) + a + 1 
```
and we can then argue that $\forall \,a \in \mathbb{Z},\, a(a^3+1)$ is an EVEN number - if $a$ is ODD then $a^3+1$ is EVEN and so $a(a^3+1)$ is EVEN 
and likewise if $a$ is EVEN, $a(a^3+1)$ is EVEN, hence we have:
```{math}
(a+1)^5 = 10m' + a + 1,\quad a,\,m' \in \mathbb{Z}
```
which is $P_a\Bigg|_{a \rightarrow a+1}$ and hence proven.  

However lets explore the numbers a little deeper here, lets start with what happens if we square the first 10 natural numbers:
```{math}
1 &\rightarrow&\, 1\\
2 &\rightarrow&\, 4\\
3 &\rightarrow&\, 9\\
4 &\rightarrow&\, 16\\
5 &\rightarrow&\, 25\\
6 &\rightarrow&\, 36\\
7 &\rightarrow&\, 49\\
8 &\rightarrow&\, 64\\
9 &\rightarrow&\, 81\\
10 &\rightarrow&\, 10
```
We notice that the last digit of the square numbers is always one of ${0,\, 1,\, 4,\, 5,\, 6,\, 9}$, the digits ${2,\, 3,\, 7,\, 8}$ never 
enter in to this.  Likewise we could keep going to cube numbers and quartic powers etc, but lets just think about what happens when we take 
numbers to higher an higher powers and what that last digit does, as outlined in {numref}`cycliclastdigits`.  

```{figure} ../figures/cycliclastdigits.png
---
name: cycliclastdigits
---
The effect of higher and higher powers on the last digit of an integer.
```
We see that some digits under increasing integer powers return back to the same digit immediately (e.g. $6 \rightarrow 6$), others take 
another digit first (e.g. $9 \rightarrow 1 \rightarrow 9$) and some go through up to four other digits (e.g. $2 \rightarrow 4 \rightarrow 8 \rightarrow 6 \rightarrow 2$), 
therefore for <em>any</em> digit, to guarantee the digit has returned we must raise the power to five, that's why $a^5$ will have a righthand digit 
equal to $a$ plus another number that has a factor of ten, shifting it along to the higher digits.

