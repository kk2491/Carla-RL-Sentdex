import matplotlib.pyplot as plt 
reward_list = []

with open("reward_file.txt", "r") as rfile:
	data = rfile.read()
	data = data.split()
	#print(data)
	#reward_list.append(data)

print(reward_list)
plt.plot(data)
plt.show()
