## What is a Two-phase commit explained
<details>
<summary><b>Reveal answer</b></summary>
- A coordinator transaction asks participant transactions to vote on whether they are prepared to commit to a change<br>- While waiting for the vote to end, Each participant holds locks on its data.<br>- If one says no, then no commit is made by the coordinator and they all abort<br>Slow things down! everyone has to wait!<br><br><img src="../../../../../media/paste-e3f88ee92cef6135e67857ee0268e025355e8bd4.jpg">
</details>
