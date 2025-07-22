## Explain the scan line algorithm for filling
<details>
<summary><b>Reveal answer</b></summary>
For each scan line:<br>- Find intersections of scan line with all polygon edges<br>- Sort intersections into increasing order of x coordinate<br>- Fill alternate segments of scan line (spans) according to parity rule
</details>
