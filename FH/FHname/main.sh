# u may need to run the line below first
#sudo apt-get install gnumeric
#ssconvert FH_Names.xlsx FH_Names.csv
awk -F";" '{$0="name;" OFS $0; print}' result.csv > result1.csv
python match.py
bash format.sh
