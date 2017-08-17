#!/usr/bin/env python3
import argparse

# Parse arguments
def parse_arguments():
	parser = argparse.ArgumentParser(description='Given the input points, generate valid sequences to be used by a laser.'
									'Each line in the input file must be a list of unique points.'
									'A valid list of points will be written to the output file if a valid sequence can be generated.'
									'Else it will write the word "INVALID SEQUENCE" for the list of points.')
	parser.add_argument('input', help='Input file')
	parser.add_argument('output', help='Output file')
	args = parser.parse_args()

	return args.input, args.output

# Convert points to string
def points_to_string(points):
	return ','.join(['(' + str(p[0]) + ':' + str(p[1]) + ')' for p in points])

# Write list of points to file, [[(1,1), (2,3), ...], ...]
def write_to_file(list_of_points, file):
	with open(file, 'w') as f:
		for points in list_of_points:
			f.write(points_to_string(points) + '\n')

# Return list of points from the input file
def input_getter(input_filename):
	with open(input_filename, 'r') as f:
		for line in f:
			points = line.strip().split(',')
			points = [p.split(':') for p in points]
			points = [(int(p[0][1:]), int(p[1][:-1])) for p in points]

			yield points

# Return true if x is a neighbor of y, else false
def neighbor(x, y):
	relative_position = [(0,1), (0,-1), (1,0), (-1,0)]

	for pos in relative_position:
		if x[0] + pos[0] == y[0] and x[1] + pos[1] == y[1]:
			return True

	return False

# Recursively generate valid sequence
def generate_sequence_helper(seq, arr):
	if not seq:
		return arr

	for i in range(len(seq)):
		if neighbor(seq[i], arr[-1]):
			continue
		else:
			res = generate_sequence_helper(seq[:i] + seq[i+1:], arr + [seq[i]])

			if res:
				return res

	return None

# Return a valid sequence if possible, else return None
def generate_sequence(seq):
	for i in range(len(seq)):
		res = generate_sequence_helper(seq[:i] + seq[i+1:], [seq[i]])

		if res:
			return res
	
	return None

# Yield valid sequence
def sequence_generator(input_filename):
	inputs = input_getter(input_filename)

	for seq in inputs:
		seq = generate_sequence(seq)
		seq = points_to_string(seq) if seq else "INVALID SEQUENCE"		
		yield seq

def main():
	# Get arguments
	input_filename, output_filename = parse_arguments()

	sequences = sequence_generator(input_filename)	

	with open(output_filename, 'w') as f:
		for s in sequences:
			f.write(s + '\n')

if __name__ == '__main__':
	main()