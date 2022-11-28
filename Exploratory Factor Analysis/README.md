# Exploratory Factor Analysis

In this project, we shall apply **exploratory factor analysis** in the [dataset](http://archive.ics.uci.edu/ml/datasets/Student+Performance) from the **UCI Machine Learning Repository** that contains grades, demographic, and social information of students in secondary education from two Portuguese schools. There are two datasets related with two subjects: Mathematics (mat) and Portuguese language (por). 

In the `descriptive_analysis.ipynb` file, we perform a *descriptive analysis* on the dataset. Thus, we set the relevant variables to apply factor analysis.

## Important files

- `dataset/student-mat.csv`: CSV file (dataset) with the student's grades in Mathematics;

- `dataset/student-por.csv`: CSV file (dataset) with the student's grades in Portuguese;

- `descriptive_analysis.ipynb`: Jupyter Notebook that contains a descriptive analysis of the dataset;

## Dataset

| Order | Variable | Description | Values |
| --- | --- | --- | --- |
| 1 | school | student's school | 'GP' (Gabriel Pereira)<br> 'MS' (Mousinho da Silveira) |
| 2 | sex | student's sex | 'F' (female)<br> 'M' (male) |
| 3 | age | student's age | from 15 to 22 |
| 4 | address | student's home address type |'U' (urban)<br> 'R' (rural) |
| 5 | famsize | family size | 'LE3' (less or equal to 3)<br> 'GT3' (greater than 3) |
| 6 | Pstatus | parent's cohabitation status | 'T' (living together)<br> 'A' (apart) |
| 7 | Medu | mother's education | 0 (none)<br> 1 (4th grade)<br> 2 (5th to 9th grade)<br> 3 (secondary education)<br> 4 (higher education) |
| 8 | Fedu | father's education | 0 (none)<br> 1 (4th grade)<br> 2 (5th to 9th grade)<br> 3 (secondary education)<br> 4 (higher education) |
| 9 | Mjob | mother's job | 'teacher'<br> 'health' (care related)<br> 'services' (e.g. administrative or police)<br> 'at_home'<br> 'other' |
| 10 | Fjob | father's job | 'teacher'<br> 'health' (care related)<br> 'services' (e.g. administrative or police)<br> 'at_home'<br> 'other' |
| 11 | reason | reason to choose this school | 'home' (close to home)<br> 'reputation' (school reputation)<br> 'course'<br> 'other' |
| 12 | guardian | student's guardian | 'mother'<br> 'father'<br> 'other' |
| 13 | traveltime | home to school travel time | 1 ( less than 15 min.)<br> 2 (15 to 30 min.)<br> 3 (30 min. to 1 hour)<br> 4 (greater than 1 hour) |
| 14 | studytime | weekly study time | 1 (less than 2 hours)<br> 2 (2 to 5 hours)<br> 3 (5 to 10 hours)<br> 4 (greater than 10 hours) |
| 15 | failures | number of past class failures | {1, 2, 3} |
| 16 | schoolsup | extra educational support | {'yes', 'no'} |
| 17 | famsup | family educational support | {'yes', 'no'} |
| 18 | paid | extra paid classes within the course subject | {'yes', 'no'} |
| 19 | activities | extra-curricular activities | {'yes', 'no'} |
| 20 | nursery | attended nursery school | {'yes', 'no'} |
| 21 | higher | wants to take higher education | {'yes', 'no'}) |
| 22 | internet | Internet access at home | {'yes', 'no'} |
| 23 | romantic | with a romantic relationship | {'yes', 'no'} |
| 24 | famrel | quality of family relationships | from 1 (very bad) to 5 (excellent) |
| 25 | freetime | free time after school | from 1 (very low) to 5 (very high) |
| 26 | goout | going out with friends | from 1 (very low) to 5 (very high) |
| 27 | Dalc | workday alcohol consumption | from 1 (very low) to 5 (very high) |
| 28 | Walc | weekend alcohol consumption | from 1 (very low) to 5 (very high) |
| 29 | health | current health status | from 1 (very bad) to 5 (very good) |
| 30 | absences | number of school absences | from 0 to 93 |
| 31 | G1 | first period grade | from 0 to 20 |
| 31 | G2 | second period grade | from 0 to 20 |
| 32 | G3 | final grade | from 0 to 20 |