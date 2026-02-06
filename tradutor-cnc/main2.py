from funcs import *

F  = 0.2
C  = 0.1
Vc = 100
Rm = 630
Wt = 1

"""
header( rpm_lim, vc )
end()
add()
finish()
facear(        p, i, f, F, C, D, d )
usinar(        p, i, f, F, C, Z, z )
desbaste(      p, i, f, F, C, D, d, w )
circular_cwc(  p, x, z, F, C, r )
circular_cw(   p, x, z, F, C, r )
recuo(         xS,    zS )
"""
#	tool 1
add( header(rpm_lim=630, vc=Vc) )
add( recuo( xS=-100, zS=-1 ) )
#	facear / tool 1
add( facear( p=-0.5, i=0, f=-1, F=F, C=C, D=-82, d=0 ) )
add( recuo( xS=-100, zS=-1 ) )
#	usinar / tool 2
add( usinar( p=1.0, i=-80, f=-76, F=F, C=C, Z=0, z=-50 ) )
add( usinar( p=0.4, i=-76, f=-75.6, F=F, C=C, Z=0, z=-50 ) )
#	usinar / tool 2
add( usinar( p=1.0, i=-75, f=-44, F=F, C=C, Z=0, z=-10 ) )
add( usinar( p=1.0, i=-44, f=-38, F=F, C=C, Z=0, z=-7 ) )
add( move( xS=-44, zS=-7, F=F ) )
#	arredondamento / tool 3
add( circular_cwc( p=0.25, x=-44, z=-7, F=F, C=C, r=3 ) )
add( recuo( xS=-100, zS=-15 ) )
#	rasgo / tool 4
add( move( xS=-80, zS=-15, F=F ) )
add( desbaste( p=-0.5, i=-15, f=-21, F=F, C=C, D=-76, d=-52, w=Wt ) )
add( desbaste( p=-0.5, i=-21, f=-28.5, F=F, C=C, D=-76, d=-40, w=Wt ) )
add( desbaste( p=-0.5, i=-28.5, f=-34.5, F=F, C=C, D=-76, d=-52, w=Wt ) )
add( recuo( xS=-80, zS=-39.5 ) )
add( desbaste( p=-0.5, i=-39.5, f=-43.5, F=F, C=C, D=-76, d=-41.6, w=Wt ) )
add( recuo( xS=-80, zS=-21 ) )
add( move( xS=-52, zS=-21, F=F ) )
add( circular_cw(  p=0.25, x=-52, z=-21, F=F, C=C, r=6 ) )
add( move( xS=-52, zS=-28.5, F=F ) )
add( circular_cwc( p=0.25, x=-52, z=-28.5, F=F, C=C, r=6 ) )
add( recuo( xS=-90, zS=-42.5 ) )
add( desbaste( p=-1.0, i=-42.5, f=-42.5-Wt, F=F, C=C, D=-76, d=0, w=Wt) )

add( end() )

gcode = finish()

print( gcode )
