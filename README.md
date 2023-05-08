<div align="center">
 <h1>Real Estate Price Prediction</h1>
</div>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

# 1. Data Acquisition

#### Duration : 5 days

<div align="justify">
This part of the project was a team project, we had as goal to collect at 
least 10.000 buildings properties with as many numerical values as possible to be able to analyze 
them more easily in the next steps of this project. 
We decided to scrap the date we can on 
<a href="https://www.immoweb.be/fr/annonce/">ImmoWeb</a>. 
As final result, we created a dataset with all the data we scraped stored 
in a csv file.
</div>

### Collecting the urls from each page

1. Generate somes url to scrape the announces
2. Scrap the urls and get the hrefs in each pages
3. Clean the hrefs by excluding all urls that are not starting by https://www.immoweb.be/fr/annonce/
4. Store the freshly obtained urls into a csv file of this shape :

| URLS (name of the column not present in the csv) |
| ------------------------------------------------ |
| url 1                                            |
| url 2                                            |
| ...                                              |
| url i                                            |
| ...                                              |
| url n-1                                          |
| url n                                            |

### Scrapping all the content of each url in the built csv file

1. Open and read the csv file of the first part
2. Get all the urls in the file
3. Scrap all the webcontent of each webpage attached to the url
4. Save each webcontent into a large ammount of html files

### Sorting and storing the data in a dictionary

1. Open and read each html file

2. Exctrat the data with bs4 and transform the data into usable types (int,bool etc.)

3. Make a dictionary with this structure:
   
   Dictionnary:
   
   * id : Inner dictionnary
   
   Inner dictionnary:
   
   * To rent : bool
   * To sell : bool
   * Price : int
   * Number of rooms : int
   * Living Area : float
   * Fully equipped kitchen : bool
   * Furnished : bool
   * Open fire : bool
   * Terrace : bool
   * Area of the terrace : float
   * Garden : bool
   * Area of the garde : float
   * Surface of the land : float
   * Surface area of the plot of land : float
   * Number of facades : int
   * Swimming pool : bool
   * State of the building : str
   * zipcode : int
   * type : str

### Storing the dictionary in a pandas' dataframe

1. Store the previous dictionary as a csv file of the shape below

| ID     | To rent | To sell | Price  | Number of rooms | ... | zipcode | type        |
| ------ | ------- | ------- | ------ | --------------- | --- | ------- | ----------- |
| id 1   | False   | True    | 97000  | 3               | ... | 4000    | Appartement |
| id 2   | True    | False   | 800000 | None            | ... | 1825    | Penthouse   |
| ...    | ...     | ...     | ...    | ...             | ... | ...     | ...         |
| id i   | None    | None    | None   | None            | ... | None    | None        |
| ...    | ...     | ...     | ...    | ...             | ... | ...     | ...         |
| id n-1 | None    | None    | 54000  | 5               | ... | 1000    | Maison      |
| id n   | True    | False   | 1000   | 85              | ... | 1010    | Bugalow     |

## How to use it

just run scraper.py and it should do the trick but your can import the file as a library and use the functions in your own project

---

# 2. Data Analysis

#### Duration : 7 days

<div align="justify">
My client's question was : "Where should I buy an appartment to rent it at the best price afterwards ?" 
</div>

## Data Cleaning

<div align="justify">
I managed the duplicates and the NaN values. I also converted the datas 
who needed it to the right format. After that, I selected only the 
renting appartements and "Rez-de-chaussée" to create a dataframe. 
And finally, I calculated and added the columns "Price per square meter" 
and "Price per bedrooms".

</div>

## Data Analysis

<div align="justify">
During my analysis, I deleted the outliers. As I need them, I added the 
Province column. I plot the average renting and selling prices for 
appartments per Province.
</div>

Here is the graph for the renting prices :

![Mean renting price](Visuals/Average%20Renting%20Price%20Appartment%20Belgium%20Province%20Units.png)

Here is the graph for the selling prices :

![Mean renting price](Visuals/Average%20selling%20price%20Appart%20Belgium%20Province%20Units.png)

And finally, I combined the mean renting price per province with the mean selling price to calculate the number of years required to refund the purchase and I plotted it.

![Mean renting price](Visuals/Number%20of%20years%20to%20refund%20my%20buying.png)

In conclusion of this phase, I could recommend my client to buy in Hainaut or in Brussels if he want to have his refund before 20 years.

---

# 3. Modeling

#### Duration : 7 days

This part's goal is to answer my fictive client's question who could be : 

