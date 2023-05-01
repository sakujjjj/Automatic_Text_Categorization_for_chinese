# Automatic_Text_Categorization_for_chinese
### 定義訓練數據集  
![image](https://user-images.githubusercontent.com/95430501/235434095-a08b210b-e5c1-4fbc-b618-bd2b36be0f98.png)

### 預測新的文本
test_data = ['這家餐廳的服務很好', '餐廳的食物很難吃', '這家餐廳CP值很高']  
![image](https://user-images.githubusercontent.com/95430501/235434119-63500524-fdb1-4d8c-9624-7dfddd5bcaf5.png)  
### 輸出預測結果
![image](https://user-images.githubusercontent.com/95430501/235434040-edb1ee5b-dd06-4cef-ab43-0783bad10bd0.png)


## References
* **jieba中文分詞工具**  
jieba是一個中文文本分詞的工具，它可以將一段中文文本切割成一個個詞語，並去除停用詞等無意義的詞語，只保留有意義的詞語，這樣可以幫助我們更好地進行文本分析、文本處理等操作。在這個範例中，我們使用jieba將中文文本轉換成詞向量。  
* **CountVectorizer**  
CountVectorizer是sklearn中的一個文本向量化的工具，它可以將一段文本轉化成一個詞頻矩陣。詞頻矩陣是一個二維矩陣，每一行代表一篇文本，每一列代表一個詞語，矩陣中的每個元素代表該詞語在該篇文本中出現的次數。在這個範例中，我們使用CountVectorizer將中文文本轉化成詞頻矩陣。  
* **MultinomialNB**  
MultinomialNB是sklearn中的一個Naive Bayes classifier，它是基於貝葉斯定理和特徵獨立假設的一種機器學習算法。貝葉斯定理是基於條件概率的定理，它可以計算出在某個條件下某個事件發生的概率。在文本分類中，我們可以將每個詞語視為一個特徵，然後計算每個特徵在每個類別中出現的概率，並根據貝葉斯定理計算文本屬於每個類別的概率，從而實現文本分類。在這個範例中，我們使用MultinomialNB進行文本分類。
