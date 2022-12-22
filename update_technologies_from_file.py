import os

tech_source_directory = os.getcwd() + '\\Technologies'

tech_display_begin_tag = '<!-- TECH_DISPLAY -->'
tech_display_end_tag = '<!-- TECH_DISPLAY_END -->'

advanced_tech_begin_tag = '<!-- ADVANCED_TECH -->'
advanced_tech_end_tag =  '<!-- ADVANCED_TECH_END -->'

img_replacer = '<a><img src=\'$sourceImage\' alt=\'$altDesc\' style=\'max-width:128px;\' height=\'32\'/></a>'

def search_files(directory='.', extension=''):
    extension = extension.lower()
    file_array = []
    for dirpath, dirnames, files in os.walk(directory):
        for name in files:
            if extension and name.lower().endswith(extension):
                path = os.path.join(dirpath, name).replace("\\","/")
                file_array.append(path)
            elif not extension:
                path = os.path.join(dirpath, name).replace("\\","/")
                file_array.append(path)
    return file_array

def process_tech_files(src_dir:str,begin_tag,prefix:str = ''):
    tech_display_arr = search_files(os.getcwd() + src_dir)
    stringified = begin_tag + '\n'
    counter = 1
    for i in tech_display_arr:
        i ='.'+ i.replace(os.getcwd().replace('\\','/'),'').replace(' ','%20')
        string = prefix.replace('{num}',str(counter)) + img_replacer
        string = string.replace('$sourceImage',i).replace('$altDesc',os.path.basename(i))
        stringified += f'{string}\n'
        counter+=1
    return stringified



def replace_between_tags(dir:str,file: str, first_tag: str, second_tag: str,prefix:str = ''):
    stringified = process_tech_files(dir,first_tag,prefix)
    read_file = open(file, 'r', encoding="utf8")
    file_content = ''
    begun = False
    for line in read_file:
        if begun:
            if second_tag in line:
                begun = False
        if first_tag in line:
            begun = True
            line = line.replace(first_tag,stringified)
            file_content += line
        if not begun:
            file_content += line
    with open(file,'w', encoding="utf8") as write_file:
        write_file.write(file_content)

def generateTags():
    # Generate tags between given tags
    replace_between_tags('\\Technologies','README.md',tech_display_begin_tag,tech_display_begin_tag)
    replace_between_tags('\\AdvancedTechnologies','README.md',advanced_tech_begin_tag,advanced_tech_end_tag,'+ ')