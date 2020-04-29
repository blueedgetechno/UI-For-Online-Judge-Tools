import os,time,sys

path="/media/stuxnet/OS/Users/Rohan/OneDrive/Atom/RoundCodeforces/codeforces/"
def test(contestID,prob,file,lang,retest):
    if not retest:
        try:
            dele='rm -rf test'
            os.system(dele)
        except:
            print('\033[1m \033[31m \033[4m' +  "\n\n\t\tERROR OCCURED\n" + '\033[0m')
            time.sleep(2)
            return

        cmd="oj d https://codeforces.com/contest/"+str(contestID)+"/problem/"+prob
        os.system(cmd)

    os.system("clear")
    if lang==1:
        cmd='oj t -c "python '+path+file+'" --tle 2.5'
    else:
        os.system("cd "+path)
        cmd="oj t --tle 2.5"

    # print(cmd)
    os.system(cmd)
    res=int(input("\n\n\t\t1) SUBMIT\n\t\t2) RETEST\n\t\t3) BACK : "))
    if res==1:
        submit(contestID,prob,file)
    elif res==2:
        test(contestID,prob,file,lang,1)
    else:
        return

def submit(contestID,prob,file):
    file=path+file
    cmd="oj s https://codeforces.com/contest/"+str(contestID)+"/problem/"+prob+" "+file
    os.system(cmd)
    print("\n\n\n")
    return

def quick():
    os.system("clear")
    print('\033[1m \033[32m \033[4m' +  "\n\n\t\tWELCOME USER\n" + '\033[0m')
    contestID=int(input("\n\n\t\tContest : "))
    lang=int(input("\n\t\t1) Python\n\t\t2) C++ \n\t\t3) Exit : "))
    if lang==3:
        return
    file="main"
    if lang==1:
        file+=".py"
    else:
        file+=".cpp"

    os.system("clear")
    print('\033[1m \033[32m \033[4m' +  "\n\n\t\tWELCOME USER\n" + '\033[0m')
    print("\n\n\t\tContest : ",contestID,"\t\tCurrent file : ",file)
    prob=input("\n\n\t\tProblem : ")
    prob=prob.upper()
    file2=input("\n\n\t\tFile : ")
    if file2!=" ":
        file=file2
        if lang==1:
            file+=".py"
        else:
            file+=".cpp"

    ch=int(input("\n\n\t\t1) Test\n\t\t2) Submit\n\t\t3) Back : "))
    print("\n")
    if ch==1:
        test(contestID,prob,file,lang,0)
    elif ch==2:
        submit(contestID,prob,file)
    else:
        quick()

    ch=int(input("\n\t\t1) Another\n\t\t2) Exit : "))
    if ch==1:
        quick()

    return

def contest():
    os.system("clear")
    print('\033[1m \033[32m \033[4m' +  "\n\n\t\tWELCOME USER\n" + '\033[0m')
    contestID=int(input("\n\n\t\tContest : "))
    lang=int(input("\n\t\t1) python\n\t\t2) cpp : "))

    file="main"
    if lang==1:
        file+=".py"
    else:
        file+=".cpp"

    while True:
        os.system("clear")
        print('\033[1m \033[32m \033[4m' +  "\n\n\t\tWELCOME USER\n" + '\033[0m')
        print("\n\n\t\tContest : ",contestID,"\t\tCurrent file : ",file)
        prob=input("\n\n\t\tProblem : ")
        prob=prob.upper()
        file2=input("\n\n\t\tFile : ")
        if file2!=" ":
            file=file2
            if lang==1:
                file+=".py"
            else:
                file+=".cpp"

        ch=int(input("\n\n\t\t1) Test\n\t\t2) Submit\n\t\t3) Back : "))
        print("\n\n")
        if ch==1:
            test(contestID,prob,file,lang,0)
        elif ch==2:
            submit(contestID,prob,file)
        else:
            start()

    return

def start():
    s="\n\n\t\t\t\t\t\t"
    i=int(input("\n\n\n\n\n\n\n\n"+s+"1) Quick Mode"+s+"2) Contest Mode"+s+"3) EXIT : "))
    if i==1:
        quick()
    elif i==2:
        contest()
    else:
        return

start()
if True:
    s="""
                                       $$$$
                                      $$  $
                                      $   $$
                                      $   $$
                                      $$   $$
                                       $    $$
                                       $$    $$$
                                        $$     $$
                                        $$      $$
                                         $       $$
                                   $$$$$$$        $$
                                 $$$               $$$$$$$$
                                $$    $$$$            $$$$$
                                $   $$$  $$$            $$$
                                $$        $$$            $$
                                 $$    $$$$$$            $$
                                 $$$$$$$    $$           $$
                                 $$       $$$$           $$
                                  $$$$$$$$$  $$         $$$
                                   $        $$$$     $$$$
                                   $$    $$$$$$    $$$$$$
                                    $$$$$$    $$  $$
                                      $     $$$ $$$
                                       $$$$$$$$$$
    """
print("\n\n\n\n")
print('\033[1m \033[32m \033[1m' +  s + '\033[0m')
print("\n")
time.sleep(0.5)
