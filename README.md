# Marvel vs. DC - Good vs. Bad

### Group Members:
Christina Chau | 
Nitin Dhiman | 
Robert Harvey | 
Justin Kiang | 
Xander Polny

### Where We Started
Initially started with looking at Videogames.  
Then we began exploring potential movie franchises (Fast & Furious, James Bond, Star Wars).  
Finally, we landed on Marvel/DC - Good/Bad.

### Project Focus
Can Character traits be an indicator of whether a character is morally "Good" or "Bad"?  
Traits:
Identity (Secret or Publicly-known) | 
Hair Color | 
Sex (Biological) |  
Gender/Sexual Preference | 
Eye Color | 
Studio 

### Data Sources
We utilized two datasets found on Kaggle: 
Marvel-wikia-data.csv  
DC-wikia-data.csv

### Extract, Transform, Load
Jupyter Notebook
1. Loaded Marvel and DC Kaggle CSVs
2. Cleaned datasets
3. Added Studio column to differentiate between Marvel vs DC datasets
4. Concatenated both datasets into one
5. Created SQLAlchemy engine to link pandas DataFrame with PostgreSQL

Tableau
1. Loaded cleaned CSV
2. Edited some of the dimensions
   a. Groups, Sets, Re-naming etc.
3. Created visualizations
4. Developed three Dashboards
5. Constructed a Story

### Data Model Implementation
Used Google Collab script to:
   Read CSVs
   Convert categorical data to numerical
   Develop ML models
      Target was 75%
      Started around 50/50
      Ended up with ~68%
 
 Best ML Model: Decision Tree Training, Random Forest Training, Extra Trees Training (68.22%)
 Best Scaled ML Models: Decision Tree Scaled, Random Forest Scaled, Extra Trees Scaled (68.22%)

### Results
We can condlue that certain characteristics are somewhat (68%) predictive of a comicbook character's moral compass | 
Specific traits lean one way or another | 
GSM was the most important feature within the Random Forest model

### Web Form Using Flask
Create API from the Postgres database |
Pass form inputs through app using For loop | 
Pickle ML Model

### Limitations
Time | 
Access to specific datasets | 
Predictive modelling based on string data provides additional challenges | 
New software/packages we were previously unaware of (PKL)
