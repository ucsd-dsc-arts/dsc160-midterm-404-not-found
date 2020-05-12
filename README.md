# Using Machine Learning for Feature Extraction and Identification of Artworks of Pablo Picasso and Henri Matisse and Analysis in the Emotional Content 

DSC160 Data Science and the Arts - Midterm Project Repository - Spring 2020

Project Team Members: 
* Tianran Qiu       tiq004@ucsd.edu 
* Zishun Jin        zij034@ucsd.edu 
* Yijun Liu         yil724@ucsd.edu 
* Weihua Zhao       wez205@ucsd.edu 
* Da Gong           dagong@ucsd.edu


## Abstract

For this homework, we are analyzing artworks from Pablo Picasso and Henri Matisse, especially from 1900 to 1940. The dataset we are going to use is from two websites (https://www.pablo-ruiz-picasso.net/topviews.php, http://www.henri-matisse.net/paintingssectionone.html). Since both of them were pioneers of Modern Art, their works shared quite a few similarities in their works after their first meeting in 1906; therefore our research question is Whether this Meeting Significantly Influenced Their Styles in Artworks. We believe that since their meeting, Pablo Picasso and Henri Matisse started to influence each other. We also are interested in discovering the color usuage and the emotional content within.

Our hypothesis is that the similarities in terms of RMS between their artworks grow after their meeting; our another hypothesis is that the they have different levels of erotic charge(a complexity of RMS and entropy) on portraits on their wives and their muses/mistresses. We are going to use a series of features, including color, entropy and etc, to compare and predict the pictures of the two artists. We will be using jupyter notebook, python, openCV to extract the features. For visualization, we choose Interactive Plots and Matplotlib charts to show our analysis of the similarities. In class, we learned web scraping and basic image features. In the project, we will use the same web scraping skills to acquire data, but, as the expansion, we will be using advanced image features such as self-defined complex scores to compare the artwork of two artists. Furthermore, we will be using Bayes classifier to predict and classify paintings of these two artists based on features and complexity scores we defined.

We were always fascinated by the rivalry between artists. The rivalry was like a catalyst; it created tension, ignited each other’s creativity, and inspired each other through the process of creation. We are particularly interested in discovering the similarities of artworks of Pablo Picasso and Henri Matisse, two stars whose light shined through the history of modern art. Picasso once said, "If I were not making the paintings I make, I would paint like Matisse," and Matisse said much the same about Picasso. In the following decades, these two had an interesting relationship: they cherished each other, yet were in rivalry with each other. From time to time, their paintings were put together side by side and commented on. When Matisse created a sensational painting, Picasso would create one as a response. I believe studying the similarity of artworks between these two would give us an insight not only in their relationship but in the development of modern art as well.

## Data

We have acquired two datasets from two websites, [Pablo Picasso Painting Website](https://www.pablo-ruiz-picasso.net/topviews.php) and [Henry Matisse Painting Website](http://www.henri-matisse.net/paintingssectionone.html). The two websites consisted paintings created by Pablo Picasso and Henry Martisse. In our datasets, we chosed the paintings created between 1900 and 1942. We scrapped down 235 Picasso's painting's from the first website, [Picasso Paintings](/data/picasso). And we scrapped down 154 Martisse's paintings from the second website, [Matisse Paintings](/data/henri-matisse). The data is the digital copy of two artisits' original paintings. All of the data are in JPG form. 


## Code
- Data Acquisition/ Scraping 
  * [Scraping](/code/run_scraping.ipynb): This part is for running scraping data from the dataset mentioned above. The main code is in the [scraping_data](/code/scraping_data.py)file.
- Preprocessing / Cleaning
  * [Label portraits into Maternity and Mistress](/code/run_Mat_vs_mis.ipynb): This part is for running labeling the images of these two artists into Maternity and Mistress by using keywords in the image name. The main code is in the [mat_vs_mis](/code/mat_vs_mis.py)file.
  * [Calculate the RMS Contrast and Average Entropy features](/code/run_calculating_RMS_Entropy.ipynb): This part is for extracting the RMS Contrast and Average Entropy features from images. The main code is in the [calculate_RMScontrast_AVGentropy](/code/calculate_RMScontrast_AVGentropy.py)file. `Root mean square (RMS) contrast` does not depend on the angular frequency content or the spatial distribution of contrast in the image. RMS contrast is defined as the standard deviation of the pixel intensities. `Average Entropy` is for evaluating the complexity of an image.
- Analysis / Generating Results
  * [Analysis on Erotic Charge](/code/Erotic_charge.ipynb): This is a notebook for analyzing erotic charge in images for these two artists.
  * [Classifier for these two artists](/code/Classifier.ipynb): This is a notebook for classfying the images of these two artists. 
  * [Visualization Result](/results/Visualization_final.ipynb): This is the interactive data visualization notebook for these two artists according to RMS Contrast and Average Entropy features.
  
 To see how to run our code, please refer to [Midterm Project Showcase](/code/Midterm.ipynb)


## Results


We chose RMS value to evaluate the contrast of a portrait and the entropy to evaluate the complexity of a portrait.

- We find that the correlation between their RMS contrasts grows after 1906, the year they met, from -0.05345678 to -0.0961737.

- We used five models for our classifiers: SVC, decision tree, Bernoulli NB, K-nearest neighbor and random forest; among those, the Random Forest Classifier performs the best with the test accuracy of 83.3%. 
  * [Classifier for these two artists](/code/Classifier.ipynb)

- RMS contrast value in Picasso's paintings grouped by Maternity and Mistress: The RMS contrast for Mistress group is higher that that of Maternity group.
  * [RMS contrast of Picasso's portraits](/results/Picasso's%20Maternity%20Paintings'%20RMS%20Contrast%20Value%20vs.%20Mistress%20Paintings'%20RMS%20Contrast%20Value.png):

- RMS contrast value in Matisse's paintings grouped by Maternity and Mistress: The RMS contrast for Mistress group is higher that that of Maternity group.
  * [RMS contrast of Matisse's portraits](/results/Matisse's%20Maternity%20Paintings'%20RMS%20Contrast%20Value%20vs.%20Mistress%20Paintings'%20RMS%20Contrast%20Value.png):

- RMS contrast value in Picasso's and Matisse's paintings: Overall, Picasso's portraits have higher RMS contrasts.
  * [RMS contrast of Picasso's and Matisse's portraits](/results/Picasso's%20Paintings'%20RMS%20Contrast%20Value%20vs.%20Matisse's%20Paintings'%20RMS%20Contrast%20Value.png)

- Mean RMS contrast over years in Picasso's and Matisse's portraits: Since the year 1906 when they met, through the twenty years after, their RMS contrast have a overall similar pattern.
  * [Mean RMS contrast over years in Picasso's and Matisse's portraits](/results/bokeh_mean_rms_overyears_2.png)
  
- Bokeh visualization of these two artists: please run the notebook, we displayed all the portraits with the corresponding points.
  * [Boheh visualization](/results/Visualization_final.ipynb)


## Discussion



- Firstly, we start our artist identification with experimenting with five models for our classifiers: SVC, decision tree, Bernoulli NB, K-nearest neighbor and random forest; among those, the Random Forest Classifier performs the best with the test accuracy of 83.3%. The accuracy score for SVC is 68%, for Decision Tree Classifier is 0.743, and for K-nearest classifier is 79.5%. The reason why the random forest classifier achieved the highest accuracy is that it creates many trees for different features and combines their results which is more better than a single tree for decision tree algorithm. In addition, the random forest classifier works very well with high dimensionality, which means it fits well with our 7 features. In terms of erotic charge, we found that the erotic charge on Mistress portraits are higher than Materinity portraits; Matisse's paintings have condenser usuages of colors than Picasso, while Picasso's paintings have larger range of RMS since he himself had many different styles. Compared with Maternity portraits, Mistress portraits have higher contrasts and entropy; the RMS correlation between their portraits grows after they met each other, which validates our initial assumption.
- Pablo Picasso and Henri Matisse are two giants whose light shined through the history of modern art. Picasso once said, "If I were not making the paintings I make, I would paint like Matisse," and Matisse said much the same about Picasso. In the following decades, these two had an interesting relationship: they cherished each other, yet were in rivalry with each other. We used the technique of Exploratory Data Analysis to decipher the subtle connections between their portraits. 
- Picasso's style has a larger range of variety: from the early period to the later cubism period; while Matisse's style has less variance, he was influenced by a variaty of cultures including African art and Eastern art. What they have in common is that they both created lots of portraits of women, some of them were wives, others were mistresses, or muses. In the documentary, Matisse Meets Picasso, "Matisse saw his models as assitants, while Picasso saw his models as muses." Also, Matisse was famous for his bold usage of colors; in the article, Matisse and His Models, "Matisse himself knew perfectly well that the erotic charge in his work came from a passionate desire that overrode straightforward lust." Matisse embedded his desire within the colors. This idea inspired us to take a deeper look into the color usages, more specifically, RMS contrast and entropy, of both artists and compared them to have insight of their inner worlds about women, and the differences and similarities of their paintings. While there are artist identification projects in the wild, no one actually discovered their inner worlds, explored the erotic charge and the differences through picture contrast and entropy values.
- In our opinions, art is a private conversation. Though a single painting can be seen by millions of eyes publicly, people perceive differently. The conversation in which artists communicate their ideas can differ largely from individual to individual. For Picasso and Matisse themselves, our findings might unveil the secrets and mysterious attitudes that only they know, to which they might be surprised since they are made public, although these are only our assumptions.
- Our findings can be helpful in studying the development of art and modern art genre since these two are the pioneers; what is more, people might be able to find how the Industry Revolutions ultimately changed the way people saw the world and how cultures were transferred, elevated, and entered these artists' lives. If we want to expand this work, directions might possibly be to expand this workframe towards other artists and discover their artists towards sex, gender, wars, and life and death, any topic might be possible.

## Team Roles

* Tianran Qiu: Extracted painting features, constructed classification models, summarize Data and Reference part.
* Zishun Jin：Extracted painting features, constructed classification models, contributed to parts of the abstract. 
* Yijun Liu: Scraping data, calculate RMS Contrast and average Entropy and Summarize Code Part
* Weihua Zhao: Came up with the idea, exploratory data analysis, data cleaning, erotic charge calculation,Visualization, discussion.
* Da Gong: Visualization of data using Bokeh, matplot.

## Technical Notes and Dependencies
 
- OpenCV
- Bokeh

## Reference

- (https://www.smithsonianmag.com/arts-culture/matisse-and-his-models-70195044/)
- (https://dsp.stackexchange.com/questions/58374/can-the-entropy-be-used-as-a-measure-of-the-contrast-of-an-image)
- (https://www.anothermag.com/art-photography/8799/the-women-behind-the-work-picasso-and-his-muses)
- (https://www.youtube.com/watch?v=_b2eTU6fOEE&t=2504s)
