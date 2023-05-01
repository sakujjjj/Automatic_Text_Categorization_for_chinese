import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 定義訓練數據集
train_data = ['我喜歡這家餐廳的食物', '我對這家餐廳的服務感到滿意', '這家餐廳的價格很合理',  '這家餐廳的CP值很高', '我覺得這家餐廳非常棒', '我對這家餐廳的環境很滿意',
              '這間餐廳的食物不太好吃', '這家餐廳的服務很差', '這家餐廳的價格太貴了', '這家餐廳的環境不是很好', '我非常討厭這家餐廳',  '這家餐廳的CP值很低']
train_labels = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]

# 將中文文本轉換成詞向量
vectorizer = CountVectorizer()
train_vectors = vectorizer.fit_transform(
    [' '.join(jieba.cut(text)) for text in train_data])

# 訓練模型
clf = MultinomialNB()
clf.fit(train_vectors, train_labels)

# 預測新的文本
test_data = ['這家餐廳的服務很好', '餐廳的食物很難吃', '這家餐廳CP值很高']
test_vectors = vectorizer.transform(
    [' '.join(jieba.cut(text)) for text in test_data])
predicted_labels = clf.predict(test_vectors)
print(predicted_labels)

# 輸出預測結果
for i in range(len(test_data)):
    print(
        f'"{test_data[i]}" 的預測結果是：{"正面" if predicted_labels[i]==1 else "負面"}')
