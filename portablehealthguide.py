#python version 3.8.5

print("Good morning, afternoon, evening or whenever. Regardless of the time, your health is important, so let's get you ready and welcome to The Healthy Field Guide, patent pending (lol, jk)!")
print("\nToday, you will be able to do any of the following: Take a Covid symptoms assessment (not CDC - approved lol), learn about Covid - 19, tips to avoid Covid - 19, etc.")

symptoms = ("Fevers", "Shortness of breath", "Headaches", "Coughing", "Fatigue or tired", "Sore throat", "Loss of taste or smell", "Body aches")

choice = None
while choice != "0":
    print(
        """
        Welcome to the Portable Health Guide

        0 - Quit
        1 - List the symptoms of Covid - 19
        2 - Take a Covid - 19 test
        3 - The basic facts and how to prevent getting Covid - 19
        4 - Tips on improving your mental health
        5 - Get a positivity boost
        """
        )

    choice = input("Please make your selection: ")
    print()

    if choice == "0":
        print("Good-bye, thank you for using the Portable Health Guide!")

    elif choice == "1":
        print(symptoms)

    elif choice == "2":
        points = 0
        print("Welcome to the Covid - 19 self test. Disclaimer: this is not a formal assessment and the best way to tell is to get tested. You will be asked a series of questions. Answer with either a 'yes' or a 'no.")
        answer = input("Do you feel like you have a fever?: ")
        if answer == "yes":
            points += 2

        answer = input("Do you feel like you have shortness of breath or difficulty breathing?: ")
        if answer == "yes":
            points += 3

        answer = input("Do you feel like you have a headache?: ")
        if answer == "yes":
            points += 1

        answer = input("Do you feel like you have been coughing a lot recently?: ")
        if answer == "yes":
            points += 2

        answer = input("Do you feel like you have fatigue or you are tired?: ")
        if answer == "yes":
            points += 1

        answer = input("Do you feel like you have a sore throat?: ")
        if answer == "yes":
            points += 1

        answer = input("Do you feel like you have a loss of taste or smell?: ")
        if answer == "yes":
            points += 2

        answer = input("Do you feel like you have body or muscle aches?: ")
        if answer == "yes":
            points += 1

        print("Your total points is:", points)
        print("If your points is over 10, you might have Covid - 19 and the best thing to do is to just stay home, get some rest, and relax. Don't worry and stay calm. If you need a positivity boost or tips to handle the stress, choose 4 or 5 in the menu.")
            

    elif choice == "3":
        print("\nCovid - 19, better known as the Coronavirus, is a respiratory illness caused by a relatively new virus that is spread from person to person, usually from respiratory droplets or close contact. It is a very contagious virus that has spread to most if not all countries of the world. Covid - 19 is a serious matter and should cause some concern but no panic. The best things that you can do are to wear a mask, stay home, wash your hands, and use hand sanitizer. Try to social distance and stay at least 6 feet from others around you. You can save someone's life if you just stay home and watch Netflix instead of going to that party. If you ever feel sick or dizzy, stay home and try to contact a doctor. If you need immediate help, call 911.")
 
    elif choice == "4":
        mentalhealth = {"Stress" : "Stress is a feeling of emotional or physcial tension. It can come from any event or thought that makes you feel frustrated, angry or nervous. Usually it is a reaction to worry or a challenge. Although it is usually considered bad, it could also be good such as to keep you alert and on time. Some ways to relieve stress are: 1. Take deep breaths. I know it's cliche, but sometimes even taking a minute to control your breathing could keep you calm. 2. Exercise. Try to go out for a walk or even just stretch on the floor. It is a healthy distraction that will help you feel better. 3. Take a nap or get some rest. Usually whenever you are sleep-deprived, you get in a bad mood and stress could be one of them. Try to relax and forget about it and just sleep.",
                        "Panic attack" : "A sudden episdoe of intense fear or anxiety and physical symptoms, based on a perceived threat rather than imminent danger. Panic attacks are basically sudden instances where you are under intense fear and they are very frightening. Some things that you can try to prevent panic attacks are: 1. Once again, try deep breathing. Don't just count down from 10 and breathe in and out, but try using new techniques like box breathing. Picture a square box. Then each side is 4 second. Breathe in while going up one side for 4 seconds. Hold it in while going sideways on the top side for 4 seconds. Then breathe out while going down the side for 4 seconds. And finallly hold it in for 4 seconds. Try and do this three times and it should help you. 2. Close your eyes and cover your eyes. This will help prevent overwhelming yourself. Keep calm and just forget about it. Close your eyes to block out the view and cover your eyes to block all sounds. 3. Picture your happy place like a vacation on a tropical island with beautiful views of the jungle and ocean. Think of a quote or a mantra in your head to distract yourself. You could even do the times table in your head.",
                        "Anger" : "Anger is an emotion where you dislike something or someone and you feel like they are wrong or have done something wrong. Anger is usually expressed through negative feelings. It could be triggered by an emotional hurt, physical pain or even rage at someone. Some ways to cope are: 1. Try to relax and notice that everything will be fine. Just because something doesn't go your way or the way you expected to doesn't mean that you have to be angry about it. First calm down and relax. It's not a big deal. Just stay calm and talk it out. 2. Use humor to release tension. Lightening up can help you face what's making you angry. Avoid sarcasm as that could make things worse. 3. Forgive. Learn to forgive but not forget. Don't let your anger or other feelings overwhelm the positive thoughts and the happiness. Try to put yourself in other people's shoes and just forgive."}
        health = input("Choose either the term 'Stress', 'Panic attack', or 'Anger'")
        if health in mentalhealth:
            definition = mentalhealth[health]
            print("\n",definition)
            
    elif choice == "5":
        import random
        print("I know that things are tough, but I hope that your day will get better.")

        quote = random.randint(1,5)
        a = "Here is your positivity boost: "
        if quote == 1:
            print(a + "'You're brave than you believe, and stronger than you seem, and smarter than you think.' - A. A. Mine.")
        elif quote == 2:
            print(a + "'Happiness is an attitude. We either make ourselves miserable, or happy and strong. The amount of work is the same.' - Francesca Reigler.")
        elif quote == 3:
            print(a + "'In three words I can sum up everything I've learning about life. It goes on.' - Robert Frost.")
        elif quote == 4:
            print(a+ "'The good life is a process, not a state of being. It is a direction, not a destination.' - Carl Rogers.")
        elif quote == 5:
            print(a + "'Challenges are what make life interesting. Overcoming them is what makes life meaningful.' - Joshua J. Marine.")
                  
                  
        
        


        


    
        

    
