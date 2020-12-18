### Title:

Chilling effects of the Snowden Revelations: a permanent and worldwide impact ? 
 
### Abstract:

The paper explores the existence of a chilling effect on people's online behaviour due to the Snowden revelations.
We propose to answer two additional questions about this effect. First, we study the long-term persistence
of this effect. Secondly, we explore the possibility of a chilling effect happening outside the US.  

The dataset used will contain the German counterparts of the terrorism-related articles. We will 
apply similar analysis as in the paper on this dataset and study the trends pre and post revelations.
We will also use segmented regression on the original english articles where the study period is extended until 2016.


### Research Questions:  

1. Is the Chilling Effect found by the author in the paper permanent ? 
   Is there evidence of the effect fading away with time?   
   Are there possible confounders if we extend the analysis to a longer period ? 
2. Did the Snowden revelations affect behaviour of people outside the US?
   Precisely, is there a chilling effect on users of German Wikipedia?


### Proposed dataset:

http://cricca.disi.unitn.it/datasets/pagecounts-raw-sorted/?fbclid=IwAR0ppAvCNpXsYcrtYk_8A072jFND7h5F9CDDq7QBznWd9ZEyTgxk8X-i6Pg , which was created by processing Wikimedia’s page-counts raw dataset: 
https://dumps.wikimedia.org/other/pagecounts-raw/.
The dataset contains hourly pageview counts for different languages and for a time period from 2008 until 2016.
The dataset comes with a few scripts that would help us download the monthly data:
https://github.com/CristianCantoro/pagecounts-download-tools


### Methods: 

**Data collection:**
Initially, we wanted to get the pageview counts data from the same source as the paper : https://www.stats.grok.se
However, the website has been down for a few days. 
In the case where https://www.stats.grok.se will be available again, it would be easier to get the pageviews from here, and use Wikimedia’s REST API: https://wikimedia.org/api/rest_v1/ to get the page views after July 2015.

We will use the scripts provided with the available dataset of Cristian Cantoro of hourly pageview counts to have a monthly aggregate. Then, we will filter the dataset to have only interesting articles i.e privacy-sensitive ones. 
After this, we need to filter for the specific pages and languages (English and German) we need. We will download the data from this source from 2012 through 2016. This may take some time and resources, as each month represents 24GB of data.

We will consider data of a more extended period of time to test the hypothesis of long term chilling effects.


**Method of analysis:**
We will be applying the same interrupted time-series with segmented regression method on the newly acquired data: German articles and longer period of study.
Depending on the results we obtain, we may resort to applying discontinuous analysis methods for the extended data in order to look for potential confounders / events.

### Organization within the team
Milestone 1: 04/ 12/ 2020 Data cleaned, filtered and loaded into a DataFrame.

Milestone 2: 07/ 12/ 2020 Segmented regression applied on German articles and on extended english data.

Milestone 3: 11/ 12/ 2020 Discontinuous analysis methods applied to extended data.

Milestone 4: 18/ 12/ 2020 Report and video ready.

* We will all take part in the data preprocessing step (Retrieving pageviews of the considered articles for the considered period).
* Starting from week 2 and once we get the data cleaned in easily-handled dataframes, 
    Karim will be in charge of implementing the ITS on the data of German wikipedia and testing the significance of the results. 
    Anas will be responsible of applying the analysis on the extended datasets and generating plots and results.
    Ahmed will be further investigating on possible confounders/events or hidden variables that were not taken into account. Some other statistical methods can be    applied to test the significance of these events on the analysis.
* During week 3, 
Karim and Anas will be in charge of writing the report, while Ahmed will work on recording the video.

### Questions for TAs (optional)
We have an idea on how to download data for each month. However, each month consists of 750 files, containing all sorts of information. Any advice on how to optimize our iterations (library, etc,..)? 

What methods of discontinuous analysis are useful for the dataset extended until 2016? 




