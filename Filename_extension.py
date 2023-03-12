Filename=input('enter the filename:')
extension= Filename.split('.')
print("file extension is:",extension[-1] if len(extension)>1 else"unkonwn extension:")