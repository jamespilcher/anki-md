## Two-phase commit explained
<details>
<summary><b>Reveal answer</b></summary>
Using a two-phase commit, a coordinator transaction asks a number of participant transactions to vote on whether they are prepared to commit to a change<br><br>Each participant holds locks on its data involved in the transaction until the coordinator decides to commit or abort.<br><br>Slow things down! everyone has to wait!<br><br><img src="../../../../../media/paste-e3f88ee92cef6135e67857ee0268e025355e8bd4.jpg">
</details>
