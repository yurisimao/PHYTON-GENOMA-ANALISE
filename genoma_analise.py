bacterium_filename_path = "massa/bacteria.fasta"
bacterium_filename_path_html = bacterium_filename_path.replace(".fasta", ".html")
human_filename_path = "massa/human.fasta"
human_filename_path_html = human_filename_path.replace(".fasta", ".html")

input_file = open(bacterium_filename_path).read()
output_file = open(bacterium_filename_path_html, "w")

#dicionario
cont = {}

for i in ['A', 'T', 'C', 'G']:
	for j in ['A', 'T', 'C', 'G']:
		cont[i+j] = 0

input_file = input_file.replace("\n", "")

for k in range(len(input_file)-1):
	cont[input_file[k]+input_file[k+1]] += 1

i = 1
for k in cont:
	transparency = cont[k]/max(cont.values())
	output_file.write("<div style='width: 100px; border:1px solid #111; color:#ffff; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(transparency)+"')>"+k+"</div>")

	if i%4 == 0:
		output_file.write("<div style='clear:both'></div>")

	i+=1
	

output_file.close()