import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

romwe = pd.read_excel(r'C:\Users\runab\Documents\GitHub\USEC\ROMWE.xlsx')

# cleaning
clean = romwe.dropna(subset=['USE', 'UNDERSTANING', 'RATING', 'MALICIOUS'], how='all')
clean.head()

# Plot
questions = ['USE', 'UNDERSTANING', 'RATING', 'MALICIOUS']

for question in ['USE', 'UNDERSTANING', 'RATING', 'MALICIOUS']:
    plt.figure(figsize=(8, 5))
    sns.countplot(data=clean, x=question, palette='Set3')
    plt.title(f'Response Distribution for: {question}')
    plt.xticks(rotation=45)
    plt.show()

# Chi analysis


response_mapping = {
    'Strongly Disagree': 1,
    'Disagree': 2,
    'Neutral': 3,
    'Agree': 4,
    'Strongly Agree': 5
}

clean['EaseOfUse'] = clean['USE'].astype(str)
clean['EaseOfUnderstand'] = clean['UNDERSTANING'].astype(str)
clean['AppRating'] = clean['RATING'].astype(str)
clean['MaliciousBinary'] = clean['MALICIOUS'].astype(str)

hypotheses = [
    ('EaseOfUnderstand', 'MaliciousBinary'),
    ('EaseOfUse', 'MaliciousBinary'),
    ('AppRating', 'MaliciousBinary')
]

for hypo in hypotheses:
    contingency = pd.crosstab(clean[hypo[0]], clean[hypo[1]])
    chi2, p, dof, expected = chi2_contingency(contingency)
    print(f'Hypothesis: {hypo[0]} vs {hypo[1]}')
    print(f'Chi-square value: {chi2}, p-value: {p}')
    print(f'Degrees of freedom: {dof}')
    print(f'Expected frequencies: \n{expected}\n')
    print('-' * 50)
