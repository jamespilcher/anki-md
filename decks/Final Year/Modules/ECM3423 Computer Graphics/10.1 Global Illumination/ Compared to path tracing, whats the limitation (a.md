## Compared to path tracing, whats the limitation (and benefit!) of ray tracing, in terms of the way the it approximates the integral below<br><img src="../../../../../media/paste-b95d309099573fbe4e58306d69b12ee77443f6ae.jpg">
<details>
<summary><b>Reveal answer</b></summary>
Ray tray tracing approximates by the summation of the contribution of 3 terms (at most)<br>- Speculart reflection<br>- refraction<br>- diffuse (non recursive)<br><br>Only considers 3 terms...<br>Benefit: Ignores the complex global illumination - computationally simpler, more performant.
</details>
