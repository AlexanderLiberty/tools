#Автор Александр Свобода
import requests
import argparse

def get_api_endpoints(url, proxies=None):
    # 发送请求获取 Swagger/OpenAPI 文档
    response = requests.get(url, proxies=proxies)
    
    # 检查请求是否成功
    if response.status_code == 200:
        swagger_data = response.json()
        
        # 提取 API 端点
        endpoints = []
        
        # 遍历路径
        for path in swagger_data.get('paths', {}).keys():
            endpoints.append({'path': path})
        
        return endpoints
    else:
        print(f"Failed to retrieve Swagger document: {response.status_code}")
        return None

def main():
    # 设置命令行参数解析器
    parser = argparse.ArgumentParser(description="Fetch API endpoints from a Swagger/OpenAPI document.")
    parser.add_argument('-url', '--url', required=True, help="URL to the Swagger/OpenAPI document.")
    parser.add_argument('-proxy', '--proxy', help="Proxy server URL (e.g., http://127.0.0.1:8080).")

    args = parser.parse_args()
    
    # 设置代理
    proxies = None
    if args.proxy:
        proxies = {
            'http': args.proxy,
            'https': args.proxy
        }

    # 获取并打印 API 端点
    api_endpoints = get_api_endpoints(args.url, proxies=proxies)
    if api_endpoints:
        for endpoint in api_endpoints:
            # 仅打印路径
            print(endpoint['path'])

if __name__ == "__main__":
    main()
