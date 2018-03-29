from pymongo import MongoClient

client = MongoClient()
hello_db = client.hello
user_collection = hello_db.user

# 增加
user = {
    "name":"py_xutao"
    ,"age":14
    ,"sex":"py_male"
}
users = [
    {
    "name":"py_xutao"
    ,"age":14
    ,"sex":"py_male"
    },
    {
    "name":"py_123"
    ,"age":14
    ,"sex":"py_male"
    }
]
res = user_collection.insert(user) # 插入一条
res = user_collection.insert(users) # 插入多条
# 查询
# user={
#     "name":"py_xutao"
# }
# res = user_collection.find_one(user) # 查询一条，无则返回none
# res = user_collection.find(user) # 查询多条

# 修改
# user1={
#     "sex":"py_male"
# }
# user2 = {
#     "$set":{
#         "name":"xutao123"
#     }
# }
# res = user_collection.update(user1,user2) # 更新一条
# res = user_collection.update_many(user1,user2) #更新多条
# print(res)

# 删除
user = {
    "name":"xutao123"
}
res = user_collection.remove(user)
print(res)


