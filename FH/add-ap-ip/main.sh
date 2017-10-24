awk -F";" '{$0="IP;" OFS $0; print}' result2.csv > temp.csv
awk -F";" '{$0="APname;" OFS $0; print}' temp.csv > result2.csv
rm -r temp.csv
python match.py
bash format.sh
