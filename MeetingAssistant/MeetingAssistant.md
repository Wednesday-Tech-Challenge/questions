Implement a simple meeting assistant. A list of strings, events[n], in the form "<person_name> <action> <start> <end>" is provided where person_name performs action from start to end, both inclusive. Times are formatted HH:MM.

Find the earliest time in the day, from "00:00" to "23:59", when all people mentioned in at least one event are available for a meeting of k minutes.

Report the answer as "HH:MM" or the string "-1" if it is not possible.

Example:
events = ["Alex sleep 00:00 08:00", Sam sleep 07:00 13:00", "Alex lunch 12:30 13:59"]
k = 60

Alex is not available until 8:00. After that, Sam is not available until 13:00. Then Alex is bus until 13:59. Return the earliest time they are both available, "14:00".
