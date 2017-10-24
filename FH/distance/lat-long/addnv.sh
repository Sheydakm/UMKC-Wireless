awk -F";" '{$0="N/A;" OFS $0; print}' result3.csv > output.csv
rm result3.csv
awk -F";" '{$0="N/A;" OFS $0; print}' output.csv > result3.csv
rm output.csv
#awk -F";" 'BEGIN { OFS = ";" } ; {$0="nv" OFS $0; print}' Flarshim.csv >output2.csv
