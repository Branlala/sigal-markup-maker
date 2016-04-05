#!/usr/bin/python3
import sys, getopt, os

def main(argv):
   directory = ''
   author = ''
   force = False
   try:
      opts, args = getopt.getopt(argv,"hd:a:f",["dir=","author=","force"])
   except getopt.GetoptError:
      print('smm.py -d <sigal picture directory> -a <author> -f')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('smm.py -d <sigal picture directory> -a <author> -f')
         sys.exit()
      elif opt in ("-d", "--directory"):
         directory = arg
      elif opt in ("-a", "--author"):
         author = arg
      elif opt in ("-f", "--force"):
         force = True
   print('> Working on directory', directory)

   file_name = {'index.md'}
   for dirs in get_directories_without_index(directory, file_name, force):
     generate_index(dirs, author)

def get_directories_without_index(root, file_name, force):
    for root, dirs, files in os.walk(root):
        for file in files:
            if file in file_name and not force:
                break
        else:
            yield root

def generate_index(directory, author):
    dir_name = os.path.basename(os.path.normpath(directory)).replace("-", " ").replace("_", " ")
    lines_of_index = []

    file = open(directory+"/index.md", "w")

    lines_of_index.append('Title: ' + dir_name.capitalize() + '\n')
    lines_of_index.append('Thumbnail:' + '\n')
    lines_of_index.append('Author: ' + author + '\n')
    lines_of_index.append('' + '\n')
    lines_of_index.append('# ' + dir_name.capitalize() + '\n')

    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            lines_of_index.append('* ' + dir + '\n')

    file.writelines(lines_of_index)
    file.close()

if __name__ == "__main__":
   main(sys.argv[1:])
