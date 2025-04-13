## Z buffer (depth buffer) Algorithm steps
<details>
<summary><b>Reveal answer</b></summary>
Initialise all elements of Zbuf to max-depth<br><br>For each polygon P in the model<br>&nbsp; &nbsp; transform vertices of P to 3D screen coords (x,y,z)<br>&nbsp; &nbsp; if zs &lt; Zbuf(xs,ys) for a vertex:<br>&nbsp; &nbsp; &nbsp; &nbsp; Zbuf(xs,ys) = zs<br>&nbsp; &nbsp; &nbsp; &nbsp; shade the polygon (in screen coords) by interpolating vertex shades
</details>
