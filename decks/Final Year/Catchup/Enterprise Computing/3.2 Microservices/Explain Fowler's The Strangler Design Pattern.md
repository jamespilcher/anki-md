## Explain Fowler's The Strangler Design Pattern
<details>
<summary><b>Reveal answer</b></summary>
How teams might migrate from a monolithic MVP to a microservices one.<br><br>Put a facade in front of the monolith which serves as a proxy that manages all communication between them, then slowly replace the modules behind it. If one fails, just change the facade to route back to the modules. Go one at a time.<br><img src="../../../../../media/paste-de53d5cf166272dc2e3dc5889004e6cb88749581.jpg">
</details>
