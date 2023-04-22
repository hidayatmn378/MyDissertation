#Kode berikut menggunakan bahasa Python
#Syntax untuk mendownload data variabel CMEMS
#Sesuaikan akronim nama, tahun, dan koordinat

#Untuk data arus, temperatur, salinitas, MLD
#Eksperimen CMEMS: GLOBAL_ANALYSISFORECAST_PHY_001_024 (Analysis and Forecast), cakupan waktu: Since 29 Nov 2020
python -m motuclient --motu https://nrt.cmems-du.eu/motu-web/Motu --service-id GLOBAL_ANALYSISFORECAST_PHY_001_024-TDS --product-id cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m --date-min "2023-03-24 00:00:00" --date-max "2023-03-26 23:59:59" --depth-min 0.49402499198913574 --depth-max 3.5 --variable uo --variable vo --out-dir <OUTPUT_DIRECTORY> --out-name <OUTPUT_FILENAME> --user <USERNAME> --pwd <PASSWORD>
#Eksperimen CMEMS: GLOBAL_MULTIYEAR_PHY_001_030 (Reanalysis), cakupan waktu: 1 Jan 1993 to 31 Dec 2020
python -m motuclient --motu https://my.cmems-du.eu/motu-web/Motu --service-id GLOBAL_MULTIYEAR_PHY_001_030-TDS --product-id cmems_mod_glo_phy_my_0.083_P1D-m --date-min "2020-12-31 00:00:00" --date-max "2020-12-31 23:59:59" --depth-min 0.49402499198913574 --depth-max 3.5 --variable bottomT --out-dir <OUTPUT_DIRECTORY> --out-name <OUTPUT_FILENAME> --user <USERNAME> --pwd <PASSWORD>

#Untuk data chl-a
#Eksperimen CMEMS: GLOBAL_ANALYSIS_FORECAST_BIO_001_028 (Analysis and Forecast), cakupan waktu: Since 4 May 2019
python -m motuclient --motu https://nrt.cmems-du.eu/motu-web/Motu --service-id GLOBAL_ANALYSIS_FORECAST_BIO_001_028-TDS --product-id global-analysis-forecast-bio-001-028-daily --date-min "2020-12-31 00:00:00" --date-max "2020-12-31 23:59:59" --depth-min 0.49402499198913574 --depth-max 3.5 --variable chl --out-dir <OUTPUT_DIRECTORY> --out-name <OUTPUT_FILENAME> --user <USERNAME> --pwd <PASSWORD>
#Eksperimen CMEMS: GLOBAL_MULTIYEAR_BGC_001_029 (Hindcast), cakupan waktu: 1 Jan 1993 to 31 Dec 2020
python -m motuclient --motu https://my.cmems-du.eu/motu-web/Motu --service-id GLOBAL_MULTIYEAR_BGC_001_029-TDS --product-id cmems_mod_glo_bgc_my_0.25_P1D-m --date-min "2020-12-31 00:00:00" --date-max "2020-12-31 23:59:59" --depth-min 0.5057600140571594 --depth-max 3.5 --variable chl --out-dir <OUTPUT_DIRECTORY> --out-name <OUTPUT_FILENAME> --user <USERNAME> --pwd <PASSWORD>

