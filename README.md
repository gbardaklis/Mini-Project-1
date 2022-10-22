# Emotion and Sentiment Classification of Reddit Posts

## Team Members
| Name               | Student ID    | Github Account   |
| -------------      | ------------- |-------------     |
| Georgia Bardaklis  | 40096586      | gbardaklis       |
| Daniel Baggs       | 40046045      | DanielWill-Baggs |
| Lina Tran          | 40130446      | linatran1        |

## Github repository:
https://github.com/gbardaklis/Mini-Project-1

## Instructions on how to run our program:
- All tasks were completed using Google Colab (https://colab.research.google.com/).
- Opening the notebook files in Colab will ensure that the same environment is being used.

### Task 1: Dataset Preparation & Analysis
- Task 1 was completed in the `Q1&Q2.ipynb` file
- Open the notebook file in Colab
- Once opened, make sure to upload the `goemotions.json` to session storage
- In the third cell, ensure the path to the `goemotions.json` aligns with its true location
- ![Screen Shot 2022-10-22 at 4 10 51 PM](https://user-images.githubusercontent.com/43450986/197360605-f5a2768d-381d-4288-87e9-1d8d67dcf285.png)
- Now you can run every cell before the Task 2 heading

>Note: the commented cells in Task 1 do not need to be run, they were for exploration purposes.

### Task 2: Words as Features
- Task 2 was completed in the `Q1&Q2.ipynb` file
- This task follows the first task and therefore Task 1 must be run for Task 2 to be run
- Once Task 1 has been run, all cells past the Task 2 heading 
- 2.4 will create and write to a file called `performance.txt`
- 2.5 will create and write to a file called `experiment.txt`

### Task 3: Embeddings as Features
- Task 3 from 3.1 to 3.7 was completed in the `Q3Embeddings_as_Features.ipynb` file
- Open the notebook file in Colab
- Once opened, make sure to upload the `goemotions.json` to session storage
- In the third cell, ensure the path to the `goemotions.json` aligns with its true location
- ![Screen Shot 2022-10-22 at 4 10 51 PM](https://user-images.githubusercontent.com/43450986/197360605-f5a2768d-381d-4288-87e9-1d8d67dcf285.png)
- Run cells 1 through 4 prior to everything else as they are a prerequisite to section 3
- 3.1 make sure to load `word2vec-google-news-300` model using `gensim.downloader.load`
- Run remaining cells in order
- 3.7 will create and write to a file called `performanceTxt.txt` as a requirement for the trained Base-MLP of 3.5
- 3.7 will create and write to a file called `performanceTop.txt` as a requirement for the trained Top-MLP of 3.6
- 3.8 was completed in the `Q3Embeddings_as_Features_Wiki_GigaWord_Model.ipynb` and `Q3Embeddings_as_Features_Wiki_News_Model.ipynb`
- Open the notebook `Q3Embeddings_as_Features_Wiki_GigaWord_Model.ipynb` file in Colab
- Once opened, make sure to upload the `goemotions.json` to session storage
- In the third cell, ensure the path to the `goemotions.json` aligns with its true location
- ![Screen Shot 2022-10-22 at 4 10 51 PM](https://user-images.githubusercontent.com/43450986/197360605-f5a2768d-381d-4288-87e9-1d8d67dcf285.png)
- Run cells 1 through 5 prior to everything else as they are a prerequisite to section 3
- make sure to load `glove-wiki-gigaword-300` model using `gensim.downloader.load`
- Run remaining cells in order
- The last cell will create and write to a file called `performanceWordEmb_Wiki_GigaWord.txt` using the best performing model Base-MLP
- Repeat the same steps for `Q3Embeddings_as_Features_Wiki_News_Model.ipynb` ensuring to load `fasttext-wiki-news-subwords-300` model using `gensim.downloader.load`
