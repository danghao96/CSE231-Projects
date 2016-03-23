import times

print("Test Program for the Times Class\n")
# Output Test
print("Output Test".center(30, "-"))
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

# From String Test
print("\n", "From String Test".center(30, "-"), sep="")
T = times.Time()
T.from_str( "06:15:30+05" )
print("Input String: \"06:15:30+05\"\nOutput Time:  ", T)

# Get As Local Test
print("\n", "Get As Local Test".center(30, "-"), sep="")
local_A = A.get_as_local()  # 06:15:30 AM  
local_B = B.get_as_local()  # 08:09:15 AM  
local_C = C.get_as_local()  # 02:20:45 PM  
local_D = D.get_as_local()  # 11:59:00 PM  
local_E = E.get_as_local()  # Noon  
local_F = F.get_as_local()  # Midnight
print("Input Time:  ", A, "\nOutput Local:", local_A)
print("Input Time:  ", B, "\nOutput Local:", local_B)
print("Input Time:  ", C, "\nOutput Local:", local_C)
print("Input Time:  ", D, "\nOutput Local:", local_D)
print("Input Time:  ", E, "\nOutput Local:", local_E)
print("Input Time:  ", F, "\nOutput Local:", local_F)

# Comparison Test
print("\n", "Comparison Test".center(30, "-"), sep="")
T1 = times.Time( 7, 35, 15, -6 )
T2 = times.Time( 7, 21, 30, -5 )
print( "Time 1 is:", T1, "\nTime 2 is:", T2 )
print( "T1 == T2:", T1 == T2 )
print( "T1 != T2:", T1 != T2 )
print( "T1 < T2: ", T1 < T2 )
print( "T1 <= T2:", T1 <= T2 )
print( "T1 > T2: ", T1 > T2 )
print( "T1 >= T2:", T1 >= T2 )

# Addition Test
print("\n", "Addition Test".center(30, "-"), sep="")
T1 = times.Time( 23, 15, 0, 5 )
T2 = T1 + 300
T3 = T1 + 3600
T4 = T1 + -90000
print( "T1:         ", T1 )
print( "T1 + 300:   ", T2 )
print( "T1 + 3600:  ", T3 )
print( "T1 + -90000:", T4 )

#Subtraction Test
print("\n", "Subtraction Test".center(30, "-"), sep="")
T1 = times.Time( 14, 20, 45 )
T2 = times.Time( 14, 18, 15 )
print( "Time 1 is:", T1, "\nTime 2 is:", T2 )
print( "T1 - T2:", T1 - T2 )
print( "T2 - T1:", T2 - T1 )
print()
T1 = times.Time( 7, 35, 15, -6 )
T2 = times.Time( 7, 21, 30, -5 )
print( "Time 1 is:", T1, "\nTime 2 is:", T2 )
print( "T1 - T2:", T1 - T2 )
print( "T2 - T1:", T2 - T1 )

print("\nTest Completed!")