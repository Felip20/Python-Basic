# file = open('./text.txt')

# # for line in file:
# #     print(line);

# file.seek(0);

# # linelist = file.readlines()
# # print(linelist);

with open('./text.txt') as file:
        for line in file:
            print(line);
print('ok');