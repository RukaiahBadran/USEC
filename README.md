
# Usec

Dark pattern analysis

After manually removing unnecessary columns from survey_data.xlsx and renaming the headings to USE, UNDERSTADING, RATING and MALICIOUS, we start cleaning the file from empty cells.

And plot and chi squared analysis the survey data in according to the coursework.


## Plots


![use](https://github.com/user-attachments/assets/4ad26112-d50e-4c9c-b925-c3e849ea4926)

![understanding](https://github.com/user-attachments/assets/639f3214-daa0-43f4-b775-bc507e8b3207)

![rate](https://github.com/user-attachments/assets/a634e180-82dd-4602-8b0e-fcff4363c0ed)

![mal](https://github.com/user-attachments/assets/e1fcd8a6-4ff7-46ec-bae3-362be10e7dfa)


## Chi analysis results:


Hypothesis: EaseOfUnderstand vs MaliciousBinary
Chi-square value: 4.426870556794211, p-value: 0.21890675869958354
Degrees of freedom: 3
Expected frequencies:
[[  7.77272727   1.22727273]
 [ 35.40909091   5.59090909]
 [114.          18.        ]
 [ 32.81818182   5.18181818]]

--------------------------------------------------
Hypothesis: EaseOfUse vs MaliciousBinary
Chi-square value: 0.21974491501145893, p-value: 0.9743405594886153
Degrees of freedom: 3
Expected frequencies:
[[  6.05405405   0.94594595]
 [ 30.27027027   4.72972973]
 [117.62162162  18.37837838]
 [ 38.05405405   5.94594595]]

--------------------------------------------------
Hypothesis: AppRating vs MaliciousBinary
Chi-square value: 5.452538306250657, p-value: 0.24393300841203408
Degrees of freedom: 4
Expected frequencies:
[[10.36123348  1.63876652]
 [22.44933921  3.55066079]
 [62.16740088  9.83259912]
 [82.88986784 13.11013216]
 [18.13215859  2.86784141]]

--------------------------------------------------
