from sentence_transformers import SentenceTransformer, util
import json

sbert_model = SentenceTransformer('all-MiniLM-L6-v2')

def combine_info(obj):
  return obj['title']+'. '+obj['description']

data = json.load(open('data.json'))
answers = [str(combine_info(obj)) for obj in data]

def get_answer(question):
  qs = [question]
  embed_qs = sbert_model.encode(qs, convert_to_tensor=True)
  embed_ans = sbert_model.encode(answers, convert_to_tensor=True)
  score = util.cos_sim(embed_qs, embed_ans)
  score_dict = [{'data':data[i],'score':float(score[0][i])}for i in range(len(embed_ans))]
  return sorted(score_dict,key=lambda x:x['score'], reverse=True)