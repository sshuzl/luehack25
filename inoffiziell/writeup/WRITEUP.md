# inoffiziell - Writeup

We are given a network capture and the source code of the server.

From the source code we learn that it implements a symmetric challenge-response-scheme.
The secret $k$ is a vector of $n=40$ integers $k = (k_1, k_2, \cdots, k_{n})$ where each vector entry $k_i$ was chosen randomly from $\mathbb{Z}_p$ for a given 128-bit prime $p$.
When a client provides the server with a correct response for a challenge, i.e., it proves that it knows $k$, then the server uses $k$ to encrypt the flag and transmits the encrypted flag to the client.

Each challenge $c$ consists of $n=40$ values $c = (c_0, \cdots, c_n)$ where each $c_i$ is again chosen randomly from $\mathbb{Z}_p$.
The correct response $r$ for a given challenge $c$ is computed as

$$r = \sum_{i=1}^{40}(c_i\cdot k_i \bmod p).$$

So our goal is to learn the unknown values $k_i$.
If we take a look at the given network capture file, we find the communication of a client that talks to the server. The client solves 40 challenges by providing the correct response and receives the encrypted flag every time.

The good thing for us is, that the capture contains all challenge and response values in plaintext. That means that we have 40 equations and since we need to learn 40 unknown values, we just have to solve the resulting equation system. This can easily be done with Sagemath. The hardest part is parsing the given capture file to extract the challenge an response values.

Given all challenge values in a matrix `C` and all response values in a vector `r`, then we can compute the key $k$ as follows using Sagemath:

```python
k = C.solve_right(r)
```

A complete implementation of the solution including the capture parsing (pased on Wireshark's CLI implementation `tshark`) is provided in `solve.py`.
