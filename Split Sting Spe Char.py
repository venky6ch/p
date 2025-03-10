# Split String at special character loc
Iam = "I,am!currently$ enrolled%in,data!science ^ course^Conducted  @UpGrad@IITB^Banglore^Karnataka"
spec_char = "@[_!#$%^&*()<>?/|,}{~:]"
index_list = []
for i in range(len(Iam)):
    if Iam[i] in spec_char:
        index_list.append(i)
final_list = []

for i in range(len(index_list)):
    if i < 1:
        final_list.append(Iam[0 : index_list[i]].strip())
    else:
        final_list.append(Iam[index_list[i - 1] + 1 : index_list[i]].strip())
final_list.append(Iam[index_list[i] + 1 : len(Iam)])
final_list
