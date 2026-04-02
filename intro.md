# Data Science Workflow and Applications
*Summer Term 2026* - BHT Berlin - Room: D 139 (?)<br>
[Moodle Course](https://lms.bht-berlin.de/course/view.php?id=37443)

This course will cover end-to-end lifecycle of a Data Science project. The course will be structured in two parts: the first part will cover more general data science workflow topics, teaching you about modern MLOps practices. The second part will be focused on recommender systems, where you will learn about different approaches to building recommendation engines. For your final project, you will be expected to apply the concepts and tools covered in the lectures to build a recommender system for a dataset of your choice (More under: [Final Project](#final-project)).

## Course Structure

Part 1 of the lecture *Data Science Workflow and Applications* will include 5 sessions covering the following topics:

| Date        | Topics                                                                    |
| ----------- | ------------------------------------------------------------------------- |
| 09.04.2026  | [Data Acquisition and Labeling](DSW-sessions/session1_data_acquisition.ipynb)          |
| 16.04.2026  | [Kubernetes Cluster and Experiments Logging](DSW-sessions/session2_cluster.ipynb)      |
| 23.04.2026  | [Data Exploration, Preprocessing & Quality](DSW-sessions/session3_data_quality.ipynb)  |
| 30.04.2026  | [Model Training and Evaluation](DSW-sessions/session4_model_training_evaluation.ipynb) |
| 07.05.2026  | [Dashboards and Demos](DSW-sessions/session5_demos.ipynb)                              |

Starting from 14.05.2026, lecturer *Leonhard Liu* will take over, covering topics around *Recommender Systems*.

| Date        | Topics                                                                              |
| ----------- | ----------------------------------------------------------------------------------- |
| 14.05.2026  | [The Recommendation Problem](DSA-sessions/lecture-06.md)                                     |
| 21.05.2026  | [Content-Based Methods](DSA-sessions/lecture-07.md)                                          |
| 28.05.2026  | [Matrix Factorization & AutoRec](DSA-sessions/lecture-08.md)                                 |
| 04.06.2026  | [Neural Embeddings & Semantic Search](DSA-sessions/lecture-09.md)                            |
| 11.06.2026  | [Two-Tower, Evaluation & Retrieval](DSA-sessions/lecture-10.md)                              |

## Final Project

The final project will be an end-to-end data science workflow, developing a recommender system for a dataset of your choice. You will be expected to apply the concepts and tools covered in the lectures. Students may choose from the following work packages. Each work package will reward with a certain number of points, and students can choose to complete the work packages they want.

### Work Packages
<span style="color: red;">[Vipin TODO: Bitte helft hier, ob das mit den Punkten überhaupt Sinn macht. Ich dachte mir es wäre hilfreich klare Rahmen zu setzen, was erwartet wird.]</span>

| Work Package | Description | Points |
|--------------|-------------|--------|
| Data Scraping | Scrape (not download!) a dataset from a website or API, using tools like Beautiful Soup or Selenium. | 10 |
| Data Annotation | Use Label Studio to annotate a dataset of at least X samples. | 10 |
| Data Quality | Define and apply data quality metrics to a dataset, identifying and addressing issues. | 10 |
| Kubernetes Cluster | Deploy and manage experiments on our Kubernetes cluster. | 10 |
| Experiments Logging | Log your experiments using Weights & Biases, including metrics, configurations, and hyperparameters. | 10 |
| Vector Embeddings* | Create and use vector embeddings for items. | 10 |
| Hyperparameter Tuning | Optimize the hyperparameters of your machine learning models (e.g. Grid Search) using tools like optuna. | 10 |
| Recommender System* | Develop a recommender system using the collected data and embeddings. | 10 |
| Performance Evaluation* | Evaluate the performance of your recommender system (Precision@k/Recall@k) using two methods (?). | 10 |
| Perturbation Analysis | Analyze the robustness of your recommender system by introducing errors to the input data. | 10 |
| Frontend Application | Develop a frontend application (e.g. with Streamlit) to visualize and interact with your recommender system. | 10 |

\* Mandatory work packages for all students.

### Examination Modalities
- **Project presentation**: 15 minutes presentation of the final project. Can be a Jupyter notebook, a slide deck, or your frontend application.
- **Discussion**: 5 minutes after the presentation.
- **Markdown Report**: describing the workflow and work packages completed, with links to the respective sections in your repository showing your completion of the work packages.


The final project should then be presented in 15mins at the end of the semester (date TBA) and a markdown report should be submitted, in which you describe your workflow and the work packages you completed. Please refer to the respective sections in your repository showing your completion of the work packages.
The presentation format can be a Jupyter notebook, your Frontend application, or a slide deck.

### Evaluation Criteria
You can choose whether you want to spend more effort on the data collection and preprocessing part, the modelling, the descriptive analysis or the user interaction part. A good project must not necessarily cover all work packages, but it should be well executed in the work packages that are covered. The criteria evaluated will be based on:

- **Task difficulty**: a Kaggle task is less difficult in terms of data preparation and project structure than acquiring your own data set.
- **Solution complexity**: aim for an appropriate tradeoff of algorithmic/computational complexity and quality of the solution.
- **Structure and Quality of the presentation**


## Lecturer

Prof. Dr. Felix Bießmann<br>
Haus Bauwesen, D 138

Mail: [felix.biessmann@bht-berlin.de](mailto:felix.biessmann@bht-berlin.de)<br>
Links:
- https://prof.bht-berlin.de/biessmann
- https://www.digital-future.berlin/ueber-uns/professorinnen/prof-dr-felix-biessmann
- https://calgo-lab.de

---

M. Sc. Leonhard Liu<br>
Haus Elsa-Neumann, E 3.011

Mail: [leonhard.liu@bht-berlin.de](mailto:leonhard.liu@bht-berlin.de)