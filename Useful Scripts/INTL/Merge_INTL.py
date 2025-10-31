

# This script will merge the Old done INTL with the new not done INTL

def Merge_INTL(txt1, txt2, output_file):
    with open(txt1, 'r', encoding='utf-8') as f1, open(txt2, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
    
    modified_lines = lines1[:]
    not_allowed = ["""Break"""] # add this for not replace ambiguous translations like "Casser" (French) -> "Break" (English), "Break" (French) -> "Pause" (French)
    for i in range(len(lines1) - 1):
        current = lines1[i].strip()
        next_line = lines1[i + 1].strip().replace('  ', ' ')
        if current == next_line and current not in not_allowed:
            try:
                index_in_txt2 = lines2.index(current + '\n')
                replacement_line = lines2[index_in_txt2 + 1] if index_in_txt2 + 1 < len(lines2) else ''
                modified_lines[i + 1] = replacement_line
            except ValueError:
                continue
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(modified_lines)

# Exemple
txt1 = 'INTL1.txt'
txt2 = 'INTL2.txt'
output_txt = 'Merge_INTL.txt'
Merge_INTL(txt1, txt2, output_txt)