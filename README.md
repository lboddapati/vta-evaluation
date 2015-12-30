#####################
# ABOUT THE PROJECT #
#####################
This project attempts to evaluate the public transportation system in the Silicon Valley by analyzing the VTA ridership data. The VTA service is modeled as a directed graph where nodes correspond to stops and edges correspond to the connections between 2 stops. Weights are assigned to the nodes as a function of the number of VTA lines running through them, frequency of the lines and the number of commuters using the service. A "productivity rank" for the nodes is calculated using the Page Rank algorithm. Other analyses include finding average monthly and weekly ridership and service productivity per line. 

The analysis was performed using MapReduce (written in python) on the Hadoop ecosystem (using Hadoop streaming).


##########################################
### GENERATING STOPS LIST & STOP PAIRS ###
##########################################
1. MR1:: stopslist_map1.py & stopslist_reduce1.py
    <br/>Input : Ridership.csv
    <br/>Map Output : \<Direction, Service, Line\> \<Sequence, StopName, Date\>
    <br/>Reduce Output : \<Direction, Service, Line\> \<List[Stops in sequence]\>

2. MR2 :: stopslist_map2.py & stopslist_reduce2.py
    <br/>Input : Output of MR1
    <br/>Map Output : \<Stop Pair\>  \<Direction, Service, Line\>
    <br/>Reduce Output : \<Stop Pair\> \< List[Direction, Line] \>

3. MR3 :: stopslist_map3.py & stopslist_reduce3.py
    <br/>Input : Output of MR1
    <br/>Map Output : \<Stop Name\>  \<Direction, Service, Line, Sequence\>
    <br/>Reduce Output : \<Stop Name\> \< List[Direction, Service, Line, Sequence] \>


###########################################
### GENERATING PER STOP COMMUTERS COUNT ###
###########################################
1. MR1:: per_stop_commuters_map1.py & per_stop_commuters_reduce1.py
    <br/>Input : Ridership.csv
    <br/>Map Output : \<Direction, Service, Line, Date, TripId \> \<Sequence, On, Off\>
    <br/>Reduce Output : \<Direction, Service, Line, Date, TripId \> \< List[Sequence, On, Off] \>

2. MR2:: per_stop_commuters_map2.py & per_stop_commuters_reduce2.py
    <br/>Input : Output of MR1
    <br/>Map Output : \<Direction, Service, Line, Date\> \< List[Commuters at each stop in sequence per trip] \>
    <br/>Reduce Output : \<Direction, Service, Line, Date\> \< List[Total Commuters at each stop in sequence per day] \>

3. MR3:: per_stop_commuters_map3.py & per_stop_commuters_reduce3.py
    <br/>Input : Output of MR2
    <br/>Map Output : \<Direction, Service, Line\> \< List[Total Commuters at each stop in sequence per day] \>
    <br/>Reduce Output : \<Direction, Service, Line\> \< List[Average Commuters at each stop in sequence] \>


#####################################
### GENERATING PER LINE FREQUENCY ###
#####################################
1. MR1:: per_line_freq_map1.py & per_line_freq_reduce1.py
    <br/>Input : Ridership.csv
    <br/>Map Output : \<Direction, Service, Line, Date\> \<TripId, Sequence\>
    <br/>Reduce Output : \<Direction, Service, Line, Date\> \< # of Unique trips per day\>


2. MR2:: per_line_freq_map2.py & per_line_freq_reduce2.py
    <br/>Input : Output of MR1
    <br/>Map Output : \<Direction, Service, Line\> \< # of Unique trips per day\>
    <br/>Reduce Output : \<Direction, Service, Line\> \< Average Daily Frequency\>


#############################################
### GENERATING MONTHLY PER LINE COMMUTERS ###
#############################################
commuters_per_line_monthly_map.py & commuters_per_line_monthly_reduce.py
    <br/>Input : Ridership.csv
    <br/>Map Output : \<Line, Month, ServiceType\> \<Commuters\>
    <br/>Reduce Output : \<Line, Month, ServiceType\> \<Total Commuters\>


############################################
### GENERATING WEEKLY PER LINE COMMUTERS ###
############################################
commuters_per_line_weekly_map.py & commuters_per_line_weekly_reduce.py
    <br/>Input : Ridership.csv
    <br/>Map Output : \<Line, Day_of_Week\> \<Commuters\>
    <br/>Reduce Output : \<Line, Day_of_Week\> \<Total Commuters\>


############################################
### GENERATING WEEKLY PER LINE FREQUENCY ###
############################################
freq_per_line_monthly_map.py & freq_per_line_monthly_reduce.py
    <br/>Input : Ridership.csv
    <br/>Map Output : \<Line, Month, ServiceType\> \<TripId\>
    <br/>Reduce Output : \<Line, Month, ServiceType\> \<Frequency\>
    
    
###############################
### GENERATING STOP WEIGHTS ###
###############################
generate_stopweights.py
    <br/>Input:  total_commuters.txt (\<stops\> \<commuterscount\>)
    <br/>        total_frequency.txt (\<stops\> \<commuterscount\>)
    <br/>Output: stopweight.txt


###########################################
### GENERATING PAGE RANK ADJACENCY LIST ###
###########################################
generate_adjacency_list.py
    <br/>Input: stopweight.txt,stoplist.txt
    <br/>Output: Adjacency list(\<source\> \<source weight\> \<destination\> \<destination weight\>)


##############################################
### GENERATING PAGE RANKS (ITERATIVE STEP) ###
##############################################
MR1: Map Reduce step to convert
    <br/>Input: Adjacency list(\<source\> \<source weight\> \<destination\> \<destination weight\>)
    <br/>Output: \<STOPNAME\>  \<initial rank , list(Outgoing Neighbours)\>

MR2: Map Reduce step to compute the new rank (the iterative step)
    <br/>Map Input : \<STOPNAME\> \<Rank, List[outgoing neighbours]\>
    <br/>Map Output: \<STOPNAME\> \<Partial sum(in contribution from neighbours), Partial list(outgoing neighbours)\>
    <br/>Reduce Output : \<STOPNAME\> \<New rank, List[outgoing neighbours]\>
