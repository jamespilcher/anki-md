## LZW decoding algortihm
<details>
<summary><b>Reveal answer</b></summary>
1. Input the received sequence of codewords<br>2. Repeat until end of that sequence:<br>- Find the sequence to the current codeword from the dictionary and output it. Insert the ""prior sequence + first letter of current sequence"" to the dictionary""<br>- If the current codeword does not exist in the dictionary, generate its entry: insert ""prior sequence + first letter of the prior sequence"" then use it to decode the current word<br>- Update the prior sequence with the current sequence<br>3. output the encoded codewords
</details>
