## Graham's Scan Algorithm explained
<details>
<summary><b>Reveal answer</b></summary>
1. Start from left most point<br>2. Set up an orientation tournament. Calculate all polar angles from start point and, sort in ascending order. Then iterate through;<br>Are Pp, Cp, and Np CCW?<br>Are the previous point (in the stack), current point and next point creates a CCW turn.<br><br>otherwise discard.<br>3. Terminate if the next point is the starting point
</details>
