## PSO how to determine the new velocity?
<details>
<summary><b>Reveal answer</b></summary>
vij(1+1) = vij + c1 * z1 * (pij - xij) + c2 + z2 * (gj - xij)<br><br><img src="../../../../../media/paste-29a99ebcfbe8d48a657e0c9bbb2e03746c074b63.jpg"><br><br>vij - current velocity<br><br><br>(pij - xij) difference between particles best position and current positoin<br><br>(gj - xij) difference between population's best postion and current position<br><br>c1 and c2 - constants controlling weighting between personal and global best<br><br>z1 and z1 - U(0,1) are two random draws from uniform distribution.<br>
</details>
