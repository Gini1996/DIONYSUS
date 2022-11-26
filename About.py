import Init as Ini

def Sobre():
  print("---------------------------------------------------------------------------------------------------")
  print("+ TEMA:                                                                                           +")
  print("+ O tema do projeto é o desenvolvimento de um aplicativo de gerenciamento para restaurantes finos.+")
  print("---------------------------------------------------------------------------------------------------")
  print("+ OBJETIVO:                                                                                       +")
  print("+   O objetivo do projeto é proporcionar o gerenciamento automatizado para todo o restaurante,    +") 
  print("+   facilitando assim o gerenciamento do negócio e também proporcionando conforto ao proprietario.+")
  print("---------------------------------------------------------------------------------------------------")
  print("+ DESENVOLVIDO POR:             RA:                                                               +")
  print("+   Leonardo Gini Ferreira        2840482013022                                                   +")
  print("---------------------------------------------------------------------------------------------------")
  
  print("---------------------------------------------------------------------------------------------------")
  print("+   Pressione 9 para voltar ao inicio                                                             +")
  print("---------------------------------------------------------------------------------------------------")
  
  btVolta = int(input(""))
  
  if btVolta == 9:
   Ini.TelaInicial()