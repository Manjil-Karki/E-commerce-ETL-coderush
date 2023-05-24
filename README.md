<h1> E-commerce-ETL </h1>

This is a simple project to demonstrate the ETL process in E-commerce data. For this purpose data was scraped from daraz more specifically the data about mobile phines only. THe data related to the price, reviews and features of the phones were scraped. Subsequently requeried transformations were done and stored in a suitable form. Thus obtained data was finally stored in a csv. Finally, in the data simple analysis were performed and some visualizations of the data are created.

<h2> Work-FLow</h2>
The overal workflow of this project looks like:

![workflow](outputs/workflow.png?raw=true "workflow")

<h3> Extract </h3>
As mentioned earlier data regarding mobile phone prices, features and reviews were scraped from daraz. For the purpose of scraping the scrapy package in python was used. Spider was created to crawl product pages containing moble phones then scraping was done. The raw scraped data were stored in a csv file.
<h3> Transform </h3>
In case of transformation following mentioned things were done:

<h4> Parsing </h4>
As the scraped data were string it had to be converted into some efffecient data structure like dictionary which was done as a part of transformation

<h4> Cleaning </h4>
As a part of transformation cleaning was done part of it was also done at extraction. In cleaning only necessary and prominent and more usable features were kept and others were discarded. 

<h4> Structuring and validating </h4>
In case of structuring the parsed and cleaned data was kept in a dataframe and fnally written to a csv file and manual scanning and validation of the data was done.

<h3> Load </h3>
Being a sinmple small process data were stored as a csv file.

<h3> Analyze and visualize </h3>
For the part of analysis and visualization simple things were done as following:

<ul>
<li> Brand and their available phones count </li>

![brand_count](outputs/brand_count.png?raw=true "brand_count")

<li> Overall Phone price distribution in the site </li>

![price_distribution](outputs/price_distribution.png?raw=true "price_distribution")

<li> Price relation with various factors </li>


![price_correlations](outputs/price_correlations.png?raw=true "price_correlations")

</ul>

Furthermore, NLP can be used to analyze the reviews and that can also be visualized and a lot of other things could be done.