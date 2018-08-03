num = 1000
path = 'E:/video/'


def response(flow):
    global num
    # 测试得出视频url前缀主要下面几个
    urls = ['http://v1-dy.ixigua.com/', 'http://v3-dy-z.ixigua.com/', 'http://v3-dy.ixigua.com/',
            'http://v9-dy.ixigua.com/', 'http://v6-dy.ixigua.com/','http://v7.pstatp.com']
    # 过滤一下
    for url in urls:
        if flow.request.url.startswith(url):
            # 保存文件路径和文件名
            filename = path + str(num) + '.mp4'
            res = flow.response.content
            # 写入视频
            with open(filename, 'ab') as f:
                f.write(res)
                f.flush()
                print(filename, 'win')
                num += 1
