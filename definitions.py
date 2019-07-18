# Feel free to code your definitions here in order to separate your concerns.
from similar_text import similar_text

career_list=["healthcare", "business",
    "arts", "infrastructure/transportation/basic services",
    "science/engineering/architecture", "social workers"]

#career scores
career_scores = {"healthcare" : 20,
    "business" : 15,
    "arts" : 10,
    "infrastructure/transportation/basic services" : 5,
    "science/engineering/architecture" : 15,
    "social workers" : 5
}
# score is set to zero at the beginning of the program.
# life score = total scores.
#Calculates the score whenever the requirements are met.

#year edu factor 

#year experience factor 

def life_choice_proto(choice, years_edu, years_exp):
    lifescore=0
    if choice.lower() in career_scores:
        lifescore = career_scores[choice]*(years_edu+years_exp)
    else: 
        max_sim=0
        for char in career_list:
            if similar_text(choice.lower(), char)>max_sim:
                max_sim=similar_text(choice.lower(), char)
        if max_sim>=5:
            print("invalid choice, but close")
            new_input=input("Please try again with something in the categories we listed for you: ")
            if new_input.lower() in career_scores:
                lifescore = career_scores[new_input]*(years_edu+years_exp)
        else:
            print("Invalid string")
    return lifescore