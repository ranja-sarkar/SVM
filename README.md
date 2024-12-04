
**SVM (support vector machine)** is a go-to ML algorithm for classification problems - it finds the optimal hyperplane (decision boundary) that divides the data into classes. 
Although primarily used for only binary classification tasks, it can very well be extended to multi-class classification. 
It is highly effective for high-dimensional spaces and when the number of data points is smaller than the number of dimensions (e.g. text classification).
Functions called kernels are used in SVMs that enable handling of non-linear relationships by transforming data into higher dimension. 

**Chapter 5** of my book discusses this SVM algorithm.


<img width="174" alt="1" src="https://github.com/user-attachments/assets/a2874186-1b73-4330-8b13-761b0012e63a">

Buy from Amazon: https://a.co/d/1zUEkNQ

An excerpt from the book:

<img width="448" alt="10" src="https://github.com/user-attachments/assets/8599c5b8-e371-4888-86c2-3bbb3872988e">

The one-class SVM approach is unsupervised learning and effective in problems where very few deviations (outliers) from normal (inlying data points) are expected. 

The following figures show classifications (find the **py-file**) estimated by this approach (anomalies are marked in yellow) - left one results when the model is trained with 1% outliers in the data and right one results when the model is trained with 2% outliers. 

<img width="316" alt="10" src="https://github.com/user-attachments/assets/67396369-ae48-413c-9b37-d51ee4cd97d2">    
<img width="320" alt="20" src="https://github.com/user-attachments/assets/459c243a-7cb8-4edd-9bb5-ed0b3afbb347">



