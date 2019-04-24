import os
from xpinyin import Pinyin

p = Pinyin()

def get_new_name(name, x):
    pinyin = p.get_pinyin(name, '')
    new_name = pinyin.replace('@'+x+'x', '')
    return new_name

def copyFiles(sourceDir,  targetDir, x): 
    for file in os.listdir(sourceDir): 
        sourceFile = os.path.join(sourceDir,  file) 
        targetFile = os.path.join(targetDir,  file) 
        if os.path.isfile(sourceFile):
            if sourceFile.find('@'+x+'x.png') < 0:
                continue
            targetFile = get_new_name(targetFile, x)
            if not os.path.exists(targetDir):  
                os.makedirs(targetDir)  
            if not os.path.exists(targetFile) or (os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):  
                open(targetFile, "wb").write(open(sourceFile, "rb").read()) 
        elif os.path.isdir(sourceFile):
            copyFiles(sourceFile, targetFile)

if __name__ == "__main__":
    sourceDir = input("请输入原目录(结尾加上/): ")
    targetDir = input('请输入导出目录:')
    x = input('请输入转化几倍图: ')

    copyFiles(sourceDir, targetDir, x)
    print('转化完成')