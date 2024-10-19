## Algorithm for generating a random program using:&nbsp;<img src="../../../../../media/paste-2bc8128d180cee1bd5e9881abbd0d6f8a856c72b.jpg">
<details>
<summary><b>Reveal answer</b></summary>
Define a max depth<br>Initialise a random member of F for the root - set depth 1<br>Reapeat:<br>- Choose function node X which does not have children<br>- If depth of node is &lt; max depth - 1:<br>&nbsp; &nbsp; - Randomly select appropriate child (from T or F) and set their depth to parent depth + 1<br>- If depth of node is max depth - 1:<br>&nbsp; &nbsp; - Randomly select child from T
</details>
