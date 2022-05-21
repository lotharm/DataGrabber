# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:21:14 2021

@author: Schroeder
"""
#https://www.dividendenadel.de/indexmonitor-maerz-2021/
#zykliker: Chemie , rohstoofe (spaet im zyklus)Bauträger, Maschiennebau, REITS, Banken, Versicheurngen, Autobauer, ReisenHotels, Kreuztfahreten
#Antizyklishc/Defneisv: telekom, nestle, Metro,

import my_setup

path = my_setup.path + "ETFS/Mutterlisten/"

Universe = {'quellpfad':[  path,
                           path,
                           path,
                           path,
                           path,
                        #    path,
                           path,
                           path,
                           path],
                        #    path,
                        #    path,
                        #    path] ,
             'quelldatei': [ 'EUsektoren', 
                             'USSectors',
                             'SP500',
                             'europa',
                             "PrimeAllShare",
                            #  "styles",
                             "Aristokraten",
                             "Rohstoffe",
                             "MDAX"],
                            #  "AMERICA600",
                            #  'AlleAnbieter',
                            #  'AlleInternational'], 
             'plotdir':[ my_setup.path+"ETFS/RES_EUsektoren/Plots/",
                        my_setup.path+"ETFS/RES_USSectors/Plots/",
                        my_setup.path+"ETFS/RES_SP500/Plots/",
                        my_setup.path+"ETFS/RES_europa/Plots/",
                        my_setup.path+"ETFS/RES_PrimeAllShare/Plots/",
                        # my_setup.path+"ETFS/RES_styles/Plots/",
                        my_setup.path+"ETFS/RES_Aristokraten/Plots/",
                        my_setup.path+"ETFS/RES_Rohstoffe/Plots/",
                        my_setup.path+"ETFS/RES_MDAX/Plots/"],
                        # my_setup.path+"ETFS/RES_AMERICA600/Plots/",           
                        # my_setup.path+"ETFS/RES_AlleAnbieter/Plots/",
                        # my_setup.path+"ETFS/RES_AlleInternational/Plots/"],
             'resdir':[ my_setup.path+"ETFS/RES_EUsektoren/Res/",
                        my_setup.path+"ETFS/RES_USSectors/Res/",
                        my_setup.path+"ETFS/RES_SP500/Res/",
                        my_setup.path+"ETFS/RES_europa/Res/",
                        my_setup.path+"ETFS/RES_PrimeAllShare/Res/",
                        # my_setup.path+"ETFS/RES_styles/Res/",
                        my_setup.path+"ETFS/RES_Aristokraten/Res/",
                        my_setup.path+"ETFS/RES_Rohstoffe/Res/",
                        my_setup.path+"ETFS/RES_MDAX/Res/"],
                        # my_setup.path+"ETFS/RES_AMERICA600/Res/",
                        # my_setup.path+"ETFS/RES_AlleAnbieter/Res/",
                        # my_setup.path+"ETFS/RES_AlleInternational/Res/"],
             'vamsdir':[my_setup.path+"ETFS/RES_EUsektoren/Vams/",
                       my_setup.path+"ETFS/RES_USSectors/Vams/",
                       my_setup.path+"ETFS/RES_SP500/Vams/",
                       my_setup.path+"ETFS/RES_europa/Vams/",
                       my_setup.path+"ETFS/RES_PrimeAllShare/Vams/",
                    #    my_setup.path+"ETFS/RES_styles/Vams/",
                       my_setup.path+"ETFS/RES_Aristokraten/Vams/",
                       my_setup.path+"ETFS/RES_Rohstoffe/Vams/",
                       my_setup.path+"ETFS/RES_MDAX/Vams/"],
                    #    my_setup.path+"ETFS/RES_AMERICA600/Vams/",
                    #    my_setup.path+"ETFS/RES_AlleAnbieter/Vams/",
                    #    my_setup.path+"ETFS/RES_AlleInternational/Vams/"],
            'tmpdatadir':[my_setup.path+"ETFS/RES_EUsektoren/Data/",
                       my_setup.path+"ETFS/RES_USSectors/Data/",
                       my_setup.path+"ETFS/RES_SP500/Data/",
                       my_setup.path+"ETFS/RES_europa/Data/",
                       my_setup.path+"ETFS/RES_PrimeAllShare/Data/",
                    #    my_setup.path+"ETFS/RES_styles/Data/",
                       my_setup.path+"ETFS/RES_Aristokraten/Data/",
                       my_setup.path+"ETFS/RES_Rohstoffe/Data/",
                       my_setup.path+"ETFS/RES_MDAX/Data/"],
                    #    my_setup.path+"ETFS/RES_AMERICA600/Data/",
                    #    my_setup.path+"ETFS/RES_AlleAnbieter/Data/",
                    #    my_setup.path+"ETFS/RES_AlleInternational/Data/"]   
            }

################################################################################################################
# EUsektoren  USSectors SP500 europa Aristokraten Rohstoffe styles stylesbroad asiapacificeats 
# AlleAnbieter AlleInternational macro MDAX PrimeAllShare AMERICA600 MyPortfolio 
#################################################################################################################

"""
keyword = "PrimeAllShare"

Universe = {'quellpfad':[path],
            'quelldatei': [keyword], 
            'plotdir':[my_setup.path+"ETFS/RES_" + keyword + "/Plots/"],
            'resdir':[my_setup.path+"ETFS/RES_" + keyword + "/Res/"],
            'vamsdir':[my_setup.path+"ETFS/RES_" + keyword + "/Vams/"],
            'tmpdatadir':[my_setup.path+"ETFS/RES_" + keyword + "/Data/"],
            } 
"""

enddatum=my_setup.enddatum 
Anzahl = 0 

if my_setup._for_backtesting_purpose:
    periode = "15y"
    ll=1000
else:
    periode = "12mo"
    ll=80

