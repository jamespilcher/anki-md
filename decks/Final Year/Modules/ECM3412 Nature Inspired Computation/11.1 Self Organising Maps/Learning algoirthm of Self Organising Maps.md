## Learning algoirthm of Self Organising Maps
<details>
<summary><b>Reveal answer</b></summary>
1. Initialise network<br>- Set weights to small random values<br>- Define large neighbourhood size<br><br>Repeat until converges:&nbsp;<br>2. Sample random input (xt) from the data and input to the network<br>3. Compute the Euclidean distance of each output node j's weights from the current input using<br><br>d(xt, wj) = root[ SUM [ (xi-wij)^2 ] ]<br><br><img src="../../../../../media/paste-71bc81ecb9cfeafd6b3e613bddb29b75672acd54.jpg"><br><br>4. Identify the node closest to the input (the best matching unit - BMU)<br>5. Adjust the weights of the BMU and its neighbours with<br>wij(t+1) = wij(t) + n(t)(xij(t) - wij(t))<br><img src="../../../../../media/paste-c1f0a6afd5b7631e97f7c7612876b9c9ea664350.jpg">
</details>
