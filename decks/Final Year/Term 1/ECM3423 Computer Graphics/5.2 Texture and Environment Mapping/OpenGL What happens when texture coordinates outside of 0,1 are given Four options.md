## OpenGL What happens when texture coordinates outside of 0,1 are given? Four options:
<details>
<summary><b>Reveal answer</b></summary>
GL_REPEAT: Pattern is repeated periodically<br>GL_MIRRORED_REPEAT: Texture is flipped in alternance<br>GL_CLAMP_TO_EDGE: Coord is clamped to 0,1<br>GL_CLAMP_TO_BORDER: Anything outside of 0,1 set to a default value<br><br><img src="../../../../../media/paste-5e395d67b5169404d724b5d8b5e2e36e5dc0463b.jpg">
</details>
