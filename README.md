# LaLiga games predictions 
## Malis Project 
### Introduction : 
The project aim is to have an accuracy as good as possible on predicting football matches results. Our choice of the Spanish
league is based on the recent regulations that made the teams more balanced because of the limited budget they can spend.
The input to our algorithms is a collection of features like the Team, the opponent Team, average scores of the teams (goals,
shots, blocks, FIFA players’ scores, etc.) and the ”home/away” feature. We then used different models; KNN, Random Forest,
SVM and Logistic Regression, to output the predicted result (0:Loss - 1:Win - 2:Draw). Then, we did feature selection on
the mentioned models (RFE - Lasso regularization) to minimize the number of features and achieve better accuracy.
### Notebooks : 
The final Notebook is Final.ipynb. The dataset used to test is "finalData20-21.csv" processed in the final notebook. 
Final_2Data.ipynb is a similar file to the Final one but using two datasets : season 20-21 and season 21-22. The results are not good enough while using both datasets. Some modifications must be done. 
### Acknowledgements :  
The code used to scrap the matches' reports Webscrapping.ipynb is inspired by the code of Kempa, M. on his project : Machine Learning Algorithms for Football Predictions.
The fifa20-21.csv is extracted from this repository : https://github.com/othmbela/fifa-21-web-scraping .