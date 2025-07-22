## Z buffer (depth buffer) algorithm idea
<details>
<summary><b>Reveal answer</b></summary>
<div>A depth value is stored for every pixel on the screen.<br></div><div><br></div><div> For each fragment, the Z-buffer keeps track of the depth (distance to the camera) of the closest surface so far.</div><div><br> When drawing a new fragment, if it is closer than the stored depth, update the color and depth for that pixel. Otherwise, discard it.</div>
</details>
