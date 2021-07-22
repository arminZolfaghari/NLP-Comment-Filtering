# NLP Comment Filtering
Artificial Intelligence Course 4th Project: Implementing Bigram and Unigram models for filtering comments.
<br>
In this group project we ([Amirhossein-Rajabpour](https://github.com/Amirhossein-Rajabpour) and [arminZolfaghari](https://github.com/arminZolfaghari)) 
implemented `Bigram` and `Unigram models` to filter comments.<br>

We trained these models on these [positive](https://github.com/arminZolfaghari/NLP/blob/main/dataset/rt-polarity.pos) and [negative](https://github.com/arminZolfaghari/NLP/blob/main/dataset/rt-polarity.neg)
datasets. We also used `smoothing` in both models (you can change coefficients). For preprocessing first we removed punctuation marks and we also have a `cut_down` parameter which specifies
that words with equal or less number of repetition to this parameter should be removed. Also there is a `cut_above` parameter that specifies that how many of most repeated words 
should be removed.
<br>
<br>
A sample run:

![alt text](https://github.com/arminZolfaghari/NLP/blob/main/sample%20run.jpg "sample run")


Check full description [here](https://github.com/arminZolfaghari/NLP-Comment-Filtering/blob/main/AI_P4.pdf)

Project report (in persian): tried different coefficients and tried the models with and without cut_down and cut_above and checked the results [here](https://github.com/arminZolfaghari/NLP-Comment-Filtering/blob/main/AI_P4_Report.pdf) 

Check our other AI Course projects:
* [Project 1: Searching Algorithms (IDS, BBFS, A*)](https://github.com/arminZolfaghari/AI_project1)
* [Project 2: Genetic-Algorithm](https://github.com/Amirhossein-Rajabpour/Genetic-Algorithm)
* [Project 3: Constraint-Satisfaction-Problems](https://github.com/Amirhossein-Rajabpour/Constraint-Satisfaction-Problems)
