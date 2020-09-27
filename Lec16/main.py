import pickle 

data = {'a' : 1, 'b' : 2, 'c' : [1,2,3]}

#dump() # превращает объект в байтовую последовательность
#и сохраняет в файл

#dumps() # --//-- сохраняет в виде строки

ans_bytes = pickle.dumps(data)
print(ans_bytes)

# load() -- загружает объект на основе байтовой последовательности в файле
# loads() -- --//-- из строки

data_from_bytes = pickle.loads(ans_bytes)
print(data_from_bytes, type(data_from_bytes))