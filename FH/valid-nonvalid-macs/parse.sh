grep "/ Cisco Systems. Inc" Condensed\ Acrylic\ AP\ -\ non\ Ideal.txt > macs.log
awk -F "," '{print$2}' AP*.csv > AP.log
#sort macs.log| uniq -d > unique.log
#awk -F "-" '{print$1}' unique.log> macs.log
#rm -r unique.log
awk -F "-" '{print$1}' macs.log> macsACC.log
rm -r macs.log
#cat AP.log | rev | cut -d ':' -f2- | rev > APmaclower.log
sed 's/.$//' AP.log > APmaclower.log
tr '[:lower:]' '[:upper:]' <APmaclower.log> APmac.log
rm -r APmaclower.log
grep -B 1 'UMKCWPA' Condensed\ Acrylic\ AP\ -\ non\ Ideal.txt > macs.log
sed '/UMKCWPA/d' macs.log > tempmacs.log
sed '/--/d' tempmacs.log > macs.log
rm -r tempmacs.log
