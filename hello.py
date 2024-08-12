res = "Here are five new work notes for the task \"Salary Review\" in the project \"Digital Transformation\":\n\n1. Need to clarify guidelines for tracking extra hours worked outside regular office time.\n2. Wiki article re: how to accurately record overtime and extra hours worked.\n3. Possibility: adjust salary review process to include feedback from previous year's reviews.\n4. Digital Transformation Salary review: need to confirm if contributions beyond carrying the income will be considered in this review.\n5. Tried setting up a template for email reminders, need to test and refine before sending out.\n\nNote that these work notes are generated based on the provided context, trying to stay close to the topics and ideas mentioned earlier."
print(res)
res1 = res.split('\n')
array_result = []
print(res1)
print(len(res1))
for i in range (len(res1)):
    line = res1[i]
    if len(line) > 0 and line[0] in "12345" and line[1] == '.':
    #if res1[i][0] in "12345":
        print(line)
        array_result.append(line)

print(array_result)
print(len(array_result))