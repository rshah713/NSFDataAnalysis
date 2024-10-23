from data_clean import BaseReader

base_reader = BaseReader()
data = base_reader.scan_contents()
for i, item in enumerate(data):
    print(f"Item {i+1}:")
    print(item)
    print("\n")

gender_counts = {'Male': 0, 'Female': 0, 'Prefer not to say': 0}
ethnicity_counts = {'Hispanic': 0, 'Non Hispanic': 0, 'White': 0, 'Other': 0, 'Prefer Not To Say': 0}
for item in data:
    gender = item['gender']
    ethnicity = item['ethnicity']
    if gender in gender_counts:
        gender_counts[gender] += 1
    if ethnicity in ethnicity_counts:
        ethnicity_counts[ethnicity] +=1
    else:
        ethnicity_counts['Other'] +=1



total_count = sum(gender_counts.values())
print("Gender Statistics:")
print(f"Males: {gender_counts.get('Male', 0)} ({gender_counts.get('Male', 0) / total_count * 100:.2f}%)")
print(f"Females: {gender_counts.get('Female', 0)} ({gender_counts.get('Female', 0) / total_count * 100:.2f}%)")
print(f"Prefer not to say: {gender_counts.get('Prefer not to say', 0)} ({gender_counts.get('Prefer not to say', 0) / total_count * 100:.2f}%)")
print("\n")
print("Ethnicity Analysis")

print(f"Non-Hispanics: {ethnicity_counts.get('Non Hispanic', 0)} ({ethnicity_counts.get('Non Hispanic', 0) / total_count * 100:.2f}%)")
print(f"Hispanics: {ethnicity_counts.get('Hispanic', 0)} ({ethnicity_counts.get('Hispanic', 0) / total_count * 100:.2f}%)")
print(f"White: {ethnicity_counts.get('White', 0)} ({ethnicity_counts.get('White', 0) / total_count * 100:.2f}%)")
print(f"Other: {ethnicity_counts.get('Other', 0)} ({ethnicity_counts.get('Other', 0) / total_count * 100:.2f}%)")
print(f"Prefer not to say: {ethnicity_counts.get('Prefer not to say', 0)} ({ethnicity_counts.get('Prefer not to say', 0) / total_count * 100:.2f}%)")


