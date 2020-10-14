
## Recommender Model Based on Tags and Countries
This model made use of the tags features of the individual hotels for each country to recommend hotels to users based on:
* Their country of choice  
* Description of their hotel choice.

For the model building, Different libraries such as numpy, pandas and natural language tool kits (NLTK) were used.\
The model accepts **'country and description of hotel'** inputs, tokenizes the hotel description, get rid of stop words and produces the hotels that have similar description as tags. This method takes care of the 'cold start problem' as hotels are recommended to users based on their respective choices.\
The model, when tested with a particular description and country, returns hotels with similar description as recommendations.\
Since this is an unsupervised learning model, it would be a bit difficult evaluating the accuracy of the model except the model is deployed for users to make use of and then evaluate.

## Recommender Model Based on Weighted Average.
The model used some feature columns from the dataset to calculate the weighted average(ratings) for each hotels and then ranked the hotels in descending order and recommended them to the user.\
**Formula used:**\
**W = (Rv + Cm)/(v + m)**
Where :\
W = weighted rating
v = number of votes for each hotel ( here we used the total number of reviews     column)
R  = average rating for each hotel (Average score column was used)
C = The mean score across the average score column ( mean of the        average score column was computed
m = The minimum vote required for a hotel to be in the top list\
Steps used in  building the  recommender system based in weighted average is summarized below.
* Compute all the components from the formula required to calculate the weighted average for each hotel.
* Compute the weighted rating, W for each hotel
* Rank the hotels in descending order
* Define a class called recommender system based on weighted average: The class takes in a dataframe as an argument and preprocesses the data.
* Addition of a method called recommend  to the class. This method, when called, asks the user for an input, implements the weighted rating, and then recommends the top hotels to the user based on the user's input.

## Recommender Model Based on Reviews
This model recommends hotels based on samples of both positive and negative reviews.\
In building the model, various libraries such as pandas,numpy and sklearn were used\.
The model takes in a hotel name as input and uses reviews for the inputed hotel to recommend other hotels based on similar  reviews.\
In the model the positive and negative reviews for every lodger have been combined and vectorized using a vectorizer from a sklearn feature extraction module.
The similarity scores for each hotel with every other hotel are then computed from the vectorized data.\
The values are sorted to output a ranking of the most similar hotels to each hotel, which is then used as the output for the recommendation system.


