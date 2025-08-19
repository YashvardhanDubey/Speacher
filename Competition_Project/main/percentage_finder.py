import Levenshtein

def calc_accuracy(primary_string,secondary_string):
    distance=Levenshtein.distance(primary_string,secondary_string)
    length=max(len(primary_string),len(secondary_string))
    percentage=round(100*(1-(distance/length)))
    return percentage

def acc_message(percentage):
    if percentage==100:
        return "SUPER DUPER GOOD! Wanna try again? Also check out audio files"
    if percentage>=90:
        return "Excellent! Keep working to improve yourself. Also check out audio files"
    if percentage>=75:
        return "Good, if you keep this up, you'll get to 100% in no time! Also check out audio files"
    if percentage<=74:
        return "Try Again, Practice, and you'll get to 100% in no time! Also check out audio files"