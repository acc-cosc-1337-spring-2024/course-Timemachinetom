# Homework 2

def get_options_ratio(option, total):
    ratio= option/total

    return ratio

def get_faculty_rating(ratio):
    if ratio >= .9 and ratio < 1:
        rating = "Excellent"
        return rating
    elif ratio > .8:
        rating = "Very Good"
        return rating
    elif ratio > .7:
        rating = "Good"
        return rating
    elif ratio > .6:
        rating = "Needs Improvement"
        return rating
    else:
        rating = "Unacceptable"
        return rating