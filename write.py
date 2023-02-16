# with open('./about.txt','w') as file:
#     file.write('i am ok');

lists = ['i am ok ','\ni am all right']

with open('./about.txt','w') as file:
    file.writelines(lists);