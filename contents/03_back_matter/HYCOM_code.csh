#Kode berikut menggunakan bahasa Shell Scripting (terminal linux)
#Syntax untuk mendownload data variabel HYCOM
#Sesuaikan akronim nama, tahun, dan koordinat: #AKRONIM, #TAHUN, #KOORDINAT

#Eksperimen HYCOM: GOFS 3.1: 41-layer HYCOM + NCODA Global 1/12° Analysis, cakupan waktu: 2014-July to Present
for k in {01..12}; do for i in {01..31}; do for j in 00 03 06 09 12 15 18 21; do wget -O HYCOM_#AKRONIM_months_${k}_days_${i}_hours_${j}.nc4 "https://ncss.hycom.org/thredds/ncss/GLBy0.08/expt_93.0?var=#AKRONIM&north=#KOORDINAT&west=#KOORDINAT&east=#KOORDINAT&south=#KOORDINAT&disableProjSubset=on&horizStride=1&time=#TAHUN-${k}-${i}T${j}%3A00%3A00Z&vertCoord=&addLatLon=true&accept=netcdf4";done;done;done

#Eksperimen HYCOM: GOFS 3.1: 41-layer HYCOM + NCODA Global 1/12° Reanalysis, cakupan waktu: 1994-01-01 to 2015-12-31
for k in {01..12}; do for i in {01..31}; do for j in 00 03 06 09 12 15 18 21; do wget -O HYCOM_#AKRONIM_months_${k}_days_${i}_hours_${j}.nc4 "http://ncss.hycom.org/thredds/ncss/GLBv0.08/expt_53.X/data/#TAHUN?var=#AKRONIM&north=#KOORDINAT&west=#KOORDINAT&east=#KOORDINAT&south=#KOORDINAT&disableProjSubset=on&horizStride=1&time=#TAHUN-${k}-${i}T${j}%3A00%3A00Z&vertCoord=&addLatLon=true&accept=netcdf4";done;done;done
