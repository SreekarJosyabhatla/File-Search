import os
import sys
import string


def line_to_terms(line_string):
  final_terms_list = []
  raw_terms_list = line_string.split()
  
  for i in range(len(raw_terms_list)):
    raw = raw_terms_list[i]
    term = raw.strip(string.punctuation)
    if term not in final_terms_list:
      final_terms_list.append(term)
      
  return final_terms_list

def create_index(filenames, index, file_titles):
    
    for filename in filenames:
      with open(filename) as f:
        for i, line in enumerate(f):
          if i == 0:
            file_titles[filename] = line.strip()
          terms_list = line_to_terms(line.lower())
          for term in terms_list:
            if term not in index.keys():
              index[term] = []
            temp_list = index[term]
            if filename not in temp_list:
             temp_list.append(filename)
            index[term] = temp_list


def textfiles_in_dir(directory):
    
    
    filenames = []

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filenames.append(os.path.join(directory, filename))

    return filenames
def main():
    
    # Get command line arguments
    args = sys.argv[1:]

    num_args = len(args)
    if num_args < 1:
        print('Please specify directory of files to index as first argument.')
    else:
        # args[0] is the folder containing all the files to index/search.
        directory = args[0]
        if os.path.exists(directory):
            # Build index from files in the given directory
            files = textfiles_in_dir(directory)
            index = {}          # index is empty to start
            file_titles = {}    # mapping of file names to article titles is empty to start
            create_index(files, index, file_titles)

            print('Index:')
            #print(index)
            print(str(index).replace('],','],\n '))
            print('File names -> document titles:')
            #print(file_titles)
            print(str(file_titles).replace(',',',\n '))
        else:
            print('Directory "' + directory + '" does not exist.')


if __name__ == '__main__':
    main()

#To run use command python searchengine.py <directory> -s