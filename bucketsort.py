def bucket_sort(sequence):
	"""Sort sequence of entries with integer keys in range[0, n-1] using bucket-sort."""
	# Array of n sequences, each of which initially empty
	n = len(sequence)
	buckets = []
	for i in range(n):
		buckets.append([])
	# List comprehension to avoid iterating over modified sequence list
	seq = [k for k in sequence]
	# For each entry in sequence 
	for i in range(n):
		# Assign key to index for buckets
		index = (seq[i][0])
		# Append entry to respective buckets' index
		buckets[index].append(seq[i])
		# Remove entry from sequence
		sequence.remove(seq[i])
	# List comprehension to avoid iterating over modified buckets list
	buc = [p for p in buckets]
	# For each entry in buckets
	for q in range(len(buc)):
		# Append entry at end of sequence
		for z in range(len(buc[q])):
			sequence.append((buc[q][z]))
		# Remove entry from buckets
		buckets.remove(buc[q])
