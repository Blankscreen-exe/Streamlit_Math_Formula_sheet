# Snippet by: Muhammad Hammad Hassan

import math

def relativity(M,v):
  """
  this finction implements Einstien's Relativity Theory's derived formula (the Lorentz version of it)
  input;
  M :float
  v :float
  returns;
  r :float
  """
  c = 299792458 # m/s
  generalRelativity = M * math.pow(c,2)
  LF_sub = 1-(v/math.pow(c,2))
  lorentzFactor = math.pow(LF_sub,(1/2))
  r = generalRelativity / lorentzFactor
  return r
