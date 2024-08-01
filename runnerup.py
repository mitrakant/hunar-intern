def find_runner_up_score(scores): 
    unique_scores = sorted(set(scores), reverse=True)
    if len(unique_scores) > 1: 
        return unique_scores[1] 
    else: 
        return None 
if _name_ == "_main_": 
    n = int(input("Enter the number of scores: ")) 
    scores = list(map(int, input("Enter the scores separated by space: ").split())) 
    runner_up = find_runner_up_score(scores) 
    if runner_up is not None: 
        print("The runner-up score is:", runner_up) 
    else: 
        print("There is no runner-up.")
