

def ChronalCalibrationCalculateSum():
    filename = 'input.txt'
    with open(filename, 'r') as input:
        frequency = 0
        for line in input:
            new_freq = int(line.split()[0])
            frequency += new_freq

    print('Total frequency is {}'.format(frequency))

def ChronalCalibrationFindDouble():
    filename = 'input.txt'
    with open(filename, 'r') as input:
        frequency_list = []
        first_double_freq = None
        for line in input:
            new_freq = int(line.split()[0])
            frequency_list.append(new_freq)

    frequency = 0
    found_frequencies = [0]
    while first_double_freq is None:
        print('Looping through numbers...', len(found_frequencies))
        for freq in frequency_list:
            frequency += freq
            if frequency not in found_frequencies:
                found_frequencies.append(frequency)
            else:
                if first_double_freq is None:
                    first_double_freq = frequency

    print('First frequency found twice is {}'.format(first_double_freq))