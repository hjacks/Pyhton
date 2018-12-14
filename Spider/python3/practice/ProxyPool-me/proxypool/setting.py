# Redis数据库地址
redis_host = '127.0.0.1'

# Redis端口
redis_port = 6379

# Redis密码，如无填None
redis_password = None

redis_key = 'proxies'

# 代理分数
max_score = 100
min_score = 0
initial_score = 10

valid_status_code = [200,302]

# 代理池数量界限
pool_upper_threshold = 10000

# 检查周期
tester_cycle = 20

# 获取周期
getter_cycle = 300

# 测试api，建议抓哪个网站测哪个
test_url = 'http://www.baidu.com'

# API设置
api_host = '0.0.0.0'
api_port = 5555

# 开关
tester_enabled = True
getter_enabled = True
api_enabled = True

# 最大批测试量
batch_test_size = 10
