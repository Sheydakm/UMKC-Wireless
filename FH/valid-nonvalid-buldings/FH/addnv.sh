awk -F";" '{$0="nv;" OFS $0; print}' output.csv > output1.csv
#awk -F";" 'BEGIN { OFS = ";" } ; {$0="nv" OFS $0; print}' Flarshim.csv >output2.csv
