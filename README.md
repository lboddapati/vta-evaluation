######################################
# GENERATING STOPS LIST & STOP PAIRS #
######################################
1. MR1:: stopslist_map1.py & stopslist_reduce1.py
    Input : Ridership.csv
    Map Output : <Direction, Service, Line> <Sequence, StopName, Date>
    Reduce Output : <Direction, Service, Line> <List[Stops in sequence]>

2. MR2 :: stopslist_map2.py & stopslist_reduce2.py
    Input : Output of MR1
    Map Output : <Stop Pair>  <Direction, Service, Line>
    Reduce Output : <Stop Pair> < List[Direction, Line] >

3. MR3 :: stopslist_map3.py & stopslist_reduce3.py
    Input : Output of MR1
    Map Output : <Stop Name>  <Direction, Service, Line, Sequence>
    Reduce Output : <Stop Name> < List[Direction, Service, Line, Sequence] >


#######################################
# GENERATING PER STOP COMMUTERS COUNT #
#######################################
1. MR1:: per_stop_commuters_map1.py & per_stop_commuters_reduce1.py
    Input : Ridership.csv
    Map Output : <Direction, Service, Line, Date, TripId > <Sequence, On, Off>
    Reduce Output : <Direction, Service, Line, Date, TripId > < List[Sequence, On, Off] >

2. MR2:: per_stop_commuters_map2.py & per_stop_commuters_reduce2.py
    Input : Output of MR1
    Map Output : <Direction, Service, Line, Date> < List[Commuters at each stop in sequence per trip] >
    Reduce Output : <Direction, Service, Line, Date> < List[Total Commuters at each stop in sequence per day] >

3. MR3:: per_stop_commuters_map3.py & per_stop_commuters_reduce3.py
    Input : Output of MR2
    Map Output : <Direction, Service, Line> < List[Total Commuters at each stop in sequence per day] >
    Reduce Output : <Direction, Service, Line> < List[Average Commuters at each stop in sequence] >


#################################
# GENERATING PER LINE FREQUENCY #
#################################
1. MR1:: per_line_freq_map1.py & per_line_freq_reduce1.py
    Input : Ridership.csv
    Map Output : <Direction, Service, Line, Date > <TripId, Sequence>
    Reduce Output : <Direction, Service, Line, Date > < # of Unique trips per day >


2. MR2:: per_line_freq_map2.py & per_line_freq_reduce2.py
    Input : Output of MR1
    Map Output : <Direction, Service, Line > < # of Unique trips per day >
    Reduce Output : <Direction, Service, Line > < Average Daily Frequency >


#########################################
# GENERATING MONTHLY PER LINE COMMUTERS #
#########################################
commuters_per_line_monthly_map.py & commuters_per_line_monthly_reduce.py
    Input : Ridership.csv
    Map Output : <Line, Month, ServiceType > <Commuters>
    Reduce Output : <Line, Month, ServiceType > <Total Commuters>


########################################
# GENERATING WEEKLY PER LINE COMMUTERS #
########################################
commuters_per_line_weekly_map.py & commuters_per_line_weekly_reduce.py
    Input : Ridership.csv
    Map Output : <Line, Day_of_Week > <Commuters>
    Reduce Output : <Line, Day_of_Week > <Total Commuters>


########################################
# GENERATING WEEKLY PER LINE FREQUENCY #
########################################
freq_per_line_monthly_map.py & freq_per_line_monthly_reduce.py
    Input : Ridership.csv
    Map Output : <Line, Month, ServiceType > <TripId>
    Reduce Output : <Line, Month, ServiceType > <Frequency>


#######################################
# GENERATING PAGE RANK ADJACENCY LIST #
#######################################
generate_adjacency_list.py


###########################
# GENERATING STOP WEIGHTS #
###########################
generate_stopweights.py
