import difflib



# This script take 2 file (like 2 INTL txt) and show the diff between them
# usefull to show what new thing is delete or added on a new json file for exemple




def find_nb_line(file, line_recherche):
    with open(file, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, start=1):
            if line.strip() == line_recherche.strip():
                return i
    return -1

def compare_file(file1, file2, diff1, diff2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
    
    d = difflib.Differ()
    result = list(d.compare(lines1, lines2))
    
    diff_f1 = []  # lines found in file1 but not in file2
    diff_f2 = []  # lines found in file2 but not in file1
    
    for line in result:
        if line.startswith('- '):  # line sub from file1
            line_no_prefixe = line[2:].strip()
            num_line = find_nb_line(file1, line_no_prefixe)
            diff_f1.append(f"{line_no_prefixe} (line {num_line})\n")
        elif line.startswith('+ '):  # line add in file2
            line_no_prefixe = line[2:].strip()
            num_line = find_nb_line(file2, line_no_prefixe)
            diff_f2.append(f"{line_no_prefixe} (line {num_line})\n")
    
    with open(diff1, 'w', encoding='utf-8') as d1:
        d1.writelines(diff_f1)
    
    with open(diff2, 'w', encoding='utf-8') as d2:
        d2.writelines(diff_f2)


# Exemple
compare_file('oldFile.json', 'newFile.json', './Diff/diff1.txt', './Diff/diff2.txt')
