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
However, the website has been down for a few days. Unfortunately the website wasn't put online again so we had to use the REST API provided at http://petermeissner.de:8880/


**Method of analysis:**
We applied the same interrupted time-series with segmented regression scheme on the newly acquired data: German articles and longer period of study.


### Organization within the team
Week1: Data cleaned, filtered and loaded into a DataFrame.

Week2: 07/ 12/ 2020 Segmented regression applied on German articles and on extended english data.

Milestone 3: 11/ 12/ 2020 Discontinuous analysis methods applied to extended data.

Milestone 4: 18/ 12/ 2020 Report and video ready.

* We took part in the data preprocessing step (Retrieving pageviews of the considered articles for the considered period).
* Starting from week 2 and once we get the data cleaned in easily-handled dataframes, 
 Karim was in charge of implementing the ITS on the data of German wikipedia and testing the significance of the results. 
 Anas was be responsible of applying the analysis on the extended datasets and generating plots and results.
 Ahmed further investigated on possible confounders/events or hidden variables that were not taken into account. He also took care of applying matching methods using Facebook inspired MUSE embeddings. 
*Karim and Ahmed took care of writing the report while Anas concentrated on the pitch presentation.





