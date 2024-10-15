## When does poisoned reverse not work? How did the engineers fix this?
<details>
<summary><b>Reveal answer</b></summary>
If there are more than 1 hop, it does not work.<br>The engineers add a counter to how many hops have been made. then theres a max number of hops (15 or 31) after which the packet is destroyed
</details>
