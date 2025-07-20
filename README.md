
**SVM (support vector machine)** finds the optimal hyperplane (decision boundary) to divide data into classes. Although primarily used for only binary classification tasks, it can very well be extended to multi-class classification. It is highly effective for high-dimensional spaces and when the number of data points is smaller than the number of dimensions (e.g. text classification).
Functions called kernels are used in SVMs that enable handling non-linear relationships in a dataset by transforming the dataset into higher dimension. 

SVMs can be applied to a wide range of classification, regression, novelty detection tasks, and they can also be applied to unsupervised learning. 

<img width="401" alt="11" src="https://github.com/user-attachments/assets/da28cd61-cccb-481e-9953-0ca737d858ab" />

Using the concepts of margin/regularization, duality, kernels, one can extend the method to meet the demands of wide variety of tasks. 

<img width="224" alt="22" src="https://github.com/user-attachments/assets/df8695ce-e047-479e-9dfe-687346fcab0e" />


**Chapter 5** of my book discusses SVMs.


<img width="174" alt="1" src="https://github.com/user-attachments/assets/a2874186-1b73-4330-8b13-761b0012e63a">

Buy from Amazon: https://a.co/d/1zUEkNQ

An excerpt from the book:

<img width="448" alt="10" src="https://github.com/user-attachments/assets/8599c5b8-e371-4888-86c2-3bbb3872988e">

The **one-class SVM approach is unsupervised learning** and effective in problems where very few deviations (outliers) from normal (inlying data points) are expected. 

scikit-learn: https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM


The scikit-learn OneClassSVM algorithm requires the choice of a kernel and a scalar parameter to define a frontier. The RBF kernel is usually chosen (default), although there exists no exact formula or algorithm to set its bandwidth parameter. The 'nu' parameter, also known as the margin, corresponds to the probability of finding a new, but regular, observation outside the frontier.

If new observations lay within the frontier-delimited subspace, they are considered as coming from the same population as the initial observations. If they lay outside the frontier, we can say that they are abnormal with a given confidence in our assessment.

The following figures show classifications estimated with one-class SVM (anomalies are marked in yellow) - 

  **L** fig. -> results when the model is trained with **1% outliers** in the data 
  
  **R** fig. -> results when the model is trained with **2% outliers**

<img width="316" alt="10" src="https://github.com/user-attachments/assets/67396369-ae48-413c-9b37-d51ee4cd97d2">    
<img width="320" alt="20" src="https://github.com/user-attachments/assets/459c243a-7cb8-4edd-9bb5-ed0b3afbb347">



