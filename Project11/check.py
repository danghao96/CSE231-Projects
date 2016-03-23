
import times

A = times.Time( 6, 15, 30, 5 )
B = times.Time( 8, 9, 15, -4 )
C = times.Time( 14, 20, 45 )
D = times.Time( 23, 59 )
E = times.Time( 12 )
F = times.Time()

print( "str  A: ", str(A) )
print( "repr A: ", repr(A) )
print( "str  B: ", str(B) )
print( "repr B: ", repr(B) )
print( "str  C: ", str(C) )
print( "repr C: ", repr(C) )
print( "str  D: ", str(D) )
print( "repr D: ", repr(D) )
print( "str  E: ", str(E) )
print( "repr E: ", repr(E) )
print( "str  F: ", str(F) )
print( "repr F: ", repr(F) )

T = times.Time()
T.from_str( "06:15:30+05" )
print(T)

local_A = A.get_as_local()  # 06:15:30 AM  
local_B = B.get_as_local()  # 08:09:15 AM  
local_C = C.get_as_local()  # 02:20:45 PM  
local_D = D.get_as_local()  # 11:59:00 PM  
local_E = E.get_as_local()  # Noon  
local_F = F.get_as_local()  # Midnight

print(local_A)
print(local_B)
print(local_C)
print(local_D)
print(local_E)
print(local_F)

T1 = times.Time( 7, 35, 15, -6 )
T2 = times.Time( 7, 21, 30, -5 )
print( T1 == T2 )
print( T1 != T2 )
print( T1 < T2 )
print( T1 <= T2 )
print( T1 > T2 )
print( T1 >= T2 )

T1 = times.Time( 23, 15, 0, 5 )
T2 = T1 + 300
T3 = T1 + 3600
T4 = T1 + -90000
print( T1 )
print( T2 )
print( T3 )
print( T4 )

T1 = times.Time( 14, 20, 45 )
T2 = times.Time( 14, 18, 15 )
print( T1 - T2 )
print( T2 - T1 )

T1 = times.Time( 7, 35, 15, -6 )
T2 = times.Time( 7, 21, 30, -5 )
print( T1 - T2 )
print( T2 - T1 )

error_test = times.Time( 50, 100, 1240, 1443 )