#Surface:
#path = "C:/Users/_schr/OneDrive/Trading/"
#Desktop:
path = "C:/Users/Schroeder/OneDrive/Trading/"
#RWE:
#path = "C:/Temp/Trading/"


### Um eine spezielle Sektor oder Datendataei auszuwählen zb fuer analysis
specific_datapath = "ETFS/Analyse_data/"


#Desktop fuer Daten fuer BAcktetsting
#path = "C:/Michael/"

logger = "On"

python_path=  path + "ETFS/python/"
output_path = path + "ETFS/Analyse_data/"

## for Options tool:
trade_path = python_path + "Options/Trades/"

# Datensaetze fuer Backtesting oder Produktionslauf:
_for_backtesting_purpose = False


# Bis zu welchem Datum sollen hist. Daten gezogen werden ?
enddatum = "2022-03-04" 
