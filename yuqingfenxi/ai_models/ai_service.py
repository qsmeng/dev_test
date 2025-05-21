from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from gensim.models import LdaModel
from gensim.corpora import Dictionary
import numpy as np

class ModelService:
    def __init__(self):
        # 加载预训练模型
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.sentiment_model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")
        
        # 示例LDA模型
        self.lda_model = self._load_lda_model()

    def _load_lda_model(self):
        # 创建示例语料库
        texts = [["apple", "fruit", "red"], ["car", "drive", "fast"]]
        dictionary = Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]
        
        # 训练LDA模型
        return LdaModel(corpus, num_topics=2, id2word=dictionary)

    def analyze_sentiment(self, text: str) -> float:
        # 文本情感分析
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.sentiment_model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1).numpy()[0]
        
        # 返回正面情感概率 - 负面情感概率
        return float(probabilities[1] - probabilities[0])

    def analyze_topics(self, text: str) -> list:
        # 主题分析
        bow = self.lda_model.id2word.doc2bow(text.lower().split())
        topics = self.lda_model.get_document_topics(bow)
        return sorted(topics, key=lambda x: x[1], reverse=True)