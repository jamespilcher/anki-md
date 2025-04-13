## Brewer's observaction CAP (consistency, availability, partition tolerance) theorem might apply to migrating monolith to microservices
<details>
<summary><b>Reveal answer</b></summary>
When migrating, teams can only choose two of:<br><ul><li><b>Consistency </b>- all clients see the same data at the same time, no matter which node they conenct to</li><li><b>Availability </b>- Any client making a request for data gets a response from a node, even if others are down</li><li><b>Partition Tolerance</b> - the system must continue to work despite communication breakdowns between nodes.</li></ul><div>AP normally chosen... eventually consistent...</div>
</details>
