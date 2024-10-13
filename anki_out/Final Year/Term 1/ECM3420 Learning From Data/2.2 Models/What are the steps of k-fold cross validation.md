# What are the steps of k-fold cross validation
<details>
<summary><b>Reveal answer</b></summary>
1. Shuffle dataset<br>2. Split dataset into k groups<br>3. for each group:<br>- Use the group as a test set<br>- Use the remaining groups as a training set<br>- Fit the model on the training set, then evaulate model on the test set<br>- Store the evaluation score, then discard the model<br>4. Summarise model performance using the model evaluation scores.
</details>
