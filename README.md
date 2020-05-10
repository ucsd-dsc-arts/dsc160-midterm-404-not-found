# Using Machine Learning for Feature Extraction and Identification of Artworks of Pablo Picasso and Henri Matisse

DSC160 Data Science and the Arts - Midterm Project Repository - Spring 2020

Project Team Members: 
* Tianran Qiu       tiq004@ucsd.edu 
* Zishun Jin        zij034@ucsd.edu 
* Yijun Liu         yil724@ucsd.edu 
* Weihua Zhao       wez205@ucsd.edu 
* Da Gong           dagong@ucsd.edu


## Abstract

For this homework, we are analyzing artworks from Pablo Picasso and Henri Matisse, especially from 1900 to 1942. The dataset we are going to use is from two websites (https://www.pablo-ruiz-picasso.net/topviews.php, http://www.henri-matisse.net/paintingssectionone.html). These two artists shared quite a few similarities in their works after their first meeting in 1906, therefore our research question is Whether this Meeting Significantly Influenced Their Styles in Artworks. We believe that since their meeting, Pablo Picasso and Henri Matisse started to influence each other.

Our hypothesis is that the similarities between their artworks grow after their meeting. We are going to use Complexity scores, including color, variance, entropy and etc, as features to compare and predict the pictures of the two artists. We will be using jupyter notebook, python, openCV to extract the features. For visualization, we choose Interactive Plots and Matplotlib charts to show our analysis of the similarities. In class, we learned web scraping and basic image features. In the project, we will use the same web scraping skills to acquire data, but, as the expansion, we will be using advanced image features such as self-defined complex scores to compare the artwork of two artists. Furthermore, we will be using Bayes classifier to predict and classify paintings of these two artists based on features and complexity scores we defined.

We were always fascinated by the rivalry between artists. The rivalry was like a catalyst; it created tension, ignited each other’s creativity, and inspired each other through the process of creation. We are particularly interested in discovering the similarities of artworks of Pablo Picasso and Henri Matisse, two stars whose light shined through the history of modern art. Picasso once said, "If I were not making the paintings I make, I would paint like Matisse," and Matisse said much the same about Picasso. In the following decades, these two had an interesting relationship: they cherished each other, yet were in rivalry with each other. From time to time, their paintings were put together side by side and commented on. When Matisse created a sensational painting, Picasso would create one as a response. I believe studying the similarity of artworks between these two would give us an insight not only in their relationship but in the development of modern art as well.

## Data

We have acquired two datasets from two websites, [Pablo Picasso Painting Website](https://www.pablo-ruiz-picasso.net/topviews.php) and [Henry Matisse Painting Website](http://www.henri-matisse.net/paintingssectionone.html). The two websites consisted paintings created by Pablo Picasso and Henry Martisse. In our datasets, we chosed the paintings created between 1900 and 1942. We scrapped down 235 Picasso's painting's from the first website, [Picasso Paintings](https://github.com/ucsd-dsc-arts/dsc160-midterm-404-not-found/tree/master/data/picasso). And we scrapped down 154 Martisse's paintings from the second website, [Matisse Paintings](https://github.com/ucsd-dsc-arts/dsc160-midterm-404-not-found/tree/master/data/henri-matisse). The data is the digital copy of two artisits' original paintings. All of the data are in JPG form. 


## Code
- Data Acquisition/ Scraping 
  * [Scraping](/code/run_scraping.ipynb): This part is for running scraping data from the dataset mentioned above. The main code is in the [scraping_data](/code/scraping_data.py)file.
- Preprocessing / Cleaning
  * [Label portraits into Maternity and Mistress](/code/run_Mat_vs_mis.ipynb): This part is for running labeling the images of these two artists into Maternity and Mistress by using keywords in the image name. The main code is in the [mat_vs_mis](/code/mat_vs_mis.py)file.
  * [Calculate the RMS Contrast and Average Entropy features](/code/run_calculating_RMS_Entropy.ipynb): This part is for extracting the RMS Contrast and Average Entropy features from images. The main code is in the [calculate_RMScontrast_AVGentropy](/code/calculate_RMScontrast_AVGentropy.py)file. `Root mean square (RMS) contrast` does not depend on the angular frequency content or the spatial distribution of contrast in the image. RMS contrast is defined as the standard deviation of the pixel intensities. `Average Entropy` is for evaluating the complexity of an image.
- Analysis / Generating Results
  * [Analysis on Erotic Charge](/code/Erotic_charge.ipynb): This is a notebook for analyzing erotic charge in images for these two artists.
  * [Classifier for these two artists](/code/Classifier.ipynb): This is a notebook for classfying the images of these two artists. 
  * [Visualization Result](/results/Visualization.ipynb): This is the interactive data visualization notebook for these two artists according to RMS Contrast and Average Entropy features.
  
 To see how to run our code, please refer to [Midterm Project Showcase](/code/Midterm.ipynb)


## Results

(30 points) 

This section will contain links to documentation of your results. This can include figures, sound files, videos, bitmaps, as appropriate to your domain of analysis. Each result should include a brief textual description, and all should be listed below: 

- image files (`.jpg`, `.png` or whatever else is appropriate)
- audio files (`.wav`, `.mp3`)
- written text as `.pdf`

## Discussion

(30 points, three to five paragraphs)

The first paragraph should be a short summary describing your results.

The subsequent paragraphs could address questions including:
- Why is this culturally relevant?
- How does your computational approach differ from the traditional art historical, musicological, manuel/subjective approach to analyzing your cultural subject? 
- How do you think the original artists/musicians would respond to this type of analysis? Would it change/inform their practice in some way?
- How do your results relate to broader social, cultural, economic political, etc., issues? 
- In what future directions could you expand this work?

## Team Roles

* Tianran Qiu
* Zishun Jin
* Yijun Liu: Scraping data, calculate RMS Contrast and average Entropy and Summarize Code Part
* Weihua Zhao:
* Da Gong:

## Technical Notes and Dependencies

Any implementation details or notes we need to repeat your work. 
- Additional libraries you are using for this project
- Does this code require other pip packages, software, etc?
- Does this code need to run on some other (non-datahub) platform? (CoLab, etc.)

## Reference

References to any papers, techniques, repositories you used:
- Papers
- Repositories
- Blog posts
