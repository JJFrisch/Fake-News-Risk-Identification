Fake News Risk Identifier
Jake Frischmann, Eesha Shara, Shivansh Bansal

End Goal:
	Train a model to scan a website’s text and predict (0-1) if the website contains fake news, misinformation, or disinformation.

Use:
	A tool to help judge how much a reader should trust a website. 

Problem solved:
	People blindly trusting information found on websites that may be misleading or give false claims.


Plan:       Python TensorFlow through GitHub
Build a supervised ML ensemble logistic regression to produce a risk number for false information in the news website being read. This is a natural language processing problem so the documents will be cleaned up into one solid page then data points (#of verbs, punctuation, author’s other written pages etc.) will be extracted. The data will be split 70/30 and the trained model accuracy rate (takes both the false positive and the false negative observations into account) will be aimed for 85% or greater.
1.	Data collection
a.	https://drive.google.com/file/d/1IoTRrJNDJqvaG3hnUpnHQyGvPAJbO8y3/view
b.	https://www.kaggle.com/datasets/jruvika/fake-news-detection
c.	https://www.hindawi.com/journals/complexity/2020/8885861/#materials-and-methodshttps://www.hindawi.com/journals/complexity/2020/8885861/#materials-and-methods
2.	Data Cleaning and formatting
a.	Reduce all pages to one page
b.	Bring values like title, author, etc. out
c.	Remove formatting
d.	Remove pages with  <20 words
3.	Extract Lingustic variables
a.	Reasurch important variables
4.	Choose features/variables to train on
5.	Split training and testing data
Repeat until 85% accuracy is achieved -
Train model using training data
Evaluate model
Hyperperameters and model tuning 
User website >> trained model >> Output (Classification * certainty)

The Model
Boosting Classifier (XGBoost) ensamble method
Detailed paper on XGBoost - https://dl.acm.org/doi/epdf/10.1145/2939672.2939785
ABSTRACT
Tree boosting is a highly effective and widely used machine learning method. In this paper, we describe a scalable end-to-end tree boosting system called XGBoost, which is used widely by data scientists to achieve state-of-the-art results on many machine learning challenges. We propose a novel sparsity-aware algorithm for sparse data and weighted quantile sketch for approximate tree learning. More importantly, we provide insights on cache access patterns, data compression and starting to build a scalable tree boosting system. By combining these insights, XGBoost scales beyond billions of examples using far fewer resources than existing systems.

https://docs.google.com/document/d/1aaY2hRCRSlCajybiN_aJmWEdbDknDrmo/edit?usp=sharing&ouid=113375915943200795842&rtpof=true&sd=true

