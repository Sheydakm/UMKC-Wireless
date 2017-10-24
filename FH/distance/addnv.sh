awk -F";" '{$0="N/A;" OFS $0; print}' extra.csv > output.csv
#rm extra.csv
#awk -F";" 'BEGIN { OFS = ";" } ; {$0="nv" OFS $0; print}' Flarshim.csv >output2.csv
