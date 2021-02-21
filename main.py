将 cv2 导入为 cv
导入 操作系统
将 numpy 导入为 np
＃图片的存储路径
img_path  =  'imgs'
＃output_path ='游戏\\ res \\原始资产'
output_path  =  os。路径。加入（'game'，'res'，'raw-assets'）
＃每个水果的尺寸
尺寸 = [ 52，80，108，119，152，183，193，258，308，309，408 ]
＃水果图片存放路径
路径 = [ 'ad'，'0c'，'d0'，'74'，'13'，'03'，'66'，'84'，'5f'，'56'，'50' ]
＃水果图片名字
名称 = [ 'ad16ccdc-975e-4393-ae7b-8ac79c3795f2.png'，
         '0cbb3dbb-2a85-42a5-be21-9839611e5af7.png'，
         'd0c676e4-0956-4a03-90af-fee028cfabe4.png'，
         '74237057-2880-4e1f-8a78-6d8ef00a1f5f.png'，
         '132ded82-3e39-4e2e-bc34-fc934870f84c.png'，
         '03c33f55-5932-4ff7-896b-814ba3a8edb8.png'，
         '665a0ec9-6c43-4858-974c-025514f2a0e7.png'，
         '84bc9d40-83d0-480c-b46a-3ef59e603e14.png'，
         '5fa0264d-acbf-4a7b-8923-c106ec3b9215.png'，
         '564ba620-6a55-4cbe-a5a6-6fa3edd80151.png'，
         '5035266c-8df3-4236-8d82-a375e97a0d9c.png'
         ]
＃读取水果的信息
def  read_info（）：
    ＃返回指定的文件夹包含的文件或文件夹的名字的列表
    dir_path  =  os。listdir（output_path）
    为 DIR 在 dir_path：
        ＃连接路径
        dir  =  os。路径。加入（output_path，DIR）
        对于 IMG 的 操作系统。listdir（dir）：
            ＃阅读图片
            im  =  cv。imread（OS，路径，加入（DIR，IMG））
            ＃输出图片
            打印（DIR，IMG，即时通讯。形状）

＃无限生成水果
def  generate_circle（）：
    经过

def  main（）：
    ＃读取输入的图片
    img_list  =  os。listdir（img_path）
    ＃如果输入的图片不是十张就报错，否则将输入的图片加入游戏的图片列表
    如果 len（img_list）！=  11：
        打印（“错误！请输入11个文件！”）
        返回
    img_list。排序（）
    ＃设置图片路径
    对于 我 在 范围（len个（img_list））：
        path  =  os。路径。加入（img_path，img_list [ i ]）
        ＃判断图片格式是否正确
        如果 不是 img_list [ i ]。降低（）。endswith（（（'. png '，'.jpg'，'.jpeg'））：
            打印（“请仅放入图像。”）
            返回
        打印（路径）

        ＃设置图片所在的圆的尺寸
        im  =  cv。读（路径）
        高度，宽度 = 尺寸[ i ]，尺寸[ i ]
        im  =  cv。调整大小（im，（height，width））
        circleIn  =  np。零（（高度，宽度，1），NP。UINT8）
        circleIn  =  cv。圆（circleIn，（width  //  2，height  //  2），min（height，width）//  2，（1，），- 1）
        imgIn  =  np。零（（高度，宽度，4），NP。UINT8）

        imgIn [：，：，0 ] =  np。相乘（im [：，：，0 ]，circleIn [：，：，0 ]）
        imgIn [：，：，1 ] =  np。相乘（im [：，：，1 ]，circleIn [：，：，0 ]）
        imgIn [：，：，2 ] =  np。相乘（im [：，：，2 ]，circleIn [：，：，0 ]）

        circleIn [ circleIn  ==  1 ] =  255
        imgIn [：，：，3 ] =  circleIn [：，：，0 ]
        CV。imwrite（OS。路径。加入（output_path，路径[我]，名称[我]），IMGIN）


如果 __name__  ==  ' __main__ '：
    ＃read_info（）
    主要（）
