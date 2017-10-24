#grep -B 11 '# Point' Flarshim.csv > output.csv
sed '/# Point/,$!d' Flarshim.csv | sed '/# Point/d'> output.csv

