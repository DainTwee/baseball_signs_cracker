# After this add something for once we have it right
from nltk.classify import NaiveBayesClassifier

def cracker_function():
    no_steal = []
    steal = []
    model = None
    while True:
        current = get_current_sign()
        if current == "qq":
            break
        '''if current == "train":
            steal_feats = [(f, 'steal') for f in steal]
            no_steal_feats = [(f, 'no steal') for f in no_steal]
            training_data = steal_feats + no_steal_feats
            model = NaiveBayesClassifier.train(training_data)'''
        pred_outcome = predict_outcome(current, no_steal, steal)
        ai_result = None
        '''if model:
            ai_result = get_ai_result(current, model)'''
        output_pred_outcome(pred_outcome, ai_result)
        true_outcome = get_true_outcome()
        if true_outcome == "steal":
            steal.append(current)
        elif true_outcome == "no steal":
            no_steal.append(current)
        else:
            print("Please enter the data correctly")

def get_current_sign():
    print("Enter the sequence then click enter.")
    sign = input()
    return sign

def predict_outcome(current, no_steal, steal):
    if not steal:
        return ["need data", "0"]
    prediction = proper_prediction(current, steal, no_steal)
    if prediction[0] != "N/A":
        return prediction
    prediction = guess_prediction(current, steal)
    return prediction

def proper_prediction(current, steal, no_steal):
    for i in range(len(current) - 1):
        check = True
        pattern = current[i] + current[i + 1]
        for sign in steal:
            if pattern not in sign:
                check = False
                break
        if check:
            for sign in no_steal:
                if pattern in sign:
                    check = False
                    break
        if check:
            print(pattern)
            return ["steal", "100"]
    return ["N/A", "0"]

def guess_prediction(current, steal):
    for i in range(len(current) - 1):
        check = True
        pattern = current[i] + current[i + 1]
        for sign in steal:
            if pattern not in sign:
                check = False
                break
        if check:
            print(pattern)
            return ["steal", "50"]
    return ["no steal", "75"]

def get_ai_result(current, model):
    return model.classify(current)

def output_pred_outcome(pred_outcome, ai_result):
    print_statement = ""
    if pred_outcome[0] == "steal":
        if pred_outcome[1] == "100":
            print_statement += "Basic: Steal incoming"
        else:
            print_statement += "Basic: Likely steal"
    elif pred_outcome[0] == "no steal":
        print_statement += "Basic: Probably no steal"
    elif pred_outcome[0] == "need data":
        print_statement += "Basic: Still need more data"
    else:
        print_statement += "Basic: something happened, investigate this"
    '''if ai_result:
        print(ai_result)'''
    print(print_statement)

def get_true_outcome():
    print("What actually happened?\tPlease enter 'steal' or 'no steal'.")
    while True:
        outcome = input()
        if outcome in ['steal', 'no steal']:
            break
        else:
            print('Please enter the data correctly')
    return outcome

if __name__ == "__main__":
    cracker_function()
