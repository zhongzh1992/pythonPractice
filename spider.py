from urllib import request
import re
import ssl


class Spider:
    # 爬去的网页
    __url = 'https://book.douban.com/top250?icn=index-book250-all'
    __root_pattern = '<td valign="top">([\s\S]*?)</td>'
    __name_pattern = '<p class="pl">([\s\S]*?)</p>'
    __number_pattern = '<span class="rating_nums">([\s\S]*?)</span>'

    # 获取HTML
    def __getHTML(self):
        header = headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
        r = request.Request(url=self.__url, headers=header)
        # ssl解决https证书问题
        context = ssl._create_unverified_context()
        res = request.urlopen(r, context=context)
        html = res.read().decode("utf8", 'ignore')
        # print(html)
        # 转成字符串
        return html

    # 正则表达式
    def __analysis(self, html):
        root_html = re.findall(self.__root_pattern, html)
        anchors = []
        for html in root_html:
            name = re.findall(self.__name_pattern, html)
            number = re.findall(self.__number_pattern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        return anchors

    # 精炼数据
    def __refine(self, anchors):
        return anchors

    # 排序
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    # 排序方法
    def __sort_seed(self, anchor):
        print(anchor)
        r = re.findall('\d+.\d+', anchor['number'][0])
        number = float(r[0])
        return number

    # 输出
    def __print(self, anchors):
        for anchor in anchors:
            print(anchor['name'][0] + '----->' + anchor['number'][0])

    # 入口
    def run(self):
        html = self.__getHTML()
        anchors = self.__analysis(html)
        anchors = self.__refine(anchors)
        anchors = self.__sort(anchors)
        self.__print(anchors)


a = Spider()
a.run()
