import definitions
# The line above will let you separate your concerns by defining functions your calculator might use in a separate file.
import definitions

print("Welcome to the Life Calculator.")
print("Your career choices are: " + str(definitions.career_list))
choice=input("What is your career? ")
exp_years=input("How many years of experience do you have? ")
edu_years=input("How many years of education do you have? ")

exp_years=int(exp_years)
edu_years=int(edu_years)

print(definitions.life_choice_proto(choice, edu_years, exp_years))

    
    
#   
    	
# elif choice == 
#     exit();


# def advanced_scored_game(number):
#     score=0
#     for x in range(0, number):
#         print("Your score is " + str(score))
#         selected_question = input("Please select what number (0-100) of question you'd like: ")
#         selected_question=int(selected_question)
#         print("Your question is: " + response[selected_question]["question"])
#         user_answer = input("What is your answer? ")
#         #check to see if exactly equal
#         if user_answer.lower() == response[selected_question]["answer"].lower():
#             print("You're right! Congratulations!")
#             score+=response[selected_question]["value"]
#         #check to see if value is within 30% similar
#         elif (similar_text(user_answer.lower(), response[selected_question]["answer"].lower())>=30):
#                 print(str(similar_text(user_answer.lower(),  response[selected_question]["answer"].lower())))
#                 try_two=input("Try again. Are you sure your answer is correct? ")
#                 if try_two.lower()==response[selected_question]["answer"].lower():
#                     score+=response[selected_question]["value"]
#                     print("Good job, you got the answer right!")
#                 else:
#                     print("Sorry, you're wrong.")
#                     score-=response[selected_question]["value"]
#         else:
#             print("You're wrong, but the right answer was " + response[selected_question]["answer"])
#             score-=response[selected_question]["value"]
#     print("Game Over! You finished with a score of " + str(score))
#     return "Your game has been completed " + str(number) + " times."

# trials = input("How many times do you want to play? ")
# advanced_scored_game(int(trials))

