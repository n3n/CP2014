(m, n) = tuple(map(int, raw_input().split()))
d, work_List = { }, { }
for i in xrange(m):
	n_Worker, lvl_Worker, wage_Worker = tuple(map(int, raw_input().split()))
	d[lvl_Worker] = wage_Worker
budget = 0
for j in xrange(n):
	works, work_Time = raw_input().split()
	#d[int(works[1])] = wage*int(work_Time)

	if int(works[1:]) not in work_List:
		work_List[int(works[1:])] = int(work_Time)
	else:
		work_List[int(works[1:])] += int(work_Time)
	budget += d[int(works[1:])] * int(work_Time)
time_List = work_List.values()

print budget, max(time_List)
	
		
