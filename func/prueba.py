from datetime import datetime

current_time = datetime.utcnow()
print(current_time)
arr_time = datetime.strptime("2023-07-27 13:45", "%Y-%m-%d %H:%M")
diff = arr_time - current_time
print(diff.total_seconds()/60)
