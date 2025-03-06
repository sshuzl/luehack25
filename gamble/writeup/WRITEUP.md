# gamble - Writeup

While reading up on the [Decisional Diffie Hellman assumption](https://en.wikipedia.org/wiki/Decisional_Diffie%E2%80%93Hellman_assumption) we learn that there are groups for which DDH is assumed to hold and that there are groups for which DDH does not hold.

The Wikipedia article states:
> Importantly, the DDH assumption does not hold in the multiplicative group $\mathbb{Z}_{p}^{*}$, where $p$ is prime. This is because if $g$ is a generator of $\mathbb{Z}_{p}^{*}$, then the Legendre symbol of $g^{a}$ reveals if $a$ is even or odd. Given $g^{a}$, $g^{b}$ and $g^{ab}$, one can thus efficiently compute and compare the least significant bit of $a$, $b$ and $ab$, respectively, which provides a probabilistic method to distinguish $g^{ab}$ from a random group element.

So this is what we do: a probabilistic test to decide the game. The Python library `sagemath` provides the `kronecker` symbol, which is a generalization of the Jacobi symbol, which in turn is a generalization of the Legendre symbol. With its help, we mainly have to implement the communication with the server.

The final implementation of the solution is containes in `solve.py`.
