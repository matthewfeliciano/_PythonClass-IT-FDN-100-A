import pickle
import os

high_scores_filename = 'high_scores.dat'

scores = []

# first time you run this, "high_scores.dat" won't exist
#   so we need to check for its existence before we load
#   our "database"
if os.path.exists(high_scores_filename):
    # "with" statements are very handy for opening files.
    with open(high_scores_filename,'rb') as rfp:
        scores = pickle.load(rfp)
    # Notice that there's no "rfp.close()"
    #   ... the "with" clause calls close() automatically!

first_name = input("Please enter your name:")
score = input("Please enter your score:")

high_scores = first_name, score
scores.append(high_scores)

# Now we "sync" our database
with open(high_scores_filename,'wb') as wfp:
    pickle.dump(scores, wfp)

# Re-load our database
with open(high_scores_filename,'rb') as rfp:
    scores = pickle.load(rfp)

print(scores)