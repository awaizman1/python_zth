# write a function 'above_avg' which can take an arbitrary number of arguments and returns a list contains
# only the elements that are above the average


def above_avg(*args):

    avg = sum(args) / len(args)

    return list(filter(lambda e: e > avg, args))


print(above_avg(10, 2, 4, 9, 34, 3, 15))


# write a function 'is_sample_above_avg_factory' which takes a list of samples and returns a new function that:
# - takes a sample and tells if the sample is above the avg of samples.
# - prints the sample and the avg on each call in format: 'sample is 32, avg is 15'
# - avg should be calculates only once

def is_sample_above_avg_factory(samples):

    avg = sum(samples) / len(samples)

    def is_sample_above_avg(sample):

        print(f"sample is {sample}, avg is {avg}")
        return sample > avg

    return is_sample_above_avg


is_sample_above_avg = is_sample_above_avg_factory([10, 2, 4, 9, 34, 3, 15])
print(is_sample_above_avg(12))
print(is_sample_above_avg(10))
