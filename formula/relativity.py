# Snippet by: Muhammad Hammad Hassan

import math

def relativity(M,v):
  c = 299792458 # m/s
  generalRelativity = M * math.pow(c,2)
  LF_sub = 1-(v/math.pow(c,2))
  lorentzFactor = math.pow(LF_sub,(1/2))
  r = generalRelativity / lorentzFactor
  return r