<p>Every year thousands of people travel to different locations, some for vacation, some for tourism, some for business and some for other causes. They are plagued with the choice of hotel to stay in. Some make the wrong choice and ends of having bad memories. This bad memories can have ripple effect, some could be a psychological scar, demeriting a whole country/place, etc. With the help of a recommender system, we want help thousands around the world make this important decision.</p>

<p>The data is gotten from kaggle. It was scraped from [Booking.com](https://www.booking.com/) by [Jiashen Liu](https://www.kaggle.com/jiashenliu).</p>

The data is a csv file contains 17 columns. The description of each column is as below:

1. Hotel_Address: Address of hotel.

2. Review_Date: Date when reviewer posted the corresponding review.

3. Average_Score: Average Score of the hotel, calculated based on the latest comment in the last year.

4. Hotel_Name: Name of Hotel

5. Reviewer_Nationality: Nationality of Reviewer

6. Negative_Review: Negative Review the reviewer gave to the hotel. If the reviewer does not give the negative review, then it should be: 'No Negative'

7. ReviewTotalNegativeWordCounts: Total number of words in the negative review.

8. Positive_Review: Positive Review the reviewer gave to the hotel. If the reviewer does not give the negative review, then it should be: 'No Positive'

9. ReviewTotalPositiveWordCounts: Total number of words in the positive review.

10. Reviewer_Score: Score the reviewer has given to the hotel, based on his/her experience

11. TotalNumberofReviewsReviewerHasGiven: Number of Reviews the reviewers has given in the past.

12. TotalNumberof_Reviews: Total number of valid reviews the hotel has.

13. Tags: Tags reviewer gave the hotel.

14. dayssincereview: Duration between the review date and scrape date.

15. AdditionalNumberof_Scoring: There are also some guests who just made a scoring on the service rather than a review. This number indicates how many valid scores without review in there.

16. lat: Latitude of the hotel

17. lng: longtitude of the hotel

[Here is a link to the dataset](https://www.kaggle.com/jiashenliu/515k-hotel-reviews-data-in-europe)
