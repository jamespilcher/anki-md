## MIP Mapping steps, and note on cost
<details>
<summary><b>Reveal answer</b></summary>
1. Precompute (before rendering) generate subsampled copies of the texture map (over lower and lower resultions)<br>2. At runtime:<br>Select a texel from the appropriately sampled map based on distance<br>- Surface close to camera, use high resolution<br>- If far away, use low resolution<br>- Linear interpolution beteween levels improve quality<br><br><br>not: Cost is constant per pixel
</details>
