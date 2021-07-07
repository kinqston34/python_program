#使用者輸入員工編號(數字),員工姓名(文字)
while True:
    id = int(input('Input ID:'))
    if id == -1:
        break
    name = input('Input Name:')
    with open(r'C:\Users\User\Desktop\aaa.txt',mode = 'a') as f:  #'a' 寫檔 寫在文件後方(不覆寫)
        #write 裡面 f:字串符 {格式化}
        f.write(f'{id:4}{name:10}\n')
        #{id:>04} 往右邊靠不足補零長度四碼
        #{name:*<10} 往左靠不足補星號長度10碼