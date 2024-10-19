## What is the order of coordinate systems and their respected transformation matrixes (just the names of the transition matrixes)?
<details>
<summary><b>Reveal answer</b></summary>
Local space -[Model matrix]-&gt; world space<br><br>world space -[view matrix]-&gt; view space<br><br>view space -[projection matrix]-&gt; clip space<br><br>clip space -[viewport transform]-&gt; screen space
</details>