###### "How much could be the rent amount I can expect for such an appartment all around Belgium ?"

<div align="justify">
Remembering in Data Analysis part, he wanted to buy an appartment somewhere in Belgium where it could as fast as possible refund it renting it, he is looking at some appartments in Belgium and is guessing how much he could expect as rent for "such an appartment".
</div>

That will be our common thread for this whole part.

## 1) Preprocessing Data

I take the data from Data Acquisition part.

1. From the csv's file we get at the end of Data_acquisition part, I take only the renting appartment and Rez-de-chaussée everywhere in Belgium

2. I add the column "Province" because I found it was an important feature to have in my model.

3. I delete all the columns I didn't want to have in my features to only havethe features I wanted. 
   
   - ###### 9 Features remain : Number of rooms, Living Area, Open fire, Terrace, Garden, Swimming pool, State of the building, Province
   
   - ###### 1 target : Renting price

4. I looked for the outliers and found there are some. I deleted them.

5. I had also to delete nearly 2288 buildings on 11072 rows because they haven't any living area mentionned. As I had their price, before deleting them, I tried to calculate their living area calculating the mean and also the median of the price per square m for each province but at the end I saw that my model's score were tremoundsly dropping so I had to delete them unfortunately.

6. I also had to delete 2105 others rows on 8751 because they haven't any state of the building and I couldn't guess it, unfortunately.

7. I put the non-numerical into numerical values using the pandas' function get_dummies on my features nammed "Province" and "State of the building"

8. I finally get my dataframe ready to go in the modeling part with 6617 rows.

## Modeling Part

1. Features = Number of rooms, Living Area, Open fire, Terrace, Garden, Swimming pool, State of the building, Province

2. Target = Renting price of an appartment

3. I tried several differents models :
   
   - GradientBoostingRegressor
   
   - LinearRegression
   
   - Lasso
   
   - Ridge
   
   - ElasticNet
   
   - DecisionTreeClassifier
   
   - RandomForestRegressor

4. The best model is  : GradientBoostingRegressor
   
   - with a mean score of 75%
   
   - with a crossvalidation score of 62,50% (+- 20% of standard deviation)

## Conclusions on the modeling part :

<div align="justify">
GradientBoostingRegressor is the best model tested so far. But with a biggest number of buildings with their whole data completed, maybe RandomForestRegressor could also be a very good candidat for the kind of prediction I did. As I explained earlier in the modeling part, I had to delete 2288 rows (because they missed the living area) and another 2105 rows (because they missed the state of the building). I tried to calculate the missing living area but it gives me very poor results as I also explained earlier. So from 11072 rows I reached 6617 rows in my final dataframe to train and test my models. I imagine if I could have 11000 completed rows for renting price, living area, state of the building and Province I would have better crossvalidation score and a better standard deviation because 20% is huge. If I had time to do, I would also plot each variable with the renting price to be able to see and deleted some outliers remaining.
</div>

# 4. Deployment

#### Duration : 6 days

<div align="justify">
In this part, I'll give the access of my predictive model for the renting of an appartment in Belgium to my client for him to predict the prices of the appartment he would like to buy. 
</div>

## Creating an API :

#### Building a form's example to receive the datas

Route used : /prediction

I created a very simple html's form to invite my client to give me the appartment's datas he wants to predict the renting price.

#### Collecting and preprocessing datas the user give me

###### 1) Collecting

Route used : /receiving_data (in the <form action=)

Method used : POST

I collect the data the user give to the html's form with a "POST" method in the route : /receiving_data

###### 2) Preprocessing

I take the collected datas to convert them in a good format for them to fit what my model needs to make a predicted renting price

<u>Possible improvement</u> : I would like have liked to check what the user give me as datas and to tell him if there was an error with what he entered but I skipped that part for a timing reason and decided to "force" the user to fill in the html file with only numerical values for the one who need numerical values and trough the html asking the required value to be filled in.

#### Modeling the user's data

I just enter the preprocessed datas in the model to receive the prediction price in the end.

## Creating a Dockerfile

You'll find my Dockerfile in the "/deployment" repo which I used in the next step. I manage to create a image and a container working locally but I didn't find a free service who allow me to deploy the docker image or container directly on their service so I choose deploying with my Dockerfile on render.com

## Deploying the API on render.com

As render doesn't accept a docker container to be deployed, I used my Dockerfile trough render.com to deploy the API online.

Here is the address : https://belgian-appart-renting-price-prediction.onrender.com/

It takes some time to load because it's deployed on a free service but it works !!!
