## Sagas explained
<details>
<summary><b>Reveal answer</b></summary>
Solution to two-phase commit locking.<br><br>A coordinator transaction asks each participant to commit or abort in sequence.<br><br>If one aborts, the sequence end and compensating transactions are made to undo the work of those participants.<br><br>Eventual consistency
</details>
