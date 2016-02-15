import json 
import urllib, urllib.parse, urllib.request
import os 

BING_API_KEY = 'bYwC3Jb78mM/PPkFM6HXLxUnvh5nG3f2ZEtJ9yQ+BU0'

def run_query(search_terms):
    root_url = "https://api.datamarket.azure.com/Bing/Search/"
    
    source = 'Web'
    
    #每页多少结果， 从第几行开始
    results_per_page = 10 
    offset = 0 
    
    #表示 '0'
    query = "'{0}'".format(search_terms)
    query = urllib.parse.quote(query)
    
    #完整的搜索 url 
    search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
        root_url,
        source,
        results_per_page,
        offset,
        query)
    
    #设置 Bing 服务器的验证
    username = ''
    #用来处理验证
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, search_url, username, BING_API_KEY)
    
    results = []
    try:
        #准备连接到 Bing 服务器
        handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
        opener = urllib.request.build_opener(handler)
        urllib.request.install_opener(opener)
        
        #连接到 Bing 服务器并读取响应                  #需要 decode 否则会发生 json
        #the JSON object must be str, not 'bytes'
        response = urllib.request.urlopen(search_url).read().decode('utf8')
        #转化为 Python dict object 
        json_response = json.loads(response)
        
        for result in json_response['d']['results']:
            results.append({
                'title': result['Title'],
                'link': result['Url'],
                'summary': result['Description']})
    except urllib.error.URLError as e:
        print("Error when querying the Bing API: ", e)
        
    return results 
    
#输入 search_terms，生成前10个结果    
def main(search_terms="test"):
    results = run_query(search_terms)
    print(results)
    
        
if __name__ == '__main__':
    main()
    