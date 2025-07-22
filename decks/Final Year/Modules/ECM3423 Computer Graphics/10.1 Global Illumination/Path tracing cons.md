## Path tracing cons
<details>
<summary><b>Reveal answer</b></summary>
<li><div><strong>Sampling is expensive</strong>: You can simulate <strong>infinitely many</strong> possible light paths, but...</div> <ul> <li> <div>You can only afford to simulate <strong>a few thousand per pixel</strong> in practice</div> </li> <li> <div>And you’re picking <strong>paths randomly</strong>, so it’s noisy at low samples</div> </li> </ul> </li> <li> <div><strong>Performance hit</strong>: Complex scenes = many bounces = many rays = long render times</div></li>
</details>
