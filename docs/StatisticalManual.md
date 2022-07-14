![Logo](img/PcdcLogo.png)
# PCDC Data Portal Statistical Manual

The Pediatric Cancer Data Commons (PCDC) data portal offers users the ability to analyze pediatric cancer data using a web browser. The purpose of this document is to describe how the underlying data were collected and harmonized, and to describe some statistical limitations and potential pitfalls that may be encountered during analyses. 

**Careful review and understanding of this document is a condition of use of the analytics tools on the PCDC data portal.**

## Key points
Key takeaway points include the following:

- Users should understand [limitations inherent in the PCDC dataset](StatisticalManual.md#what-are-the-limitations-of-the-data).
- Users should understand the [multiple comparisons problem](StatisticalManual.md#multiple-comparisons-problem) and account for multiple comparisons, when appropriate.
- Statistical misuse, including “[p-hacking](StatisticalManual.md#p-hacking-data-dredging),” is prohibited.
- Users are expected to follow a [hypothesis-driven approach](StatisticalManual.md#p-hacking-data-dredging) using generally-accepted statistical principles and maintain a [local hypothesis record](StatisticalManual.md#local-hypothesis-record) when performing preliminary analyses using the Kaplan-Meier curve generator.
- As a condition of access to the PCDC data portal, users agree to the PCDC [Terms of Use](TermsAndConditions.md), [Acceptable Use Policy](AcceptableUsePolicy.md), and [Privacy Policy](PcdcPrivacyNotice.md). 

## Introductory videos
Key points are summarized in the brief introductory videos below:

- [Introduction to the PCDC](https://youtu.be/uSUFthO4aBs)
- [Cohort Explorer Overview](https://youtu.be/0TJJpx3m0GY)
- [Filter Sets and Survival Analysis](https://youtu.be/8I59gX3JF2o)
- [Statistical Considerations](https://youtu.be/d_x8taJ-lP8)

## Introduction to the PCDC

The Pediatric Cancer Data Commons (PCDC) is a unified home for data on pediatric cancers, which has been made available for any researcher to explore and study. 

### Who is the PCDC?
The PCDC is headquartered and managed at the University of Chicago. The **PCDC headquarters team** includes clinical data scientists; pediatric oncologists; technical developers; data standards analysts; project managers; a communications director; and regulatory, legal and governance experts, among others. This team performs several functions, including the following:

- Development of clinical data standards
- Data harmonization
- Technical infrastructure development and maintenance
- Assisting consortia in matters of governance, development of data dictionaries, and importing data into the commons

**Data contributors** are pediatric researchers or research cooperative groups that contribute pediatric cancer data to the PCDC. 

The PCDC headquarters team partners with **disease-specific consortia**. Membership of disease-specific consortia includes clinical experts and statisticians, many of whom have played a role in developing and conducting clinical trials, and who are considered experts in their fields. Disease-specific consortia provide clinical expertise to aid in development of data dictionaries, work with data contributors to integrate data into the PCDC, and provide governance structure for handling disease-specific data. 

**Users** are researchers like you who wish to explore the data and conduct research on the data available within the commons.

### Where does the data come from and how is the data organized?

All of the data in the PCDC were collected from research studies on pediatric cancer. Patients (or their parents/guardians) provided informed consent to participate in clinical trials, and data were collected using case report forms that were specific to the aims of the particular study.

Data collection was not uniform across research studies. Case report forms may include different patient attributes, or they may capture the same attribute in different ways. For example, older clinical trials may not have captured data about specific molecular features because their clinical significance was not apparent at the time the trial was conducted. Data on tumor size may be collected in several different ways: as a continuous variable (e.g., 2.4 cm), as a “binned” ordinal variable (2-3 cm), or as a binary variable, created using a dichotomous cutoff (<5 cm, >=5 cm). The process of transforming data from multiple trials into a common format that allows data to be integrated is called **harmonization**.

The harmonization process relies on the development of a common **data dictionary**, which defines all of the data variables, including their clinical meaning, type of data (e.g., integer, boolean, enumerated categories), and permissible values. The data dictionary is developed by data analysts who work with clinical experts to determine the optimal way to represent data within a common data model. Data specific to a disease is included in a disease-specific data dictionary. Where possible, features that are common across diseases are represented in a harmonized, disease-agnostic data dictionary to facilitate cross-disease studies.

### How do I access data?

Any user who registers is able to utilize the PCDC **Cohort Explorer** to identify how many patients share clinical characteristics of interest. On a limited pilot basis, the PCDC has also released a Kaplan-Meier **survival curve generator**. Plans are also underway to develop additional analytics tools, including a **demographic table generator**. These web-based tools are designed to be a starting point for investigators to explore the data that are available and perform preliminary analyses preparatory to formal research activities (e.g., sample size calculation).

Technical documentation on using these tools is available [here](https://commons.cri.uchicago.edu/wp-content/uploads/2021/11/PCDC-Data-Portal-User-Guide.pdf).

Users wishing to perform further analyses (e.g., for publication) are required to submit a project request in order to obtain line-level access to the data. The project request will be forwarded to and reviewed by the applicable disease-specific consortia. If the project request is approved, the user will be provided with line-level access to the data, which can be analyzed using third-party statistical software outside of the PCDC web-based analytics tools.

### How do I access the data dictionaries?

Data dictionaries can be found [here](https://commons.cri.uchicago.edu/data-dictionaries/). The PCDC data portal also includes a [data dictionary explorer](https://portal.pedscommons.org/DD). Each data dictionary includes a “Readme” section, which describes how the dictionary was generated and how the dictionary is structured. The dictionary groups variables by categorical relations (e.g., subject characteristics, disease characteristics). Each variable includes a name, data type, human-readable description, mapping to [NCI Thesaurus](https://ncithesaurus.nci.nih.gov/ncitbrowser/) code, and in the case of enumerated code variables, permissible values.

### Do I need Institutional Review Board (IRB) approval to analyze data from the PCDC?

Data included within the PCDC have been de-identified/pseudonymized by removal of identifiers using the HIPAA [Safe Harbor method](https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/index.html#safeharborguidance). Because local policies and regulations may vary, researchers should check with their local institutions to determine whether institutional review board approval is required to analyze data from the PCDC.

## Analytic considerations

### What are the limitations of the data?

Whenever data from heterogeneous sources are combined, there are inherent limitations. Researchers must remain informed on the appropriate statistical methods, and exercise caution regarding interpretation of results and making inferences in light of these limitations.

#### Non-uniform treatment of patients

Data within the PCDC include clinical trials conducted by different cooperative groups around the globe, and they also include studies that have been conducted over several decades. Pooling of data may not always be appropriate when patients are not treated uniformly for the following reasons:

- Patients treated on different research studies may receive different treatments.
- Patients treated on different study arms within a research study receive different treatments.
- Studies may have different inclusion and exclusion criteria (e.g., sampling bias).
- Studies may stratify risk differently, and treatment may differ according to risk stratification.
- Patients may be treated differently due to regional conventions and differences in treatment approach.
- Analyses that include data collected on older “legacy” clinical trials may not accurately reflect outcomes expected on more contemporary treatment regimens or when more contemporary supportive measures are followed. 

Researchers should take care to understand how patients were treated on each of the included studies. Whenever possible, researchers should review study protocols corresponding to the underlying research studies.

#### Data recorded differently across studies

Data collected on independently-conducted research studies may be described or recorded differently. For example, risk stratification schemes and staging systems may vary, and anatomical sites may be described differently or with varying degrees of specificity (e.g., hand vs. upper extremity). Moreover, terms that are similar but distinct in meaning may be used (e.g., second malignant neoplasm vs. secondary malignant neoplasm). The harmonization process aims to merge data which were recorded differently while minimizing loss in data fidelity. Researchers should carefully review the data dictionary and individual study protocol documents, when relevant, to understand how data were recorded on each study and may have been transformed during the harmonization process.

#### Missing data

Not all data fields were collected in all studies. There are several reasons for missing data, which researchers should be familiar with:

- Significance of the data field was not apparent at the time of the study (i.e., data was only collected in more contemporary studies).
- Data fields were not relevant to the study aims (i.e., intentionally not collected).
- Data are missing for individual patients (i.e., data was not recorded).

Researchers should also understand that some data may be missing because it is not applicable to a given patient or disease. For example, some anatomical sites or clinical features may only apply to patients of a given sex. Moreover, features may be specific to one disease and not apply to others (e.g., disease-specific molecular features or staging classification system). In analyses where a variable under study does not apply to the population of interest, users should first filter out patients in whom the variable does not apply before applying other filters.  Where possible, analysts should discriminate between data that are missing because they are truly unknown or not collected versus data that are missing because they are not applicable to a given patient or disease.

#### Limitations of underlying studies

The quality of evidence generated from studies influences the degree of certainty we can have that the study results accurately answer a clinical question. Quality of evidence can vary due to a variety of reasons, including inherent study limitations (e.g., study design), confounding factors, measurement of indirect outcomes, imprecision and reporting bias.

### Statistical pitfalls

The PCDC data portal allows users to perform analyses on the data using web-based analytics tools. Before using these tools, users should understand potential statistical pitfalls that should be avoided. All users of PCDC analytics tools must acknowledge that they understand these statistical pitfalls and agree to avoid them as a condition of use.

#### Multiple comparisons problem

Repeatedly performing inferential statistical tests of the same type, known as “multiple comparisons,” will increase the Type I statistical error of each test, and increase the chance of incorrectly rejecting the null hypothesis. 

**Example**

> Consider the following example: A user is searching for demographic features which predict inferior outcome. The user performs 200 statistical tests, each comparing different groups of factors. The user identifies one set of demographic features which are associated with an inferior outcome, with a p-value of 0.04. Is this truly a statistically significant result?
> 
> To answer this question, we must first consider what a p-value signifies. A p-value reflects the probability of obtaining results at least as extreme as the results actually observed, under the assumption that the null hypothesis–that there is no difference between groups–is correct. In this example, a p-value of 0.04 means that there is a 4% probability (one in twenty five) of observing this result if the null hypothesis is true and there is no difference between groups. When a conventional significance level of 0.05 is used, if a p-value of 0.04 is resulted, the null hypothesis is rejected. In this example where the researcher performs 200 statistical tests comparing two groups, when one test is encountered that demonstrates an apparent difference with a 1 in 25 probability of observing this result if there is no true difference between groups, there is a reasonable likelihood that this observed difference does not actually reflect a true difference between groups but instead was observed due to chance. On the other hand, if the investigator only performed one analysis and observed a difference with a p-value of 0.04, there is a more reasonable likelihood that the observed difference reflects a true difference.

Testing a large number of hypotheses is not necessarily problematic. However, when multiple analyses (comparisons) are performed, the significance level (p-value threshold for statistically significant results) must be adjusted to account for the fact that multiple comparisons were performed. For example, genome-wide association studies which attempt to identify which single nucleotide polymorphisms are associated with a trait utilize a p-value threshold of 5 x 10<sup>-8</sup> for statistical significance to account for the extremely large number of hypothesis tests which are performed in these analyses and control for the False Discovery Rate (FDR).

To avoid the multiple comparisons problem, we encourage investigators to establish a limited set of hypotheses, develop data analysis plans a priori, and utilize methods such as the [Bonferroni correction](https://en.wikipedia.org/wiki/Bonferroni_correction) or the [Holm-Bonferroni method](https://en.wikipedia.org/wiki/Holm%E2%80%93Bonferroni_method) when appropriate. Involvement of an experienced statistician is strongly encouraged.

#### P-hacking (“data dredging”)

P-hacking (also referred to as “data dredging”) refers to indiscriminate performance of multiple hypothesis tests in search of a statistically significant result while failing to account for the multiple comparisons problem. P-hacking is a malicious form of statistical misconduct which is prohibited by the PCDC. The PCDC reserves the right to review user logfile data and revoke access in cases where P-hacking is suspected.

**Example**
> Consider the following example: the user described in the above section performed 200 statistical tests in search of a statistically significant result that could be published in a medical journal. After indiscriminately conducting 199 analyses which did not yield a p-value less than 0.05, the user performs an analysis which identifies a difference with a p-value of 0.04. The user then publishes this result as a statistically-significant discovery while failing to report on or account for the 199 statistical tests which did not identify a difference. This is an example of p-hacking.

One way to avoid p-hacking is to follow a hypothesis-driven approach, where a limited set of hypotheses are established a priori along with data analysis plans. To discourage p-hacking, the PCDC web-based survival curve generator does not report a p-value.

#### Publication bias

Publication bias occurs when the decision to publish (or report) the results of an experiment is influenced by the result. Typically, it occurs when negative research studies (i.e., those which fail to identify a statistically significant result) are not published. It is important to emphasize that reporting of negative research study findings is just as important as reporting statistically significant findings, as negative results still provide answers to clinically important questions.

If a user performs preliminary hypothesis testing using the PCDC analytics tools and the results do not appear to reveal a potentially significant result, the user is encouraged to proceed with submitting a data request to gain access to the data, perform a formal analysis, and publish the result.

#### Validation of study results

When an analysis reveals an apparently-significant result, the ability to replicate the study findings using an external dataset provides further support that the study result is valid. This process is called external validation. Having partnered with many major cooperative groups which contribute data, the PCDC will be the largest publicly-available repository of clinical pediatric cancer data. For this reason, there may be limited datasets against which results can be externally validated. We encourage users to seek out datasets that may be suitable for use in external validation (e.g., recently-closed studies not yet included in the PCDC dataset).

If an external validation dataset is not available or not large enough, an alternative approach to validate results is to partition the original data cohort into a Test Set and a Validation Set. The data may be randomly divided into Test and Validation sets, with stratification to ensure balance of factors that could potentially bias the primary endpoint. Statistical hypothesis tests are performed on the Test Set; if significant, the tests are repeated in the Validation set for confirmation. Importantly, the partitioning must be completed prior to performing any statistical tests. If an investigator has already performed an analysis on the entire dataset, it is no longer valid to split the data into separate Test and Validation sets to perform additional validation.

## Best practices for using analytics tools

The PCDC, along with leadership from member consortia and statistician experts, has developed a set of “best practices” for using analytics tools. Users are expected to abide by these best practices, as well as other generally-accepted statistical principles, when using the analytics tools

### Hypothesis-driven exploration

Any analysis performed using data within the PCDC should be conducted to investigate a hypothesis that has been defined a priori. A hypothesis may be derived from casual clinical observations, previous clinical research, or observations made in the laboratory. Hypotheses may be posed as answers to clinical questions.

Clinical questions are usually formulated as a PICO question:

- Population: What is the patient population of interest? 
- Intervention/Indicator: What intervention or independent variable is of interest?
- Comparator: What group will you compare to?
- Outcome: What is the outcome of interest (endpoint measured within each experimental unit)?

An example of a clinical question is as follows:

- P: Among patients with Stage M neuroblastoma who were diagnosed 2010-2020,
- I: is MYCN amplification
- C: compared to no MYCN amplification
- O: associated with inferior event-free survival?

A hypothesis is an educated guess about the answer to the clinical question. For example, a hypothesis would be that, among patients with Stage M neuroblastoma diagnosed 2010-2020, MYCN amplification is associated with inferior event-free survival when compared to no MYCN amplification.

Once a hypothesis is declared, a reproducible and statistically valid method for testing the hypothesis should be chosen. Every effort should be made to choose methods that reduce the risk of bias to ensure results are valid, and these methods should be declared a priori.

### Local hypothesis record

Users of the PCDC who conduct analyses using analytics tools are expected to maintain a record where they document hypotheses. The purpose of maintaining a hypothesis record is to guard against the statistical pitfalls outlined above and to strengthen the credibility of the research findings by verifying that a hypothesis was declared before analysis began.

The hypothesis record may be a paper-based document (e.g., spiral-bound notebook) or an electronic document (e.g., Google Document, Microsoft Word) which documents each hypothesis that was analyzed using analytics tools on the PCDC. Hypotheses should be declared in the record, along with the date and time the hypothesis is declared, before any analyses begin. It is strongly preferred to maintain the hypothesis record as a document on a cloud-based service with an auditable version history (e.g., Google Document); this provides third-party verification of the date and time the hypothesis was recorded. Users may also wish to record a brief summary of the results of analyses in the hypothesis record, though this is not required.

Users should electronically submit hypothesis record entries (e.g., scanned copy of handwritten hypothesis record, digital file, link to “cloud”-based document) along with project requests when requesting line-level access to the data. Users who do not submit a hypothesis record with a project request may be requested to submit a hypothesis record, and failure to submit a hypothesis record may result in denial of a project request. In cases of possible or suspected statistical misconduct, user activity log data may be reviewed and compared to the submitted hypothesis record.

## Policies and restrictions on use of analytics tools

To meet commitments to data contributors and member consortia, and to prevent misuse of data, the PCDC has developed policies which users are expected to abide by. Users should become familiar with the PCDC [Terms of Use](TermsAndConditions.md), [Acceptable Use Policy](AcceptableUsePolicy.md), and [Privacy Policy](PcdcPrivacyNotice.md). 

### Prohibition on distribution of outputs

Users are strictly prohibited from distributing or publishing any data or results generated using PCDC data exploration tools, including demographic tables and Kaplan-Meier survival curves. Users are permitted to maintain copies of preliminary analyses in a secured hypothesis record and to submit hypothesis record entries to the PCDC and member consortia along with project requests.

Users who are interested in distributing or publishing data or results generated using data from the PCDC must submit a project request form, which will be reviewed by the applicable consortia. Any distribution or publication of results will be subject to publication policies set forth by individual consortia. Users must agree to abide by publication policies as a condition to being granted access to the data.

If the PCDC or member consortia become aware of unauthorized distribution or publication of results generated using analytics tools, the PCDC reserves the right to revoke a user’s access to tools. The PCDC also reserves the right to contact conference organizers and/or journals to alert them that the unauthorized distribution of results is in violation of PCDC policies and to request retraction of the abstract/paper.

### Review of user logs

For security and abuse prevention purposes, all user activity on the PCDC analytics platform is logged, and logfiles are retained for several years. The PCDC does not routinely audit individual user logfile data but reserves the right to do so when it or its affiliates (e.g., disease-specific consortia), have reason to believe that policies have been violated. The PCDC may share identifiable logfile data with affiliates (e.g., member consortia, data contributors, scientific advisory committee) as it deems appropriate. The PCDC reserves the right to share identifiable logfile data with member consortia if one or more consortia request logfile data in connection with a project request. The PCDC may, from time to time, perform global audits where aggregate user activity and trends are assessed. If global audits reveal suspected violations of PCDC policies (e.g., users who perform a large number of queries), the PCDC may review individual logfile data in detail to investigate suspected abuse. The PCDC reserves the right to contact users to clarify how they are using the tools to identify if a policy violation has occurred. De-identified and/or aggregate user data derived from logs may be used or disclosed without limitation.

Users seeking additional information about how data are handled are encouraged to review the PCDC [Privacy Policy](PcdcPrivacyNotice.md).

### Access

The PCDC reserves the right to suspend or revoke access to its platform, including analytics tools, at its sole discretion for any reason.

### Data analytics attestation

Users wishing to use analytics tools must attest that they

- Have reviewed this statistical manual in its entirety, understand the material within it, and agree to follow the principles set forth in the manual.
- Agree to not violate PCDC policies, including the [Acceptable Use Policy](AcceptableUsePolicy.md) and [Terms of Use](TermsAndConditions.md).
- Agree to not engage in p-hacking or other forms of statistical misuse.
- Agree to follow a hypothesis-driven approach with analyses and to maintain a local hypothesis record, which may be audited.

## Analytics tool pilot

Users wishing to utilize analytics tools at initial launch will be participating in a pilot release. The purpose of the pilot release is to collect data about how users utilize self-service analytics tools in order to inform more broad implementation of the tools across various consortia with additional datasets. The pilot will include review of aggregate user logfile data. Individual user logfile data will also be reviewed in cases of possible, suspected or confirmed misuse or abuse of the tools. Users may be contacted and invited to participate in a survey regarding their use of self-service analytics tools, and survey participation is voluntary. Data submitted to consortia as part of a project request may also be analyzed as part of the pilot. Results of the pilot project, including aggregate statistics and narrative descriptions of possible, suspected or confirmed misuse or abuse of the tools, may be distributed without limitation.

## Credits and acknowledgments

This document was drafted by Kirk D. Wyatt, MD, MAS (Pediatric Hematologist/Oncologist and Clinical Informatician, Sanford Health, Fargo, ND, USA) and critically revised for statistical content by Wendy B. London, PhD (Associate Professor Pediatrics, Harvard Medical School; Director of Biostatistics, Dana-Farber/Boston Children’s Cancer and Blood Disorders Center, Boston, Massachusetts, USA). The PCDC thanks the many participants from member consortia whose critical insights inspired and informed the development of this document.

