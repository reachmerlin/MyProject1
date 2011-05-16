line_list = [line for line in open("C:\Python27\Myfiles\LogFile.txt", "r")]
for i in range(0, len(line_list)):
        str = line_list[i];
        strArry = str.split("|");
        httpIndex = strArry[0].index("https");
        url = strArry[0][httpIndex:len(strArry[0])];
        print url +" : "+ strArry[3]
    
