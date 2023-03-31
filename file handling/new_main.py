names_list = []
with open("./Mail Merge Project Start/Input/Names/invited_names.txt") as name_file:
        for name in name_file:
            file_name = name.strip("\n")
            names_list.append(file_name) 

# letter template
with open("./Mail Merge Project Start/Input/Letters/starting_letter.txt") as sample_file:
    for line in sample_file:
        for i in range(len(names_list)-1): 
            creating_new_file = names_list[i]                   
            with open(f"./Mail Merge Project Start/Output/ReadyToSend/{creating_new_file}", mode='a') as create_file:
                # content = sample_file.readline()
                content = line
                content = content.replace("[name]",names_list[i].strip("\n"))
                create_file.write(content)
                print(content)
    

