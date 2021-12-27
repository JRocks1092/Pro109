import statistics
import csv

with open("data.csv", "r") as f:    
    reader = csv.reader(f)    
    data2 = list(reader)

math_score = []
reading_score = []
writing_score = []

data2.pop(0)

for i in data2:
    math_score.append(float(i[5]))
    reading_score.append(float(i[6]))
    writing_score.append(float(i[7]))

math_score_mean = statistics.mean(math_score)
math_score_mode = statistics.mode(math_score)
math_score_median = statistics.median(math_score)
math_score_stdev = statistics.stdev(math_score)

reading_score_mean = statistics.mean(reading_score)
reading_score_mode = statistics.mode(reading_score)
reading_score_median = statistics.median(reading_score)
reading_score_stdev = statistics.stdev(reading_score)

writing_score_mean = statistics.mean(writing_score)
writing_score_mode = statistics.mode(writing_score)
writing_score_median = statistics.median(writing_score)
writing_score_stdev = statistics.stdev(writing_score)

math_std_first_start, math_first_std_end = math_score_mean - math_score_stdev, math_score_mean + math_score_stdev
math_std_second_start, math_second_std_end = math_score_mean - (2 * math_score_stdev), math_score_mean + (2 * math_score_stdev)
math_std_third_start, math_third_std_end = math_score_mean - (3 * math_score_stdev), math_score_mean + (3 * math_score_stdev)

reading_std_first_start, reading_first_std_end = reading_score_mean - reading_score_stdev, reading_score_mean + reading_score_stdev
reading_std_second_start, reading_second_std_end = reading_score_mean - (2 * reading_score_stdev), reading_score_mean + (2 * reading_score_stdev)
reading_std_third_start, reading_third_std_end = reading_score_mean - (3 * reading_score_stdev), reading_score_mean + (3 * reading_score_stdev)

writing_std_first_start, writing_first_std_end = writing_score_mean - writing_score_stdev, writing_score_mean + writing_score_stdev
writing_std_second_start, writing_second_std_end = writing_score_mean - (2 * writing_score_stdev), writing_score_mean + (2 * writing_score_stdev)
writing_std_third_start, writing_third_std_end = writing_score_mean - (3 * writing_score_stdev), writing_score_mean + (3 * writing_score_stdev)

math_1_std = [result for result in math_score if result > math_std_first_start and result < math_first_std_end]
math_2_std = [result for result in math_score if result > math_std_second_start and result < math_second_std_end]
math_3_std = [result for result in math_score if result > math_std_third_start and result < math_third_std_end]

reading_1_std = [result for result in reading_score if result > reading_std_first_start and result < reading_first_std_end]
reading_2_std = [result for result in reading_score if result > reading_std_second_start and result < reading_second_std_end]
reading_3_std = [result for result in reading_score if result > reading_std_third_start and result < reading_third_std_end]

writing_1_std = [result for result in writing_score if result > writing_std_first_start and result < writing_first_std_end]
writing_2_std = [result for result in writing_score if result > writing_std_second_start and result < writing_second_std_end]
writing_3_std = [result for result in writing_score if result > writing_std_third_start and result < writing_third_std_end]

math_1_per = len(math_1_std) / len(math_score)*100
math_2_per = len(math_2_std) / len(math_score)*100
math_3_per = len(math_3_std) / len(math_score)*100

writing_1_per = len(writing_1_std) / len(writing_score)*100
writing_2_per = len(writing_2_std) / len(writing_score)*100
writing_3_per = len(writing_3_std) / len(writing_score)*100


reading_1_per = len(reading_1_std) / len(reading_score)*100
reading_2_per = len(reading_2_std) / len(reading_score)*100
reading_3_per = len(reading_3_std) / len(reading_score)*100

print("math 1 per is "+str(math_1_per))
print("math 2 per is "+str(math_2_per))
print("math 3 per is "+str(math_3_per))

print("reading 1 per is "+str(reading_1_per))
print("reading 2 per is "+str(reading_2_per))
print("reading 3 per is "+str(reading_3_per))

print("writing 1 per is "+str(writing_1_per))
print("writing 2 per is "+str(writing_2_per))
print("writing 3 per is "+str(writing_3_per))