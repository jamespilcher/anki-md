## Diffie-Hellman Key Exchange explained
<details>
<summary><b>Reveal answer</b></summary>
two shared numbers are <strong>chosen</strong>: the base and the (prime) modulus<br><br>g, p<br><br>Alice has a private key a<br><br>Bob has a private key b<br><br>Alice shares a number:<br><br>A = g^a mod p<br><br>Bob shares a number:<br><br>B = g^b mod p<br><br><br>Alice deduces the shared key using bobs number<br><br>B^a mod n = (g^b)^a mod p<br><br>Alice deduces the shared key using alices number<br><br>A^b mod n = (g^a)^b mod p
</details>
