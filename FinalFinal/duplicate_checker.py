notes = [130, 128, 128, 128, 130, 128, 130, 128, 130, 128, 130, 128, 130, 128, 130, 128, 162, 128, 130, 128, 130, 128, 130, 128, 162, 128, 130, 128, 130, 128, 138, 128, 138, 128, 130, 128, 128, 128, 130, 128, 160, 128, 138, 128, 130, 128, 130, 128, 162, 128, 130, 128, 130, 128, 130, 128, 162, 128, 130, 128, 130, 128, 136, 128, 136, 128, 130, 128, 130, 128, 130, 128, 130, 128, 130, 128, 130, 128, 128, 128, 128, 128, 130, 128, 130, 128, 128, 128, 128, 128, 130, 128, 130, 128, 128, 128, 128, 128, 130, 128, 128, 128, 130, 128, 128, 128, 130, 128, 130, 128, 128, 128, 128, 128, 130, 128, 130, 128, 130, 128, 128, 128, 130, 128, 130, 128, 130, 128, 128, 128, 130, 128, 130, 128, 128, 128, 128, 128, 130, 128, 130, 128, 128, 128, 128, 128, 136, 128, 136, 128, 128, 128, 160, 128, 128, 128, 128, 128, 128, 128, 128, 128, 130, 128, 130, 128, 128, 128, 128, 128, 130, 128, 130, 128, 128, 128, 128, 128, 136, 128, 136, 128, 128, 128, 160, 128, 128, 128, 128, 128, 128, 128, 136, 128, 130, 128, 130, 128, 138, 128, 138, 128, 128, 128, 138, 128, 130, 128, 128, 128, 128, 128, 128, 128, 128, 128, 136, 128, 130, 128, 128, 128, 128, 128, 128, 128, 138, 128, 138, 128, 130, 128, 128, 128, 138, 128, 130, 128, 138, 128, 128, 128, 200, 128, 168, 128, 128, 128, 128, 128, 200, 128, 168, 128, 128, 128, 192, 128, 192, 128, 128, 128, 192, 128, 192, 128, 192, 128, 192, 128, 192, 128, 224, 128, 192, 128, 192, 128, 192, 128, 128, 128, 192, 128, 192, 128, 224, 128, 192, 128, 192, 128, 192, 128, 192, 128, 224, 128, 192, 128, 192, 128, 192, 128, 224, 128, 192, 128, 192, 128, 192, 128, 224, 128, 192, 128, 128, 128, 200, 128, 192, 128, 128, 128, 192, 128, 128, 128, 128, 128, 192, 128, 192, 128, 128, 128, 130, 128, 130, 128, 130, 128, 128, 128, 192, 128, 192, 128, 192, 128, 128, 128, 130, 128, 130, 128, 128, 128, 128, 128, 192, 128, 192, 128, 128, 128, 128, 128, 128, 128, 130, 128, 128, 128, 128, 128, 128, 128, 192, 128, 128, 128, 128, 128, 128, 128, 136, 128, 136, 128, 136, 128, 136, 128, 136, 128, 136, 128, 136, 128, 136, 128, 136, 128, 136, 128, 136, 128, 136, 128, 136, 128, 136, 128, 138, 128, 162, 128, 130, 128, 130, 128, 130, 128, 130, 128, 130, 128, 130, 128, 130, 128, 162, 128, 130, 128, 130, 128, 130, 128, 226, 128]
for i in range(len(notes)-1):
	if notes[i] == notes[i+1] and notes[i] != 128:
		print("Found duplicate " + str(i))