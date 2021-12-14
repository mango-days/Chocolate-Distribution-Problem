# Chocolate Distribution Problem

# Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are M students, the task is to distribute chocolate packets among M students such that :

# 1. Each student gets exactly one packet.

# 2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.

chocolates_per_packet = [ 3, 4, 1, 9, 56, 7, 9, 12 ]
total_students = 5

while len ( chocolates_per_packet ) > total_students :
    
    total_chocolates = sum ( chocolates_per_packet )
    avg_chocolates = total_chocolates / len ( chocolates_per_packet )
    if avg_chocolates - min ( chocolates_per_packet ) > max ( chocolates_per_packet ) - avg_chocolates :
        chocolates_per_packet .remove ( min ( chocolates_per_packet ) )
    else :
        chocolates_per_packet .remove ( max ( chocolates_per_packet ) )

print ( chocolates_per_packet )