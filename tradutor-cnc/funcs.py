import numpy as np
import math

result = []
nround = 3

def header(rpm_lim=630,vc=100):
  return ["; header","G18 G90 G71 G40","T1D1","G95 G54",f"LIMS={rpm_lim}",f"G96 S{vc} M03"]

def end():
  return ["; fim","M30"]

def add(c):
  for line in c:
    result.append( line )

def finish():
  return "\n".join( result )

def facear(p=-1,i=0,f=-1,F=0.2,C=0.1,D=82,d=0):
  ii = round(i+1, nround)
  pre  = ["; facear",f"G00 Z{ii}",f"G00 X{D}"]
  for i in np.arange(i,f+p,p):
    i  = round(i,   nround)
    ii = round(i+1, nround)
    pre.append( f"G01 Z{i} F{F}\nG01 X{d} F{C}\nG01 Z{ii} F{F}\nG00 X{D}" )
  return pre

def usinar(p=-1,i=0,f=1,F=0.2,C=0.1,Z=-1,z=-10):
  ii = round(i-2, nround)
  pre = ["; usinar",f"G00 X{ii}",f"G00 Z{Z}"]
  for i in np.arange(i,f+p,p):
    i  = round(i,   nround)
    ii = round(i-2, nround)
    pre.append( f"G01 X{i} F{F}\nG01 Z{z} F{C}\nG01 X{ii} F{F}\nG00 Z{Z}" )
  return pre

def desbaste(p=-1,i=0,f=10,F=0.2,C=0.1,D=82,d=40,w=2):
  if w > math.fabs(f-i):
    print("#"*20)
    print("ERRO: Ãrea da peÃ§a Ã© maior que o desbaste")
    print("#"*20)
    exit(1)
  i -= w
  i = round(i,   nround)
  ii = round(i+w,nround)
  pre = ["; desbaste",f"G00 X{D}",f"G00 Z{ii}"]
  for i in np.arange(i,f+p,p):
    i  = round(i,   nround)
    pre.append( f"G01 Z{i} F{F}\nG01 X{d} F{C}\nG00 X{D} F{F}" )
  return pre

def circular_cwc(p=1,x=0,z=0,F=0.2,C=0.1,r=6):
  pre = ["; interpolacao circular h",f"G00 X{x}",f"G00 Z{z}"]
  for _ in np.arange(p,r+p,p):
    i = round(z-_, nround)
    ii = round(x+_*2, nround)
    pre.append( f"G01 X{ii} F{F}\nG03 X{x} Z{i} CR={round(math.fabs(_),nround)} F{C}\nG00 X{round(x-2, nround)}\nG00 Z{z}" )
  return pre

def circular_cw(p=1,x=0,z=0,F=0.2,C=0.1,r=6):
  pre = ["; interpolacao circular ah",f"G00 X{x}",f"G00 Z{z}"]
  for _ in np.arange(p,r+p,p):
    i = round(z+_, nround)
    ii = round(x+_*2, nround)
    pre.append( f"G01 X{ii} F{F}\nG02 X{x} Z{i} CR={round(math.fabs(_),nround)} F{C}\nG00 X{round(x-2, nround)}\nG00 Z{z}" )
  return pre

def recuo(xS=-100,zS=100):
  pre = ["; recuo", f"G00 X{xS}", f"G00 Z{zS}"]
  return pre

def move(xS=-100,zS=100,F=0.2):
  pre = ["; mover", f"G01 X{xS} F{F}", f"G01 Z{zS} F{F}"]
  return pre
