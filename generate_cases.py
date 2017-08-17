#!/usr/bin/env python3
import argparse
import numpy as np

# Parse arguments
def parse_arguments():
	def positive_integer(string):
		value = int(string)

		if value > 0:
			return value
		else:
			raise argparse.ArgumentTypeError("Value must be a positive integer that is larger than 0.")

	parser = argparse.ArgumentParser(description='Generate test cases for the laser sequencer. '
									'Generate T number of test cases with N number of points. '
									'Points are unique and will be limited to a SxS sample space. '
									'Results will be written to test_cases.txt unless specified otherwise. '
									'Each line will be a test case and there will be T number of lines '
									'Each point (x-coord, y-coord) will be separated by comma '
									'Default: T = 1, N = 50, S = 12, O = test_cases.txt')
	parser.add_argument('-n', help='Number of points to generate', type=positive_integer, default=50)
	parser.add_argument('-t', help='Number of test cases', type=positive_integer, default=1)
	parser.add_argument('-s', help='Sample space for the points', type=positive_integer, default=12)
	parser.add_argument('-o', help='Output file name', default='test_cases.txt')
	args = parser.parse_args()

	return args.n, args.t, args.s, args.o

# in other words, return true if it is possible to generate unique num_points given the sample_size
def check_valid(num_points, sample_size):
	if sample_size * sample_size < num_points:
		print("Can't generate N number of unique points given the sample size S.")
		return False
	return True

# Convert a list of points to string
def points_to_string(points):
	return ','.join(['(' + str(p[0]) + ':' + str(p[1]) + ')' for p in points])

# Write list of points to file, [[(1,1), (2,3), ...], ...]
def write_to_file(list_of_points, file):
	with open(file, 'w') as f:
		for points in list_of_points:
			f.write(points_to_string(points) + '\n')

def main():
	# Get arguments
	num_points, num_test_cases, sample_size, output_filename = parse_arguments()

	if not check_valid(num_points, sample_size):
		return

	# Generate cases
	sample = [(i,j) for i in range(sample_size) for j in range(sample_size)]
	total_sample = len(sample)
	cases = []

	for _ in range(num_test_cases):
		indexes = np.random.permutation(total_sample)
		cases.append([sample[i] for i in indexes[:num_points]])

	# Write result to file
	write_to_file(cases, output_filename)

if __name__ == '__main__':
	main()