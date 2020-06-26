code = """
storage_spot_1 = input()
storage_spot_2 = input()
storage_spot_3 = storage_spot_1

if storage_spot_1 > storage_spot_2:
	storage_spot_3 = storage_spot_1
elif storage_spot_1 < storage_spot_2:
	storage_spot_3 = storage_spot_2

print( storage_spot_3 )
"""
exec(code)
