import numpy as np
from scipy.stats import spearmanr

# Define the rankings for judges A, B, and C
rankings = {
    'A': [1, 6, 5, 10, 3, 2, 4, 9, 7, 8],
    'B': [3, 5, 8, 4, 7, 10, 2, 1, 6, 9],
    'C': [6, 4, 9, 8, 1, 2, 3, 10, 5, 7]
}

# Create an array with the rankings
rank_matrix = np.array(list(rankings.values()))

# Calculate the Spearman rank correlation coefficient for all pairs of judges
correlation_matrix = np.corrcoef(rank_matrix)

# Display the correlation matrix
print("Spearman Rank Correlation Matrix:")
print(correlation_matrix)

# Find the pair of judges with the highest correlation coefficient
max_corr = -1
judges_pair = None

for i in range(len(rankings)):
    for j in range(i + 1, len(rankings)):
        corr = correlation_matrix[i, j]
        if corr > max_corr:
            max_corr = corr
            judges_pair = ('AB'[i], 'AB'[j])

# Print the pair of judges with the highest correlation coefficient
print(f"The pair of judges with the nearest approach to common liking in music is {judges_pair} with a correlation coefficient of {max_corr:.2f}")
