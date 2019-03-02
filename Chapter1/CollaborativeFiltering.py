import pandas as pd
from math import sqrt
import os

def get_rating(data, index):
    #获取index的电影评分
    result =[]
    result = data[data["user_id"]==index]["rating"].values
    return  result

def similarity_calculate(rating_index, rating_me):
    #相似度计算
    sum = 0
    for i in range(0, 4):
        sum = sum+pow(rating_index[i]-rating_me[i],2)
        return 1/(1+sqrt(sum))

def get_similarity_with_me(data, index):
    #对比他人与我的相似度
    # 1、获取index这个人的数据（电影的评分）    [1, 2,,4,5]
    rating_index = []
    rating_me = []
    rating_index = get_rating(data, index)
    print(rating_index)
    # 2、获取我的数据（电影的评分）[1,2,3,4]
    rating_me = get_rating(data, 4)
    # 3、计算相似度
    result = similarity_calculate(rating_index, rating_me)
    return result

def find_min_distance(map):
    index = 0
    similarity = 0
    similar_max = 0
    for key, value in map.items():
        print("key: %s , vlalue:%s" %(key, value))
        if similar_max < value:
            similar_max = value
            index = key
    similarity = similar_max
    return index, similarity

#加载数据
curren_path= os.path.dirname(__file__)
file = os.path.join(curren_path, 'movie.csv')
data = pd.read_csv(file)

map = {}
for i in range(1, 4):
    map[i] = get_similarity_with_me(data, i) #{1:xx, 2:xx, 3:xx} i:表示第i个人

index, similarity = find_min_distance(map) #{1:xx, 2:xx, 3:xx}
print("第%s人跟我的喜好最接近，他与我的相似度是%s" %(index, similarity))