ids = []
scaffolds = []
props = []
same_counts = []
gen_counts = []
diffs_avg = []
mom_scaffold = ""
success = []

with open("logp_34to6_unlabel_1p.txt") as idFile:
    same_count = 0
    gen_count = 0
    diffs = []

    current = ""
    for line in idFile:
        data = line.split(" ")

        if len(data) == 3:
            id, scaffold, prop = data
            if "STOCK" in id:
                current = id
                if len(scaffolds) > 0:
                    same_counts.append(same_count)
                    gen_counts.append(gen_count)
                    diffs_avg.append(round(sum(diffs)/len(diffs), 3))
                ids.append(id)
                scaffolds.append(scaffold)
                props.append(prop)
                mom_scaffold = scaffold
                same_count = 0
                gen_count = 0
                diffs = []

        if len(data) == 4:
            id, scaffold, prop, diff = data
            if "gen" in id:
                gen_count += 1
                diffs.append(float(diff[:-1]))
                if scaffold == mom_scaffold:
                    same_count += 1
            if "6." in prop:
                success.append(line)

    same_counts.append(same_count)
    gen_counts.append(gen_count)
    diffs_avg.append(round(sum(diffs) / len(diffs), 3))

# print(same_counts, len(same_counts))
# print(gen_counts, len(gen_counts))
print(sum(same_counts))
print(sum(gen_counts))
# print(diffs_avg, len(diffs_avg))

with open("logp_34to6_unlabel_1p_count.txt", "w") as newFile:
    newFile.write("ID SCAFFOLD PROPERTY #GEN_TOTAL #GEN_OVERLAP AVGDIFF\n")
    with open("logp_67to8.txt") as oldFile:
        num = 0
        for line in oldFile:
            data = line.split(" ")
            if len(data) == 3:
                id, scaffold, prop = data
                if "STOCK" in id:
                    newFile.write(line[:-1] + " " + str(gen_counts[num]) + " " + str(same_counts[num]) + " " + str(diffs_avg[num]) + "\n")
                    num += 1

with open("logp_34to6_unlabel_1p_success.txt", "w") as newFile:
    for line in range(len(success)):
        newFile.write(line)