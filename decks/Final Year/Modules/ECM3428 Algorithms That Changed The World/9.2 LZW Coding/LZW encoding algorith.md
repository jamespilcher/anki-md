## LZW encoding algorith
<details>
<summary><b>Reveal answer</b></summary>
Input a message<br>Repeat:<br>- From the current symbol, check the sequence composed of itself and the immediately subsequent symbols, stop until the longest match (w) is found in the dictionary<br>- Output the codeword for w<br>- Add w + nextSymbol into the dictionary (as a new key)<br><br>output the codewords
</details>
