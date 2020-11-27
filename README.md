### Title:

Chilling effects of the Snowden Revelations: a permanent and worldwide impact ? 
 
### Abstract:
The author of the paper finds a statistically significant chilling effect of the Snowden
revelations on the behaviour of people, namely a decrease in the number of views of privacy sensitive
articles.  
We propose to answer two other questions about this effect. First, is this effect permanent 
or does the behaviour of people return to normal after some period. And secondly, did the revelations
have an impact on the behaviour of people outside the US.
We will start by extracting a larger dataset, both in period and language. Then we will run
segmented regression analysis on the extended data twice. First for the German counterparts
of the terrorism-related secondly. And second on an extended time period for the english articles.



### Research Questions:  

1. Is the Chilling Effect found by the author in the paper permanent or at least long-term ?  
   Did this behaviour perpetuate or did the chilling effect fade away ?
   What are the possible confounders if we extend the analysis to a longer period ? 
2. Did the Snowden revelations affect behaviour of people outside the US?
   Precisely, is there a chilling effect on users of german Wikipedia?


### Proposed dataset:

Initially, we wanted to get the page-view counts data from the same source as the paper : https://www.stats.grok.se
However, the website has been down for a few days.
We were able to find the dataset: http://cricca.disi.unitn.it/datasets/pagecounts-raw-sorted/?fbclid=IwAR0ppAvCNpXsYcrtYk_8A072jFND7h5F9CDDq7QBznWd9ZEyTgxk8X-i6Pg
Which was created by processing Wikimedia’s page-counts raw dataset: 
https://dumps.wikimedia.org/other/pagecounts-raw/
The dataset contains hourly page-view counts for different languages and for a time period from 2008 until 2016.
The dataset comes with a few scripts that would help us download the monthly data:
https://github.com/CristianCantoro/pagecounts-download-tools
After this, we need to filter for the specific pages and languages (english and german) we need. We will download the data from this source from 2012 through 2016. This may take some time and resources, as each month represents 24GB of data.
In the case where https://www.stats.grok.se will be available again, it would be easier to get the page-views from here, and use Wikimedia’s REST API:  https://wikimedia.org/api/rest_v1/ to get the page views after July 2015.

### Methods:
We will be applying the same interrupted time-series with segmented regression method on the newly acquired data: german articles and longer period of study.
Depending on the results we obtain, we may resort to applying discontinuous analysis methods for the extended data in order to look for potential confounders / events.

Proposed timeline:  
*Week 1: Downloading, filtering and cleaning the data.
*Week 2: Analysis and application of the methods.
*Week 3: Interpretation of results, shooting of video and report.

Organization within the team
Milestone 1: 04/ 12/ 2020 Data cleaned, filtered and loaded into a DataFrame.
Milestone 2: 07/ 12/ 2020 Segmented regression applied on german articles and on extended english data.
Milestone 3: 11/ 12/ 2020 Discontinuous analysis methods applied to extended data.
Milestone 3: 18/ 12/ 2020 Report and video ready.

Questions for TAs (optional)
We have an idea on how to download data for each month. However, each month consists of 750 files, containing all sorts of information. Any advice on how to optimize our iterations (library, etc,..).



