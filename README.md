# laser_sequencer
Generate sequence or order sequences to be used by a laser. In other words, the next coordinate in the sequence can't be neighbors with the previous coordinate.

## Usage
Help
```
./generate_cases.py -h
./laser_sequencer.py -h
```

Example
```
./generate_cases -n 50 -t 10 -s 15 -o input.txt
./laser_sequencer.py input.txt output.txt
```

### Note
1) Input files are expected to be in the correct format, check out the sample for an example  
