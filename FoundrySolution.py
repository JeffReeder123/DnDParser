import json
import csv
import os


#change file path to file location prior to executing.
with open("C:/Users/Jeff/Downloads/sources.json" , "r") as file:
        file_text = file.read()
        file_text_json = json.loads(file_text)
        print(type(file_text_json))

output_dict = dict()

for source_key in file_text_json:
        source_value = file_text_json[source_key]
        for spell_key in source_value:
                spell_value = source_value[spell_key]
                for parent_class_key in spell_value:
                        parent_class_value = spell_value[parent_class_key]
                        for actual_class in parent_class_value:
                                if actual_class['name'] in output_dict:
                                        pass
                                else:
                                        output_dict.update({actual_class['name'] : []})
                                output_class_spells = output_dict[actual_class['name']]
                                spell_to_add = [spell_key , source_key]
                                if spell_to_add in output_class_spells:
                                        pass
                                else:
                                        output_class_spells.append(spell_to_add)
                                
                               
                                

# Change output file path to where you want to write the file before executing.
print(json.dumps(output_dict))
output_file_path = 'C:/Users/Jeff/Downloads/sources_output.json'
file_exists = os.path.exists(output_file_path)
if file_exists: 
        os.remove(output_file_path)
open(output_file_path,'x')
with open(output_file_path, 'w') as f:
        json.dump(output_dict, f)
                                        

                                


                        













