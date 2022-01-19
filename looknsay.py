def nextseq(seq):
    new=[]
    count,lastnum =(0,seq[0])
    
    for num in seq:
        if lastnum!= num:
            newseq+=[count,lastnum]
            count,lastnum=(0,num)
        count+=1
            
    return(newseq+[count,lastnum])


def main():
    seq = [1]

    print("".join(map(str,seq)))
    for i in range(1,int(input())):
        seq =nextseq(seq)
        print("".join(map(str,seq)))

main()
