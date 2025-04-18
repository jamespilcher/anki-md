## Tesellation control shader -&gt; Tesellation&nbsp;primitive generator -&gt; Tesellation&nbsp;evaluation shader<br>explained
<details>
<summary><b>Reveal answer</b></summary>
Tessellation control shader (TCS):<br>- determines how much tessellation to do<br>- Ensuring contuinity across patches<br><br>Tessellation primitive generator takes the input patch and subdivides it based on values computed by the TCS<br><br>The Tessellation Evaluation Shader (TES) takes the tessellated patch and computes the vertex values for each generated vertex
</details>
