#Kode berikut menggunakan bahasa Shell Scripting (terminal linux)
#Syntax untuk mendownload data variabel NCEP
#Sesuaikan akronim nama, tahun, dan koordinat

#Syntax untuk mendownload data NCEP/NCAR
for i in {1994..2021}; do wget -O NCEP_AirT_years_${i}.nc4 "https://downloads.psl.noaa.gov/Datasets/ncep.reanalysis/surface_gauss/air.2m.gauss.${i}.nc";done;done;done
