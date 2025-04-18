## Updating the archive algo
<details>
<summary><b>Reveal answer</b></summary>
Given a new solution y<br>For each solution ai in the archive At:<br>- If y dominates ai; then remove ai<br>- If ai dominates y then proceed to the next memeber of At and mark y as dominated<br><br>If y is not marked as dominated add it to At
</details>
