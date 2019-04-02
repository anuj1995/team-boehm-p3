# Data Science Ethics Checklist

## A. Data Collection
 - [NA] **A.1 Informed consent**: If there are human subjects, have they given informed consent, where subjects affirmatively opt-in and have a clear understanding of the data uses to which they consent?
 - [NA] **A.2 Collection bias**: Have we considered sources of bias that could be introduced during data collection and survey design and taken steps to mitigate those?
 - [NA] **A.3 Limit PII exposure**: Have we considered ways to minimize exposure of personally identifiable information (PII) for example through anonymization or not collecting information that is not relevant for analysis?
 * The data was already collected and anonymized. We used the available data and have no idea about the collection process. We tried to search and find some information about the collection process, which we were not successful. Data source: https://github.com/codeneuro/neurofinder
 
## B. Data Storage
 - [NA] **B.1 Data security**: Do we have a plan to protect and secure data (e.g., encryption at rest and in transit, access controls on internal users and third parties, access logs, and up-to-date software)?
 - [NA] **B.2 Right to be forgotten**: Do we have a mechanism through which an individual can request their personal information be removed?
 - [NA] **B.3 Data retention plan**: Is there a schedule or plan to delete the data after it is no longer needed?
 * Similar to the previous question, the data is public and anonymized; therefore, there is no need for security, forgotten, or retention plans.
 
## C. Analysis
 - [NA] **C.1 Missing perspectives**: Have we sought to address blindspots in the analysis through engagement with relevant stakeholders (e.g., checking assumptions and discussing implications with affected communities and subject matter experts)?
 - [NA] **C.2 Dataset bias**: Have we examined the data for possible sources of bias and taken steps to mitigate or address these biases (e.g., stereotype perpetuation, confirmation bias, imbalanced classes, or omitted confounding variables)?
 - [NA] **C.3 Honest representation**: Are our visualizations, summary statistics, and reports designed to honestly represent the underlying data?
 - [NA] **C.4 Privacy in analysis**: Have we ensured that data with PII are not used or displayed unless necessary for the analysis?
 - [NA **C.5 Auditability**: Is the process of generating the analysis well documented and reproducible if we discover issues in the future?
 * Similar to previous questions, the data and the analytical approaches are public.

## D. Modeling
 - [NA] **D.1 Proxy discrimination**: Have we ensured that the model does not rely on variables or proxies for variables that are unfairly discriminatory?
 - [NA] **D.2 Fairness across groups**: Have we tested model results for fairness with respect to different affected groups (e.g., tested for disparate error rates)?
 - [NA] **D.3 Metric selection**: Have we considered the effects of optimizing for our defined metrics and considered additional metrics?
 - [NA] **D.4 Explainability**: Can we explain in understandable terms a decision the model made in cases where a justification is needed?
 - [NA] **D.5 Communicate bias**: Have we communicated the shortcomings, limitations, and biases of the model to relevant stakeholders in ways that can be generally understood?
 * The first two questions are irrelevant to this project since the data is anonymized and there is no possible grouping or discrimination issue. The three other questions answers are defined by the project and are available at https://github.com/dsp-uga/sp19/blob/master/projects/p3/project3.pdf.

## E. Deployment
 - [NA] **E.1 Redress**: Have we discussed with our organization a plan for response if users are harmed by the results (e.g., how does the data science team evaluate these cases and update analysis and models to prevent future harm)?
 - [NA] **E.2 Roll back**: Is there a way to turn off or roll back the model in production if necessary?
 - [NA] **E.3 Concept drift**: Do we test and monitor for concept drift to ensure the model remains fair over time?
 - [NA] **E.4 Unintended use**: Have we taken steps to identify and prevent unintended uses and abuse of the model and do we have a plan to monitor these once the model is deployed?
 * Again the data and model as well as approaches are public, and we just tried to modify and improve them. Therefore, the questions seem not applicable to this project. However, all the above questions are pointing very important issues, which should be considered and addressed.

*Data Science Ethics Checklist generated with [deon](http://deon.drivendata.org).*