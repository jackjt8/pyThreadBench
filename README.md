# pyThreadBench v0.0.1
# Jack Peters, St Mary's University, 28/09/2017
#
# DESCRIPTION
# 	For use in benchmarking effects of using pools to multi-thread workloads.
# 	Produces a plot showing how threads affect time to complete.
#   - A minimum is marked at the shortest time.
#
# REQUIRES
#	matplotlib
#
# SETUP (in mp_p1.py)
# 	threads		=== to the maximum number of threads available on your computer
# 	repeat		=== to the number of iterations to average over 
#					(recommend a minimum of 3)
# 	workload	=== to a large number. Don't set this too high as it can cause 
#					python to crash. (Partly due to memory usuage)
#
#         	10,000,000 approx. 1.3GB of memory.
#           100,000,000 approx. 9GB of memory.
