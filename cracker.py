# After this add something for once we have it right

def cracker_function():
    past_signs = []
    while True:
        current = get_current_sign()
        if current == "qq":
            break
        pred_outcome = predict_outcome(current, past_signs)
        output_pred_outcome(pred_outcome)
        true_outcome = get_true_outcome()
        past_signs = new_signs_list(current, true_outcome, past_signs)


def get_current_sign():
    pass

def predict_outcome(current, past_signs):
    pass

def output_pred_outcome(pred_outcome):
    pass

def get_true_outcome():
    pass

def new_signs_list(current, true_outcome, past_signs):
    pass

if __name__ == "__main__":
    cracker_function()
