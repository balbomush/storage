def parse(voc1, voc2):
    new_files = {}
    lost_files = {}
    currupted_files = {}
    keys1 = voc1.keys()
    keys2 = voc2.keys()
    for k, v in voc2.items():
        if k not in keys1:
            new_files[k] = v
        elif k in keys1 and v != voc1[k]:
            currupted_files[k] = {"old md5":voc1[k], "new md5":v}
        else:
            pass
    for k, v in voc1.items():
        if k not in keys2:
            lost_files[k] = v
    return lost_files, currupted_files, new_files


def toVoc(L):
    voc = {}
    for st in L:
        if st:
            # print (st)
            k, v = st.split("\t")
            voc[k] = v
    return voc

def reporter(title, voc):
    print ("%s:" % title)
    for k, v in voc.items():
        print ("\t%s, md5: %s" % ((k, v)))

if __name__ == "__main__":
    data1 = open("test1.txt", "r").read().split("\n")
    data2 = open("test2.txt", "r").read().split("\n")

    if (data1 == data2):
        print("All correct! Bye...")
    else:
        lost_files, currupted_files, new_files = parse(toVoc(data1), toVoc(data2))
        reporter("Lost files", lost_files)
        reporter("Corrupted files", currupted_files)
        reporter("Intrusion", new_files)
