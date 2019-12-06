#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    score_total = 0
    for score in scores:
        score_total += score
    
    # calculate average score
    average = score_total / len(scores)

    # calculating median
    n = len(scores) 
    scores.sort() 
  
    if n % 2 == 0: 
        median1 = scores[n//2] 
        median2 = scores[n//2 - 1] 
        median = (median1 + median2)/2
    else: 
        median = scores[n//2] 
    
    # format and display the result
    print()
    print("Score total:       ", score_total)
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", average)
    print("Low Score:         ", min(scores))
    print("High Score:        ", max(scores))
    print("Median Score:      ", median)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
