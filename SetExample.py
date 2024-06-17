lucky_draws = set()
lucky_draws_o = {14,18,35,37,67,55,40}
lucky_draws_s = {11,18,35,36,66,55,43}
print("online draws",lucky_draws_o)
print("Shop draws",lucky_draws_s)
print((len(lucky_draws_s)))
print("set union",lucky_draws_o | lucky_draws_s)
print("set intersection",lucky_draws_o & lucky_draws_s)
print("set difference",lucky_draws_o - lucky_draws_s)
print("set difference",lucky_draws_s - lucky_draws_o)
set_1={1,3,5}
set_2={3,5,1}
print(set_1==set_2)