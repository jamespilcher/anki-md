## Algorithm steps for downhill simplex
<details>
<summary><b>Reveal answer</b></summary>
Select initial simplex<br>Repeat until converge:<br>- Order verticies according to f(W) &gt;= f(G) &gt;= ... &gt;= f(B)<br>- Centroid of the best side: C = 1/2 SUM(B + G +...)<br>- Transform simplex:<br>&nbsp; &nbsp; - See if replace W by reflection, expansion, contraction<br>&nbsp; &nbsp; - Otherwise shrink simplex towards B
</details>
