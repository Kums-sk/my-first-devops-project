{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh14900\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Import os\
\
#Define the new directory and file name\
new_directory = \'93my_new_folder\'94\
new_file = \'93my_first_file.txt\'94\
\
# Create the new directory\
os.makedirs(new_directory, exist_ok=True)\
print(f\'94Directory \'91\{new_directory\}\'92 created successfully\'94)\
\
#Define the content of the file\
file_content = \'93Hello, DevOps world! This is my first Python script.\'94\
\
#Create and write to the new file\
With open(os.path.join(new_directory, new_file), \'93w\'94) as f:\
f.write(file_content)\
\
print(f\'94File \'91\{new_file\}\'92 created in \'91\{new_directory\}\'92.\'94)}