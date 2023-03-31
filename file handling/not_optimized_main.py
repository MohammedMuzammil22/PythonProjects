# letter template
with open("./Mail Merge Project Start/Input/Letters/starting_letter.txt") as sample_file:
    # creating new files with given names
    with open("./Mail Merge Project Start/Input/Names/invited_names.txt") as name_list:
        for line in sample_file:
            for name in name_list:
                file_name = name.strip("\n")
                with open(f"./Mail Merge Project Start/Output/ReadyToSend/{file_name}", mode='a') as create_file:
                        # content = sample_file.readline()
                        content = line
                        content = content.replace("[name]",name.strip("\n"))
                        create_file.write(content)
                        print(content)
        


