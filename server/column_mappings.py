# Column mapping dictionaries for categorical feature encoding
# Following the exact pattern from data_cleaning.ipynb

# Binary encoding
gender_map = {"female": 0, "male": 1}
lunch_map = {"free/reduced": 0, "standard": 1}
prep_map = {"none": 0, "completed": 1}
first_child_map = {"no": 0, "yes": 1}

# Ordinal encoding (logical order of education levels)
education_map = {
    "some high school": 0,
    "high school": 1,
    "some college": 2,
    "associate's degree": 3,
    "bachelor's degree": 4,
    "master's degree": 5
}

# Ordinal encoding for ethnic group
ethnicity_map = {
    "group A": 0,
    "group B": 1,
    "group C": 2,
    "group D": 3,
    "group E": 4
}

# Nominal encoding (arbitrary order, but still manually assigned)
marital_map = {
    "single": 0,
    "married": 1,
    "divorced": 2,
    "widowed": 3
}

sport_map = {
    "never": 0,
    "sometimes": 1,
    "regularly": 2
}

transport_map = {
    "school_bus": 0,
    "private": 1
}

study_map = {
    "< 5": 0,
    "5 - 10": 1,
    "> 10": 2
}
